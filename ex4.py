import os

input_name = 'video_cortado.mp4'
# we check if the video's audio is stereo or mono and save the answer in a text file.
check_command = 'ffprobe -i {} -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1 -v 0 > ' \
                'channel_layouts.txt'.format(input_name)

os.system(check_command)
archivo = open("channel_layouts.txt")  # we open the file where the mono or stereo message is stored
channel_layouts = archivo.readline()  # the message is stored in the channel_layout variable
# if the audio is stereo we will convert it to mono and vice-versa

if channel_layouts == 'stereo\n':
    stereo2mono = 'ffmpeg -i {} -ac 1 mono.mp4'.format(input_name)
    os.system(stereo2mono)
    # check if the conversion is done good
    check_command = 'ffprobe -i mono.mp4 -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1' \
                    '-v 0 > channel_layouts_response.txt '
    # we can check if the conversion has done it well saving it into another text file
    os.system(check_command)
elif channel_layouts == 'mono\n':
    mono2stereo = 'ffmpeg -i {} -ac 2 stereo.mp4'.format(input_name)
    os.system(mono2stereo)
    # check if the conversion is done good
    check_command = 'ffprobe -i mono.mp4 -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1' \
                    '-v 0 > channel_layouts_response.txt '
    # we can check if the conversion has done it well saving it into another text file
    os.system(check_command)