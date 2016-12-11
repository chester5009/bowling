# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from form import Ui_MainWindow
from manager import Manager

class Formmanager():

    def __init__(self):
        self.ui=Ui_MainWindow()
        self.MainWindow=QtGui.QMainWindow()

        self.ui.setupUi(self.MainWindow)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.setSignals()

        self.manager = Manager()

        pass

    def calculate(self):
        manager = Manager()
        manager.loadPlayers('tablica.csv')

        manager.sortPlayers()
        manager.setRanks()
        manager.showPlayers()


    def goToOtvety(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.manager.loadPlayers(self.ui.lineEdit.text())
        self.manager.sortPlayers()
        self.manager.setRanks()
        self.createTable(3,len(self.manager.players))
        self.fillTable()

    def createTable(self,cols,rows):
        table=self.ui.tableWidget
        table.setColumnCount(cols)
        table.setRowCount(rows)
        pass

    def fillTable(self):
        colors=[QtGui.QColor(21,212,72),
                QtGui.QColor(181, 191, 38),
                QtGui.QColor(209, 78, 48)]
        for p in self.manager.players:
            index=self.manager.players.index(p)
            newItem1=QtGui.QTableWidgetItem()
            newItem2=QtGui.QTableWidgetItem()
            newItem3=QtGui.QTableWidgetItem()
            newItem1.setText(QtCore.QString(unicode(p.name)))
            newItem2.setText(QtCore.QString(unicode(p.score)))
            newItem3.setText(QtCore.QString(unicode(p.status)))

            newItem3.setBackgroundColor(colors[p.status-1])

            self.ui.tableWidget.setItem(index,0,newItem1)
            self.ui.tableWidget.setItem(index,1,newItem2)
            self.ui.tableWidget.setItem(index,2,newItem3)
            index+=1

        pass

    def setSignals(self):
        self.ui.pushButton.clicked.connect(self.goToOtvety)

    pass



