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
mkdir -p data/video/processed data/video/unprocessed data/audio logs db
sudo apt-get install ffmpeg
```

Run all python files with src directory as working directory in the following order:
```
python initdb.py
python download.py
python process.py
```

### Usage of data

Copy the `data/video/processed`, `data/audio` and `db` directories to the directory where you will be using the data. Also copy `src/extractor.py` to the direcory where you will be using the data.

In your script, create an `Extractor` object using the full paths of the new locations for the `data/video/processed`, `data/audio` and `db` directories.

```extractor = Extractor(video_path, audio_path, db_path)```

To get an iterator object over the videos, call video_loop:

```
vidlooper = extractor.video_loop()
for video_id, video in vidlooper:  # To get the frames, you must create a frame iterator from each video
    vid_frame_iterator = video.frame_iterator()
    for frame in vid_frame_iterator:
        # Do stuff with frame. frame is a numpy array of h*w*
        pass
```

You may also include parameters to get a different sized numpy array for each frame or to skip every n frames:
```
n = 5
for video in vidlooper:
    vid_frame_iterator = video.frame_iterator(h=480, w=854, step_sz=n)
    for frame in vid_frame_iterator:
        # Do stuff with frame.
        pass
```

To get metadata for a video, use the `Extractor` object.
`extractor.get_metadata(video_id, ['fps','abr','captions'])`

The interesting attributes listed above come in the following format:
- `fps` is frames per second as an integer
- `abr` is a string of the audio bitrate (i.e. '124kbps')
- `captions` is the srt form of the captions as a string
