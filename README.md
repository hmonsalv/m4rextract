# tonemaker

Tonemaker creates a M4R audio extract from a youtube video in an easy way.

## Quickstart

Build the Docker image:
```python
docker build -t tonemaker .
```
Every time you want to generate a new audio extract, run the container as follows:
```python
docker run -it --rm -v /path/to/output/folder:/app/tones tonemaker tonemaker.sh "AUDIO_EXTRACT" "YOUTUBE_URL" StartMin StartSec
```
For example:
```python
docker run -it --rm -v /path/to/output/folder:/app/tones tonemaker tonemaker.sh "My audio extract" "https://www......." 0 30
```
Tonemaker will generate the **My audio extract.m4r** audio extratct from the youtube video starting on **0:30**, will save it to **/path/to/output/folder**, and will destrroy the container once done.

## Dependencies

Tonemaker uses the following python libraries:

 - [pydub](https://github.com/jiaaro/pydub)
 - [youtube_dl](https://github.com/ytdl-org/youtube-dl)

And also, for audio format conversion: [ffmpeg](http://www.ffmpeg.org/)
