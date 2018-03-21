from os import path
import os
import sys
import argparse
from pytube import YouTube

def record_stream_data(stream):
    # TODO decide what info would be useful and record it here
    # stream.fmt_profile -> fps, abr, resolution
    # stream.filesize
    # stream.player_config_args, only some of them are actually useful like keywords
    # stream.mime_type

    pass

def is_valid_stream(stream):
    # TODO implement the conditions for a video stream to be valid eg. quality, resolution, fps
    # maybe based on stream.itag?
    return stream.resolution >= 360

def single_file_download_urls(input_filename, output_folder):
    '''Downloads videos from URL in input_file. URLs should be separated by newlines.
    '''
    with open(input_filename) as f:
        for line in f:
            try:
                yt = YouTube(line)
                streams = yt.streams.filter(progressive=True).desc().all()  # We only want the whole file
                print(streams)
                for stream in streams:
                    if is_valid_stream(stream):
                        # TODO parallelize this part. Or not.
                        stream.download(output_folder)
                        # TODO log that this stream has been downloaded
                        break
                # TODO log that this video wasn't downloaded because none of its streams satisfied is_valid_stream
            except:
                print('something bad happened while downloading')
                pass
                # TODO log that an error occurred while trying to download this video

def download_folder_url(input_folder, output_folder):
    all_files = [f for f in os.listdir(input_folder) if path.isfile(path.join(input_folder, f))]
    for filename in all_files:
        single_file_download_urls(path.join(input_folder, filename), output_folder)

if __name__ == '__main__':
    arguments = sys.argv
    proj_root = path.join('..', path.dirname(__file__))
    output_folder = path.join(proj_root, 'data', 'video', 'unprocessed')
    if len(arguments) > 2:
        raise ValueError('Wrong number of arguments. Single argument must be either the relative path from project root directory to directory in which input files live or a single input file.')
    elif len(arguments) == 1:
        input_folder = path.join(proj_root, 'input')
    else:
        parser = argparse.ArgumentParser('Download input folder url')
        parser.add_argument('folder', help='Youtube videos in files in given directory will be downloaded to data/video/unprocessed.')
        input_folder = path.join(proj_root, parser.parse_args().folder)

    if path.isfile(input_folder):
        # user actually input a file
        single_file_download_urls(input_folder)
    else:
        download_folder_url(input_folder, output_folder)
