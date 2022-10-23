import os

input_name = 'video_cortado.mp4'
check_command = 'ffprobe -i {} -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1 -v 0 > ' \
                'channel_layouts.txt'.format(input_name)
os.system(check_command)
archivo = open("channel_layouts.txt")
channel_layouts = archivo.readline()
if channel_layouts == 'stereo\n':
    stereo2mono = 'ffmpeg -i {} -ac 1 mono.mp4'.format(input_name)
    os.system(stereo2mono)
    # check if the conversion is done good
    check_command = 'ffprobe -i mono.mp4 -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1' \
                    '-v 0 > channel_layouts_response.txt '
    os.system(check_command)
elif channel_layouts == 'mono\n':
    mono2stereo = 'ffmpeg -i {} -ac 2 stereo.mp4'.format(input_name)
    os.system(mono2stereo)
