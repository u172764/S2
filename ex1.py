import ffmpeg
import os

def video_cut(seconds, name):
    # Nos aseguramos que si el video tiene que durar más de 1 minuto.
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    #APLICAMOS EL COMANDO
    command = 'ffmpeg -i {} -ss 00:00:00 -to {}:{}:{} -c:v copy -c:a copy video_cortado.mp4'.format(name, str(hour),
                                                                                                    str(minutes),
                                                                                                    str(seconds))
    print(command)
    os.system(command)
    print('DONE')

def ex1():
    print('How many seconds do you want the video would to last? \nInsert Here: ')
    N = int(input())
    name_video = 'BigBuckBunny_512kb.mp4'
    video_cut(N, name_video)

