import ex5_functions as act
import PySimpleGUI as sg

layout = [[sg.Text('Name of the video (with extension)', size=(30, 1)), sg.InputText()],
          [sg.Text('Be careful, the file must be inside the same folder')],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Ffmpeg variations', layout)

event, values = window.read()
video_name = values[0]  # obtenemos el nombre del video al que le queremeos aplciar los cambios
window.close()
if event == 'Submit':
    layout = [[sg.Text('SELECT THE ACTION YOU WANT TO DO', size=(40, 1))],
              [sg.Button(button_text='Cut N seconds'), sg.Button(button_text='View Histogram'),
               sg.Button(button_text='Resize the video'),
               sg.Button(button_text='Change channels')]]

    window = sg.Window('Actions to apply', layout)
    event2, values = window.read()
    window.close()
    if event2 == 'Cut N seconds':
        layout = [[sg.Text('Seconds to cut', size=(30, 1)), sg.InputText()],
                  [sg.Text('Name of the file to save the result', size=(30, 1)), sg.InputText()],
                  [sg.Submit()]]
        window = sg.Window('Exercise one', layout)
        event3, values = window.read()
        act.ex1(int(values[0]), video_name, values[1])
    elif event2 == 'View Histogram':
        layout = [[sg.Text('Name of the file to save the result', size=(30, 1)), sg.InputText()],
                  [sg.Button('stack')],  [sg.Button('parade')],  [sg.Button('overlay')]]
        window = sg.Window('Exercise two', layout)
        display_mode, values = window.read()
        act.ex2(video_name, display_mode, values[0])

    elif event2 == 'Resize the video':
        layout = [[sg.Text('Name of the file to save the result', size=(30, 1)), sg.InputText()],
                  [sg.Button('720p')], [sg.Button('480p')], [sg.Button('360x240')], [sg.Button('160x120')]]
        window = sg.Window('Exercise three', layout)
        event3, values = window.read()
        act.ex3(video_name, event3, values[0])

    elif event2 == 'Change channels':
        layout = [[sg.Text('If the file is mono you will convert to stereo.\nIf the file is stereo you will convert to mono', size=(50, 5))],
                  [sg.Submit()]]
        window = sg.Window('Exercise four', layout)
        event3, values = window.read()
        act.ex4(video_name)
