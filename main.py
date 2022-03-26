from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMainWindow
from PyQt5.uic import loadUi

import _thread
import time
import sys

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
        QtCore.QTimer.singleShot(50, self.OnLoad)

    def OnLoad(self):
        _thread.start_new_thread(self.run_time,('time',0.001))
    
    def run_time(self, name, delay):
        print("starting time thread")
        while(1):
            t = time.localtime()
            current_time = time.strftime('%H:%M:%S',t)
            self.label.setText(current_time)
            time.sleep(delay)

def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.setWindowTitle("Clock")
    mainwindow.setWindowIcon(QtGui.QIcon('./images/icon.jpg'))
    mainwindow.show()

    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')

main()