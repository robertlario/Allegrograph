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
#AG_HOST = os.environ.get('AGRAPH_HOST', '76.97.184.104')
AG_PORT = int(os.environ.get('AGRAPH_PORT', '10035'))
AG_CATALOG = os.environ.get('AGRAPH_CATALOG', 'system')
# AG_CATALOG = ''
AG_REPOSITORY = 'RxNormSnomed140715'
AG_USER = 'testUser'
AG_PASSWORD = 'testUser'

def createTables():
    table = {}
    INGREDIENT = 0
    ACUI = 1
    RXCUI = 2
    with open('D:/My Utah/PharmD - Nelson/DataSet/analysis140715/Analysis140716/igredients acui rxcui.csv', 'r') as f:
        lineRaw = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for line in lineRaw:
            ingredient = line[INGREDIENT]
            acui = line[ACUI]
            rxcui = line[RXCUI]
            print("%s \t\ %s \t %s\n" % (ingredient, acui, rxcui))
            if rxcui not in table :
                row = {acui,rxcui}
                table[rxcui] = row
        f.close()
    return table
def repairProduct():
    starttime = time.clock()
    conn = getConnection()

    SCUIPredicate = conn.createURI("http://purl.bioontology.org/ontology/RXNORM/SCUI")
    x = 0
    with open('D:/My Utah/PharmD - Nelson/DataSet/Analysis140716/igredients acui rxcui.csv', 'r') as f:
        try:
            lineRaw = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                x = x+ 1
                print("%s \t- \t%s\t\t" % (x,line[0])),
                queryString = QueryGetProductUsingIngredient(line[0])
                try:
                    tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
                    result = tupleQuery.evaluate()
                    for bindingSet in result:
                        productWithHasIngredient = bindingSet.getValue("productWithHasIngredient")
                    conn.add(line[2], SCUIPredicate, productWithHasIngredient)
                    result.close()
                    print("%s\t%s\t%s" % (line[2], SCUIPredicate, productWithHasIngredient))
                except:
                    e = sys.exc_info()[0]
                    print(  "Error: %s" % e )
                    print("\t FAILED %s \t- \t%s" % (x,line[0]))
        finally:
            f.close()
            conn.close()
            myRepository = conn.repository
            myRepository.shutDown()
    print("\nElapsed time: %s seconds." % (time.clock() - starttime))


def repairSubstance():
    starttime = time.clock()
    conn = getConnection()

    SCUIPredicate = conn.createURI("http://purl.bioontology.org/ontology/RXNORM/SCUI")
    x = 0
    with open('D:/My Utah/PharmD - Nelson/DataSet/analysis140715/RXCUI_Substance_False.csv', 'r') as f:
        try:
            lineRaw = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            for line in lineRaw:
                x = x+ 1
                print("%s \t- \t%s\t\t" % (x,line[0])),
                queryString = finalRrepareSubstanceSelect(line[0])
                try:
                    tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
                    result = tupleQuery.evaluate()
                    for bindingSet in result:
                        Ancestor = bindingSet.getValue("Ancestor")
                        acui = bindingSet.getValue("acui")
                    conn.add(acui, SCUIPredicate, Ancestor)
                    result.close()
                    print("%s\t%s\t%s" % (acui, SCUIPredicate, Ancestor))
                except:
                    e = sys.exc_info()[0]
                    print(  "Error: %s" % e )
                    print("\t FAILED %s \t- \t%s" % (x,line[0]))
        finally:
            f.close()
            conn.close()
            myRepository = conn.repository
            myRepository.shutDown()
    print("\nElapsed time: %s seconds." % (time.clock() - starttime))



def Main():
    starttime = time.clock()
    conn = getConnection()
    outStream = open('D:/My Utah/PharmD - Nelson/DataSet/analysis140715/results_RXCUI_140715-fixedsubstance-raw.csv', 'w')
    x = 0
    try:
        with open('D:/My Utah/PharmD - Nelson/DataSet/RXCUI.csv', 'r') as f:
            try:
                lineRaw = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
                for line in lineRaw:
                    x = x+ 1
                    print("%s \t- \t%s" % (x,line[0])),
                    queryString = finalQueryEquivalent(line[0])
                    runQuery(line[0],conn,queryString,outStream)
            finally:
                f.close()
    finally:
        outStream.close()
    print("\nElapsed time: %s seconds." % (time.clock() - starttime))


def getConnection(accessMode=Repository.ACCESS):

    print "getConnection"
    print "Default working directory is '%s'" % (CURRENT_DIRECTORY)
    server = AllegroGraphServer(AG_HOST, AG_PORT, AG_USER, AG_PASSWORD)
    print "Available catalogs", server.listCatalogs()
    catalog = server.openCatalog()
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

def finalQueryEquivalent(rxcui):
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
            "((rdfs:subClassOf+/(owl:equivalentClass*/owl:intersectionOf/rdf:rest*/rdf:first)*)*) ?Ancestor .\n"\
            "?Ancestor rdfs:label ?Ancestorlabel.}" %(rxcui,rxcui,rxcui)

    return query


def finalQueryEquivalentSomeValuesFrom(rxcui):
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
            "(rdfs:subClassOf+/(owl:equivalentClass*/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom*/rdfs:subClassOf*)*)* ?Ancestor .\n"\
            "?Ancestor rdfs:label ?Ancestorlabel.}" %(rxcui,rxcui,rxcui)

    return query

def finalQueryBrokenSubstance(rxcui):
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
            "(rdfs:subClassOf/owl:equivalentClass*/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom) ?Ancestor .\n"\
            "?Ancestor rdfs:label ?Ancestorlabel.}" %(rxcui,rxcui,rxcui)

    return query

def finalRrepareSubstance(rxcui):
    query = "PREFIX rx: <http://purl.bioontology.org/ontology/RXNORM/>\n"\
            "insert\n"\
            "{\n"\
            "\t?acui <http://purl.bioontology.org/ontology/RXNORM/RXCUI>  \"%s\"^^xs:string;\n"\
  		    "\t<http://purl.bioontology.org/ontology/RXNORM/SCUI> ?Ancestor;\n"\
  		    "\t<http://purl.bioontology.org/ontology/RXNORM/SAB> \"SNOMEDCT_US\"^^xs:string ;\n"\
  		    "\t<http://purl.bioontology.org/ontology/RXNORM/TTY> \"IN\"^^xs:string ;\n"\
  		    "\t<http://purl.bioontology.org/ontology/RXNORM/TTY>  \"PIN\"^^xs:string ;\n"\
  		    "\t<http://www.visumpoint/RXNORM_REPAIR>  \"Substance\"^^xs:string  .\n"\
            "}\n"\
            "where\n"\
            "{\n"\
            "\tselect  ?Ancestor ?acui"\
            "\t{\n"\
            "\t\t?acui rx:RXCUI \"%s\"^^xsd:string;\n"\
            "\t\t\trx:SCUI ?scui;\n"\
            "\t\t\trx:SAB \"SNOMEDCT_US\"^^xs:string .\n"\
            "\t{{\n"\
            "\t\t?acui2 rx:RXCUI \"%s\"^^xsd:string;\n"\
            "\t\t\trx:TTY \"IN\"^^xs:string .}\n"\
            "\tUNION\n"\
            "\t{\n"\
            "\t\t?acui2 rx:RXCUI \"%s\"^^xsd:string;\n"\
            "\t\t\trx:TTY \"PIN\"^^xs:string .}}\n"\
            "\t?scui rdfs:label ?label;\n"\
            "\t\trdfs:subClassOf/(owl:equivalentClass*/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom*)* ?Ancestor  .\n"\
            "\t?Ancestor rdfs:label ?Ancestorlabel.\n"\
	        "\tFILTER regex(?Ancestorlabel, \"substance\") \n"\
            "\t} LIMIT 1\n"\
            "}" %(rxcui,rxcui,rxcui,rxcui)
    return query


def finalRrepareSubstanceSelect(rxcui):
    query = "PREFIX rx: <http://purl.bioontology.org/ontology/RXNORM/>\n"\
            "select  ?Ancestor ?acui"\
            "\t{\n"\
            "\t\t?acui rx:RXCUI \"%s\"^^xsd:string;\n"\
            "\t\t\trx:SCUI ?scui;\n"\
            "\t\t\trx:SAB \"SNOMEDCT_US\"^^xs:string .\n"\
            "\t{{\n"\
            "\t\t?acui2 rx:RXCUI \"%s\"^^xsd:string;\n"\
            "\t\t\trx:TTY \"IN\"^^xs:string .}\n"\
            "\tUNION\n"\
            "\t{\n"\
            "\t\t?acui2 rx:RXCUI \"%s\"^^xsd:string;\n"\
            "\t\t\trx:TTY \"PIN\"^^xs:string .}}\n"\
            "\t?scui rdfs:label ?label;\n"\
            "\t\trdfs:subClassOf/(owl:equivalentClass*/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom*)* ?Ancestor  .\n"\
            "\t?Ancestor rdfs:label ?Ancestorlabel.\n"\
	        "\tFILTER regex(?Ancestorlabel, \"substance\") \n"\
            "\t} LIMIT 1\n" %(rxcui,rxcui,rxcui)
    return query


def QuerygetIgredient(rxcui):
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
            "?hasIngredients owl:someValuesFrom ?ingredient.\n"\
  	        "?hasIngredients owl:onProperty <http://snomed.info/id/127489000>.\n"\
            "} LIMIT 1" %(rxcui,rxcui,rxcui)
    return query

def QueryGetProductUsingIngredient(ingredient):
    query = "PREFIX rx: <http://purl.bioontology.org/ontology/RXNORM/>\n"\
            "SELECT DISTINCT ?productWithHasIngredient\n"\
            "?productWithHasIngredient rdfs:subClassOf/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom  %s;\n"\
            "\trdfs:label ?label.\n"\
            "} LIMIT 1" %(ingredient)
    return query

def runQuery(rxcui,conn,queryString,outStream, trip = 0):
    try:
        tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
        result = tupleQuery.evaluate()
        try:
            if result.rowCount() < 1 :
                print(" \t\t %s No rows"% (rxcui) ),
                runQuery(rxcui,conn,finalQuery(rxcui),outStream,2)
            else :
                 if result.rowCount() > 0 :
                    print(" \t\t %s ok"% (rxcui) )
            for bindingSet in result:
                scui = bindingSet.getValue("scui")
                label = bindingSet.getValue("label")
                Ancestor = bindingSet.getValue("Ancestor")
                Ancestorlabel = bindingSet.getValue("Ancestorlabel")

                outStream.write("%s\t%s\t%s\t%s\t%s\n" % (rxcui,scui,label,Ancestor,Ancestorlabel))
        except:
                 outStream.write("%s\t%s\t%s\t%s\t%s\n" % (rxcui,'ERROR','ERROR','ERROR','ERROR'))
        finally:
             result.close()
    except:
        if trip == 0 :
            print(" \t\t %s trip 1"% (rxcui) ),
            runQuery(rxcui,conn,finalQueryEquivalent(rxcui),outStream, 1)
        else :
            if trip == 1 :
                print(" \t\t %s trip 2"% (rxcui) ),
                runQuery(rxcui,conn,finalQuery(rxcui),outStream,2)


        #outStream.write("%s\t%s\t%s\t%s\t%s\n" % (rxcui,'Query-ERROR','Query-ERROR','Query-ERROR','Query-ERROR'))

def Test1(rxcui):
    print (rxcui)
    conn = getConnection()

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
        finally:
            result.close();
    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )
    finally:
        conn.close();
        myRepository = conn.repository
        myRepository.shutDown()


#Main()
#repairSubstance()
repairProduct()

