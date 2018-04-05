import skvideo.io
import os
import time
import numpy as np
import logging
import sqlite3
import subprocess
import datetime

proj_root = os.path.join('..', os.path.dirname(__file__))
logger = logging.getLogger('Data Processing logger')

def get_start_end_frame(fps, start_time, end_time):
    start_frame, end_frame = start_time * fps, end_time * fps
    return int(start_frame), int(end_frame)

def get_metadata(yt_video_id, conn_cursor):
    conn_cursor.execute('SELECT fps, abr, full_length_sec, start_time, end_time FROM metadata WHERE video_id=?', (yt_video_id,))
    return conn_cursor.fetchone() 

def rip_audio_as_wav(filename, input_dir, output_dir, conn_cursor):
    yt_video_id = filename.split('.')[0]
    _, abr, _, start_t, end_t = get_metadata(yt_video_id, conn_cursor)
    convert = lambda t: str(datetime.timedelta(seconds=int(t)))
    start, end = convert(start_t), convert(end_t)
    bitrate = abr.split('b')[0]
    yt_video_id = filename.split('.')[0]
    input_filepath = os.path.join(input_dir, filename)
    output_filepath = os.path.join(output_dir, yt_video_id+'.wav')
    subprocess.call(['ffmpeg', '-i', input_filepath, '-b:a', bitrate, '-map', 'a', output_filepath])
    #ffmpeg -i R1JT7tcKfOw.mp4 -b:a 96k -map a sample.mp3

def rip_video_as_array(filename, input_dir, output_dir, conn_cursor):
    '''yt_video_id: id of video to extract data from.
    conn_cursor: cursor to metadata db sqlite connection.
    '''
    yt_video_id = filename.split('.')[0]
    fps, _, full_length, start_t, end_t = get_metadata(yt_video_id, conn_cursor)
    start_frame, end_frame = get_start_end_frame(fps, start_t, end_t)

    input_filepath = os.path.join(input_dir, filename)
    output_filepath = os.path.join(output_dir, filename)
    if end_t == -1:
        video_arr = skvideo.io.vread(input_filepath)
    else:
        video_arr = skvideo.io.vread(input_filepath, num_frames=end_frame)
    output = video_arr[start_frame:]
    skvideo.io.vwrite(output_filepath, output)

def process_videos(input_dir, vid_output_dir, aud_output_dir, conn_cursor):
    all_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    for filename in all_files:
        if filename != '.gitkeep':
            video_id = filename.split('.')[0]
            rip_video_as_array(filename, input_dir, vid_output_dir, conn_cursor)
            rip_audio_as_wav(filename, input_dir, aud_output_dir, conn_cursor)

if __name__ == '__main__':
    logging.basicConfig(filename=os.path.join(proj_root, 'logs', time.strftime("DataProcessingLog_%a,%d-%b-%Y-%H:%M:%S_", time.localtime())+time.tzname[0]), \
       format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    conn = sqlite3.connect(os.path.join(proj_root, 'db', 'metadata.db'))
    input_dir = os.path.join(proj_root, 'data', 'video', 'unprocessed')
    vid_output_dir = os.path.join(proj_root, 'data',  'video', 'processed')
    aud_output_dir = os.path.join(proj_root, 'data', 'audio')
    conn = sqlite3.connect(os.path.join(proj_root, 'db', 'metadata.db'))
    c = conn.cursor()

    process_videos(input_dir, vid_output_dir, aud_output_dir, c)

    conn.close()
