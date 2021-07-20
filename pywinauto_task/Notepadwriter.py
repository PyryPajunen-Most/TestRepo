from pywinauto import Application, application
import time
import pyautogui

#Opening application
def staring_app(app):
    app = application.Application(backend= "win32")
    app.start("notepad.exe")
    time.sleep(1) #delay
    return app

def type_content(app, content):
    app.Notepad.edit.TypeKeys(content, with_spaces = True) #This line will write the content with spaces.
    time.sleep(1) #delay before saving.

def saving_file():
    app.Notepad.MenuSelect("File -> SaveAs")
    app.SaveAs.dit.SetText("pywinautotask.txt")
    time.sleep(1) #Just for fun
    app.SaveAs.Save.click()
    pyautogui.click(x=1005, y=527)
    time.sleep(3)
    print("File saved!!")



app = staring_app("notepad.exe") # write here the app name.
type_content(app,"Hello from python code - then save the file!!!")
saving_file()
