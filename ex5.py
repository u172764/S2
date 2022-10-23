import ex1
import ex2
import ex3
import ex4
import PySimpleGUI as sg

layout = [[sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
                        [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
                        [sg.Submit(), sg.Cancel()]]

window = sg.Window('Rename Files or Folders', layout)

event, values = window.read()
window.close()
folder_path, file_path = values[0], values[1]       # get the data from the values dictionary
print(folder_path, file_path)

