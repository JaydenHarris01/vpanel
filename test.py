import sys
from PyQt4 import QtGui, QtCore
  
class window(QtGui.QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(300, 300, 1200, 700)
        self.setWindowTitle("V - Panel")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100, 100)
        btn.move(100, 100)

        btn1= QtGui.QPushButton("Quit", self)
        btn1.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn1.resize(100, 100)
        btn1.move(300, 100)
        self.show()
    
         
        

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = window()
    sys.exit(app.exec_())

run()
