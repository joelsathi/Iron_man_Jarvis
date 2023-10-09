import os

class Open_application():
    def Open_calculator(self):
        os.system('cmd /c calc')

    def Open_calendar(self):
        os.system("cmd /c start outlookcal:")

    def Open_clock(self):
        os.system("cmd /c start ms-clock:")

    def Open_notepad(self):
        os.system("cmd /c notepad")

    def Open_Camera(self):
        os.system("cmd /c start microsoft.windows.camera:")

    def Open_mail(self):
        os.system("cmd /c start outlookmail:")

    def Open_word(self):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk")

    def Open_excel(self):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk 2013.lnk")

    def Open_powerpoint(self):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk 2013.lnk")

    def Open_pycharm(self):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PyCharm\PyCharm Community Edition with Anaconda plugin 2020.1.2.lnk")

    def Open_IDLE(self):
        os.startfile(r"C:\Users\MAC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.8\IDLE (Python 3.8 32-bit).lnk")

    def Open_telegram(self):
        os.startfile(r"C:\Users\MAC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk")

    def Open_Zoom(self):
        os.startfile(r"C:\Users\MAC\AppData\Roaming\Zoom\bin\Zoom.exe")



#bot  = Open_application()
#bot.Open_mail()