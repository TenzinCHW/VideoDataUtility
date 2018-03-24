import os
import sys
import argparse
import logging
import time
from pytube import YouTube

formats = ['mp4', '3gpp', 'webm']
logger = logging.getLogger('Download logger')

def record_stream_data(yt, stream):
    # TODO decide what info would be useful and record it here
    # stream.fmt_profile -> fps, abr, resolution
    # stream.itag ?
    # stream.filesize
    # stream.player_config_args['keywords'], only some of them are actually useful like keywords
    # stream.mime_type
    # yt.title
    # yt.captions.captions # This is a list, may be empty. Use as condition for valid stream?
    # yt.video_id
    pass

def is_valid_stream(stream):
    res = stream.resolution[:-1]
    return int(res) >= 360 and int(res) <= 480 #and stream.includes_video_track and stream.includes_audio_track

def get_valid_stream(streams):
    for stream in streams[::-1]:  # They are ordered in descending resolution, we want the highest res so we reverse the order
        if is_valid_stream(stream):
            return stream

def single_file_download_url(input_filename, output_folder):
    '''Downloads videos from URL in input_file. URLs should be separated by newlines.
    '''
    with open(input_filename) as f:
        for line in f:
            yt = YouTube(line)
            # TODO check if this file has been downloaded
            streams_by_type = [yt.streams.filter(type='video', subtype=tp).order_by('resolution').all() for tp in formats]
            # TODO parallelize this part. Or not.
            for i, streams in enumerate(streams_by_type):
                stream = get_valid_stream(streams)
                if stream is not None:
                    try:
                        stream.download(output_path=output_folder, filename=yt.video_id)
                        logger.info('Stream for {} with video id {} has been downloaded'.format(yt.title, yt.video_id))
                        record_stream_data(yt, stream)
                        break
                    except:
                        logger.error('{}, video id {}, itag {} not downloaded: connection error or something'.format(yt.title, yt.video_id, stream.itag))
                        pass
                logger.warning('{}, video id {}, subtype {} not downloaded: no valid formats'.format(yt.title, yt.video_id, formats[i]))

def download_folder_url(input_folder, output_folder):
    all_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    for filename in all_files:
        if filename != '.gitkeep':
            single_file_download_url(os.path.join(input_folder, filename), output_folder)

if __name__ == '__main__':
    arguments = sys.argv
    proj_root = os.path.join('..', os.path.dirname(__file__))
    output_folder = os.path.join(proj_root, 'data', 'video', 'unprocessed')
    logging.basicConfig(filename=os.path.join(proj_root, 'logs', time.strftime("DownloadLog_%a,%d-%b-%Y-%H:%M:%S_", time.localtime())+time.tzname[0]), \
       format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    if len(arguments) > 2:
        raise ValueError('Wrong number of arguments. Single argument must be either the relative path from project root directory to directory in which input files live or a single input file.')
    elif len(arguments) == 1:
        input_folder = os.path.join(proj_root, 'input', 'links')
    else:
        parser = argparse.ArgumentParser('Download input folder url')
        parser.add_argument('folder', help='Youtube videos in files in given directory will be downloaded to data/video/unprocessed.')
        input_folder = os.path.join(proj_root, parser.parse_args().folder)

    if os.path.isfile(input_folder):
        # user actually input a file
        single_file_download_url(input_folder)
    else:
        download_folder_url(input_folder, output_folder)
