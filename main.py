# coding: utf8

import sys
from PyQt4 import QtGui,QtCore
from formmanager import Formmanager

def main():

    app=QtGui.QApplication(sys.argv)
    myform=Formmanager()
    myform.MainWindow.show()

    sys.exit(app.exec_())

    pass


if __name__ == '__main__':
    main()


