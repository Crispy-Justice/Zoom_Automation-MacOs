import subprocess
import os
import pyautogui
import pyttsx3
from join import *
from info import *
from time import sleep
from datetime import datetime

# Clears the screen.
os.system('clear')

# Prints the intro.
print('''

    ███████╗ ██████╗  ██████╗ ███╗   ███╗     █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
    ╚══███╔╝██╔═══██╗██╔═══██╗████╗ ████║    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
      ███╔╝ ██║   ██║██║   ██║██╔████╔██║    ███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
     ███╔╝  ██║   ██║██║   ██║██║╚██╔╝██║    ██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
    ███████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                              
''')

# Initiates Pyttsx3.
engine = pyttsx3.init()

date_time = str(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))


while True:
    
    try:  
        
        while True:
            
            log_file = open("log.txt","a")
            
            _input = str(input('> ')).lower().strip().replace(" ", "")
            
            # Math
            if _input == 'math':
                info = join.math(subject, meetingid, meetingpass)
                break
            # Chemistry
            elif _input == 'chemistry' or _input == 'chem':
                info = join.chemistry(subject, meetingid, meetingpass)
                break
            # Physics
            elif _input == 'physics' or _input == 'phy':
                info = join.physics(subject, meetingid, meetingpass)
                break
            # Biology
            elif _input == 'biology' or _input == 'bio':
                info = join.biology(subject, meetingid, meetingpass)
                break
            # English
            elif _input == 'english' or _input == 'eng':
                info = join.english(subject, meetingid, meetingpass)
                break
            # History
            elif _input == 'history' or _input == 'his':
                info = join.history(subject, meetingid, meetingpass)
                break
            # Geography
            elif _input == 'geography' or _input == 'geo':
                info = join.geography(subject, meetingid, meetingpass)
                break
            # Help
            elif _input == 'help' or _input == '-h':
                join._help()
            elif _input == 'help-tt' or _input == '-h-tt':
                join.timetable()
            # to Quit
            elif _input == 'quit' or _input == '-q':
                os.system('clear')
                exit()
            else:
                print('\nInvalid Input.')
                print(data_help)
    except:
        os.system('clear') # Clears screen.
        exit() # Exits code.
    

    try:
        def sign_in(subject,meeting_id,pswd):

            engine.say(f'Joining {subject} meeting.')
            engine.runAndWait()
            
            print(f'Joining {subject} meeting...')
            
            log_file.write(f'\n{date_time}          Joined {subject} meeting.')

            # Opens Zoom.
            subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])

            sleep(10)
            
            # Locates & Clicks the Join button.
            position_join = pyautogui.locateCenterOnScreen('join_button.png')
            pyautogui.click(position_join)
            # for MacBooks with RETINA DISPLAY.
            #pyautogui.click(position_join.x/2,position_join.y/2)
         
            sleep(5)
            
            # Enters the Meeting Id.
            pyautogui.press('tab',presses=2)
            pyautogui.write(meeting_id)
            pyautogui.press('enter')
            sleep(7)
            
            # Enters the Password.
            pyautogui.write(pswd)
            pyautogui.press('enter')
            
            sleep(2)
            engine.say(f'Joined {subject} meeting.')
            engine.runAndWait()
            engine.stop()
            print(f'Joined {subject} meeting.')

        sign_in(info[0],info[1],info[2])

    except Exception as exc:
        print(exc)
        print('An Error Occured.')
        