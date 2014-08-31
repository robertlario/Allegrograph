__author__ = 'lario'
import csv
import re

def createTables():
    table = {}
    rxcuiN = 0
    scuiN = 3
    with open('D:/My Utah/PharmD - Nelson/DataSet/analysis140715/results_RXCUI_140715-fixedsubstance-clean.csv', 'r') as f:
        lineRaw = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for line in lineRaw:
            rxcui = line[rxcuiN]
            scui = line[scuiN]
            print("%s \t\ %s\n" % (rxcui, scui))
            if rxcui in table :
                row = table[rxcui]
            else :
                row = {}
                table[rxcui] = row
            if not scui in row :
                row[scui] = line[1]

        f.close()
    return table

def loadRootNode():
    root = {}
    with open('d:/My Junk/resultsRootNodes.csv', 'r') as f:
        lineRaw = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for line in lineRaw:
            root[line[0]] = 0
    return root

def markReleventRootNodes(root,table):
    for rootKey in root:
        for scuiKey in table:
            if rootKey in table[scuiKey]:
                root[rootKey] = 1



def runAnalysis():
    table = createTables()
    outStream = open('D:/My Utah/PharmD - Nelson/DataSet/analysis140715/resultsAnalysis140715-fixedsubstance.csv', 'w')
    outStream.write("RXCUI\tSubstance\tProduct\tNull\n")
    for key in table:
        outStream.write("%s\t%s\t%s\t%s\n" % (key,"105590001" in table[key],"373873005" in table[key],0))

runAnalysis()