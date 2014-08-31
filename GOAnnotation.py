__author__ = 'lario'

import csv
import re
import visumpointGene

def printHeader(outStream):

    #outStream.write("@prefix %s: <%s#> .\n\n" % (visumpointGene.VP , MAIN_NAMESPACE))
    outStream.write("@prefix VP: <%s/> .\n" % (visumpointGene.VP))
    outStream.write("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n")
    outStream.write("@prefix owl:  <http://www.w3.org/2002/07/owl#> .\n")
    outStream.write("@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .\n")
    outStream.write("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n")
    outStream.write("@prefix umls: <http://bioportal.bioontology.org/ontologies/umls/> .\n")
    outStream.write("@prefix GO: <%s/> .\n" % (visumpointGene.GO))
    outStream.write("@prefix PMID: <http://purl.obolibrary.org/obo/> .\n")
    outStream.write("@prefix vtw-cpt: <http://www.omg.org/spec/VTW/Concepts/>.\n")
    outStream.write("\n\n")

def buildTable(infilename, outfilename):
    x = 0
    outStream = open(outfilename, 'w')
    #printHeader(outStream)
    table = {}
    item = ""
    symbol = ""
    go = ""
    printHeader(outStream)
    print(outfilename)
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                if not line[0].startswith("!") and not line[0].startswith("\""):
                    item = line[1]
                    symbol = line[2]
                    go = line[4]
                    if not item in table :
                        table[item] = {}


                    if not symbol in table[item] :
                        table[item][symbol] = {}

                    if not go in table[item][symbol] :
                        table[item][symbol][go] = [line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13]]
                x = x + 1
                if x > 30000000 :
                    return table
                print(x)
    finally:
        f.close()
        outStream.close()
    return table

def printFile(table,outfilename):
    outStream = open(outfilename, 'w')
    #printHeader(outStream)

    printHeader(outStream)
    for item in table:
        outStream.write('<%s/%s> \n\ta  VP:GeneAnnotation ;\n' % (visumpointGene.GO, item))
        outStream.write('\trdfs:subClassOf VP:GeneConcept ;\n')
        for symbol in table[item]:
            outStream.write('\tVP:GeneSymbol %s;\n' % (visumpointGene.symbol(visumpointGene.strip(symbol))))
            for go in table[item][symbol]:
                row = table[item][symbol][go]
                outStream.write('%sVP:hasReference [\n' % ("\t"))
                outStream.write('\t\ta\tVP:GO;\n')
                outStream.write('\t\tVP:ID %s;\n' % (visumpointGene.urlGO(visumpointGene.strip("GO_" + go[3:len(go)]))))
                if row[0].startswith("GO_REF"):
                    outStream.write('\t\tVP:GO_REF %s;\n' % (visumpointGene.urlGO(visumpointGene.strip("GO_" + row[0][7:len(row[0])]))))

                outStream.write('\t];\n')
        outStream.write('.\n\n')



def readFile(infilename, outfilename):
    x = 0
    outStream = open(outfilename, 'w')
    #printHeader(outStream)

    printHeader(outStream)
    print(outfilename)
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                if not line[0].startswith("!"):
                    if x < 1000000:
                        print(line[1])
                        printClass(outStream,line)
                    x = x + 1
                    if x > 10:
                        return
    finally:
        f.close()
        outStream.close()
    return

def printClass(outStream,line):
    outStream.write('<%s/%s> \n\ta  owl:Class ;\n' % (visumpointGene.GO, line[1]))
    outStream.write('\tVP:Symbol %s;\n' % (visumpointGene.symbol(visumpointGene.strip(line[2]))))
    outStream.write('\tVP:Symbol %s;\n' % (visumpointGene.symbol(visumpointGene.strip(line[2]))))
    #outStream.write('\trdfs:label "%s"^^xsd:string ;\n' % (visumpointGene.strip(line[2])))
    #outStream.write('\trdfs:subClassOf VP:HUGO ;\n')

    outStream.write('.\n\n')

def main(inFile = "D:/My Ontologies/GO/gene_association.goa_human", outfile = "D:/My Workspaces/EmptyTest/visumpoint/140815/GoAnnotationHuman.ttl"):
    table = buildTable(inFile ,outfile)
    printFile(table,outfile)
main()