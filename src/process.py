import skvideo
import os
import skvideo.measure
import numpy as np

def get_start_end(yt_video_id):
    # TODO get start and end of video
    pass

def rip_audio_as_wav(media_file):
    pass

def rip_video_as_array(media_file):
    pass


import skvideo.io
import skvideo.datasets
import skvideo.utils

filename = os.path.join('..','data','video','unprocessed','vLfAtCbE_Jc.mp4')

print("Loading all channels")
vid = skvideo.io.vread(filename, outputdict={"-pix_fmt": "gray"})[:, :, :, :]
vid1 = skvideo.io.vread(filename)#[:, :, :, 0]
vid = skvideo.utils.vshape(vid)
vid1 = skvideo.utils.vshape(vid1)
print(vid.shape)
print(vid1.shape)
print("")

skvideo.io.vwrite("rgb.mp4", vid1[:, :, :, :])

if __name__ == '__main__':
    pass
