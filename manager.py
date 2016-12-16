# coding: utf8
from player import Player
import sys
class Manager():

    def __init__(self):
        self.players=[]
        self.bottom=0
        self.top=0
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
        self.bottom=0
        self.top=len(self.players)
        pass

    def sortPlayers(self,array):
        #if(len(self.players)>0):
        a=array
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
            print str(self.players.index(p))+" "+p.name+" "+str(p.score)+" "+str(p.status)
        pass

    pass


    def isMootable(self):

        for p in self.players:
            if(p.status==2):
                return 1
        return 0
        pass




    def setAllZeroStatus(self):
        for p in self.players:
            p.status=0
        pass

    def showNumberOfStatus(self,s):
        number=0
        for p in self.players:
            if p.status==s:
                number+=1
        print number
        pass

    def delete(self):
        '''for p in self.players:
            if p.status==3: self.players.remove(p)'''
        for i in reversed(range(len(self.players))):
            if(self.players[i].status==3):self.players.remove(self.players[i])
        pass

    def setRanks(self):
        self.delete()
        #if(self.isMootable()==0):

        n=len(self.players)
        middle = n / 2-1
        for p in self.players:
            index=self.players.index(p)
            if index<=n/2:self.players[index].status=1
            else:self.players[index].status=3
        score1=self.players[middle].score
        score2=self.players[middle+1].score
        if score1==score1:
            for p in self.players:
                if(p.score==score1):
                    self.players[self.players.index(p)].status=2





        pass

Manager