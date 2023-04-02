# Visit => https://github.com/ytdl-org/youtube-dl
#
# This script downloads the audio of a youtube video as mp3
#
# Arguments:
#       - youtube_url: url of the youtube video
#
# Output:
#       - ./output.mp3
#
# Example:
#
#   python youtubetomp3.py https://www.youtube.com/watch?v=_abcdef


#import youtube_dl
import yt_dlp
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if __name__ == "__main__":
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[1:]
        ydl.download(filenames)

