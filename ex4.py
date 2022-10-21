from subprocess import Popen, PIPE, STDOUT
import os
import subprocess
#saber que tipo de canal es
command ='ffprobe -i video_cortado.mp4 -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1 -v 0'
#saber cuantos canales hay
command2='ffprobe -i video_cortado.mp4 -show_entries stream=channels -select_streams a:0 -of compact=p=0:nk=1 -v 0'


res = Popen(command, stdout=PIPE, stderr=STDOUT)
stdout, err = res.communicate()
print(stdout)