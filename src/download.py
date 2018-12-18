import os
import re
import sys
import argparse
import logging
import time
import sqlite3
import db
import subprocess
from pytube import YouTube

formats = ['mp4', '3gpp', 'webm']
proj_root = os.path.join('..', os.path.dirname(__file__))
logger = logging.getLogger('Download logger')

def update_true_fps(filename, filepath, sqlite_conn, conn_cursor):  # YT does not give accurate fps
    ps = subprocess.Popen(['ffmpeg', '-i', filepath], stderr=subprocess.PIPE)
    _, err = ps.communicate()
# ffmpeg -i ../data/video/unprocessed/bwYadEhuFI8-0-84.mp4 2>&1 | sed -n "s/.*, \(.*\) fp.*/\1/p"

    reg = re.search(r'\d+\.?\d?\d? fps', str(err))
    fps = float(reg.group().split(' ')[0])
    #conn_cursor.execute('UPDATE metadata SET fps=? WHERE video_id=?', (fps,filename))
    #sqlite_conn.commit()

def record_stream_data(yt, stream, filename, start, end, db_conn):
    '''start and end are the start and end times in seconds as strings
    '''
    vid = filename
    title = yt.title
    fmt = stream.fmt_profile
    res, fps, abr = fmt['resolution'], 0, fmt['abr']
    kw = stream.player_config_args['keywords']
    itag = stream.itag
    mime = stream.mime_type
    length = int(stream.player_config_args['length_seconds'])
    cap = yt.captions.get_by_language_code('en').generate_srt_captions()
    start, end = int(start), int(end)
    if start < 0:
        raise ValueError('Start time of {} is before the start of the {} with video id {}.'.format(start, title, vid))
    elif end > length or end < -1:
        raise ValueError('End time of {} is not in a valid range for {} with video id {}. Full length is {}. Set to -1 for whole video to be included.'.format(end, title, vid, length))
    elif end < start and end != -1:
        raise ValueError('End time of {} is before start time of {} for {} with id {}.'.format(end, start, title, vid))
    data = (vid, title, fps, abr, res, kw, itag, mime, length, cap, start, end)
    db_conn.insert('metadata', 'metadata', ('video_id', 'title', 'fps', 'abr', 'resolution', 'keywords', 'itag', 'mime_type', 'full_length_sec', 'captions', 'start_time', 'end_time'), data)
    #conn_cursor.execute('''INSERT INTO metadata (video_id, title, fps, abr, resolution, keywords, itag, mime_type, full_length_sec, captions, start_time, end_time) VALUES ({})'''.format('?,'*11+'?'), data)
    #sqlite_conn.commit()

def is_valid_stream(yt, stream, lower_res, upper_res):
    res = stream.resolution[:-1]
    return int(res) >= lower_res and int(res) <= upper_res and stream.includes_video_track and stream.includes_audio_track and yt.captions.get_by_language_code('en') is not None

def get_valid_stream(yt, streams, lower_res=360, upper_res=480):
    for stream in streams[::-1]:  # They are ordered in descending resolution, we want the highest res so we reverse the order
        if is_valid_stream(yt, stream, lower_res, upper_res):
            return stream

def get_filename(yt, stream, start, end):
    if end == '-1':
        end = stream.player_config_args['length_seconds']
    return yt.video_id + '-' + start + '-' + end

def single_file_download_url(input_filename, output_dir, db_conn):
    '''Downloads videos from URL in input_file. URLs should be separated by newlines.
    '''
    with open(input_filename) as f:
        for line in f:
            link, start, end = line.strip().split(' ')  # start and end should be whole numbers representing start and end times in seconds as a string
            yt = YouTube(link)
            not_exists = db_conn.fetchone('metadata', 'metadata', ['video_id'], ('video_id', yt.video_id)) is None
            if not_exists:
            conn_cursor.execute('SELECT video_id FROM metadata WHERE video_id=?', (yt.video_id,))
            #if conn_cursor.fetchone() is None:  # No records of this video in metadata, proceed to download
                streams_by_type = [yt.streams.filter(type='video', subtype=tp).order_by('resolution').all() for tp in formats]
                for i, streams in enumerate(streams_by_type):
                    stream = get_valid_stream(yt, streams)
                    if stream is not None:
                        #try:
                            filename = get_filename(yt, stream, start, end)
                            record_stream_data(yt, stream, filename, start, end, db_conn)
                            stream.download(output_path=output_dir, filename=filename)
                            update_true_fps(filename, os.path.join(output_dir, filename+'.'+stream.subtype),  db_conn) 
                            logger.info('Stream for {} with video id {} has been downloaded'.format(yt.title, yt.video_id))
                            break
                        #except:
                        #    logger.error('{}, video id {}, itag {} not downloaded: connection error or something'.format(yt.title, yt.video_id, stream.itag))
                    logger.warning('{}, video id {}, subtype {} not downloaded: no valid formats'.format(yt.title, yt.video_id, formats[i]))

def download_folder_url(input_dir, output_dir, sqlite_conn):
    all_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    for filename in all_files:
        if filename != '.gitkeep':
            single_file_download_url(os.path.join(input_folder, filename), output_dir, sqlite_conn)

if __name__ == '__main__':
    arguments = sys.argv
    output_dir = os.path.join(proj_root, 'data', 'video', 'unprocessed')
    logging.basicConfig(filename=os.path.join(proj_root, 'logs', time.strftime("DownloadLog_%a,%d-%b-%Y-%H:%M:%S_", time.localtime())+time.tzname[0]), \
       format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    if len(arguments) > 2:
        raise ValueError('Wrong number of arguments. Single argument must be either the relative path from project root directory to directory in which input files live or a single input file.')
    elif len(arguments) == 1:
        input_folder = os.path.join(proj_root, 'input')
    else:
        parser = argparse.ArgumentParser('Download input folder url')
        parser.add_argument('folder', help='Youtube videos in files in given directory will be downloaded to data/video/unprocessed.')
        input_folder = os.path.join(proj_root, parser.parse_args().folder)

   # conn = sqlite3.connect(os.path.join(proj_root, 'db', 'metadata.db'))
   # c = conn.cursor()
    db_conn = db.DatabaseConnector(['metadata'])

    if os.path.isfile(input_folder):
        # user actually input a file
        single_file_download_url(input_folder, output_dir, db_conn)
    else:
        download_folder_url(input_folder, output_dir, db_conn)

    #conn.close()
