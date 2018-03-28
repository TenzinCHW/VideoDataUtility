# Capstone Labeller

This is a mini project for the purpose of curating, downloading and preprocessing video data for
SUTD's Capstone Team 72. We are a team of 2 Engineering Systems and Design and 5 Information
Systems Technology and Design students working on a machine learning application project for our
final year project.

The goal is to broadly understand occurrences of events, relationships between characters,
significance of objects, actions and places through video and some background data.

## Context for videos we are looking for:
- 2 - 4 people
- must be able to see torso and face (optional)
- must have an indoor context
- must be in English
- must have English captions
- duration of interest should be 2 minutes or less
- include start and end time of the period of interest unless the whole video should be included
- must have some action and interaction between actors involved

## Instructions
### Processing

Run the following for prerequisites:
```
pip install -r requirements.txt
mkdir -p input data/video/processed data/video/unprocessed data/audio logs db
sudo apt-get install ffmpeg
```

In the `input` folder, add a file (any name) with the links to the video and start and end times (in seconds) separated by a space.
e.g.
`https://www.youtube.com/watch?v=yZDQwfBtyO8 24 62`

Run all python files with src directory as working directory in the following order:
```
python initdb.py
python download.py
python process.py
```

### Usage of data

Copy the `data/video/processed`, `data/audio` and `db` directories to the directory where you will be using the data. Also copy `src/extractor.py` to the direcory where you will be using the data.

In your script, create an `Extractor` object using the full paths of the new locations for the `data/video/processed`, `data/audio` and `db` directories.

```
from extractor import Extractor
ext = Extractor(video_path, audio_path, db_path)
```

To get an iterator object over the videos, call video_loop:

```
vidlooper = ext.video_loop()  # Use ext.video_loop(shuffle=False) to loop through videos in same order every time
for video_id, video in vidlooper:
    vid_frame_iterator = video.frame_iterator()  # To get the frames, you must create a frame iterator from each video
    for frame in vid_frame_iterator:
        # Do stuff with frame. frame is a numpy array of h*w*c
        pass
```

You may also include parameters to skip every n frames:
```
n = 5
for video_id, video in vidlooper:
    vid_frame_iterator = video.frame_iterator(step_sz=n)
    for frame in vid_frame_iterator:
        # Do stuff with frame.
        pass
```

To get an iterator object over all the audio filenames, call audio_loop:
```
audlooper = ext.audio_loop()  # Use ext.audio_loop(shuffle=False) to loop through audio filenames in the same order every time
for audio in audlooper:
    print(audio)
```

To get metadata for a video, use the `Extractor` object:
```
vidlooper = ext.video_loop()
for video_id, video in vidlooper:
    fps, abr, captions = extractor.get_metadata(video_id, ['fps','abr','captions'])
    # Do something with fps, abr and captions
```

The interesting attributes listed above come in the following format:
- `fps` is frames per second as an integer
- `abr` is a string of the audio bitrate (i.e. '124kbps')
- `captions` is the srt form of the captions as a string
