import skvideo.io
import sqlite3
import os
import random

class Video():
    def __init__(self, filepath):
        self.filepath = filepath

    def frame_iterator(self, step_sz=1):
        reader = skvideo.io.vreader(self.filepath)
        for i, frame in enumerate(reader):
            if i % step_sz == 0:
                yield frame

class Extractor():
    def __init__(self, video_dir, audio_dir, db):
        '''db is the full path of the metadata.db file'''
        self.video_dir = video_dir
        self.audio_dir = audio_dir
        self.db = db
        self.conn = sqlite3.connect(db)
        self.conn_c = self.conn.cursor()

    def video_loop(self, shuffle=True):
        all_files = [f for f in os.listdir(self.video_dir) if os.path.isfile(os.path.join(self.video_dir, f))]
        if shuffle:
            random.shuffle(all_files)
        for filename in all_files:
            video_id = filename.split('.')[0]
            yield video_id, Video(os.path.join(self.video_dir, filename))

    def audio_loop(self, shuffle=True):
        all_files = [f for f in os.listdir(self.audio_dir) if os.path.isfile(os.path.join(self.audio_dir, f))]
        if shuffle:
            random.shuffle(all_files)
        for filename in all_files:
            yield filename

    def get_metadata(self, video_id, list_of_attributes):
        '''list_of_attributes can contain title, fps, abr, resolution, keywords, itag, mime_type, full_length_sec, captions, start_time or end_time
        fps - framse per second
        abr - audio bitrate
        resolution - 360p or 480p
        mime_type - a string containint 'video/<type>' where <type> is mp4, 2gpp or webm
        full_length_sec - length of full video before processing
        start_time and end_time - start and end time between which processed video was extracted from unprocessed video
        '''
        query = ','.join(list_of_attributes)
        self.conn_c.execute('SELECT {} FROM metadata WHERE video_id=?'.format(query), (video_id,))
        return self.conn_c.fetchone()

    def __del__(self):
        self.conn.close()
