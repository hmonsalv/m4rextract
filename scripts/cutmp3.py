# Visit => https://github.com/jiaaro/pydub
#
# This script extracts 30sec from a mp3 file.
#
# Arguments:
#       - startMin: minute where to start the segment
#       - startSec: second of the minute where to start the segment
#
# Output:
#       - ./output-extract.mp3
#
# Example:
#
#   python cutmp3.py 0 15
#

import sys
from pydub import AudioSegment

files_path = './'
file_name = 'output'

startMin = int(sys.argv[1])
startSec = int(sys.argv[2])
duration = 30

# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
#endTime = endMin*60*1000+endSec*1000
endTime = startTime+duration*1000

# Opening file and extracting segment
song = AudioSegment.from_mp3( files_path+file_name+'.mp3' )
extract = song[startTime:endTime]

# Fade in and out
fades = extract.fade_in(2000).fade_out(1000)

# Saving
fades.export( file_name+'-extract.mp3', format="mp3")
