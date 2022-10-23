import subprocess
import ffmpeg
import os



def play_yuv_histogram(name, name_scaled, w, h, display_mode):
    w = str(w)
    h = str(h)
    command = 'ffmpeg -i {} -vf scale=600:600 {} '.format(name, name_scaled)
    os.system(command)
    command2 = 'ffmpeg -i {} -vf "split=2[a][b],[a]histogram=display_mode={}, scale={}:{},format=yuva444p[hh],[b][hh]overlay" ' \
               '-c:a copy output.mp4'.format(name_scaled, display_mode, w,h)
    os.system(command2)
    print('DONE')



def ex2():
    name_video = 'video_cortado.mp4'
    name_video_scaled = 'scaled.mp4'
    display_mode = 'stack'
    histogram_width = 100
    histogram_height = 200
    play_yuv_histogram(name_video, name_video_scaled, histogram_width, histogram_height, display_mode)