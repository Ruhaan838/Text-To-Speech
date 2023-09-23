import PySimpleGUI as sg
from gtts import gTTS
import os
sg.theme('Topanga')
layout = [
    [sg.Text(' - - -: ENTER THE TEXT :- - - ', size=(15, 1),font=('Arial Bold', 20), expand_x=True, justification='center')], 
    [sg.Multiline(key='-INPUT-',size=(10,10),expand_x=True,expand_y=True,justification='left')],
    [sg.Button("Open text")],
    [sg.Text('',size=(100,10),key='-OUTPUT-')],
    [sg.Button("Convert"),sg.Button("Open (.mp3)"), sg.Button("Close")]
]

window = sg.Window('Text To Speech Converter', layout,size=(850,450))
icon = 'Screenshot 2023-09-10 205819.ico'
window.set_icon(icon)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == 'Convert':
        text_to_convert = values['-INPUT-']
        language = 'en'

        if text_to_convert:
            myobj = gTTS(text=text_to_convert, lang=language, slow=False)
            myobj.save("texttospeech.mp3")
            sg.popup('Text converted to speech and saved as "texttospeech.mp3"', title='Conversion Complete')
        else:
            sg.popup_error('Please enter text to convert.', title='Error')
    elif event == 'Open (.mp3)':
       text_to_convert = values['-INPUT-']
       if text_to_convert:
            os.system("texttospeech.mp3")        
       else :
           sg.popup_error('Please submit the File or Enter The text.',title='Error')
    elif event == 'Open text':
        file_path = sg.popup_get_file(
            'Select a text file',
            file_types=(('Text files', '*.txt'),),
            initial_folder='/home/user' 
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                    window['-INPUT-'].update(text)
            except Exception as e:
                sg.popup_error(f'Error opening the file: {str(e)}', title='Error')      
window.close()
                  