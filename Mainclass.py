#BigData Project
#Contributos: Abiesel, Ramphis, Alexander, Laizla & Andrea

import csv


#input code
'''
filename = input('Enter the file name: ')
filehandle = open(filename, 'r')
'''


results = []
with open('ASCE_Samples_v2.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
'''
    for loop saves every sentences
'''
sentences = []
counter = 0
for i in results:
    sentences.append(results[counter]['ï»¿text'])
    counter+= 1



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

'''
tweetlistHR = {'hurricane': [], 'water': [], 'power': [], 'communication': [], 'wastewater': [], 'transportion':[], 'other': []}

tweetlistHR['hurricane'] = ["hurricane Irma", "hurricane"]
tweetlistHR['water'] = ["bottle of water", "drinking water", "water", "bottled water"]
tweetlistHR['power'] = ["power off", "power down", "lost power", "fallen power service", 
                "fallen power cables", "fallen power spot", "power back", "power is back",
                ]
'''
def evaluate_




        
#print(textAnalysis(txt))


#output code


