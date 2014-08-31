__author__ = 'lario'
import csv
import re

import os, urllib, datetime, time, sys
import xml.etree.ElementTree as ET
import clinvar13

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


def processReferenceClinVarAssertion(referenceClinVarAssertion, stream = sys.stdout):
    stream.write('DECLARE @newKey AS INT;\n')
    stream.write('SET @NewKey = @@IDENTITY;\n')
    stream.write("INSERT INTO referenceClinVarAssertion (tbl1_ID,col1, col2) VALUES (@NewKey, 'moredata1', 'moredata2'....);\n'")
    stream.write('\n')

def processClinVarSet(clinVarSet, stream):
    if 'ID' in clinVarSet.attrib :
        stream.write("INSERT INTO ClinVarSet (")
        stream.write("RecordStatus")
    # some more column names
        stream.write(") VALUES (")
        stream.write("%s" % (clinVarSet.xpath('RecordStatus/text()[1]')[0]))
        stream.write(");\n")
        referenceClinVarAssertion = clinVarSet.xpath('ReferenceClinVarAssertion[1]')
        if len(referenceClinVarAssertion) > 0 :
            processReferenceClinVarAssertion(referenceClinVarAssertion[0], stream)

def main() :
    try:
        stream = sys.stdout
        tree = etree.parse('D:\My Ontologies\ClinVar\VisualizeClinvar-master\database\clinvar-demo.xml')
        root = tree.getroot()

        for clinVarSet in root:
            processClinVarSet(clinVarSet,stream)

    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )

main()