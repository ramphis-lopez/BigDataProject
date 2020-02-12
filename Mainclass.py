#BigData Project
#Contributos: Abiesel, Ramphis, Alexander, Laizla & Andrea

#import panda as pd
#import numpy as np 
import csv

#input code
"""
with open('ASCE_Samples_v2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for col in row:
            print (col)
        
"""

#Text Analysis
"""
    Disruption Type: 
        hurricane related:
            power - 1
            communication - 2
            water - 3
            wastewater - 4
            transportation - 5
            other - 6
    
        hurricante not related: 7

    Disruption Status:
        actual disruption - 1
        not disruption - 0
        
        

"""
tweetlistHR = {'hurricane': [], 'water': [], 'power': [], 'communication': [], 'wastewater': [], 'transportion':[], 'other': []}

tweetlistHR['hurricane'] = ["hurricane Irma", "hurricane"]
tweetlistHR['water'] = ["bottle of water", "drinking water", "water", "bottled water"]
tweetlistHR['power'] = ["power off", "power down", "lost power", "fallen power service", 
                "fallen power cables", "fallen power spot", "power back", "power is back",
                ]

text = "Friends in Overtown and Miramar already lost power"
def textAnalysis(text):
    txt = text.split()
    result = [0,1,2]
    for i in txt:
        for j in tweetlistHR['hurricane']:
            if(i == j):
                result[0] = 1
            else:
                result[0] = 0
        for k in tweetlistHR['water']:
            if(i == k):
                result[1] = 1
            else:
                result[1] = 0
        for l in tweetlistHR['power']:
            if(i == l):
                result[2] = 1
            else:
                result[2] = 0
    
    return result
        
print(textAnalysis(text))


#output code


