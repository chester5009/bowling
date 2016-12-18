# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(816, 737)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 30, 731, 631))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.main = QtGui.QWidget()
        self.main.setObjectName(_fromUtf8("main"))
        self.label = QtGui.QLabel(self.main)
        self.label.setGeometry(QtCore.QRect(280, 60, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.main)
        self.lineEdit.setGeometry(QtCore.QRect(240, 320, 231, 27))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.main)
        self.label_2.setGeometry(QtCore.QRect(-10, 209, 741, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.main)
        self.pushButton.setGeometry(QtCore.QRect(310, 450, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.stackedWidget.addWidget(self.main)
        self.otvet = QtGui.QWidget()
        self.otvet.setObjectName(_fromUtf8("otvet"))
        self.tableWidget = QtGui.QTableWidget(self.otvet)
        self.tableWidget.setGeometry(QtCore.QRect(110, 30, 511, 551))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_2 = QtGui.QPushButton(self.otvet)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 590, 211, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.otvet)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 590, 141, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_3 = QtGui.QLabel(self.otvet)
        self.label_3.setGeometry(QtCore.QRect(320, 10, 68, 17))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.stackedWidget.addWidget(self.otvet)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Bowling", None))
        self.label_2.setText(_translate("MainWindow", "Укажите название файла. Файл должен лежать в одной директории с программой ", None))
        self.pushButton.setText(_translate("MainWindow", "Готово", None))
        self.pushButton_2.setText(_translate("MainWindow", "Внести изменения", None))
        self.pushButton_3.setText(_translate("MainWindow", "Новый раунд", None))

