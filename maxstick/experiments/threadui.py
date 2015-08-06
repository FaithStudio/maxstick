'''''
testing thread ui
by Carlos Anguiano
'''
import MaxPlus
from PySide import QtCore,QtGui
import sys, random

#inherit from Qthread and setup our own thread class
class upateThread(QtCore.QThread):
    progress = QtCore.Signal(str) #create a custom sygnal we can subscribe to to emit update commands
    def __init__(self,parent=None):
        super(upateThread,self).__init__(parent)
        self.exiting = False

    def run(self):
        while True:
            self.msleep(10)
            self.progress.emit(str(random.randint(0,100)))

class myDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        super(myDialog,self).__init__(parent)
        self.resize(200,0)
        self.qlabel = QtGui.QLabel(self)
        self.qlabel.setText('Processor:')
        self.qlabelSt = QtGui.QLabel(self)
        self.btn = QtGui.QToolButton(self)
        l = QtGui.QVBoxLayout(self)

        l.addWidget(self.qlabel)
        l.addWidget(self.qlabelSt)
        l.addWidget(self.btn)

        self.btn.pressed.connect(lambda :self.qlabelSt.setText(str(random.randint(0,100))))

        self.setupUpdateThread()

    def updateText(self,text):
        self.qlabel.setText('random number: '+text)
        MaxPlus.Core.EvalMAXScript("delete objects;teapot();completeRedraw();windows.processPostedMessages()")

    def setupUpdateThread(self):
        self.updateThread = upateThread()
        #connect our update functoin to the progress signal of the update thread
        self.updateThread.progress.connect(self.updateText,QtCore.Qt.QueuedConnection)
        if not self.updateThread.isRunning():#if the thread has not been started let's kick it off
            self.updateThread.start()


class _GCProtector(object):
    controls = []


if __name__ == '__main__':
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])

    win = myDialog()
    _GCProtector.controls.append(win)
    win.show()