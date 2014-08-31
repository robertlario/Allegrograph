__author__ = 'lario'
from franz.openrdf.sail.allegrographserver import AllegroGraphServer
from franz.openrdf.repository.repository import Repository
from franz.miniclient import repository
from franz.openrdf.query.query import QueryLanguage
from franz.openrdf.model import URI
from franz.openrdf.vocabulary.rdf import RDF
from franz.openrdf.vocabulary.rdfs import RDFS
from franz.openrdf.vocabulary.owl import OWL
from franz.openrdf.vocabulary.xmlschema import XMLSchema
from franz.openrdf.query.dataset import Dataset
from franz.openrdf.rio.rdfformat import RDFFormat
from franz.openrdf.rio.rdfwriter import NTriplesWriter
from franz.openrdf.rio.rdfxmlwriter import RDFXMLWriter
import csv
import re

import os, urllib, datetime, time, sys

CURRENT_DIRECTORY = os.getcwd()

#AG_HOST = os.environ.get('AGRAPH_HOST', 'interconnectedhealth.org')

AG_HOST = os.environ.get('AGRAPH_HOST', '192.168.1.16')
AG_PORT = int(os.environ.get('AGRAPH_PORT', '10035'))
AG_CATALOG = os.environ.get('AGRAPH_CATALOG', 'system')
# AG_CATALOG = ''
AG_REPOSITORY = 'RxNormSnomed140625'
AG_USER = 'testUser'
AG_PASSWORD = 'testUser'


def Main():
    starttime = time.clock()
    conn = getConnection()
    outStream = open('d:/My Junk/results140626.csv', 'w')
    x = 0
    with open('d:/My Junk/rxcui.csv', 'r') as f:
        lineRaw = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for line in lineRaw:
            x = x+ 1
            print("%s \t- \t%s" % (x,line[0]))
            queryString = finalQuery(line[0])
            runQuery(line[0],conn,queryString,outStream)
        f.close()
    outStream.close()
    print("\nElapsed time: %s seconds." % (time.clock() - starttime))


def example0():
    """
    Can we connect to AG?
    """
    print ("Starting example example0().")
    print "Current working directory is '%s'" % (os.getcwd())
    server = AllegroGraphServer(AG_HOST, AG_PORT, AG_USER, AG_PASSWORD)
    print "Available catalogs", server.listCatalogs()


def getConnection(accessMode=Repository.ACCESS):
    """
    Tests getting the repository up.  Is called by the other examples to do the startup.
    """
    print "Starting example1()."
    print "Default working directory is '%s'" % (CURRENT_DIRECTORY)
    server = AllegroGraphServer(AG_HOST, AG_PORT, AG_USER, AG_PASSWORD)
    print "Available catalogs", server.listCatalogs()
##    catalog = server.openCatalog(AG_CATALOG)  ## named catalog
    catalog = server.openCatalog()             ## default rootCatalog
    print "Available repositories in catalog '%s':  %s" % (catalog.getName(), catalog.listRepositories())
    myRepository = catalog.getRepository(AG_REPOSITORY, accessMode)

    conn = myRepository.getConnection()

    print "Repository %s is up!  It contains %i statements." % ( myRepository.getDatabaseName(), conn.size())
    indices = conn.listValidIndices()
    print "All valid triple indices: %s" % (indices)
    indices = conn.listIndices()
    print "Current triple indices: %s" % (indices)
    return conn

def finalQuery(rxcui):
    query = "PREFIX rx: <http://purl.bioontology.org/ontology/RXNORM/>\n"\
            "SELECT DISTINCT ?rxcui ?scui ?label ?Ancestor ?Ancestorlabel\n"\
            "where\n"\
            "{\n"\
            "?acui rx:RXCUI \"%s\"^^xsd:string;\n"\
            "rx:SCUI ?scui;\n"\
            "rx:SAB \"SNOMEDCT_US\"^^xs:string .\n"\
            "{{\n"\
            "?acui2 rx:RXCUI \"%s\"^^xsd:string;\n"\
            "rx:TTY \"IN\"^^xs:string .}\n"\
            "UNION\n"\
            "{\n"\
            "?acui2 rx:RXCUI \"%s\"^^xsd:string;\n"\
            "rx:TTY \"PIN\"^^xs:string .}}\n"\
            "?scui rdfs:label ?label;\n"\
            "((rdfs:subClassOf+/(owl:intersectionOf/rdf:rest*/rdf:first)*)*) ?Ancestor .\n"\
            "?Ancestor rdfs:label ?Ancestorlabel.}" %(rxcui,rxcui,rxcui)

    return query
def getQueryString(rxcui):
    query = "PREFIX rx: <http://purl.bioontology.org/ontology/RXNORM/>\n"\
            "SELECT DISTINCT ?rxcui ?scui ?label ?Ancestor ?Ancestorlabel\n"\
            "where\n"\
            "{\n"\
            '?acui rx:RXCUI "%s"^^xsd:string;\n'\
            'rx:SCUI ?scui;\n'\
            'rx:SAB "SNOMEDCT_US"^^xs:string .\n'\
            '{{\n'\
            '?acui2 rx:RXCUI "%s"^^xsd:string;\n'\
            'rx:TTY "IN"^^xs:string .}\n'\
            'UNION\n'\
            '{\n'\
            '?acui2 rx:RXCUI "%s"^^xsd:string;\n'\
            'rx:TTY "PIN"^^xs:string .}}\n'\
            '?scui rdfs:label ?label;\n'\
            '((rdfs:subClassOf+/(owl:intersectionOf/rdf:rest*/rdf:first)*)*) ?Ancestor .\n'\
            '?Ancestor rdfs:label ?Ancestorlabel.}' % (rxcui,rxcui,rxcui)

    return query

def getQueryString2(rxcui):
    query = "PREFIX rx: <http://purl.bioontology.org/ontology/RXNORM/>\n"\
            "SELECT DISTINCT ?rxcui ?scui ?label ?Ancestor ?Ancestorlabel\n"\
            "where\n"\
            "{\n"\
            "?acui rx:RXCUI \"1841\"^^xsd:string;\n"\
            "rx:SCUI ?scui;\n"\
            "rx:SAB \"SNOMEDCT_US\"^^xs:string .\n"\
            "{{\n"\
            "?acui2 rx:RXCUI \"1841\"^^xsd:string;\n"\
            "rx:TTY \"IN\"^^xs:string .}\n"\
            "UNION\n"\
            "{\n"\
            "?acui2 rx:RXCUI \"1841\"^^xsd:string;\n"\
            "rx:TTY \"PIN\"^^xs:string .}}\n"\
            "?scui rdfs:label ?label;\n"\
            "((rdfs:subClassOf+/(owl:intersectionOf/rdf:rest*/rdf:first)*)*) ?Ancestor .\n"\
            "?Ancestor rdfs:label ?Ancestorlabel.}"

    return query


def getQueryString3(rxcui):
    query = "PREFIX rx: <http://purl.bioontology.org/ontology/RXNORM/>\n"\
            "SELECT DISTINCT ?s\n"\
            "where\n"\
            "{\n"\
            "?s rx:RXCUI \"1841\"^^xsd:string.\n"\
            "}"

    return query


def getQueryString4(rxcui):
    query = "SELECT DISTINCT ?s where { ?s <http://purl.bioontology.org/ontology/RXNORM/RXCUI> \"1841\"^^xsd:string.}"
    return query

def runQuery(rxcui,conn,queryString,outStream):
    tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
    result = tupleQuery.evaluate()
    try:
        for bindingSet in result:
            scui = bindingSet.getValue("scui")
            label = bindingSet.getValue("label")
            Ancestor = bindingSet.getValue("Ancestor")
            Ancestorlabel = bindingSet.getValue("Ancestorlabel")

            outStream.write("%s\t%s\t%s\t%s\t%s\n" % (rxcui,scui,label,Ancestor,Ancestorlabel))
    finally:
         result.close()

def Test1(rxcui):
    print (rxcui)
    conn = getConnection()
    print "Starting Test1()."
    print "Default working directory is '%s'" % (CURRENT_DIRECTORY)
    print "SPARQL query for all triples in repository."
    try:
        queryString = rxcui
        tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
        result = tupleQuery.evaluate()
        try:
            #?rxcui ?scui ?label ?Ancestor ?Ancestorlabel
            for bindingSet in result:
                scui = bindingSet.getValue("scui")
                label = bindingSet.getValue("label")
                Ancestor = bindingSet.getValue("Ancestor")
                Ancestorlabel = bindingSet.getValue("Ancestorlabel")
                print "%s %s %s %s %s" % ("1841",scui,label,Ancestor,Ancestorlabel)
                #print(bindingSet.getValue("s"))
        finally:
            result.close();
    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )
    finally:
        conn.close();
        myRepository = conn.repository
        myRepository.shutDown()
print("start")
#print (getQueryString("1841"))
#Test1(finalQuery("1841"))
Main()
print("end")
