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

AG_HOST = os.environ.get('AGRAPH_HOST', 'www.interconnectedHealth.org')
#AG_HOST = os.environ.get('AGRAPH_HOST', '76.97.184.104')
AG_PORT = int(os.environ.get('AGRAPH_PORT', '10035'))
AG_CATALOG = os.environ.get('AGRAPH_CATALOG', 'system')
# AG_CATALOG = ''
AG_REPOSITORY = 'HUGO_CLIN_SNOMED140813'
AG_USER = 'testUser'
AG_PASSWORD = 'testUser'

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
def getQuery (geneName):
    return "select ?hugo \n"\
           "{\n"\
            "?hugo rdfs:subClassOf	<http://www.visumpoint.com/2014/gene/HUGO>.\n" \
            "?hugo <http://www.visumpoint.com/2014/gene/ApprovedSymbol>  <http://www.visumpoint.com/2014/gene/HGNC/symbol/%s>.\n" \
            "}\n" % geneName
def main():
        x = 0
        queryString =   "select ?date ?symbol {?s rdfs:subClassOf <http://www.visumpoint.com/2014/gene/HUGO>. "\
                        "?s <http://www.visumpoint.com/2014/gene/DateSymbolChanged> ?date. "\
                        "?s <http://www.visumpoint.com/2014/gene/ApprovedSymbol> ?symbol. "\
                        "}"
        queryString = getQuery("FOXA2")
        conn = getConnection()
        tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
        try:
            with open('d:/my junk/text.txt', 'r') as f:
                try:
                    lineRaw = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
                    for line in lineRaw:
                        queryString = getQuery(line[0])
                        tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
                        result = tupleQuery.evaluate()
                        try:
                            for bindingSet in result:
                                hugo = bindingSet.getValue("hugo")
                                print ("HUGO %s " % (hugo))

                        except:
                            e = sys.exc_info()
                            print( "Error1: %s - %s -%s" % (e[0], e[1], e[2]))
                        finally:
                            result.close()
                except:
                    e = sys.exc_info()
                    print( "Error2: %s - %s -%s" % (e[0], e[1], e[2]))
        except:
            e = sys.exc_info()
            print( "Error3: %s - %s -%s" % (e[0], e[1], e[2]))


main()