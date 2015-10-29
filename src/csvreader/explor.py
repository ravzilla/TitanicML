'''
Created on Oct 28, 2015

@author: Ravi
'''
import csvr
import math
import statistics as stats
anaProps = 'age'.split(sep = ' ')
discreteProps = 'pclass '
passList = csvr.csvread()
ageMedian = stats.median([x.age for x in passList])
def getBasicData()->list:
    propVals = []
    for traits in anaProps:
        propVals.append([traits,
                         round(stats.mean([eval('x.'+traits) for x in passList]),3),
                         round(stats.median([eval('x.'+traits) for x in passList]),3),
                         round(stats.mode([eval('x.'+traits) for x in passList]),3),
                         sum(1 for x in passList if x!='')]
                         
                        
                        )
    return propVals

for i in getBasicData():
    print(i[0]+' mean= '+str(i[1])+' median= '+str(i[2])+' mode= '+str(i[3]))


