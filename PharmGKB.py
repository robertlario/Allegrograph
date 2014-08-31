__author__ = 'lario'

import csv
import re
import regex
import os, urllib, datetime, time, sys

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

DBSource = visumpointGene.VP_PharmGKB
Namespace = visumpointGene.URI_PharmGKB


def dbReference(inStr):
    str = visumpointGene.strip(inStr.lower())
    if str == "snomedct":
        return visumpointGene.VP_SnoMedCT
    if str == "umls":
        return visumpointGene.VP_UMLS
    if str == "ndfrt":
        return visumpointGene.VP_NDFRT
    if str == "meddra":
        return visumpointGene.VP_MedDRA
    if str == "mesh":
        return visumpointGene.VP_Mesh
    if str == "humancycgene":
        return visumpointGene.VP_HumanCycGene
    if str == "alfred":
        return visumpointGene.VP_Alfred
    if str == "ctd":
        return visumpointGene.VP_CTD
    if str == "ensembl":
        return visumpointGene.VP_Ensembl
    if str == "entrezgene":
        return visumpointGene.VP_EntrezGene
    if str == "genatlas":
        return visumpointGene.VP_GenAtlas
    if str == "genecard":
        return visumpointGene.VP_GeneCard
    if str == "go":
        return visumpointGene.VP_GO
    if str == "hgnc":
        return visumpointGene.VP_HGNC
    if str == "hugo":
        return visumpointGene.VP_HUGO
    if str == "huge":
        return visumpointGene.VP_HUGE
    if str == "dBase":
        return visumpointGene.VP_DBase
    if str == "hgnc":
        return visumpointGene.VP_HGNC
    if str == "hugo":
        return visumpointGene.VP_HUGO
    if str == "modbase":
        return visumpointGene.VP_ModBas
    if str == "mutdb":
        return visumpointGene.VP_MutDb
    if str.startswith("refseq"):
        return visumpointGene.VP_RefSeq
    if str == "omim":
        return visumpointGene.VP_OMIM
    if str == "uniprotkb":
        return visumpointGene.VP_UniProtKb
    if str == "ucscgenomebrowser":
        return visumpointGene.VP_UCSCGenomeBrowser
    if str == "iupharreceptor":
        return visumpointGene.VP_IupharReceptor
    if str == "url":
        return visumpointGene.VP_URL
    if str == "ttd":
        return visumpointGene.VP_TTD
    if str == "bindingdb":
        return visumpointGene.VP_BindingDb
    if str == "chemspider":
        return visumpointGene.VP_ChemSpider
    if str == "drugbank":
        return visumpointGene.VP_DrugBank
    if str == "keggcompound":
        return visumpointGene.VP_KeggCompound
    if str == "pubchemcompound":
        return visumpointGene.VP_PubChemCompound
    if str == "pubchemsubstance":
        return visumpointGene.VP_SubChemSubstance
    if str == "dailymed":
        return visumpointGene.VP_DailyMed
    if str == "het":
        return visumpointGene.VP_HET
    if str == "clinicaltrials":
        return visumpointGene.VP_ClinicalTrials
    if str == "dpd":
        return visumpointGene.VP_DPD
    if str == "chebi":
        return visumpointGene.VP_Chebi
    if str == "genbank":
        return visumpointGene.VP_Genbank
    if str == "ndc":
        return visumpointGene.VP_NDC
    if str == "iupharligand":
        return visumpointGene.VP_Iupharligand
    if str == "keggdrug":
        return visumpointGene.VP_Keggdrug
    if str == "pdb":
        return visumpointGene.VP_PDB
    if str == "refseqprot":
        return visumpointGene.VP_RefSeqProt
    return "ERROR %s" % inStr

def printRSIDClass(outStream,line):
    outStream.write('<%s/%s>\n' % (Namespace, line[1]))
    visumpointGene.printCrossReference(outStream,visumpointGene.VP_dbSNP,visumpointGene.strip(line[0]),visumpointGene.VP_PharmGKB,"\t\t")
    outStream.write('\t. # %s %s\n\n' % (line[1], line[0]))

def printDrugClass(outStream,line, table):
    drugName = visumpointGene.strip(line[1])
    outStream.write('<%s/%s> \n\ta  %s;\n' % (Namespace, line[0], visumpointGene.VP_PharmGKBDrug))
    try :
        outStream.write('\trdfs:label "%s"^^xsd:string ;\n' % (drugName))
        if(len(line[7])):
            outStream.write('\t%s %s;\n' % (visumpointGene.VP_SMILES, visumpointGene.smiles(line[7])))
        if len(line[2]) > 0 :
            for name in line[2].split(','):
                visumpointGene.printGenericName(outStream, "", visumpointGene.strip(name), visumpointGene.VP_PharmGKB,"\t")
        if len(line[3]) > 0 :
            for name in line[2].split(','):
                visumpointGene.printTradeName(outStream, "", visumpointGene.strip(name), visumpointGene.VP_PharmGKB,"\t")
        try:
            if len(line[6]) > 0 :
                for xref in line[6].split(','):
                    try :
                        db = xref.split(":")[0]
                        if db == "go":
                            id = xref.split(":")[2]
                        elif db =="url":
                            id = xref.split(":")[1] + ":" + xref.split(":")[2]
                        else:
                            id = xref.split(":")[1]
                        visumpointGene.printCrossReference(outStream,dbReference(db),visumpointGene.strip(id),visumpointGene.VP_PharmGKB, "\t")
                    except :
                        outStream.write('# ERROR PROCESSING printDrugClass -  %s %s %s\n\n' % (line[1], line[0], xref))
        except:
            outStream.write('# ERROR PROCESSING printDrugClass -  %s %s\n\n' % (line[1], line[0]))
        if drugName in table:
            for gene in table[drugName]:
                if not gene == NO_GENE:
                    visumpointGene.printHasGeneRelationship(outStream, visumpointGene.VP_Unknown , visumpointGene.strip(gene),  visumpointGene.VP_PharmGKB,"\t")
    except:
        outStream.write('# ERROR PROCESSING printDrugClass -  %s %s\n\n' % (line[1], line[0]))
    outStream.write('\t. # %s %s\n\n' % (line[1], line[0]))


#printDiseaseClass
def printDiseaseClass(outStream,line):
    outStream.write('<%s/%s> \n\ta  %s;\n' % (Namespace, line[0], visumpointGene.VP_PharmGKBDisease))
    outStream.write('\trdfs:label "%s"^^xsd:string ;\n' % (visumpointGene.strip(line[1])))
    outStream.write('\tskos:prefLabel "%s"^^xsd:string ;\n' % (visumpointGene.strip(line[1])))
    trip = ""
    useName = ""
    if len(line[2]) > 0 :
        for name in line[2].split(','):
            if name.startswith("\"") and name.endswith("\""):
                useName = name
            elif name.startswith("\""):
                trip = name
            elif name.endswith("\""):
                useName = (trip + "," +name).strip("\"")
                trip = ""
            else :
                useName = name
            if len(useName) > 0:
                visumpointGene.printAlternativeName(outStream, "", visumpointGene.strip(useName), visumpointGene.VP_PharmGKB,"\t\t")
                useName = ""

    db_id_type_strB = "(.+):(.+)\((.+)\[(.+)/(.+)\]"
    db_id_PP = r'(.+):(.+)\(([^()]++)\((.*)\)+'
    strExp = "(.+):(.+)\((.+)"
    if len(line[4]) > 0 :
        for name in line[4].split('),'):
                #db_id_type_strB = "(.+):(.+)\((.+)\[(.+)/(.+)\]"
                try:
                    match = regex.match(db_id_type_strB, name, regex.M|regex.I)
                    if (match):
                        visumpointGene.printCrossReference(outStream, dbReference(match.group(1)), visumpointGene.strip(match.group(2)), visumpointGene.VP_PharmGKB,"\t\t")
                    else :
                        #db_id_PP = r'(.+):(.+)\(([^()]++)\((.*)\)+'
                        try:
                            match1 = regex.match( db_id_PP, name, re.M|re.I)
                            if (match1):
                                visumpointGene.printCrossReference(outStream, dbReference(match1.group(1)), visumpointGene.strip(match1.group(2)), visumpointGene.VP_PharmGKB,"\t\t")
                            else :
                                #strExp = "(.+):(.+)\((.+)"
                                try:
                                    match2 = regex.match( strExp, name, re.M|re.I)
                                    if(match2):
                                        visumpointGene.printCrossReference(outStream, dbReference(match2.group(1)), visumpointGene.strip(match2.group(2)), visumpointGene.VP_PharmGKB,"\t\t")
                                    else :
                                        outStream.write("#ERROR : processing External References : %s\n" % name)
                                        outStream.write("#\t\t %s\n" % line[4])
                                except:
                                    e = sys.exc_info()[0]
                                    print( "Error: %s" % e )
                        except:
                            e = sys.exc_info()[0]
                            print( "Error: %s" % e )
                except:
                    e = sys.exc_info()[0]
                    print( "Error: %s" % e )

    outStream.write('\t. # %s %s\n\n' % (line[1], line[0]))

def printGeneClass(outStream,line):
    outStream.write('<%s/%s> \n\ta  %s;\n' % (Namespace, line[0], visumpointGene.VP_PharmGKBGene))
    outStream.write('\trdfs:label "%s"^^xsd:string ;\n' % (visumpointGene.strip(line[3])))

    visumpointGene.printCrossReference(outStream, visumpointGene.EntrezGene_ID , visumpointGene.strip(line[1]), visumpointGene.VP_PharmGKB, "\t\t")
    visumpointGene.printCrossReference(outStream, visumpointGene.Ensembl_ID , visumpointGene.strip(line[2]), visumpointGene.VP_PharmGKB, "\t\t")
    visumpointGene.printHasSymbol(outStream, visumpointGene.Ensembl_ID , visumpointGene.strip(line[4]),  visumpointGene.VP_PharmGKB,"\t\t")
    try:
        if line[0] == "PA134868213":
            x = 0
        if len(line[10]) and line[10] != 'null' :
            outStream.write('\tVP:CPIC "%s"^^xsd:boolean ;\n' % (visumpointGene.trueFalse(visumpointGene.strip(line[10]))))
        if len(line[11]) > 0 and line[11] != 'null' :
         outStream.write('\tVP:Chromosome "%s"^^xsd:string;\n' % (visumpointGene.strip(line[11])))
        if len(line[12]) > 0 and line[12] != 'null' :
         outStream.write('\tVP:Start "%s"^^xsd:integer;\n' % (visumpointGene.strip(line[12])))
        if len(line[13]) > 0 and line[13] != 'null' :
         outStream.write('\tVP:End "%s"^^xsd:integer ;\n' % (visumpointGene.strip(line[13])))
    except:
       outStream.write('# Error XREF %s\n\n\n' % (line[0]))
    try:
        if len(line[9]) > 0 :
            for xref in line[9].split(','):
                db =""
                id = ""
                try:
                    db = xref.split(":")[0]
                    if db == "go":
                        id = xref.split(":")[2]
                    elif db =="url":
                        id = xref.split(":")[1] + ":" + xref.split(":")[2]
                    else:
                        id = xref.split(":")[1]
                        if len(db) > 0 and len(id) > 0:
                            visumpointGene.printCrossReference(outStream,dbReference(visumpointGene.strip(db)),visumpointGene.strip(id),visumpointGene.VP_PharmGKB, "\t\t")
                except:
                     outStream.write('#Error XREF -> %s - %s\n\n\n' % (line[0], xref))
    except:
        outStream.write('# Error XREF %s\n\n\n' % (line[0]))

        #outStream.write('\t\t\t # %s\n' % (visumpointGene.strip(xref)))

    outStream.write('\t. # %s\n\n\n' % (line[0]))

def readDrugsFile(infilename, outStream, table):
    x = 0
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                if x > START:
                    print("Disease : %s - %s" % (x,line[0]))
                    try:
                        printDrugClass(outStream,line, table)
                    except:
                         print("ERROR ON ROW - readDrugsFile : %s - %s" % (x,line[0]))
                         outStream.write("\n# ERROR ON ROW: %s - PharmGKB ID : %s\n\n" % (x,line[0]))

                if x > END:
                    return
                x = x + 1
    except:
        print("ERROR ON ROW - readDrugsFile")
        e = sys.exc_info()[0]
        print( "Error: %s" % e )
    finally:
        f.close()
    return

NO_GENE = "NO_GENE"
def readDrugLabelsFile(infilename):
    drug = ""
    genes = ""
    x = 0
    table = {}
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                if x > START:
                    print("Drug Labels : %s - %s" % (x,line[1]))
                    try:
                        match = regex.match(r'FDA Label for ([a-zA-Z0-9 \-,]+) and (.+)', line[1], regex.M|regex.I)
                        if not match:
                            match = regex.match(r'European Medicines Agency \(EMA\) Label for ([a-zA-Z0-9 \-,]+) and (.+)', line[1], regex.M|regex.I)
                        if(match):
                            drug = match.group(1)
                            genes = match.group(2)

                        else :
                            match = regex.match(r'FDA Label for ([a-zA-Z0-9 \-,]+)', line[1], regex.M|regex.I)
                            if not match:
                                match = regex.match(r'European Medicines Agency \(EMA\) Label for ([a-zA-Z0-9 \-,]+)', line[1], regex.M|regex.I)
                            if (match):
                                drug = match.group(1)
                                genes = ""
                            else:
                                print("ERROR ON ROW - readDrugLabelsFile : %s - %s" % (line[1]))

                        if len(drug) > 0:
                            if drug in table:
                                row = table[drug]
                            else:
                                row = {}
                                table[drug] = row
                            if(len(genes) > 0):
                                for gene in genes.split(","):
                                    row[gene] = {gene, line[2], line[3],line[4]}
                            else :
                                row[NO_GENE] = {NO_GENE, line[2], line[3],line[4]}

                        drug = ""
                        genes = ""
                    except:
                         print("ERROR ON ROW - readDrugLabelsFile 2: %s - %s" % (x,line[0]))

                if x > END:
                    return table
                x = x + 1
    finally:
        f.close()
    return table

def readDiseasesFile(infilename, outStream):
    x = 0
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                if x > START:
                    print("Disease : %s - %s" % (x,line[0]))
                    try:
                        printDiseaseClass(outStream,line)
                    except:
                         print("ERROR ON ROW - readDiseasesFile: %s - %s" % (x,line[0]))
                         outStream.write("\n# ERROR ON ROW - readDiseasesFile: %s - PharmGKB ID : %s\n\n" % (x,line[0]))

                if x > END:
                    return
                x = x + 1
    except:
        print("ERROR ON ROW - readDiseasesFile")

    finally:
        f.close()
    return

def readRSIFFile(infilename, outStream):
    x = 0
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                if x > START+1:
                    print("RSID : %s - %s" % (x,line[0]))
                    try:
                        printRSIDClass(outStream,line)
                    except:
                         print("ERROR ON ROW - readRSIFFile: %s - %s" % (x,line[1]))
                         outStream.write("\n# ERROR ON ROW - readRSIFFile: %s - PharmGKB ID : %s\n\n" % (x,line[1]))

                if x > END:
                    return
                x = x + 1
    finally:
        f.close()
    return

def readGeneFile(infilename, outStream):
    x = 0
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                if x > START:
                    print("GENE : %s - %s" % (x,line[0]))
                    try:
                        printGeneClass(outStream,line)
                    except:
                         print("ERROR ON ROW - readGeneFile: %s - %s" % (x,line[0]))
                         outStream.write("\n# ERROR ON ROW - readGeneFile: %s - PharmGKB ID : %s\n\n" % (x,line[0]))

                if x > END:
                    return
                x = x + 1
    finally:
        f.close()
    return

def readFiles(dir, ttlFile):
    #ttlFile = "D:/My Workspaces/EmptyTest/visumpoint/140815/PharmGKB.ttl"
    #dir = "D:/My Ontologies/PharmGKB/140815"
    geneFile = "%s/%s" % (dir, "genes.tsv")
    rsidFile = "%s/%s" % (dir, "rsid.tsv")
    diseaseFile = "%s/%s" % (dir, "diseases.tsv")
    drugsFile = "%s/%s" % (dir, "drugs.tsv")
    drugLabelsFile = "%s/%s" % (dir, "drugLabels.tsv")
    try:
        outStream = open(ttlFile, 'w')
        printHeader(outStream)
        table = readDrugLabelsFile(drugLabelsFile)
        readGeneFile(geneFile, outStream)
        readRSIFFile(rsidFile, outStream)
        readDiseasesFile(diseaseFile, outStream)
        readDrugsFile(drugsFile, outStream, table)

        x = 0
    finally:
        outStream.close()
START = 0
END = 20000000000
def main():
  readFiles("D:/My Ontologies/PharmGKB/140815","D:/My Workspaces/EmptyTest/visumpoint/140815/PharmGKB.ttl" )

  str = "NDFRT:N0000002071(Mycobacterium Infections [Disease/Finding])"
  str1 = "MeSH:D015430(Weight Gain)"
  str2 = "SnoMedCT:109978004(T-cell lymphoma (clinical)"
  str3 = "MeSH:D016399(Lymphoma, T-Cell)"
  str4 = "MeSH:D015430(Weight Gain"
  #match = re.match( r'(.+):(.+)\((.+)\)', str, re.M|re.I)
  match = re.match( r'(.+):(.+)[\(+](.+)[\)+]', str3, re.M|re.I)
  #match = re.match( r'(.+):(.+)[\(+](.+)[\(*](.+)[\)+][\)*]', str2, re.M|re.I)
  match = re.match( r'(.+):(.+)[\(+](.+)[\(*](.*)[\)*]', str2, re.M|re.I)
  #match = re.match( r'(.+):(.+)[\(+](.+)([\(*].+[\)*])[\)+]', str3, re.M|re.I)
  #match = re.match( r'(.+):(.+)\(+(.+)\)', str2, re.M|re.I)
  if match:
      print "matchObj.group() : ", match.group()
      print "matchObj.group(1) : ", match.group(1)
      print "matchObj.group(2) : ", match.group(2)
      print "matchObj.group(3) : ", match.group(3)
      #print "matchObj.group(4) : ", match.group(4)
  else:
      print "No match!!"

db_id_type_strB = "(.+):(.+)\((.+)\[(.+)/(.+)\]"

db_id_PP = r'(.+):(.+)\(([^()]++)\((.*)\)+'

strExp = "(.+):(.+)\((.+)"

def test():
    s = 'aaa(((1+0)+1)+1)bbb'
    db_id_type_str = r'(.+):(.+)\((.+)'

    str1 = "NDFRT:N0000002071(Mycobacterium Infections [Disease/Finding])"
    db_id_type_strB = "(.+):(.+)\((.+)\[(.+)/(.+)\]"

    str2 = "SnoMedCT:109978004(T-cell lymphoma (clinical)"
    db_id_PP = r'(.+):(.+)\(([^()]++)\((.*)\)+'

    str3 = "MeSH:D015430(Weight Gain"
    strExp = "(.+):(.+)\((.+)"

    str4 = "MeSH:D015430(Weight Gain"
    match = regex.match(db_id_PP, str4, regex.M|regex.I)


    if match:
      print "matchObj.group() : ", match.group()
      print "matchObj.group(1) : ", match.group(1)
      print "matchObj.group(2) : ", match.group(2)
      print "matchObj.group(3) : ", match.group(3)
      print "matchObj.group(4) : ", match.group(4)
      print "matchObj.group(5) : ", match.group(5)
    else:
      print "No match!!"

def test2() :
    str = 'Achromatopsia,"Acquired Color Blindness","Blindness, Color","Blue Color Blindness","Color Blindness","Color Blindness, Acquired","Color Blindness, Blue","Color Blindness, Green","Color Blindness, Inherited","Color Blindness, Red","Color Blindness, Red Green","Color Blindness, Red-Green","Color Vision Defect","Defect, Color Vision","Defect, Deutan","Defects, Color Vision","Deutan Defect","Green Color Blindness","Inherited Color Blindness","Monochromatopsia","Protan Defect","Red Color Blindness","Red-Green Color Blindness","Tritan Defect","Vision Defect, Color","Vision Defects, Color",'
    pattern = regex.compile(r'\"*[a-zA-Z ]+\"*')

    for (drug) in regex.findall(pattern, str):
        print drug
        #print numbers, '*', letters

def test3() :
    str = 'Achromatopsia,"test","Acquired Color Blindness","Blindness, Color","Blue Color Blindness","Color Blindness","Color Blindness, Acquired","Color Blindness, Blue","Color Blindness, Green","Color Blindness, Inherited","Color Blindness, Red","Color Blindness, Red Green","Color Blindness, Red-Green","Color Vision Defect","Defect, Color Vision","Defect, Deutan","Defects, Color Vision","Deutan Defect","Green Color Blindness","Inherited Color Blindness","Monochromatopsia","Protan Defect","Red Color Blindness","Red-Green Color Blindness","Tritan Defect","Vision Defect, Color","Vision Defects, Color",'
    str = 'Grafting,NOS,"Transplant procedure","Transplantation - action","Tx - Transplant",'
    trip = ""
    for name in str.split(','):
        if name.startswith("\"") and name.endswith("\""):
           useName = name
        elif name.startswith("\""):
            trip = name
        elif name.endswith("\""):
            useName = (trip + "," +name).strip("\"")
            trip = ""
        else :
            useName = name
        if len(useName) > 0:
            print useName.strip("\"")
            useName = ""

def TestreadDrugsFile(infilename):
    x = 0
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
               print "Row %s - %s OK" % (x, line[0])
               x = x + 1
    except:
        print("Row %s FAILED!" % (x))
        e = sys.exc_info()
        print( "Error: %s - %s -%s" % (e[0], e[1], e[2]))
    finally:
        f.close()
    return

#TestreadDrugsFile("D:/My Ontologies/PharmGKB/140815/drugs2.tsv")
main()