# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from form import Ui_MainWindow
from manager import Manager

class Formmanager():

    def __init__(self):
        self.colors = [QtGui.QColor(21, 212, 72),
                  QtGui.QColor(181, 191, 38),
                  QtGui.QColor(209, 78, 48)]
        self.ui=Ui_MainWindow()
        self.MainWindow=QtGui.QMainWindow()

        self.ui.setupUi(self.MainWindow)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.setSignals()

        self.manager = Manager()

        self.manager.loadPlayers('tablica.csv')
        self.round=1
        pass

    def calculate(self):

        self.manager.setAllZeroStatus()
        self.manager.sortPlayers(self.manager.players)
        self.manager.setRanks()
        #sself.manager.showPlayers()

        print "Kolucvhestvo"
        self.manager.showNumberOfStatus(1)
        self.manager.showNumberOfStatus(2)
        self.manager.showNumberOfStatus(3)

        self.manager.delete()
        self.fillTable()

        print "Kolucvhestvo"
        self.manager.showNumberOfStatus(1)
        self.manager.showNumberOfStatus(2)
        self.manager.showNumberOfStatus(3)

        self.changeTableSize()
        print u"Игроков "+str(len(self.manager.players))


    def goToOtvety(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        '''self.manager.loadPlayers(self.ui.lineEdit.text())
        self.manager.sortPlayers()
        self.manager.setRanks()'''
        self.createTable(3,len(self.manager.players))
        #self.fillTable()

    def removeFromTableAndList(self,vec):
        row=vec.row()
        self.ui.tableWidget.removeRow(row)
        self.manager.players.remove(self.manager.players[row])
        print "players "+str(len(self.manager.players))
        print "Kolucvhestvo"
        self.manager.showNumberOfStatus(1)
        self.manager.showNumberOfStatus(2)
        self.manager.showNumberOfStatus(3)
        pass

    def createTable(self,cols,rows):
        table=self.ui.tableWidget
        table.setColumnCount(cols)
        table.setRowCount(rows)

        #self.fillTable()
        pass



    '''def reDrawTable(self):
        t=self.ui.tableWidget
        t.clear()
        cols=1+len(self.manager.players[0].score)+1
        rows=len(self.manager.players)
        t.setColumnCount(cols)
        t.setRowCount(rows)
        pass'''

    '''def addRoundToTable(self):
        for p in self.manager.players:
            newItem1 = QtGui.QTableWidgetItem()
            newItem2 = QtGui.QTableWidgetItem()

            newItem1.setText(QtCore.QString(unicode(p.name)))
            if(p.status==1):
                newItem2.setText(QtCore.QString(unicode(p.score[len(p.score) - 1])))


        pass'''

    def changeTableSize(self):
        new_rows=len(self.manager.players)
        self.ui.tableWidget.setRowCount(new_rows)

        pass

    def getScoresFromTable(self):
        t = self.ui.tableWidget
        for i in range(len(self.manager.players)):
            itemScore=t.item(i,1)
            newScore=unicode(itemScore.text().toUtf8(),encoding="UTF-8")
            self.manager.players[i].score=int(newScore)

        pass

    def fillTable(self):

        for p in self.manager.players:
            index=self.manager.players.index(p)
            newItem1=QtGui.QTableWidgetItem()
            newItem2=QtGui.QTableWidgetItem()
            newItem3=QtGui.QTableWidgetItem()
            #newItem4=QtGui.QTableWidgetItem()
            newItem1.setText(QtCore.QString(unicode(p.name)))
            newItem2.setText(QtCore.QString(unicode(p.score)))
            newItem3.setText(QtCore.QString(unicode(p.status)))

            newItem3.setBackgroundColor(self.colors[p.status-1])

            '''if(p.status==1):
                newItem4.setText(QtCore.QString(unicode(p.score[len(p.score)-1])))
            elif(p.status==3):
                newItem4.setText(QtCore.QString(unicode("#")))
                newItem4.setBackgroundColor(self.colors[p.status-1])
            newItem4.setText(QtCore.QString(unicode("#")))'''
            self.ui.tableWidget.setItem(index,0,newItem1)
            self.ui.tableWidget.setItem(index,1,newItem2)
            self.ui.tableWidget.setItem(index,2,newItem3)


            index+=1
        #self.addColAndCopyScores()
        #self.reDrawTable()

        head1=QtGui.QTableWidgetItem()
        head2=QtGui.QTableWidgetItem()
        head3=QtGui.QTableWidgetItem()

        head1.setText(QtCore.QString(unicode(u"Фамилия")))
        head2.setText(QtCore.QString(unicode(u"Очки")))
        head3.setText(QtCore.QString(unicode(u"Статус")))

        self.ui.tableWidget.setHorizontalHeaderItem(0,head1)
        self.ui.tableWidget.setHorizontalHeaderItem(1,head2)
        self.ui.tableWidget.setHorizontalHeaderItem(2,head3)

        self.ui.label_3.setText(QtCore.QString(unicode(u"Раунд " + str(self.round))))
        self.round += 1

        pass

    def setSignals(self):
        self.ui.pushButton.clicked.connect(self.goToOtvety)
        self.ui.pushButton_2.clicked.connect(self.getScoresFromTable)
        self.ui.pushButton_3.clicked.connect(self.calculate)
        self.ui.tableWidget.doubleClicked.connect(self.removeFromTableAndList)
    pass



