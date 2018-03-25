import sqlite3
import os

proj_root = os.path.join('..', os.path.dirname(__file__))

if __name__ == '__main__':
    tables = {'metadata' : 'video_id, title, fps, abr, resolution, keywords, itag, mime_type, full_length_sec, captions, start_time, end_time'}
    for k, v in tables.items():
        db = os.path.join(proj_root, 'db', k+'.db')
        conn = sqlite3.connect(db)
        c = conn.cursor()
        try:
            c.execute('''CREATE TABLE {} ({})'''.format(k, v))
        except sqlite3.Error as e:
            print('Error occured: ', e.args[0])
        conn.commit()
        conn.close()
