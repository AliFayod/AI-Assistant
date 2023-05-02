import os
import glob
import subprocess
import main
def openApp(app,close =False):
    app = app.lower()
    try:
        #Calculator
        if app == "calculator":
            q = os.system("calc.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im CalculatorApp.exe")
        #notepad
        elif app == "notepad":
            q = os.system("notepad.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im notepad.exe")
        #Camera
        elif app == "camera":
            q = os.system("start microsoft.windows.camera:")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im WindowsCamera.exe")
        #word
        elif app == "word":
            q = os.system("start winword")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im winword.exe")
        #excel
        elif app == 'excel':
            q = os.system("start excel")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im excel.exe")
        #powerpoint
        elif app == "powerpoint" or app == "power point":
            q = os.system("start powerpnt")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im powerpnt.exe")
        # Open Outlook
        elif app == "outlook":
            q = os.system("start outlook")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im outlook.exe")
        # Access
        elif app == "access":
            q = os.system("start msaccess")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im msaccess.exe")
        #Microsoft teams
        elif app == "microsoft teams" or app == "teams":
            q = os.system("start teams")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im teams.exe")
        #Skype
        elif app == 'skype':
            q = os.system("start skype")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im skype.exe")
        #Windows Media Player
        elif app == 'media player' or app == 'windows media player':
            q = os.system("start wmplayer")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im setup_wm.exe")
        #VLC
        elif app == 'vlc':
            q = os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im vlc.exe")
        #Zoom, you have to change the path to your user instead of newtech.
        elif app == 'zoom':
            q = subprocess.Popen(r"C:\Users\newtech\AppData\Roaming\Zoom\bin\Zoom.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im Zoom.exe")
        #Atom, you have to change the path to your user instead of newtech.
        elif app == 'atom':
            q = os.startfile(r"C:\\Users\\newtech\\AppData\\Local\\atom\\atom.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im powerpnt.exe")
        #PyCharm
        elif app =='pycharm':
            # Search for PyCharm executable with wildcard in path
            path = glob.glob("C:\\Program Files\\JetBrains\\PyCharm*\\bin\\pycharm64.exe")[0]
            # Open PyCharm
            q = os.startfile(path)
            if close == False:
                return q
            else:
                os.system("taskkill /f /im pycharm64.exe")
        #VS Code
        elif app == 'vscode' or app == 'vs code':
            q = os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im code.exe")
        #Screen Recorder
        elif app == 'screen recorder' or app == 'recorder' or app == 'recorder screen':
            q = os.startfile("C:\\Windows\\System32\\psr.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im psr.exe")
        #Google Chrome
        elif app == 'chrome' or app == 'chrome browser':
            q = os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im chrome.exe")
        #Mozilla Firefox
        elif app == 'firefox' or app == 'firefox browser':
            q = os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im firefox.exe")
        # Microsoft Edge
        elif app == 'edge' or app == 'edge browser':
            q = os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            if close == False:
                return q
            else:
                os.system("taskkill /f /im msedge.exe")

        else:
            raise Exception

    except Exception as exception:
        main.talk("sorry I can not find the application, please go to Apps script and add the application with its path")









