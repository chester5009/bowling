# coding: utf8
from player import Player
import sys
class Manager():

    def __init__(self):
        self.players=[]
        pass

    def loadPlayers(self,pathcsv):
        file=open(pathcsv)
        index=0
        for line in file:
            l=unicode(line,"utf-8")

            splitted=l.split(';')
            if(index>1):
                newPlayer=Player(splitted[0],splitted[1])
                self.players.append(newPlayer)

            index+=1
        pass

    def sortPlayers(self):
        #if(len(self.players)>0):
        a=self.players
        for i in reversed(range(len(a))):
            for j in range(1, i + 1):
                if int(a[j - 1].score) < int(a[j].score):
                    a[j], a[j - 1] = a[j - 1], a[j]
        self.players=[]
        self.players=a
        print "len a "+str(len(a))
        pass

    def showPlayers(self):
        for p in self.players:
            print str(self.players.index(p))+" "+p.name+" "+p.score+" "+str(p.status)
        pass

    pass


    def setRanks(self):

        n=len(self.players)
        middle = n / 2-1
        for p in self.players:
            index=self.players.index(p)
            if index<=n/2:self.players[index].status=1
            else:self.players[index].status=3

        if self.players[middle].score==self.players[middle+1].score:
            for p in self.players:
                if(p.score==self.players[middle].score): self.players[self.players.index(p)].status=2





        pass

Manager