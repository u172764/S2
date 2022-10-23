import os


def ex1(seconds, name_video, output_name):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    # APLICAMOS EL COMANDO
    command = 'ffmpeg -i {} -ss 00:00:00 -to {}:{}:{} -c:v copy -c:a copy {}'.format(name_video, str(hour),
                                                                                     str(minutes), str(seconds),
                                                                                     output_name)

    print(command)
    os.system(command)


def ex2(name_video, display_mode, output_name):
    histogram_width = '100'
    histogram_height = '200'
    name_video_scaled = 'scaled_video_for_ex2.mp4'
    command = 'ffmpeg -i {} -vf scale=600:600 {} '.format(name_video, name_video_scaled)
    os.system(command)
    command2 = 'ffmpeg -i {} -vf "split=2[a][b],[a]histogram=display_mode={}, scale={}:{},format=yuva444p[hh],' \
               '[b][hh]overlay" ' \
               '-c:a copy {}'.format(name_video_scaled, display_mode, histogram_width, histogram_height, output_name)
    os.system(command2)


def ex3(video_name, option, output_name):
    command = ''
    if option == '720p':
        command = 'ffmpeg -i {} -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(video_name, output_name)
    elif option == '480p':
        command = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(video_name, output_name)
    elif option == '360x240':
        command = 'ffmpeg -i {} -vf scale=360:240 {}'.format(video_name, output_name)
    elif option == '160x120':
        command = 'ffmpeg -i {} -vf scale=160:120 {}'.format(video_name, output_name)

    os.system(command)



def ex4(video_name):
    check_command = 'ffprobe -i {} -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1 -v 0 > channel_layouts.txt'.format(
        video_name)
    os.system(check_command)
    archivo = open("channel_layouts.txt")
    channel_layouts = archivo.readline()
    if channel_layouts == 'stereo\n':
        stereo2mono = 'ffmpeg -i {} -ac 1 mono.mp4'.format(video_name)
        os.system(stereo2mono)
        # check if the conversion is done good
        check_command = 'ffprobe -i mono.mp4 -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1 -v 0 > channel_layouts_check.txt'
        os.system(check_command)
    elif channel_layouts == 'mono\n':
        mono2stereo = 'ffmpeg -i {} -ac 2 stereo.mp4'.format(video_name)
        os.system(mono2stereo)
        check_command = 'ffprobe -i mono.mp4 -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1 -v 0 > channel_layouts_check.txt'
        os.system(check_command)