'''
Created on Oct 28, 2015

@author: Ravi
'''
import csv
from collections import namedtuple
Pass = namedtuple('Pass','pid live pclass sex age sib parch fare')
def csvread()->list:
    passList = []
    with open('train.csv') as csvfile:
        line = csv.reader(csvfile,delimiter=',')
        next(csvfile)
        next(csvfile)
        for row in line:
           age = round(float(row[4] if row[4]!='' else -1))
           fare = round(float(row[7] if row[7]!='' else -1))
           passList.append(Pass(int(row[0]),bool(row[1]),int(row[2]),bool(row[3]),age,int(row[5]),int(row[6]),fare))
        return passList