'''
Created on Oct 28, 2015

@author: Ravi
'''
import csvr
import math
import statistics as stats
from collections import namedtuple
anaProps = 'age fare'.split(sep = ' ')
discreteProps = 'pclass '
passList = csvr.csvread()
ageMedian = stats.median([x.age for x in passList])
treePass = namedtuple('treePass','sex age pclass live dead')
tPass = [treePass(x,y,z,0,0) for x in [True,False] for y in range(1,6) for z in range(1,4)]
def getBasicData(passList)->list:
    propVals = []
    for traits in anaProps:
        propVals.append([traits,
                         round(stats.mean([eval('x.'+traits) for x in passList if eval('x.'+traits)!=-1]),3),
                         round(stats.median([eval('x.'+traits) for x in passList  if eval('x.'+traits)!=-1]),3),
                         round(stats.mode([eval('x.'+traits) for x in passList if eval('x.'+traits)!=-1]),3),
                         sum(1 for x in passList if eval('x.'+traits)!='-1')]
                         
                        
                        )
    return propVals

props = getBasicData(passList)

def RemoveBlanks():
    for r in range(0,len(passList)):
        if passList[r].age == -1:
            passList[r]=passList[r]._replace(age = props[0][3])
RemoveBlanks()
passSurv = [x for x in passList if x.live == True]
passDead = [x for x in passList if x.live == False]
def gender():  
    m = 0
    f=0
    for i in passSurv:
        if i.sex:
            m+=1
        else:
            f+=1
    print(m/(m+f))
    print(f/(m+f))        
      
    
    m = 0
    f=0
    for i in passDead:
        if i.sex:
            m+=1
        else:
            f+=1
    print(m/(m+f))
    print(f/(m+f))  
def ageBuckets(age):

    if age<=5:
        return 1
    elif age>5 and age<16:
        return 2
    elif age>=16 and age<25:
        return 3
    elif age >=25 and age <60:
        return 4
    elif age>= 60:
        return 5
def incNode(age,sex,pclass,surv):
    for i in range(0,len(tPass)):
        if tPass[i].age == age and tPass[i].sex == sex and tPass[i].pclass == pclass:
            
            if surv:
                tPass[i]=tPass[i]._replace(live = tPass[i].live+1)
            else:
                tPass[i]=tPass[i]._replace(dead = tPass[i].dead+1)
            break
def genTree(): 
    for p in passList:
        incNode(ageBuckets(p.age),p.sex,p.pclass,p.live)
genTree()

