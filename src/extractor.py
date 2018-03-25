import skvideo.io
import os

class Video():
    def __init__(self, filepath, db_dir):
        self.filepath = filepath

    def frame_iterator(h=480, w=854, step_sz=1):
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

    def video_loop():
        all_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        for filename in all_files:
            video_id = filename.split('.')[0]
            yield video_id, Video(os.path.join(self.video_dir, filename)

    def audio_loop():
        pass  # TODO after extracting audio, do this

    def get_metadata(video_id, list_of_attributes):
        '''list_of_attributes can contain title, fps, abr, resolution, keywords, itag, mime_type, full_length_sec, captions, start_time or end_time
        fps - framse per second
        abr - audio bitrate
        resolution - 360p or 480p
        mime_type - a string containint 'video/<type>' where <type> is mp4, 2gpp or webm
        full_length_sec - length of full video before processing
        start_time and end_time - start and end time between which processed video was extracted from unprocessed video
        '''
        query = str(list_of_attributes)[1:-1]
        self.cursor.execute('SELECT {} FROM metadata WHERE video_id=?'.format(query), (video_id,))
        return self.cursor.fetchone()
