import ffmpeg
import os

print('How many seconds do you want the video would to last? \nInsert Here: ')
N = int(input())  # the user's input indicates hoy many seconds we are going to cut
name_video = 'BigBuckBunny_512kb.mp4'


def video_cut(seconds, name):
    # Format transformation. To manage errors if the time is bigger than 60s.
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    # ffmpeg command to cut the video between 00:00:00 and the desired time
    command = 'ffmpeg -i {} -ss 00:00:00 -to {}:{}:{} -c:v copy -c:a copy video_cortado.mp4'.format(name, str(hour),
                                                                                                    str(minutes),
                                                                                                    str(seconds))
    # executing the command
    os.system(command)


video_cut(N, name_video)
