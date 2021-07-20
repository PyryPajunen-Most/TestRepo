from pywinauto.application import Application
import Notepadwriter


def Notepadwriter_functions():
    Notepadwriter.staring_app("notepad.exe")
    Notepadwriter.type_content(Application, "TESTING TESING TESTING")
    Notepadwriter.saving_file()
 
