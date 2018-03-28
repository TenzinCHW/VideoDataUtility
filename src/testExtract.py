from extractor import Extractor
import os

if __name__ == '__main__':
    proj_root = os.path.join('..', os.path.dirname(__file__))
    vid_dir = os.path.join(proj_root, 'data', 'video', 'processed')
    aud_dir = os.path.join(proj_root, 'data', 'audio')
    db = os.path.join(proj_root, 'db', 'metadata.db')
    #E = Extractor(vid_dir, aud_dir, db)
    #loop = E.video_loop()
    #for vid, item in loop:
    #    stuff = E.get_metadata(vid, ['fps', 'abr', 'captions'])
    #    print(stuff)
    #    for i, frame in enumerate(item.frame_iterator(step_sz=2)):
    #        #print(frame.shape)
    #        print(i)

    #aud = E.audio_loop()
    #for audio in aud:
    #    print(audio)

    count = 0
    ext = Extractor(vid_dir, aud_dir, db)



    vidlooper = ext.video_loop()
    n = 5
    for video_id, video in vidlooper:
        fps, abr, captions = ext.get_metadata(video_id, ['fps','abr','captions'])
        print(fps, abr, captions)
   #     vid_frame_iterator = video.frame_iterator(step_sz=n)
   #     for frame in vid_frame_iterator:
   #         # Do stuff with frame.
   #         print(frame.shape)
   #         count += 1
   # print(count)
