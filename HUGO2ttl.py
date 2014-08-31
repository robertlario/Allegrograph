__author__ = 'lario'

import csv
import re
import visumpointGene

#MAIN_NAMESPACE = "http://ncicb.nci.nih.gov/xml/owl/EVS/Hugo"
MAIN_NAMESPACE = "http://www.visumpoint.com/2014/gene"
#MAIN_NAMESPACESHORT = "hugo"
MAIN_NAMESPACESHORT = "VP"
HUGO_NAMESPACE = MAIN_NAMESPACE
#ClinVar_NAMESPACE = "http://ncicb.nci.nih.gov/xml/owl/EVS/ClinVar"


def printHeader(outStream):

    outStream.write("@prefix %s: <%s#> .\n\n" % (MAIN_NAMESPACESHORT , MAIN_NAMESPACE))
    outStream.write("@prefix VP: <%s/> .\n" % (visumpointGene.VP))
    #outStream.write("@prefix : <%s#> .\n\n" % (HUGO_NAMESPACE))
    outStream.write("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n")
    outStream.write("@prefix owl:  <http://www.w3.org/2002/07/owl#> .\n")
    outStream.write("@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .\n")
    outStream.write("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n")
    outStream.write("@prefix umls: <http://bioportal.bioontology.org/ontologies/umls/> .\n")
    outStream.write("@prefix GO: <%s/> .\n" % (visumpointGene.GO))
    outStream.write("@prefix PMID: <http://purl.obolibrary.org/obo/> .\n")
    outStream.write("@prefix SO: <http://purl.obolibrary.org/obo/>.\n")
    outStream.write("@prefix vtw-cpt: <http://www.omg.org/spec/VTW/Concepts/>.\n")

    #outStream.write("@prefix CV: <%s/> .\n\n\n" % (ClinVar_NAMESPACE))

    outStream.write("<%s>\n" % (MAIN_NAMESPACE))
    outStream.write("\ta       owl:Ontology ;\n")
    outStream.write('\trdfs:comment "The File ontology defines the concepts and relationships related to the image file."^^xsd:string ;\n')
    outStream.write("\towl:imports <%s> ;\n" % (visumpointGene.VP))
    outStream.write('\towl:versionInfo "1.0"^^xsd:string .\n\n')

    return

inputPath = "D:/My Ontologies/Hugo"

def properties(outStream):


    #outStream.write('VP:HUGO\n')
    #outStream.write('\ta\towl:Class ;\n')
    #outStream.write('\trdfs:label "Hugo Class"^^xsd:string ;\n')
    #outStream.write('\trdfs:subClassOf owl:Thing ;\n')
    #outStream.write('\tskos:prefLabel "Hugo Class"^^xsd:string .\n\n')


    #shasAttributeSet
    outStream.write('VP:ApprovalDate\n')
    outStream.write('\ta\towl:ObjectProperty ;\n')
    outStream.write('\trdfs:domain VP:HUGO ;\n')
    outStream.write('\trdfs:label "has Approval Date"^^xsd:string ;\n')
    outStream.write('\t rdfs:range xsd:date ;\n')
    outStream.write('\tskos:prefLabel "has Approval Date"^^xsd:string .\n\n')

    outStream.write('VP:ApprovedName\n')
    outStream.write('\ta\towl:ObjectProperty ;\n')
    outStream.write('\trdfs:domain VP:HUGO ;\n')
    outStream.write('\trdfs:label "has Approved Name"^^xsd:string ;\n')
    outStream.write('\t rdfs:range xsd:string ;\n')
    outStream.write('\tskos:prefLabel "has Approved Name"^^xsd:string .\n\n')

    outStream.write('VP:ApprovedSymbol\n')
    outStream.write('\ta\towl:ObjectProperty ;\n')
    outStream.write('\trdfs:domain VP:HUGO ;\n')
    outStream.write('\trdfs:label "has Approved Symbol"^^xsd:string ;\n')
    outStream.write('\t rdfs:range xsd:string ;\n')
    outStream.write('\tskos:prefLabel "has Approved Symbol"^^xsd:string .\n\n')

    outStream.write('VP:hasLocusType\n')
    outStream.write('\ta\towl:ObjectProperty ;\n')
    outStream.write('\trdfs:domain VP:HUGO ;\n')
    outStream.write('\trdfs:label "has Locus Type"^^xsd:string ;\n')
    outStream.write('\trdfs:range VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "has Locus Type"^^xsd:string .\n\n')

    outStream.write('VP:hasLocusGroup\n')
    outStream.write('\ta\towl:ObjectProperty ;\n')
    outStream.write('\trdfs:domain VP:HUGO ;\n')
    outStream.write('\trdfs:label "has Locus Group"^^xsd:string ;\n')
    outStream.write('\trdfs:range VP:LocusGroup ;\n')
    outStream.write('\tskos:prefLabel "has Locus Group"^^xsd:string .\n\n')

    outStream.write('VP:DateModified\n')
    outStream.write('\ta\towl:ObjectProperty ;\n')
    outStream.write('\trdfs:domain VP:HUGO ;\n')
    outStream.write('\trdfs:label "has Date Modified"^^xsd:string ;\n')
    outStream.write('\trdfs:range xsd:string ;\n')
    outStream.write('\tskos:prefLabel "has Date Modified"^^xsd:string .\n\n')

    outStream.write('VP:hasStatus\n')
    outStream.write('\ta\towl:ObjectProperty ;\n')
    outStream.write('\trdfs:domain VP:HUGO ;\n')
    outStream.write('\trdfs:label "has Status"^^xsd:string ;\n')
    outStream.write('\trdfs:range VP:Status ;\n')
    outStream.write('\tskos:prefLabel "has Status"^^xsd:string .\n\n')

    outStream.write('VP:0000001\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:subClassOf GO:GO_0005694 ;\n')
    outStream.write('\trdfs:label "Chromosone 1"^^xsd:string .\n')
    outStream.write('\n')

    outStream.write('VP:0000002\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:subClassOf GO:GO_0005694 ;\n')
    outStream.write('\trdfs:label "Chromosone 2"^^xsd:string .\n')
    outStream.write('\n')

    outStream.write('VP:0000024\n')
    outStream.write('\ta       owl:TransitiveProperty , owl:ObjectProperty ;\n')
    outStream.write('\trdfs:label "Arm p"^^xsd:string .\n')

    outStream.write('VP:0000025\n')
    outStream.write('\ta       owl:TransitiveProperty , owl:ObjectProperty ;\n')
    outStream.write('\trdfs:label "Arm q"^^xsd:string .\n')


    outStream.write('VP:Status\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "Status"^^xsd:string ;\n')
    outStream.write('\tskos:prefLabel "Status"^^xsd:string .\n')

    outStream.write('VP:Withdrawn\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "withdrawn"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:Status ;\n')
    outStream.write('\tskos:prefLabel "withdrawn"^^xsd:string .\n')

    outStream.write('VP:Approved\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "Approved"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:Status ;\n')
    outStream.write('\tskos:prefLabel "Approved"^^xsd:string .\n')

###########################################
    outStream.write('VP:LocusGroup\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "Locus Group"^^xsd:string ;\n')
    outStream.write('\tskos:prefLabel "Locus Group"^^xsd:string .\n')

    outStream.write('VP:NonCodingRNA\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "non-coding RNA"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusGroup ;\n')
    outStream.write('\tskos:prefLabel "non-coding RNA"^^xsd:string .\n')

    outStream.write('VP:Other\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "Other"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusGroup ;\n')
    outStream.write('\tskos:prefLabel "Other"^^xsd:string .\n')

    outStream.write('VP:Phenotype\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "phenotype"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusGroup ;\n')
    outStream.write('\tskos:prefLabel "phenotype"^^xsd:string .\n')

    outStream.write('VP:ProteinCodingGene\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "protein-coding gene"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusGroup ;\n')
    outStream.write('\tskos:prefLabel "protein-coding gene"^^xsd:string .\n')



##########################################
    outStream.write('VP:LocusType\n')
    outStream.write('\ta\towl:Class ;\n')
    outStream.write('\trdfs:label "Locus Type"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf owl:Thing ;\n')
    outStream.write('\tskos:prefLabel "Locus Type"^^xsd:string .\n\n')

    #VP:EndogenousRetrovirus
    outStream.write('VP:EndogenousRetrovirus\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "Endogenous Retrovirus"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "Endogenous Retrovirus"^^xsd:string .\n')

    outStream.write('VP:GeneWithProteinProduct\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "gene with protein product"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "gene with protein product"^^xsd:string .\n')

    outStream.write('VP:Pseudogene\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "pseudogene"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "pseudogene"^^xsd:string .\n')

    outStream.write('VP:VirusIntegrationSite\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "virus integration site"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "virus integration site"^^xsd:string .\n')


    outStream.write('VP:GeneWithProteinProduct\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "gene with protein product"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "gene with protein product"^^xsd:string .\n')

    outStream.write('VP:ComplexLocusConstituent\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "complex locus constituent"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "complex locus constituent"^^xsd:string .\n')

    outStream.write('VP:FragileSite\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "fragile sitee"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "Fragile Site"^^xsd:string .\n')


    outStream.write('VP:ImmunoglobulinGene\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "immunoglobulin gene"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "immunoglobulin gene"^^xsd:string .\n')

    outStream.write('VP:ImmunoglobulinPseudogene\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "immunoglobulin pseudogene"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "immunoglobulin pseudogene"^^xsd:string .\n')

    outStream.write('VP:PhenotypeOnly\n')
    outStream.write('\ta       owl:PhenotypeOnly ;\n')
    outStream.write('\trdfs:label "phenotype only"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "phenotype only"^^xsd:string .\n')


    outStream.write('VP:Protocadherin\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "protocadherin"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "Protocadherin"^^xsd:string .\n')

    outStream.write('VP:Readthrough\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "readthrough"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "readthrough"^^xsd:string .\n')

    outStream.write('VP:Region\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "region"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "region"^^xsd:string .\n')

    outStream.write('VP:RNACluster\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, cluster"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, cluster"^^xsd:string .\n')

    outStream.write('VP:RNALongNonCoding\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, long non-coding"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, long non-coding"^^xsd:string .\n')

    outStream.write('VP:RNAMicro\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, micro"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, micro"^^xsd:string .\n')

    outStream.write('VP:RNAMisc\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, misc"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, misc"^^xsd:string .\n')

    outStream.write('VP:RNAPseudogene\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, pseudogene"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, pseudogene"^^xsd:string .\n')

    outStream.write('VP:RNARibosomal\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, ribosomal"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, ribosomal"^^xsd:string .\n')

    outStream.write('VP:RNASmallCytoplasmic\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, small cytoplasmic"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, small cytoplasmic"^^xsd:string .\n')

    outStream.write('VP:RNASmallNuclear\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, small nuclear"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, small nuclear"^^xsd:string .\n')

    outStream.write('VP:RNASmallNucleolar\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, small nucleolar"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, small nucleolar"^^xsd:string .\n')

    outStream.write('VP:RNATransfer\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, transfer"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, transfer"^^xsd:string .\n')

    outStream.write('VP:RNAVault\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, vault"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, vault"^^xsd:string .\n')

    outStream.write('VP:RNAY\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "RNA, Y"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "RNA, Y"^^xsd:string .\n')

    outStream.write('VP:TCellReceptorGene\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "T cell receptor gene"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "T cell receptor gene"^^xsd:string .\n')

    outStream.write('VP:TCellReceptorPseudogene\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "T cell receptor pseudogene"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "T cell receptor pseudogene"^^xsd:string .\n')

    outStream.write('VP:Region\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "region"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "region"^^xsd:string .\n')

    outStream.write('VP:TransposableElement\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "transposable element"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "transposable element"^^xsd:string .\n')

    outStream.write('VP:Unknown\n')
    outStream.write('\ta       owl:Class ;\n')
    outStream.write('\trdfs:label "Unknown"^^xsd:string ;\n')
    outStream.write('\trdfs:subClassOf VP:LocusType ;\n')
    outStream.write('\tskos:prefLabel "Unknown"^^xsd:string .\n')

def Status(status):
    if 'pproved' in status:
        return "VP:Approved"

    if 'ithdrawn' in status :
        return 'VP:Widthdrawn'

    return 'VP:Error'


def LocusType(locus):
    if locus.startswith('withdrawn'):
        return "VP:Withdrawn"

    if locus.startswith('gene with protein product') :
        return 'VP:GeneWithProteinProduct'

    if locus.startswith('pseudogene') :
        return 'VP:Pseudogene'

    if locus.startswith('virus integration site') :
        return 'VP:VirusIntegrationSite'

    if locus.startswith('withdrawn') :
        return 'VP:ComplexLocusConstituent'


    if locus.startswith('gene with protein product') :
        return 'VP:GeneWithProteinProduct'

    if locus.startswith('complex locus constituent') :
        return 'VP:ComplexLocusConstituent'

    if locus.startswith('fragile site') :
        return 'VP:FragileSite'

    if locus.startswith('immunoglobulin gene') :
        return 'VP:ImmunoglobulinGene'

    if locus.startswith('immunoglobulin pseudogene') :
        return 'VP:ImmunoglobulinPseudogene'

    if locus.startswith('phenotype only') :
        return 'VP:PhenotypeOnly'

    if locus.startswith('protocadherin') :
        return 'VP:Protocadherin'

    if locus.startswith('readthrough') :
        return 'VP:Readthrough'

    if locus.startswith('region') :
        return 'VP:Region'

    if locus.startswith('RNA, cluster') :
        return 'VP:RNACluster'

    if locus.startswith('RNA, long non-coding') :
        return 'VP:RNALongNonCoding'

    if locus.startswith('RNA, micro') :
        return 'VP:RNAMicro'

    if locus.startswith('RNA, misc') :
        return 'VP:RNAMisc'

    if locus.startswith('RNA, pseudogene') :
        return 'VP:RNAPseudogene'

    if locus.startswith('RNA, ribosomal') :
        return 'VP:RNARibosomal'

    if locus.startswith('RNA, small cytoplasmic') :
        return 'VP:RNASmallCytoplasmic'

    if locus.startswith('RNA, small nuclear') :
        return 'VP:RNASmallNuclear'

    if locus.startswith('RNA, small nucleolar') :
        return 'VP:RNASmallNucleolar'

    if locus.startswith('RNA, transfer') :
        return 'VP:RNATransfer'

    if locus.startswith('RNA, vault') :
        return 'VP:RNAVault'

    if locus.startswith('RNA, Y') :
        return 'VP:RNAY'

    if locus.startswith('T cell receptor gene') :
        return 'VP:TCellReceptorGene'

    if locus.startswith('T cell receptor pseudogene') :
        return 'VP:TCellReceptorPseudogene'

    if locus.startswith('region') :
        return 'VP:Region'

    if locus.startswith('transposable element') :
        return 'VP:TransposableElement'

    if locus.startswith('unknown') :
        return 'VP:Unknown'

    if locus.startswith('endogenous retrovirus'):
        return 'VP:EndogenousRetrovirus'

    return 'VP:ERROR'


def LocusGroup(locus):
    if locus.startswith('withdrawn'):
        return "VP:Withdrawn"

    if locus.startswith('non-coding RNA') :
        return 'VP:NonCodingRNA'

    if locus.startswith('pseudogene') :
        return 'VP:Pseudogene'

    if locus.startswith('other') :
        return 'VP:Other'

    if locus.startswith('phenotype') :
        return 'VP:Phenotype'

    if locus.startswith('protein-coding gene') :
        return 'VP:ProteinCodingGene'

    return 'VP:ERROR'

# GO:0005694 root chromosome
def readHUGOFile(infilename, outfilename):
    x = 0
    outStream = open(outfilename, 'w')
    printHeader(outStream)
    #properties(outStream)
    print(outfilename)
    try:
        with open(infilename, 'r') as f:
            lineRaw = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
           # print(x)
            #RXCUI, LAT, TS, LUI, STT, SUI, ISPREF, RXAUI, SAUI, SCUI, SDUI, SAB, TTY, CODE, STR, SRL, SUPRESS, CVF = line
                if x > 100:
                    print((line[0])[5:len(line[0])])
                    printHUGOClass(outStream,line)
                x = x + 1
                if x > 10000000:
                    return
    finally:
        f.close()
        outStream.close()
    return

def getChromosome(name):
    return "<%s/0005694>" % (visumpointGene.GO)

def stripStuff(str):
    return str.strip('" \n\t')

def printHUGOClass(outStream,line):
    outStream.write('<%s/%s> \n\ta  VP:HUGO ;\n' % (HUGO_NAMESPACE, (line[0])[5:len(line[0])]))
    outStream.write('\trdfs:label "%s"^^xsd:string ;\n' % (stripStuff(line[2])))
    #outStream.write('\trdfs:subClassOf VP:HUGO ;\n')
    outStream.write('\tskos:prefLabel "%s"^^xsd:string ;\n' % (stripStuff(line[2])))
    #outStream.write('\trdfs:subClassOf hugo:%s ;\n' % (line[0]))
    #outStream.write('\thugo:Accession_Numbers BC022009"^^xsd:string ;\n')
    outStream.write('\tVP:ApprovedName "%s"^^xsd:string ;\n' % (stripStuff(line[2])))

    outStream.write('\tVP:ApprovedSymbol %s;\n' % (visumpointGene.symbol(visumpointGene.strip(line[1]))))
    outStream.write('\tVP:ApprovedSymbolString "%s"^^xsd:string;\n' % (visumpointGene.strip(line[1])))

    #outStream.write('\thugo:CCDS_IDs "CCDS31071.1"^^xsd:string;\n')
    #outStream.write('\thugo:COSMIC_ID "RGS7"^^rdf:XMLLiteral ;\n')
    #outStream.write('\thugo:COSMIC_LINK "<a href=\"http://www.sanger.ac.ukz/perl/genetics/CGP/cosmic?action=gene&amp;ln=RGS7\">COSMIC</a>"^^rdf:XMLLiteral ;\n')
    outStream.write('\tVP:Chromosome_Sym "%s"^^xsd:string ;\n' % (line[10]))
    outStream.write('\tVP:Chromosome "%s"^^xsd:string;\n' % (line[10]))
    outStream.write('\tSO:SO_0000105 %s;\n' % (getChromosome(line[10]))) # Chromosome Arm http://en.wikipedia.org/wiki/Locus_(genetics)
    outStream.write('\tSO:SO_0000341 %s;\n' % (getChromosome(line[10]))) # Band
    outStream.write('\tSO:SO_0000001 %s;\n' % (getChromosome(line[10]))) # Region
    if len(line[11]) > 0:
        outStream.write('\tVP:ApprovalDate "%s"^^xsd:date ;\n' % (line[11]))
    if len(line[12]) > 0:
        outStream.write('\tVP:DateModified "%s"^^xsd:date ;\n'% (line[12]))
    if len(line[13]) > 0:
        outStream.write('\tVP:DateSymbolChanged "%s"^^xsd:date ;\n' % (line[13]))
    if len(line[14]) > 0:
        outStream.write('\tVP:DateNameChanged "%s"^^xsd:date ;\n' % (line[14]))
    #outStream.write('\thugo:Ensembl_ID__mapped_data_supplied_by_Ensembl "ENSG00000182901"^^xsd:string ;\n')
    #outStream.write('\thugo:Entrez_Gene_ID "6000"^^xsd:string ;\n')
    #outStream.write('\thugo:Entrez_Gene_ID__mapped_data_supplied_by_NCBI "6000"^^xsd:string ;\n')
    #outStream.write('\thugo:GDB_ID__mapped_data "GDB:5912686"^^xsd:string ;\n')
    #outStream.write('\thugo:Gene_Family_Tag "RGS"^^xsd:string ;\n')
    #outStream.write('\thugo:HGNC_ID "HGNC:10003"^^xsd:string ;\n')
    outStream.write('\tVP:hasLocusGroup %s;\n' % (LocusGroup(line[5])))
    #outStream.write('\thugo:Locus_Specific_Databases "<strong></strong>"^^xsd:string ;\n')
    outStream.write('\tVP:hasLocusType %s ;\n' % (LocusType(line[4])))
    #outStream.write('\thugo:Mouse_Genome_Database_ID "MGI:1346089"^^xsd:string ;\n')
    #outStream.write('\thugo:Mouse_Genome_Database_ID__mapped_data_supplied_by_MGI "MGI:1346089"^^xsd:string ;\n')
    #outStream.write('\thugo:OMIM_ID__mapped_data_supplied_by_NCBI "602517"^^xsd:string ;\n')
    if len(line[6]) > 0 :
        for previousSymbol in line[6].split(','):
            outStream.write('\tVP:PreviousSymbol %s ;\n ' % (visumpointGene.symbol(visumpointGene.strip(previousSymbol))))
            outStream.write('\tVP:PreviousSymbolString \"%s\"^^xsd:string ;\n' % (stripStuff(previousSymbol)))
    if len(line[7]) > 0 :
        for previousNames in line[7].split(','):
            outStream.write('\tVP:PreviousName \"%s\"^^xsd:string ;\n' % (stripStuff(previousNames)))
    if len(line[8]) > 0 :
        for synonyms in line[8].split(','):
            outStream.write('\tVP:Synonym %s ;\n' % (visumpointGene.symbol(visumpointGene.strip(synonyms))))
            outStream.write('\tVP:SynonymString \"%s\"^^xsd:string ;\n' % (stripStuff(synonyms)))

    if len(line[22]) > 0 :
        for pubmedID in line[22].split(','):
            visumpointGene.printCitation(outStream,visumpointGene.PubMed,stripStuff(stripStuff(pubmedID)),"\t")
    if len(line[23]) > 0 :
        for RefSeq in line[23].split(','):
            visumpointGene.printCrossReference(outStream,visumpointGene.RefSeq,stripStuff(RefSeq),"\t")
    if len(line[34]) > 0 :
        visumpointGene.printCrossReference(outStream,visumpointGene.RefSeq,stripStuff(line[34]),"\t")
    if len(line[32]) > 0 :
        for eg in line[32].split(','):
            visumpointGene.printCrossReference(outStream,visumpointGene.Ensembl_ID,stripStuff(eg),"\t")
    if len(line[15]) > 0 :
        for an in line[15].split(','):
            outStream.write('\tVP:hasAccessionNumber [\n')
            outStream.write('\t\t\ta\tVP:AccessionNumber;\n')
            outStream.write('\t\t\tVP:ID "%s"^^xsd:string;\n' % (an))
            outStream.write('\t\t];\n')

    if len(line[16]) > 0 :
        visumpointGene.printCrossReference(outStream,visumpointGene.Enzyme_ID,stripStuff(line[16]),"\t")

    if len(line[17]) > 0 :
        visumpointGene.printCrossReference(outStream,visumpointGene.EntrezGene_ID,stripStuff(line[17]),"\t")

    if len(line[18]) > 0 :
        visumpointGene.printCrossReference(outStream,visumpointGene.Ensembl_ID,stripStuff(line[18]),"\t")

    if len(line[19]) > 0 :
        visumpointGene.printCrossReference(outStream,"MouseGenomeID",stripStuff(line[19]),"\t")

    if len(line[29]) > 0 :
        for an in line[29].split(','):
            visumpointGene.printCrossReference(outStream,"CCSDID",stripStuff(an),"\t")
    if len(line[30]) > 0 :
        for an in line[30].split(','):
            visumpointGene.printCrossReference(outStream,visumpointGene.Vega_ID,stripStuff(an),"\t")

    if len(line[33]) > 0 :
        visumpointGene.printCrossReference(outStream,visumpointGene.OMIM_ID,stripStuff(line[33]),"\t")
    if len(line[36]) > 0 :
        visumpointGene.printCrossReference(outStream,visumpointGene.Ensembl_ID,stripStuff(line[36]),"\t")
    if len(line[37]) > 0 :
        visumpointGene.printCrossReference(outStream,"UCSCID",stripStuff(line[37]),"\t")
    if len(line[38]) > 0 :
        visumpointGene.printCrossReference(outStream,"MouseGenomeID",stripStuff(line[38]),"\t")
    if len(line[39]) > 0 :
        visumpointGene.printCrossReference(outStream,"RatGenomeID",stripStuff(line[39]),"\t")
    #outStream.write('\thugo:Rat_Genome_Database_ID__mapped_data_supplied_by_RGD "RGD:3570"^^xsd:string ;\n')
    #outStream.write('\thugo:Record_Type "Standard"^^xsd:string ;\n')
    #outStream.write('\thugo:RefSeq__mapped_data_supplied_by_NCBI "NM_002924"^^xsd:string ;\n')
    outStream.write('\tVP:Status %s;\n' % (Status(line[3])))
    #outStream.write('\thugo:UCSC_ID__mapped_data_supplied_by_UCSC "uc001hyv.2"^^xsd:string ;\n')
    #outStream.write('\thugo:UniProt_ID__mapped_data_supplied_by_UniProt "P49802"^^xsd:string ;\n')
    #outStream.write('\thugo:VEGA_IDs "OTTHUMG00000040107"^^xsd:string .\n')
    outStream.write('.\n')


def printOwlClass(RXCUI, RXAUI, STR, SCUI, TTY, SAB):
    if(RXCUI == '' or RXAUI =='' or SCUI =='' or TTY ==''):
        return
    #outStream.write('\n')
    #outStream.write('<http://purl.bioontology.org/ontology/RXNORM/%s> a owl:Class ;\n' % (RXAUI))
    #STR.translate(None,'\"')
   # STR = re.sub(r'^"|"$', '', STR)
    #STR.replace('\"','')
    #outStream.write('\tskos:prefLabel """%s"""@en ;\n' % (STR.replace('\"','').replace('\\','')))
    #print(('skos:prefLabel """%s"""@en ;' % (STR)))
    #outStream.write('skos:notation """%s"""^^xsd:string ;\n' % (RXAUI))
    #outStream.write('<http://purl.bioontology.org/ontology/RXNORM/RXCUI> """%s"""^^xsd:string ;\n' % (RXCUI))
    #outStream.write('<http://purl.bioontology.org/ontology/RXNORM/SAB> """%s"""^^xsd:string ;\n' % (SAB))
    #outStream.write('<http://snomed.info/id> """%s"""^^xsd:string ;\n' % (SCUI))
    #outStream.write('<http://purl.bioontology.org/ontology/RXNORM/SCUI> <http://snomed.info/id/%s> ;\n' % (SCUI))
    #outStream.write('<http://purl.bioontology.org/ontology/RXNORM/TTY> """%s"""^^xsd:string ;\n' % (TTY))
    #outStream.write('.\n')
    return

def main(infile = inputPath + "/download.txt", outFile = "D:/My Workspaces/EmptyTest/visumpoint/140815/hugo140813.ttl"):
    readHUGOFile(infile,outFile)

main()