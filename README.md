# M4Rextract

M4Rextract creates a M4R audio extract from a youtube video in an easy way.

## Quickstart

Build the Docker image:
```python
docker build -t m4rextract .
```
Every time you want to generate a new audio extract, run the container as follows:
```python
docker run -it --rm -v /path/to/output/folder:/app/m4r m4rextract m4rextract.sh "AUDIO_EXTRACT" "YOUTUBE_URL" StartMin StartSec
```
For example:
```python
docker run -it --rm -v /path/to/output/folder:/app/m4r m4rextract m4rextract.sh "My audio extract" "https://www......." 0 30
```
M4Rextract will generate the **My audio extract.m4r** audio extract from the youtube video starting on **0:30**, will save it to **/path/to/output/folder**, and will destroy the container once done.

## Dependencies

M4Rextract uses the following python libraries:

 - [pydub](https://github.com/jiaaro/pydub)
 - [yt-dlp](https://github.com/ytdl-patched/yt-dlp)

And also, for audio format conversion: [ffmpeg](http://www.ffmpeg.org/)
