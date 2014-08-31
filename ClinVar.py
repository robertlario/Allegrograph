__author__ = 'lario'
import csv
import re
import gc
import os, urllib, datetime, time, sys
import xml.etree.ElementTree as ET
import clinvar13
import visumpointGene

try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")

MAIN_NAMESPACE = visumpointGene.VP
MAIN_NAMESPACESHORT = "VP"
ClinVar_NAMESPACE = MAIN_NAMESPACE
_goodchars=dict()

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj).replace('\"','').replace('\\','/')
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape').replace('\"','').replace('\\','/')

def cleanString(msg):
    '''
    Author: Denis Barmenkov <denis.barmenkov@gmail.com>
    Date: 02-jul-2007

    Write string to stdout.
    On UnicodeEncodeError exception all the unsafe chars from string
    replaced by its python representation
    '''
    global _goodchars
    try:
        return str(msg)
    except UnicodeEncodeError:
        # get error,
        res=''
        for i in list(msg):
            # try to put unknown characters thru print statement:
            if i not in _goodchars:
                try:
                    print i # try print character, some extra trash on screen
                            # for each unknown printable character
                    _goodchars[i]=i # safe character, save it as is
                except UnicodeEncodeError:
                    # format character as python string constant
                    code=ord(i)
                    if code < 256:
                        t='\\x%02x' % code # 8-bit value
                    elif code < 65536:
                        t='\\u%04x' % code # 16-bit value unicode
                    else:
                        t='\\U%08x' % code # other values as 32-bit unicode
                    _goodchars[i]=t # or '.' for readability ;-)
            res+=_goodchars[i]  # append to result
        print res



def processClasses(stream = sys.stdout):


    stream.write('VP:Citable\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Citations"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Citable"^^xsd:string .\n\n')

    stream.write('VP:Referencable\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "References"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Referencable"^^xsd:string .\n\n')

    # Symbolable
    stream.write('VP:Symbolable\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Symbols"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Symbolable"^^xsd:string .\n\n')

    #Attributable
    stream.write('VP:Attributable\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Attributes associated"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Attributable"^^xsd:string .\n\n')

    # Namable
    stream.write('VP:Namable\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Names"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Names"^^xsd:string .\n\n')

    stream.write('VP:ClinVarClass\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Clin Var Class"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Clin Var Class"^^xsd:string .\n\n')

    stream.write('VP:Measurable\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Measurable"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Measurable"^^xsd:string .\n\n')

    stream.write('VP:ReferenceAssertion\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "ReferenceAssertion"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "ReferenceAssertion"^^xsd:string .\n\n')

    stream.write('VP:SequenceLocation\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "SequenceLocation"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "SequenceLocation"^^xsd:string .\n\n')

    stream.write('VP:Attribute\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Attribute"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Attribute"^^xsd:string .\n\n')

    stream.write('VP:AttributeSet\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "AttributeSet"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Attribute Set"^^xsd:string .\n\n')

    stream.write('VP:MeasureRelationship\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "MeasureRelationship"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf VP:Citable , owl:Thing , VP:Referencable,  VP:Symbolable;\n')
    stream.write('\tskos:prefLabel "MeasureRelationship"^^xsd:string .\n\n')


    stream.write('VP:Measure\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Measure"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf VP:Citable , owl:Thing , VP:Referencable , VP:Symbolable, VP:Namable;\n')
    stream.write('\tskos:prefLabel "Measure"^^xsd:string .\n\n')

    #Trait
    stream.write('VP:Trait\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Trait"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf VP:Citable , owl:Thing , VP:Referencable , VP:Symbolable, VP:Namable;\n')
    stream.write('\tskos:prefLabel "Trait"^^xsd:string .\n\n')

    stream.write('VP:Citation\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Citation"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Citation"^^xsd:string .\n\n')

    stream.write('VP:Symbol\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Symbol"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf VP:Citable , owl:Thing , VP:Referencable;\n')
    stream.write('\tskos:prefLabel "Symbol"^^xsd:string .\n\n')

    stream.write('VP:Reference\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Reference"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Reference"^^xsd:string .\n\n')

    stream.write('VP:Name\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "Name"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf VP:Citable , owl:Thing , VP:Referencable;\n')
    stream.write('\tskos:prefLabel "Name"^^xsd:string .\n\n')

    stream.write('VP:ReferenceClinVarAssertion\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "ReferenceClinVarAssertion"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf VP:Citable , VP:Measurable, VP:Referencable, owl:Thing ;\n')
    stream.write('\tskos:prefLabel "ReferenceClinVarAssertion"^^xsd:string .\n\n')

    stream.write('VP:hasCitations\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:Citable ;\n')
    stream.write('\trdfs:label "has citations"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:Citation ;\n')
    stream.write('\tskos:prefLabel "has citations"^^xsd:string .\n\n')

    stream.write('VP:hasSymbols\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:Symbolable ;\n')
    stream.write('\trdfs:label "has Symbol"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:Symbol ;\n')
    stream.write('\tskos:prefLabel "has Symbol"^^xsd:string .\n\n')

    stream.write('VP:hasNames\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:Namable ;\n')
    stream.write('\trdfs:label "has Name"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:Name ;\n')
    stream.write('\tskos:prefLabel "has Name"^^xsd:string .\n\n')

#shasAttributeSet
    stream.write('VP:hasAttributeSet\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:Attributable ;\n')
    stream.write('\trdfs:label "has AttributeSet"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:AttributeSet ;\n')
    stream.write('\tskos:prefLabel "has AttributeSet"^^xsd:string .\n\n')

    stream.write('VP:hasAttribute\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:Attributable ;\n')
    stream.write('\trdfs:label "has Attribure"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:Attribute ;\n')
    stream.write('\tskos:prefLabel "has Attribute"^^xsd:string .\n\n')

    stream.write('VP:hasMeasures\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:Measurable ;\n')
    stream.write('\trdfs:label "has Measure"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:Measure ;\n')
    stream.write('\tskos:prefLabel "has Measure"^^xsd:string .\n\n')

    stream.write('VP:hasMeasuresRelation\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:Attributable ;\n')
    stream.write('\trdfs:label "has MeasuresRelation"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:MeasureRelation ;\n')
    stream.write('\tskos:prefLabel "has MeasuresRelation"^^xsd:string .\n\n')

    stream.write('VP:hasTraits\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:ReferenceClinVarAssertion ;\n')
    stream.write('\trdfs:label "has Traits"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:Trait ;\n')
    stream.write('\tskos:prefLabel "has Traits"^^xsd:string .\n\n')

    stream.write('VP:hasReferences\n')
    stream.write('\ta\towl:ObjectProperty ;\n')
    stream.write('\trdfs:domain VP:Referencable ;\n')
    stream.write('\trdfs:label "has Reference"^^xsd:string ;\n')
    stream.write('\t rdfs:range VP:Reference ;\n')
    stream.write('\tskos:prefLabel "has Reference"^^xsd:string .\n\n')
########################


    stream.write('VP:ReferenceType\n')
    stream.write('\ta\towl:Class ;\n')
    stream.write('\trdfs:label "ReferenceType"^^xsd:string ;\n')
    stream.write('\trdfs:subClassOf owl:Thing ;\n')
    stream.write('\tskos:prefLabel "Reference Database Type"^^xsd:string .\n\n')

    stream.write('VP:SO\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Sequence Ontology"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "Sequence Ontology"^^xsd:string .\n')


    stream.write('VP:dbSNP\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "dbSNP"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "dbSNP"^^xsd:string .\n')

    stream.write('VP:OMIM\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "OMIM"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "OMIM"^^xsd:string .\n')

    stream.write('VP:Gene\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Gene"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "Gene"^^xsd:string .\n')

    stream.write('VP:GR\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "GeneReviews"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "GeneReviews"^^xsd:string .\n')


    stream.write('VP:GA\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Genetic Alliance"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "Genetic Alliance"^^xsd:string .\n')

    stream.write('VP:HP\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Human Phenotype Ontology"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "Human Phenotype Ontology"^^xsd:string .\n')

    stream.write('VP:MD\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "MedGen"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "MedGen"^^xsd:string .\n')




    stream.write('VP:GTR\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Molecular Diagnostic Laboratory,Greenwood Genetic Center"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "Molecular Diagnostic Laboratory,Greenwood Genetic Center"^^xsd:string .\n')

    stream.write('VP:RD\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Office of Rare Diseases"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "Office of Rare Diseases"^^xsd:string .\n')

    stream.write('VP:OT\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Orphanet"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "Orphanet"^^xsd:string .\n')


    stream.write('VP:RefSeq\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "RefSeq"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "RefSeq"^^xsd:string .\n')

    stream.write('VP:SCT\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "SNOMED CT"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "SNOMED CT"^^xsd:string .\n')

    stream.write('VP:dbVar\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "dbVar"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Reference ;\n')
    stream.write('skos:prefLabel "dbVar"^^xsd:string .\n')

##########################################################
#Citations
    stream.write('VP:PubMed\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "dbVar"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Citation ;\n')
    stream.write('skos:prefLabel "dbVar"^^xsd:string .\n')

    stream.write('VP:PMC\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "dbVar"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:Citation ;\n')
    stream.write('skos:prefLabel "dbVar"^^xsd:string .\n')

    stream.write('VP:General\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "General"^^xsd:string ;\n')
    stream.write('skos:prefLabel "General"^^xsd:string .\n')

    stream.write('VP:Review\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Review"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:General ;\n')
    stream.write('skos:prefLabel "Review"^^xsd:string .\n')

    stream.write('VP:Translational\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Translational/Evidence-based"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:General ;\n')
    stream.write('skos:prefLabel "Translational/Evidence-based"^^xsd:string .\n')

    stream.write('VP:PracticeGuideline\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "practice guideline"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:General ;\n')
    stream.write('skos:prefLabel "practice guideline"^^xsd:string .\n')
##############
    stream.write('VP:TraiType\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Type of Trait"^^xsd:string ;\n')
    stream.write('skos:prefLabel "Type of Trait"^^xsd:string .\n')

    stream.write('VP:Disease\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Type of Disease"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:TraiType ;\n')
    stream.write('skos:prefLabel "Type of Disease"^^xsd:string .\n')

    stream.write('VP:DrugResponse\n')
    stream.write('a       owl:Class ;\n')
    stream.write('rdfs:label "Type of DrugResponse"^^xsd:string ;\n')
    stream.write('rdfs:subClassOf VP:TraiType ;\n')
    stream.write('skos:prefLabel "Type of DrugResponse"^^xsd:string .\n')


###############




#    result = {
#        'a': lambda x: x * 5,
#        'b': lambda x: x + 7,
#        'c': lambda x: x - 2
#        }[id](x)
# Select Case domain
#        Case x<0    : y = -1
#        Case 0<=x<1 : y =  0
#        Case 1<=x<2 : y =  1
#        Case 2<=x<3 : y =  2
#        Case Else   : y =  'n/a'
#    End Select


def printHeader(outStream):
    #outStream.write("@prefix :\t<http://www.ncbi.nlm.nih.gov/clinvar#> .\n")
    outStream.write("@prefix %s: <%s/> .\n\n" % (MAIN_NAMESPACESHORT , MAIN_NAMESPACE))
    outStream.write("@prefix skos:\t<http://www.w3.org/2004/02/skos/core#> .\n")
    outStream.write("@prefix owl:\t<http://www.w3.org/2002/07/owl#> .\n")
    outStream.write("@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .\n")
    outStream.write("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n")
    outStream.write("@prefix umls: <http://bioportal.bioontology.org/ontologies/umls/> .\n")
    outStream.write("@prefix Hugo: <http://ncicb.nci.nih.gov/xml/owl/EVS/Hugo.owl/> .\n")
    #http://ncicb.nci.nih.gov/genenames.org/HGNC.owl%23HGNC_1138%3E
    outStream.write("@prefix HP: <http://purl.obolibrary.org/obo/> .\n")
    #outStream.write("@prefix GO: <http://purl.obolibrary.org/obo/> .\n")
    #outStream.write("@prefix PMID: <http://purl.obolibrary.org/obo/> .\n")
    outStream.write("@prefix SO: <http://purl.obolibrary.org/obo/>.\n")
    outStream.write("@prefix GN: <http://www.visumpoint.com/Gene/> .\n")
    outStream.write("@prefix OMIM: <http://www.omim.org/entry/> .\n")
    outStream.write("@prefix ORD: <http://www.visumpoint.com/ORD/> .\n")
    outStream.write("@prefix SCT: <http://snomed.info/> .\n")
    outStream.write("@prefix MG: <http://www.visumpoint.com/MedGen/> .\n")
    outStream.write("@prefix dbSNP: <http://www.visumpoint.com/dbSNP/> .\n")
    outStream.write("@prefix GR: <http://www.visumpoint.com/GeneReviews/> .\n")
    outStream.write("@prefix OR: <http://www.visumpoint.com/Orphanet/> .\n")
    outStream.write("@prefix SO: <http://www.visumpoint.com/SequenceOntology/> .\n")
    outStream.write("@prefix RefSeq: <http://www.visumpoint.com/RefSeq/> .\n")
    outStream.write("@prefix GL: <http://www.visumpoint.com/GeneticsLaboratory/> .\n")

    #dbVar
    outStream.write("@prefix dbVar: <http://www.visumpoint.com/dbVar/> .\n")
    # Molecular Diagnostic Laboratory,Greenwood Genetic Center
    outStream.write("@prefix MDL: <http://www.visumpoint.com/MolecularDiagnostic/> .\n")
    #Human Phenotype Ontology
    #outStream.write("@prefix HPO: <http://www.visumpoint.com/HumanPhenotypeOntology/> .\n")
    outStream.write("@prefix HP: <http://www.visumpoint.com/HumanPhenotypeOntology/> .\n")
    #GeneTests
    outStream.write("@prefix GT: <http://www.visumpoint.com/GeneTests/> .\n")
    #Genetics Home Reference
    outStream.write("@prefix GH: <http://www.visumpoint.com/GeneticsHomeReference/> .\n")
    #Emory Genetics Laboratory
    outStream.write("@prefix EHL: <http://www.visumpoint.com/EmoryGeneticsLaboratory/> .\n")
    #Counsyl
    outStream.write("@prefix CL: <http://www.visumpoint.com/Counsyl/> .\n")
    #Department of Clinical Immunology,Odense University Hospital
    outStream.write("@prefix DCI: <http://www.visumpoint.com/DepartmentClinicalImmunology/> .\n")
    #MeSH
    outStream.write("@prefix MeSH: <http://www.visumpoint.com/MeSH/> .\n")
    #Clinical Genomics,Maastricht University Medical Centre
    outStream.write("@prefix CGM: <http://www.visumpoint.com/MeSH/> .\n")
    #Michigan Medical Genetics Laboratories,University of Michigan
    outStream.write("@prefix MMG: <http://www.visumpoint.com/MeSH/> .\n")
    #InSiGHT
    outStream.write("@prefix IS: <http://www.visumpoint.com/InSiGHT/> .\n")
    #Department of Clinical Immunology,Odense University Hospital') :
    outStream.write("@prefix DCL: <http://www.visumpoint.com/DepartmentClinicalImmunology/> .\n")

    outStream.write("@prefix PubMed: <http://www.ncbi.nlm.nih.gov/pubmed/> .\n")

    outStream.write("<%s>\n" % (MAIN_NAMESPACE))
    outStream.write("\ta       owl:Ontology ;\n")
    outStream.write('\trdfs:comment "The File ontology defines the concepts and relationships related to the image file."^^xsd:string ;\n')
    outStream.write("\towl:imports <%s> ;\n" % (visumpointGene.VP))
    outStream.write('\towl:versionInfo "1.0"^^xsd:string .\n\n')


def processClinVarSet(clinVarSet, stream = sys.stdout):
    ID = ""
    if 'ID' in clinVarSet.attrib :
        ClinVarAccession = clinVarSet.xpath('ReferenceClinVarAssertion[1]/ClinVarAccession[1]')
        ACC = ClinVarAccession[0].attrib['Acc']
        version = ClinVarAccession[0].attrib['Version']
        type = ClinVarAccession[0].attrib['Type']
        dateupdate = ClinVarAccession[0].attrib['DateUpdated']

        ID = clinVarSet.attrib['ID']
        #stream.write('VP:CV_%s\n' % (ID))
        #print('VP:%s\n' % (ID))
        stream.write('<%s/%s>\n' % (visumpointGene.VP,ACC))
        print('VP:%s\n' % (ID))
        stream.write('\ta       VP:ClinVarClass ;\n')
        title = clinVarSet.xpath('Title[1]')
        if len(version) > 0 :
            stream.write('\tVP:Version "%s"^^xsd:string ;\n' % version)
        if len(type) > 0 :
            stream.write('\tVP:Type "%s"^^xsd:string ;\n' % type)
        if len(title) > 0 :
            stream.write('\tVP:UpdateDate "%s"^^xsd:Date ;\n' % dateupdate)

        if len(title) > 0 :
            stream.write('\tVP:Title "%s"^^xsd:string ;\n' % safe_str((title[0].text)))
            #stream.write('\trdfs:label "%s"^^xsd:string ;\n' % safe_str((title[0].text)))
            #stream.write('\tskos:prefLabel"%s"^^xsd:string ;\n' % safe_str((title[0].text)))
        recordStatus = clinVarSet.xpath('RecordStatus[1]')
        if len(recordStatus) > 0 :
            stream.write('\tVP:Status "%s"^^xsd:string ;\n' % safe_str((recordStatus[0].text)))
            #stream.write('\trdfs:label "%s"^^xsd:string ;\n' % safe_str((recordStatus[0].text)))
            #stream.write('\tskos:prefLabel"%s"^^xsd:string ;\n' % safe_str((recordStatus[0].text)))
        referenceClinVarAssertion = clinVarSet.xpath('ReferenceClinVarAssertion[1]')
        if len(referenceClinVarAssertion) > 0 :
                processReferenceClinVarAssertion(referenceClinVarAssertion[0], stream)
        #for clinVarAssertion in clinVarSet.xpath('ClinVarAssertion'):
        #    if('ID' in clinVarAssertion.attrib):
        #            stream.write('\tVP:ClinVarAssertion VP:%s; \n' % (clinVarAssertion.attrib['ID']))



                #processReferenceClinVarAssertion(referenceClinVarAssertion[0],stream)
        #clinVarAssertion = clinVarSet.xpath('ClinVarAssertion[1]')
        #if len(clinVarAssertion) > 0 :
            #processClinVarAssertion(clinVarAssertion[0],stream)


        recordStatus = clinVarSet.xpath('RecordStatus[1]')
        #if len(recordStatus) > 0 :
        #    stream.write('\tVP:RecordStatus "%s"^^xsd:string ;\n' % (recordStatus[0].text))

        stream.write('.\t#ClinVarSet %s\n\n' % (ID))

def processSequenceLocation(sequence, stream = sys.stdout, tab = '\t'):
    stream.write('%sVP:hasSequenceLocation\n' % (tab))
    stream.write('%s\t [a\tVP:SequenceLocation;\n' % (tab));
    if('Assembly' in sequence.attrib):
        stream.write('%s\t\tVP:Assembly "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['Assembly'])))
    if('Chr' in sequence.attrib):
        stream.write('%s\t\tVP:Chr "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['Chr'])))
    if('Accession' in sequence.attrib):
        stream.write('%s\t\tVP:Accession "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['Accession'])))
    if('outerStart' in sequence.attrib):
        stream.write('%s\t\tVP:outerStart "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['outerStart'])))
    if('innerStart' in sequence.attrib):
        stream.write('%s\t\tVP:innerStart "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['innerStart'])))
    if('start' in sequence.attrib):
        stream.write('%s\t\tVP:start "%s"^^xsd:integer; \n' % (tab, safe_str(sequence.attrib['start'])))
    if('stop' in sequence.attrib):
        stream.write('%s\t\tVP:stop "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['stop'])))
    if('innerStop' in sequence.attrib):
        stream.write('%s\t\tVP:innerStop "%s"^^xsd:integer; \n' % (tab, safe_str(sequence.attrib['innerStop'])))

    if('outerStop' in sequence.attrib):
        stream.write('%s\t\tVP:outerStop "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['outerStop'])))
    if('Strand' in sequence.attrib):
        stream.write('%s\t\tVP:Strand "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['Strand'])))
    if('variantLength' in sequence.attrib):
        stream.write('%s\t\tVP:variantLength "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['variantLength'])))
    if('referenceAllele' in sequence.attrib):
        stream.write('%s\t\tVP:referenceAllele "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['referenceAllele'])))
    if('AlternateAllele' in sequence.attrib):
        stream.write('%s\t\tVP:AlternateAllele "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['AlternateAllele'])))
    if('AssemblyAccessionVersion' in sequence.attrib):
        stream.write('%s\t\tVP:AssemblyAccessionVersion "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['AssemblyAccessionVersion'])))
    if('AssemblyStatus' in sequence.attrib):
        stream.write('%s\t\tVP:AssemblyStatus "%s"^^xsd:string; \n' % (tab, safe_str(sequence.attrib['AssemblyStatus'])))
    #stream.write('%s\t\tVP:Text "%s"^^xsd:string;\n' % (tab, sequence.text));
    stream.write('%s\t];\t#Attribute\n' % (tab))

def processAttribute(attribute, stream = sys.stdout, tab = '\t'):
    stream.write('%sVP:hasAttribute\n' % (tab))
    stream.write('%s\t [a\tVP:Attribute;\n' % (tab))
    if('Type' in attribute.attrib):
        stream.write('%s\t\tVP:Type "%s"^^xsd:string; \n' % (tab, safe_str(attribute.attrib['Type'])))
    if('Change' in attribute.attrib):
        stream.write('%s\t\tVP:Change "%s"^^xsd:string; \n' % (tab, safe_str(attribute.attrib['Change'])))
    stream.write('%s\t\tVP:Text "%s"^^xsd:string;\n' % (tab, safe_str(attribute.text)))
    #stream.write('%s\t\trdfs:label "%s"^^xsd:string;\n' % (tab, safe_str(attribute.text)))
    stream.write('%s\t];\t#Attribute\n' % (tab))

def processAttributeSet(attribtionSet, stream = sys.stdout, tab = '\t'):
    stream.write('%sVP:hasAttributeSet\n' % (tab))
    stream.write('%s\t [a\tVP:AttributeSet;\n' % (tab))
    for attribute in attribtionSet.xpath('Attribute'):
        processAttribute(attribute, stream, tab + '\t\t')
    for citation in attribtionSet.xpath('Citation'):
        processCitation(citation,stream,tab + '\t\t')
    for reference in attribtionSet.xpath('XRef'):
        processXRef(reference,stream,tab + '\t\t')
    stream.write('%s\t];\t#AttribtionSet\n' % (tab))

def processMeasureRelationship(measureRelationship, stream = sys.stdout, tab = '\t'):
    stream.write('%sVP:hasMeasuresRelationship\n' % (tab))
    stream.write('%s\t [a\tVP:MeasureRelationship;\n' % (tab))
    for symbol in measureRelationship.xpath('Symbol'):
        processSymbol(symbol,stream,tab + '\t\t')
    for name in measureRelationship.xpath('Name'):
        processName(name,stream,tab + '\t\t')
    for citation in measureRelationship.xpath('Citation'):
        processCitation(citation,stream,tab + '\t\t')
    for reference in measureRelationship.xpath('XRef'):
        processXRef(reference,stream,tab + '\t\t')
    stream.write('%s\t];\t#MeasureRelationship\n' % (tab))

def processMeasure(measure, stream = sys.stdout, tab = '\t'):
    ID = ""
    stream.write('%sVP:hasMeasures \n' % (tab))
    stream.write('%s\t\t[a\tVP:Measure;\n' % (tab));
    if('ID' in measure.attrib):
        ID = safe_str(measure.attrib['ID'])
        stream.write('%s\t\t\tVP:ID VP:CV_%s; \n' % (tab, ID))
    if('Type' in measure.attrib):
        stream.write('%s\t\t\tVP:MeasureType %s; \n' % (tab, MeasureType(safe_str(measure.attrib['Type']))))
        stream.write('%s\t\t\trdfs:label "%s"^^xsd:string; \n' % (tab, safe_str(measure.attrib['Type'])))
    for attributeSet in measure.xpath('AttributeSet'):
        processAttributeSet(attributeSet,stream,tab + '\t\t\t')
    for measureRelationship in measure.xpath('MeasureRelationship'):
        processMeasureRelationship(measureRelationship,stream,tab + '\t\t\t')
    for citation in measure.xpath('Citation'):
        processCitation(citation,stream,tab + '\t\t\t')
    for reference in measure.xpath('XRef'):
        processXRef(reference,stream,tab + '\t\t\t')
    for sequence in measure.xpath('SequenceLocation'):
        processSequenceLocation(sequence,stream,tab + '\t\t\t')
    stream.write('%s];\t #measure %s\n' % (tab,ID))



def MeasureType(measure):
    if measure.startswith('Deletion'):
        return "<http://purl.obolibrary.org/obo/SO_1000029>"
    #Bret???
    if measure.startswith('single nucleotide variant'):
        return "VP:SingleNucleotideVariant"
    if measure.startswith('Duplication"'):
        return "<http://purl.obolibrary.org/obo/SO_1000038>"
    if measure.startswith('Insert"'):
        return "<http://purl.obolibrary.org/obo/SO_0000667>"
    #Bret???
    if measure.startswith('Indel"'):
        return "VP:Indel"
    #Bret???
    if measure.startswith('Variation"'):
        return "VP:Variation"
    #translocation"
    if measure.startswith('translocation"'):
        return "<http://purl.obolibrary.org/obo/SO_1000035>"

    #copy number loss - Bret
    #copy number gain - - Bret

    return '"%s"^^xsd:string' % measure

def processTrait(trait, stream = sys.stdout, tab = '\t'):
    ID = ""
    stream.write('%sVP:hasTraits \n' % (tab))
    stream.write('%s\t\t[a\tVP:Trait;\n' % (tab))
    if('ID' in trait.attrib):
        ID = safe_str(trait.attrib['ID'])
        stream.write('%s\t\t\tVP:ID VP:CV_%s; \n' % (tab, ID))
    if('Type' in trait.attrib):
        stream.write('%s\t\t\tVP:TraitType %s; \n' % (tab, TraitType(safe_str(trait.attrib['Type']))))
    for citation in trait.xpath('Citation'):
        processCitation(citation,stream,tab + '\t\t\t')
    for symbol in trait.xpath('Symbol'):
        processSymbol(symbol,stream,tab + '\t\t\t')
    for name in trait.xpath('Name'):
        processName(name,stream,tab + '\t\t\t')
    for xref in trait.xpath('XRef'):
        processXRef(xref,stream,tab +'\t\t\t')
    stream.write('%s];\t #Trait %s\n' % (tab,ID))

def TraitType(trait):
    if trait.startswith('Disease'):
        return "VP:Disease"
    if trait.startswith('Drug'):
        return "VP:DrugResponse"
    return "VP:%s" % trait

def getDBCitation(db,id, stream):
    if db == 'Gene':
        return '"%s"^^xsd:string' % (id)
    if db == 'OMIM':
        if special_match_num(id):
            return '"%s"^^xsd:string' % (id)
        else:
            return ""
    #SNOMED CT
    if db == 'PubMed':
        return "<http://www.ncbi.nlm.nih.gov/%s>" % (id)
    if db == 'dbSNP':
        return id


def processCitation(citation, stream = sys.stdout, tab = '\t'):
    source = ''
    id = citation.xpath('ID')
    url = citation.xpath('URL')
    citationText = citation.xpath('CitationText')
    if len(id) > 0:
        source = safe_str(id[0].attrib['Source'])
    stream.write('%sVP:hasCitation \n' % (tab))
    if source == 'PubMed':
        stream.write('%s\t [a\tVP:PubMed;\n' % (tab))
        if len(id) > 0:
            stream.write('%s\t\t VP:ID <http://www.ncbi.nlm.nih.gov/pubmed/%s>;\n' % (tab, safe_str(id[0].text)))
            if 'Source' in id[0].attrib :
                stream.write('%s\t\t VP:Source "%s"^^xsd:string;\n' % (tab, safe_str(id[0].attrib['Source'])))
                stream.write('%s\t\trdfs:label "%s : %s"^^xsd:string;\n' % (tab,  safe_str(id[0].attrib['Source']), safe_str(id[0].text)))
    elif source == 'pmc':
        stream.write('%s\t [a\tVP:PMC;\n' % (tab))
        if len(id) > 0:
            stream.write('%s\t\t VP:ID <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s>;\n' % (tab, safe_str(id[0].text)))
            if 'Source' in id[0].attrib :
                stream.write('%s\t\t VP:Source "%s"^^xsd:string;\n' % (tab, safe_str(id[0].attrib['Source'])))
                stream.write('%s\t\trdfs:label "%s : %s"^^xsd:string;\n' % (tab,  safe_str(id[0].attrib['Source']), safe_str(id[0].text)))
    elif source == 'OMIM':
        stream.write('%s\t [a\tVP:OMIM;\n' % (tab))
        if len(id) > 0:
            stream.write('%s\t\t VP:ID <http://www.omim.org/entry/%s>;\n' % (tab, safe_str(id[0].text)))
            if 'Source' in id[0].attrib :
                stream.write('%s\t\t VP:Source "%s"^^xsd:string;\n' % (tab, safe_str(id[0].attrib['Source'])))
                stream.write('%s\t\trdfs:label "%s : %s"^^xsd:string;\n' % (tab,  safe_str(id[0].attrib['Source']), safe_str(id[0].text)))
    else:
        stream.write('%s\t [a\tVP:Citation;\n' % (tab))
        if 'Abbrev' in citation.attrib :
            stream.write('%s\t\t VP:Abbrev "%s"^^xsd:string;\n' % (tab, safe_str(citation.attrib['Abbrev'])))
        if len(id) > 0:
            if 'Source' in id[0].attrib :
                stream.write('%s\t\t VP:Source "%s"^^xsd:string;\n' % (tab, safe_str(id[0].attrib['Source'])))
                stream.write('%s\t\trdfs:label "%s : %s"^^xsd:string;\n' % (tab,  safe_str(id[0].attrib['Source']), safe_str(id[0].text)))
            stream.write('%s\t\t VP:ID "%s"^^xsd:string;\n' % (tab, safe_str(id[0].text)))
    if 'Type' in citation.attrib :
        stream.write('%s\t\t VP:Type %s;\n' % (tab, citationType(safe_str(citation.attrib['Type']))))
    else:
        stream.write('%s\t\t VP:Type VP:General;\n' % (tab))
        #stream.write('%s\t\t VP:Type "%s"^^xsd:string;\n' % (tab, safe_str(citation.attrib['Type'])))
    if len(url) > 0 :
          stream.write('%s\t\t VP:URL <%s>;\n' % (tab, url[0].text))
    if len(citationText)  > 0:
          stream.write('%s\t\t VP:CitationText "%s"^^xsd:string;\n' % (tab, citationText[0].text))

    stream.write('%s\t];\t#Citation\n' % (tab))

def citationType(citation):
    if citation.startswith('Translational'):
        return "VP:Translational"
    if citation.startswith('review'):
        return "VP:Review"
    if citation.startswith('PracticeGuideline'):
        return "VP:practice"
    return "VP:General"

def processSymbol(symbol, stream = sys.stdout, tab = '\t'):
    stream.write('%sVP:hasSymbols \n' % (tab))
    stream.write('%s\t[a\tVP:Symbol;\n' % (tab))
    for xref in symbol.xpath('XRef'):
        processXRef(xref,stream,tab + '\t\t')
    element = symbol.xpath("ElementValue[1]")
    if len(element) > 0 :
        if 'Type' in element[0].attrib :
            #stream.write('%s\t\tVP:Type "%s"^^xsd:string;\n' % (tab, safe_str(element[0].attrib['Type'])))
            stream.write('%s\t\tVP:Type %s;\n' % (tab, visumpointGene.ontologyClass(safe_str(element[0].attrib['Type']))))
            stream.write('%s\t\tVP:ID %s;\n' % (tab,visumpointGene.symbol(visumpointGene.strip(safe_str(element[0].text)))))
            stream.write('%s\t\tVP:Text "%s"^^xsd:string;\n' % (tab, safe_str(element[0].text)))
            stream.write('%s\t\trdfs:label "%s"^^xsd:string;\n' % (tab, safe_str(element[0].text)))
            stream.write('%s\t\tskos:prefLabel "%s"^^xsd:string;\n' % (tab, safe_str(element[0].text)))
    stream.write('%s\t];\t#Symbol\n' % (tab))


def getDBReferenceNamespace(db):
    if db == 'Gene':
        return 'GN'
    if db == 'OMIM':
        return 'OMIM'
    #SNOMED CT
    if db == 'SNOMED CT':
        return 'SCT'
    if db == 'dbSNP':
        return 'dbSNP'
    #Office of Rare Diseases
    if db == 'Office of Rare Diseases':
        return 'ORD'
    #MedGen
    if db == 'MedGen':
        return 'MG'
    #GeneReviews
    if db == 'GeneReviews':
        return 'GR'
    #'Genetic Alliance'
    if db == 'Genetic Alliance':
        return ''
    # 'Orphanet'
    if db == 'Orphanet':
        return 'OR'
    # 'Sequence Ontology'
    if db == 'Sequence Ontology':
        return 'SO'
    # 'Genetics Laboratory,Cambridge University Hospitals (Addenbrooke\\'s)'
    if db.startswith('Genetics Laboratory,Cambridge') :
       return 'GL'
    if db.startswith('RefSeq') :
       return 'RefSeq'
    #dbVar
    if db.startswith('dbVar') :
       return 'dbVar'
    # Molecular Diagnostic Laboratory,Greenwood Genetic Center
    if db.startswith('Molecular Diagnostic Laboratory') :
       return 'MDL'

    #Human Phenotype Ontology
    if db.startswith('Human Phenotype Ontology') :
       return 'HP'

    #GeneTests
    if db.startswith('GeneTests') :
       return 'GT'
    #Genetics Home Reference
    if db.startswith('Genetics Home Reference') :
       return 'GH'
    #Emory Genetics Laboratory
    if db.startswith('Emory Genetics Laboratory') :
       return 'EHL'
    #Counsyl
    if db.startswith('Counsyl') :
       return 'CL'
    #Department of Clinical Immunology,Odense University Hospital
    if db.startswith('Department of Clinical Immunology,Odense University Hospital') :
       return 'DCL'
    #MeSH
    if db.startswith('MeSH') :
       return 'MeSH'

    #Clinical Genomics,Maastricht University Medical Centre
    if db.startswith('Clinical Genomics,Maastricht University Medical Centre'):
       return 'CGM'
    #Michigan Medical Genetics Laboratories,University of Michigan
    if db.startswith('Michigan Medical Genetics Laboratories,University of Michigan'):
       return 'MMG'
    #InSiGHT
    if db.startswith('InSiGHT') :
       return 'IS'
    #1234:Genetics Laboratory
    if db.startswith('1234:Genetics Laboratory') :
       return 'GL'
    print(">>>>>>>>>>>>>  %s" % (db))
    return  ''

def getDBReferenceDEAD(db,id):
    if db == 'Gene':
        return id
    if db == 'OMIM':
        return id
    #SNOMED CT
    if db == 'SCT':
        return id
    if db == 'dbSNP':
        return id
    #Office of Rare Diseases
    if db == 'Office of Rare Diseases':
        return id
    #MedGen
    if db == 'MG':
        return id
    #GeneReviews
    if db == 'GeneReviews':
        return '"%s"^^xsd:string' % (id)
    if db.startswith('SO'):
        return id
        #return id[3:]

    return  '"%s : %s"^^xsd:string' % (db, id)



def getCleanDBID(db,id):
    if db == 'Gene':
        return id
    if db == 'OMIM':
        if special_match_num(id):
            return id
        else:
            return ""
    #SNOMED CT
    if db == 'SNOMED CT':
        return id
    if db == 'dbSNP':
        return id
    #Office of Rare Diseases
    if db == 'Office of Rare Diseases':
        return id
    #MedGen
    if db == 'MG':
        return id[2:]
    #GeneReviews
    if db == 'GeneReviews':
        return '"%s"^^xsd:string' % (id)
    if db.startswith('SO'):
        return id[3:]
    if db.startswith('HP'):
        if id.startswith('HP'):
            return "HP_%s" % (id[3:])
        else:
            return id
    if db.startswith("RefSeq"):
            return id[0:id.index(".")]
            #return id[0:id.index(":")]
    if db.startswith('DV'):
        return id
    if db.startswith('ORD'):
        return id
    if db.startswith('SCT'):
        return id
    if db.startswith('MDL'):
        return id
    if db.startswith('GR'):
        return id
    if db.startswith('OR'):
        return id
    if db.startswith('GN'):
        return id
    return  ''


def getDBReference(db,id):
    if db == 'Gene':
        return '"%s"^^xsd:string' % (id)
    if db == 'OMIM':
        if special_match_num(id):
            return '<%s/%s>' % (visumpointGene.OMIM,id)
        else:
            return ""
    #SNOMED CT
    if db == 'SNOMED CT' or db.startswith('SCT'):
        return "<http://snomed.info/id/%s>" % (id)
    if db == 'dbSNP':
        return id
    #Office of Rare Diseases
    if db == 'Office of Rare Diseases':
       return '"%s"^^xsd:string' % (id)
    #MedGen
    if db == 'MG':
        return '"%s"^^xsd:string' % (id)
    #GeneReviews
    if db == 'GeneReviews':
        return '"%s"^^xsd:string' % (id)
    if db.startswith('SO'):
        return '"%s"^^xsd:string' % (id[3:])
    if db.startswith('HP'):
        if id.startswith('HP'):
            return "<http://purl.obolibrary.org/obo/HP_%s>" % (id[3:])
        else:
            return id
    if db.startswith("RefSeq"):
            return '"%s"^^xsd:string' % (id) #(id[0:id.index(".")])
    if db.startswith('DV'):
        return '"%s"^^xsd:string' % (id)
    if db.startswith('ORD'):
        return '"%s"^^xsd:string' % (id)
    if db.startswith('MDL'):
          return '"%s"^^xsd:string' % (id)
    if db.startswith('GR'):
          return '"%s"^^xsd:string' % (id)
    if db.startswith('OR'):
          return '"%s"^^xsd:string' % (id)
    if db.startswith('GN'):
          return '"%s"^^xsd:string' % (id)
    if db.startswith('RS'):
          return '"%s"^^xsd:string' % (id)
    return '"ND:%s"^^xsd:string' % (id)


def getDBInstance(db):
    if db == 'Gene':
        return 'VP:Gene'
    if db == 'OMIM':
        return "VP:OMIM"
    #SNOMED CT
    if db == 'SNOMED CT' or db.startswith('SCT'):
        return "VP:SCT"
    if db == 'dbSNP':
        return "VP:dbSNP"
    #Office of Rare Diseases
    if db == 'Office of Rare Diseases':
       return 'VP:ORD'
    #MedGen
    if db == 'MG':
        return 'VP:MG'
    #GeneReviews
    if db == 'GeneReviews':
        return 'VP:GR'
    if db.startswith('SO'):
        return 'VP:SO'
    if db.startswith('HP'):
        return 'VP:HP'
    if db.startswith("RefSeq"):
        return 'VP:RefSeq'
    if db.startswith('DV'):
        return 'VP:dbVar'
    if db.startswith('ORD'):
        return 'VP:ORD'
    if db.startswith('MDL'):
          return 'VP:MDL'
    if db.startswith('GR'):
          return 'VP:GR'
    if db.startswith('OR'):
          return 'VP:OR'
    if db.startswith('GN'):
          return 'VP:GN'
    return '"ERROR :%s"^^xsd:string' % (id)

def processXRef(reference, stream = sys.stdout, tab = '\t'):
    stream.write('%sVP:hasReferences \n' % (tab))
    db = ''
    if 'DB' in reference.attrib :
        db = getDBReferenceNamespace(safe_str(reference.attrib['DB']))
        stream.write('%s\t[a\t%s;\n' % (tab, getDBInstance(db)))
    else:
        stream.write('%s\t[a\tVP:Reference;\n' % (tab))
    #unicode([object[, encoding[, errors]]])
    db = ''
    #if 'DB' in reference.attrib :
        #stream.write('%s\t\tVP:DB "%s"^^xsd:string;\n' % (tab, safe_str(reference.attrib['DB'])));
        #db = getDBReferenceNamespace(safe_str(reference.attrib['DB']))
        #stream.write('%s\t\tVP:DB %s;\n' % (tab,  getDBInstance(db)));
    if 'ID' in reference.attrib  and 'DB' in reference.attrib:
        tt = safe_str(reference.attrib['DB'])
        db = getDBReferenceNamespace(safe_str(reference.attrib['DB']))
        id = getCleanDBID(db,safe_str(reference.attrib['ID']))
        if db != "" and id != "" :
            #stream.write('%s\t\tVP:ID %s:%s;\n' % (tab, db,id))
            stream.write('%s\t\tVP:ID %s;\n' % (tab, getDBReference(db,id)))
            #stream.write('%s\t\tVP:ID %s:TMP_%s;\n' % (tab, db,id));
        stream.write('%s\t\trdfs:label "%s : %s"^^xsd:string ;\n' % (tab,safe_str(reference.attrib['DB']), safe_str(reference.attrib['ID'])))
    if 'Type' in reference.attrib :
        stream.write('%s\t\tVP:Type "%s"^^xsd:string;\n' % (tab, safe_str(reference.attrib['Type'])));
        #stream.write('%s\t\tVP:Type %s' % (tab, getDBInstance(db)))
    if 'Status' in reference.attrib :
        stream.write('%s\t\t\tVP:Status "%s"^^xsd:string;\n' % (tab, visumpointGene.ontologyClass(safe_str(reference.attrib['Status']))));
    stream.write('%s\t];\t#XRef\n' % (tab))

def processName(name, stream = sys.stdout, tab = '\t'):
    stream.write('%sVP:hasNames \n' % (tab))
    stream.write('%s\t[a\tVP:Name;\n' % (tab))
    element = name.xpath("ElementValue[1]")
    if len(element) > 0 :
        if 'Type' in element[0].attrib :
            stream.write('%s\t\tVP:Status %s;\n' % (tab, visumpointGene.ontologyClass(safe_str(element[0].attrib['Type']))));
        stream.write('%s\t\tVP:Text "%s"^^xsd:string;\n' % (tab, safe_str(element[0].text)))
        stream.write('%s\t\trdfs:label "%s"^^xsd:string;\n' % (tab, safe_str(element[0].text)))
    for citation in name.xpath('Citation'):
        processCitation(citation,stream,tab + '\t\t')
    for xref in name.xpath('XRef'):
        processXRef(xref,stream,tab + '\t\t')
    stream.write('%s\t];\t#Name\n' % (tab))

def processClinicalSignificance(ClinicalSignificance, stream = sys.stdout, tab = '\t'):
    ID = ""
    stream.write('%sVP:hasClinicalSignificance \n' % (tab))
    stream.write('%s\t[a\tVP:ClinicalSignificance;\n' % (tab))
    if 'DateLastEvaluated' in ClinicalSignificance.attrib :
            stream.write('%s\t\tVP:DateLastEvaluated "%s"^^xsd:date;\n' % (tab, safe_str(ClinicalSignificance.attrib['DateLastEvaluated'])));
    reviewStatus = ClinicalSignificance.xpath('ReviewStatus[1]')
    stream.write('%s\t\tVP:ReviewStatus "%s"^^xsd:string;\n' % (tab,reviewStatus[0].text))
    description = ClinicalSignificance.xpath('Description[1]')
    desType = safe_str(description[0].text)
    if desType.lower() == 'pathogenic':
         stream.write('%s\t\tVP:Description VP:Pathogenic;\n' % (tab))
    elif desType.lower() == 'uncertain significance':
         stream.write('%s\t\tVP:Description VP:UncertainSignificance;\n' % (tab))
    elif desType.lower() == 'likely pathogenic':
        stream.write('%s\t\tVP:Description VP:LikelyPathogenic;\n' % (tab))
    elif desType.lower() == 'likely benign':
        stream.write('%s\t\tVP:Description VP:LikelyBenign;\n' % (tab))
    elif desType.lower() == 'benign':
        stream.write('%s\t\tVP:Description VP:Benign;\n' % (tab))
    elif desType.lower() == 'risk factor':
        stream.write('%s\t\tVP:Description VP:RiskFactor;\n' % (tab))
    elif desType.lower() == 'protective':
        stream.write('%s\t\tVP:Description VP:Protective;\n' % (tab))
    elif desType.lower() == 'drug response':
        stream.write('%s\t\tVP:Description VP:DrugResponse;\n' % (tab))
    else:
        stream.write('%s\t\tVP:Description VP:Unknown; # %s\n' % (tab, desType))

    stream.write('\t\t\t\t%s];\t#ClinicalSignificance %s\n' %(ID, tab))



def processReferenceClinVarAssertion(referenceClinVarAssertion, stream = sys.stdout, tab = '\t'):  # ReferenceClinVarAssertion
    ID = ""
    stream.write('%sVP:hasReferencesAssertion \n' % (tab))
    stream.write('%s\t [a\t VP:ReferenceClinVarAssertion;\n' % (tab))

    if('ID' in referenceClinVarAssertion.attrib):
        ID = referenceClinVarAssertion.attrib['ID']
        stream.write('%s\t\tVP:ID VP:CV_%s; \n' % (tab, ID))
    assertion = referenceClinVarAssertion.xpath('Assertion[1]')
    if len(safe_str(assertion[0].text)) > 0:
         stream.write('%s\t\tVP:AssertionType "%s"^^xsd:string; \n' % (tab, safe_str(assertion[0].text)))
    for clinicalSignificance in referenceClinVarAssertion.xpath('ClinicalSignificance[1]'):
        processClinicalSignificance(clinicalSignificance, stream,tab + '\t\t')
    for trait in referenceClinVarAssertion.xpath('TraitSet[1]/Trait'):
        processTrait(trait,stream,tab + '\t\t')
    for citation in referenceClinVarAssertion.xpath('TraitSet[1]/Citation'):
        processCitation(citation,stream,tab + '\t\t')
    for xref in referenceClinVarAssertion.xpath('TraitSet[1]/XRef'):
        processXRef(xref,stream,tab + '\t\t')
    for measure in referenceClinVarAssertion.xpath('MeasureSet[1]/Measure'):
        processMeasure(measure,stream,tab + '\t\t')
    #processCitation()
    stream.write('\t];\t#ReferenceClinVarAssertion %s\n' %(ID))
    #stream.write('VP:%s\n' % (referenceClinVarAssertion.attrib['ID']))
   # stream.write('\ta       VP:ReferenceClinVarAssertion ;\n')



    #for xRef in referenceClinVarAssertion.xpath('MeasureSet/Measure/MeasureRelationship/XRef'):
    #            #stream.write('\tVP:xRef %s:%s;\n' % (xRef.attrib['DB'], xRef.attrib['ID']))
    #            stream.write('\tVP:MeasureRelationshipID %s;\n' % (printDomainID))


#    print '\t','referenceClinVarAssertion', referenceClinVarAssertion.tag, referenceClinVarAssertion.attrib
#    if 'DateCreated' in  referenceClinVarAssertion.attrib:
#        stream.write('\t DateCreated "%s"^^xsd:date;\n' % (referenceClinVarAssertion.attrib['DateCreated']))
#    if 'DateLastUpdated' in  referenceClinVarAssertion.attrib:
#        stream.write('\t DateLastUpdated "%s"^^xsd:date;\n' % (referenceClinVarAssertion.attrib['DateLastUpdated']))
#    if 'SubmissionDate' in  referenceClinVarAssertion.attrib:
#        stream.write('\t SubmissionDate "%s"^^xsd:date;\n' % (referenceClinVarAssertion.attrib['SubmissionDate']))
#    stream.write('\n')

#def processClinVarAssertion(clinVarAssertion) :
 #    print '\t','clinVarAssertion', clinVarAssertion.tag, clinVarAssertion.attrib

def processTree(filename):
    starttime = time.clock()
    print("\nElapsed time: %s seconds." % (time.clock() - starttime))
    tree = etree.parse(filename)

    print("\nElapsed time: %s seconds." % (time.clock() - starttime))
    root = tree.getroot()

    for ClinVarSet in root:
        processClinVarSet
        RecordStatus = ClinVarSet.xpath('RecordStatus[1]')
        if len(RecordStatus) > 0 :
            print '\t' ,RecordStatus[0].text

        Title = ClinVarSet.xpath('Title[1]')
        if len(Title) > 0 :
            print '\t', Title[0].text

        ReferenceClinVarAssertion = ClinVarSet.xpath('ReferenceClinVarAssertion[1]')
        if len(ReferenceClinVarAssertion) > 0 :
            processReferenceClinVarAssertion(ReferenceClinVarAssertion[0])

        #ClinVarAssertion = ClinVarSet.xpath('ClinVarAssertion[1]')
        #if len(ClinVarAssertion) > 0 :
            #processClinVarAssertion(ClinVarAssertion[0])

def test1():
    try:
        xml = open('D:\My Ontologies\ClinVar\VisualizeClinvar-master\database\clinvar-demo.xml').read()
        #xml = open('D:\My Ontologies\ClinVar\ClinVarFullRelease_2014-06\ClinVarFullRelease_2014-06.xml').read()
        doc = clinvar13.CreateFromDocument(xml)

        x = 2
    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )

#processTree('D:\My Ontologies\ClinVar\VisualizeClinvar-master\database\clinvar-demo.xml')
#processTree('D:\My Ontologies\ClinVar\ClinVarFullRelease_2014-06\ClinVarFullRelease_2014-06.xml')
def main2():
    x = 0
    Amount = 1000000000
    Start = 0

    try:
        starttime = time.clock()
        #stream = sys.stdout
        #stream = open('D:\My Workspaces\EmptyTest\TopBraid\Clinvar140812.ttl','w')
        stream = open('D:/My Workspaces/EmptyTest/visumpoint/Clinvar140813.ttl','w')
        #stream = open('D:\My Workspaces\EmptyTest\visumpoint\Clinvar.ttl','w')

        printHeader(stream)
        #processClasses(stream)
       # context = etree.iterparse('D:\My Ontologies\ClinVar\VisualizeClinvar-master\database\clinvar-demo.xml', tag = 'ClinVarSet') #tab='ReleaseSet')
        context = etree.iterparse('D:\My Ontologies\ClinVar\ClinVarFullRelease_2014-06\ClinVarFullRelease_2014-06.xml', tag = 'ClinVarSet')
        #context = etree.iterparse('C:\Users\lario\PycharmProjects\AllegroGraph\clinvartest4.xml', tag = 'ClinVarSet')
        for action, elem in context:
            print "%s - \t" % (x)
            x = x + 1

            if x > Start:
                processClinVarSet(elem,stream)
            #if y == 2000:
            #    gc.collect()
            #    y = 0
            #del elem
            elem.clear()
            if x > Start + Amount:
                return

    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )
    finally:
        stream.close()
        print("\nElapsed time: %s seconds." % (time.clock() - starttime))

def main3():
    x = 0
    try:
        starttime = time.clock()
        context = etree.iterparse('D:\My Ontologies\ClinVar\ClinVarFullRelease_2014-06\ClinVarFullRelease_2014-06.xml', tag = 'ClinVarSet')
        for action, elem in context:
            print "%s - \t" % (x)
            x = x + 1

    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )
    finally:
        print("\nElapsed time: %s seconds." % (time.clock() - starttime))

def runClinVar(inFile, outFile):
    x = 0
    Amount = 1000
    Start = 0

    try:
        starttime = time.clock()
        stream = open(outFile,'w')
        printHeader(stream)

        context = etree.iterparse(inFile, tag = 'ClinVarSet')
        for action, elem in context:
            print "%s - \t" % (x)
            x = x + 1

            if x > Start:
                processClinVarSet(elem,stream)

            elem.clear()
            if x > Start + Amount:
                return

    except:
        e = sys.exc_info()[0]
        print( "Error: %s - %s" % (e[0],e[1]))
    finally:
        stream.close()

def main() :
    try:
        stream = sys.stdout

        #stream = open('D:\My Workspaces\EmptyTest\TopBraid\Examples\Clinvartest.ttl','w')
        stream = open('D:\My Workspaces\EmptyTest\TopBraid\Examples\Clinvartest.ttl','w')
        printHeader(stream)
        processClasses(stream)
        tree = etree.parse('D:\My Ontologies\ClinVar\VisualizeClinvar-master\database\clinvar-demo.xml')
        #tree = etree.parse('C:\Users\lario\PycharmProjects\AllegroGraph\clinvartestfile.xml')
        #tree = etree.parse('D:\My Ontologies\ClinVar\ClinVarFullRelease_2014-06\ClinVarFullRelease_2014-06.xml')
        #context = etree.iterparse('D:\My Ontologies\ClinVar\VisualizeClinvar-master\database\clinvar-demo.xml')
        #for action, elem in context:
        #    print("%s: %s" % (action, elem.tag))
        root = tree.getroot()

        #for referenceClinVarAssertion in root.iter('ReferenceClinVarAssertion'):
        #   processReferenceClinVarAssertion(referenceClinVarAssertion,stream)
        x = 1
        for clinVarSet in root:
            print "%s - \t" % x
            x = x +1
            processClinVarSet(clinVarSet,stream)

    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )
    finally:
        stream.close()
#transform = etree.XSLT('C:/Users/lario/Downloads/XML 2 RDF/xml2rdf3.xsl')

#transform = etree.XSLT('D:/My Ontologies/ClinVar/VisualizeClinvar-master/database/clinvarXform.xsl')
def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
    return not bool(search(strg))

def special_match_num(strg, search=re.compile(r'[^0-9.]').search):
    return not bool(search(strg))

#print (special_match_num("123.98"))
runClinVar('D:\My Ontologies\ClinVar\ClinVarFullRelease_2014-06\ClinVarFullRelease_2014-06.xml','D:/My Workspaces/EmptyTest/visumpoint/140815/Clinvar140821-2.ttl')






