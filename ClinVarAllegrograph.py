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

def getConnection(host, port, user, password, repository):
    try:

        server = AllegroGraphServer(AG_HOST, AG_PORT, AG_USER, AG_PASSWORD)
        server = AllegroGraphServer(host, port, user, password)
        catalog = server.openCatalog()
        myRepository = catalog.getRepository(repository, Repository.ACCESS)
        connection = myRepository.getConnection()
    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )
    return connection



def main():
    host =  'http://www.interconnectedhealth.org'
    host =  '192.168.1.16'
    port = 10035

    repositoryName = 'clinVar140525'
    user = 'testUser'
    password = 'testUser'
    try:
        connection = getConnection(host, port, user, password, repositoryName)
        print "Repository %s is up!  It contains %i statements." % ( connection.repository.getDatabaseName(), connection.size())
        try:
            queryString = "SELECT ?s ?p ?o  WHERE {?s ?p ?o .}"
            tupleQuery = connection.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
            result = tupleQuery.evaluate();
            try:
                for bindingSet in result:
                    s = bindingSet.getValue("s")
                    p = bindingSet.getValue("p")
                    o = bindingSet.getValue("o")
                    print "%s %s %s" % (s, p, o)
            finally:
                result.close()
        finally:
            connection.close()
            myRepository = connection.repository
            myRepository.shutDown()
    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )

main()