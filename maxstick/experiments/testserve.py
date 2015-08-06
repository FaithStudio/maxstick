import os
import sys
import ctypes
import threading

from PySide import QtGui

import MaxPlus



class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        print("running...")
        time.sleep(2)
        # while not self._stop.isSet():
        #     time.sleep(0.5)
        #     print time.time()

    def stop(self):
        self._stop.set()


class _GCProtector(object):
    controls = []


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.btn_run = QtGui.QPushButton('Run')
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.btn_run)
        self.setLayout(layout)
        self.btn_run.clicked.connect(self.run)

        self.thread = None

    def run(self):
        if not self.thread:
            print "Serving"
            self.btn_run.setText('Stop...')
            self.thread = MyThread()
            self.thread.start()
        else:
            print "Stopping"
            self.btn_run.setText('Run')
            self.thread.stop()
            self.thread = None

    def closeEvent(self, *args, **kwargs):
        if self.thread:
            print "Stopping"
            self.btn_run.setText('Run')
            self.thread.stop()
            self.thread = None
        QtGui.QWidget.closeEvent(*args, **kwargs)


if __name__ == '__main__':
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])

    window = MyWindow()
    _GCProtector.controls.append(window)
    window.show()

    capsule = window.effectiveWinId()
    ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
    ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
    ptr = ctypes.pythonapi.PyCObject_AsVoidPtr(capsule)

    MaxPlus.Win32.Set3dsMaxAsParentWindow(ptr)

