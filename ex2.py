import subprocess
import ffmpeg
import os

# Inputs
name_video = 'video_cortado.mp4'
name_video_scaled = 'scaled.mp4'
display_mode = 'stack'  # define the way / format in which we will see the histogram
histogram_width = 100  # define the sizes of the histogram
histogram_height = 200


# We create the function that will play the histogram
def play_yuv_histogram(name, name_scaled, w, h, display_mode):
    w = str(w)
    h = str(h)
    command = 'ffmpeg -i {} -vf scale=600:600 {} '.format(name, name_scaled)  # I have to resize the video because it
    # was so small
    os.system(command)  # executing the command
    command2 = 'ffmpeg -i {} -vf "split=2[a][b],[a]histogram=display_mode={}, scale={}:{},format=yuva444p[hh],' \
               '[b][hh]overlay" ' \
               '-c:a copy output.mp4'.format(name_scaled, display_mode, w, h)
    os.system(command2)  # executing the second command


# calling the function
play_yuv_histogram(name_video, name_video_scaled, histogram_width, histogram_height, display_mode)
