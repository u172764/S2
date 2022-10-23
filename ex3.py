import ffmpeg
import os

print("720p = 1 \n480p = 2\n360x240 = 3\n160x120 = 4\nSELECCIONA LA OPCIÓN")
option = int(input())
vide_name = 'BigBuckBunny_512kb.mp4'


def convert_to(option, name):
    command = ''
    if option == 1:
        command = 'ffmpeg -i {} -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 output_ex3.mp4'.format(name)
    elif option == 2:
        command = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 output_ex3_480.mp4'.format(name)
    elif option == 3:
        command = 'ffmpeg -i {} -vf scale=360:240 output_ex3.mp4'.format(name)
    elif option == 4:
        command = 'ffmpeg -i {} -vf scale=160:120 output_ex3.mp4'.format(name)

    os.system(command)


convert_to(option, vide_name)
