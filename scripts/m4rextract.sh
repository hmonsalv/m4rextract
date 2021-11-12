#!/bin/sh
#
# This script downloads the mp3 audio of a youtube video, cuts 30 sec
# starting on the mm:ss specified, adds fade in and out and converts 
# it to a M4R audio file.
#
# Arguments:
#       - AUDIO_FILE_NAME: name of the output file (without extension)
#	- YOUTUBE_URL: URL of the youtube video
#	- START_MIN: min of the video from where start the tone
#	- START_SEC: sec of the minute of the video from where start the tone
#
# Output:
#       - ./tones/AUDIO_FILE_NAME.m4r   (./tones folder must exist)
#
# Example: #	   
#
#   ./tonemaker.sh "My tone" https://www.youtube.com/watch?v=_abcdef 0 15
#	Output >>> ./tones/My tone.m4r
#

# Vars
AUDIO_FILE_NAME=$1
YOUTUBE_URL=$2
START_MIN=$3
START_SEC=$4

# Download mp3 from youtube
python youtubetomp3.py $YOUTUBE_URL

# Rename mp3
mv *.mp3 output.mp3

# Cut mp3 (30secs) from selected start and adds fade in and out
python cutmp3.py $START_MIN $START_SEC

# Converts mp3 to m4a
ffmpeg -i output-extract.mp3 -c:a aac -vn output-extract.m4a

# Rename file
mv output-extract.m4a "$AUDIO_FILE_NAME.m4r"
mv *.m4r m4r

# Remove temporal files
rm -rf output*
