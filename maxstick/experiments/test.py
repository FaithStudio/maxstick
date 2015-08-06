import time
import random

from PySide import QtGui
from PySide import QtCore

import MaxPlus


class MyThread(QtCore.QThread):

    progress = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(MyThread,self).__init__(parent)
        self.exiting = False

    def run(self):
        while True:
            self.msleep(3000)
            self.progress.emit("delete objects;teapot();completeRedraw();windows.processPostedMessages()")


class MyWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.label = QtGui.QLabel("narf")
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.thread = None

    def display(self, txt):
        self.label.setText(txt)
        MaxPlus.Core.EvalMAXScript(txt)

    def show(self):
        super(MyWidget, self).show()
        self.thread = MyThread(self)
        self.thread.progress.connect(self.display, QtCore.Qt.QueuedConnection)
        if not self.thread.isRunning():
            self.thread.start()


class _GCProtector(object):
    controls = []


if __name__ == '__main__':
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])

    widget = MyWidget()
    _GCProtector.controls.append(widget)
    widget.show()

    app.exec_()
