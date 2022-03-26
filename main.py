from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMainWindow
from PyQt5.uic import loadUi

import _thread
import time
import sys
import random

puns = [
    'What is a belt made of clocks called?\nWaist of time.',
    'My favorite movie is \'The Hunchback of Notre Dame\'.\n I love it when the protagonist has a twisted back story.',
    'What do you call double standards? Burning a body at a crematorium is being respectful but doing the same at home is called destroying evidence!',
    'What do you do when elderly relatives tease you at weddings saying you\'re next? You do the same to them at funerals!'
]

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        print("main window initialized")
        loadUi("clock.ui",self)
        self.label_1.setWordWrap(True)
        self.label_1.setContentsMargins(10,10,10,10)
        QtCore.QTimer.singleShot(50, self.OnLoad)

    def OnLoad(self):
        _thread.start_new_thread(self.run_time,('time',0.001))
    
    def run_time(self, name, delay):
        flag = 0 #to be used to ensure pun is only updated once at 5 seconds
        print("starting time thread")
        self.label_1.setText(puns[random.randint(0,len(puns)-1)])
        while(1):
            t = time.localtime()
            current_time = time.strftime('%H:%M:%S',t)
            self.label.setText(current_time)
            
            if(t.tm_sec%10 == 0 and flag == 0):
                print(t.tm_sec)
                self.label_1.setText(puns[random.randint(0,len(puns)-1)])
                flag = 1

            if((t.tm_sec+1)%10 == 0 and flag == 1):
                flag = 0

            time.sleep(delay)

def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.setWindowTitle("Pun Clock")
    mainwindow.setWindowIcon(QtGui.QIcon('./images/icon.jpg'))
    mainwindow.show()

    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')

main()