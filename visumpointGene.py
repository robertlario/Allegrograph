__author__ = 'lario'
GO = "http://purl.obolibrary.org/obo"
VP = "http://www.visumpoint.com/2014/gene"
OMIM = "http://www.ncbi.nlm.nih.gov/nuccore"
RefSeq = ""
PubMed = "http://www.ncbi.nlm.nih.gov/pubmed"
URI_GO = "http://purl.obolibrary.org/obo"
URI_VP = "http://www.visumpoint.com/2014/gene"
URI_OMIM = "http://www.ncbi.nlm.nih.gov/nuccore"
URI_RefSeq = ""
URI_PubMed = "http://www.ncbi.nlm.nih.gov/pubmed"
URI_PharmGKB = "http://www.visumpoint.com/2014/gene"
URI_SnoMedCT = "http://snomed.info/id"
#http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id=HGNC:1100
HUGO = VP + "/HGNC"
HGNC = VP + "/HGNC"
#Mouse Genome Database ID(supplied by MGI)
MGI = ""

#Rat Genome Database ID(supplied by RGD)
RGD = ""

#Entrez Gene ID(supplied by NCBI)
EG = "http://www.ncbi.nlm.nih.gov/gene/"
URI_EG = "http://www.ncbi.nlm.nih.gov/gene"

#Ensembl ID(supplied by Ensembl)
ENSG = ""

def trueFalse(value):
    str = value.lower()
    if str.startswith("t"):
        return "true"
    return "false"

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

def urlHGNC (str):
    return "<%s/%s>" % (HUGO,str)

def urlGO (str):
    return "<%s/%s>" % (GO,str)

def symbol (str):
    return "<%s/symbol/%s>" % (HUGO,str)

def printHasSymbol(stream, type, id, tab = "",endWith = ";"):
    stream.write ("#ERROR Deprecated printHasSymbol %s %s %s\n" % (type,id))

def printHasGeneRelationship(stream, type, id, source, tab = "", endWith = ";"):
    stream.write('%sVP:hasGeneRelationship [\n' % (tab))
    stream.write('%s\t\tVP:Symbol %s;\n' % (tab,symbol(id)))
    stream.write('%s\t\trdfs:label "%s"^^xsd:string;\n' % (tab,id))
    stream.write('%s\t\tVP:Source %s ;\n' % (tab, source))
    stream.write('%s\t]%s\n' % (tab,endWith))


def printHasSymbol(stream, type, id, source, tab = "", endWith = ";"):
    stream.write('%sVP:hasSymbol [\n' % (tab))
    stream.write('%s\t\tVP:Symbol %s;\n' % (tab,symbol(id)))
    stream.write('%s\t\trdfs:label "%s"^^xsd:string;\n' % (tab,id))
    stream.write('%s\t\tVP:Source %s ;\n' % (tab, source))
    stream.write('%s\t]%s\n' % (tab,endWith))

def printCitation(stream, type, id, tab = "",endWith = ";"):
    stream.write ("#ERROR Deprecated printCitation %s %s %s\n" % (type,id))

def printCitation(stream, type, id, source, tab = "", endWith = ";"):
    stream.write('%sVP:hasCitation [\n' % (tab))
    if len(id) < 1:
        return;
    if type == "PubMed":
        stream.write('%s\t\ta\tVP:PubMed;\n' % (tab))
        stream.write('%s\t\tVP:ID <%s/%s>;\n' % (tab,PubMed,id))
        stream.write('%s\t\tVP:Source %s ;\n' % (tab,source))
    stream.write('%s\t]%s\n' % (tab,endWith))

def printReferenceTriple(stream, type, id, tab = "",endWith = ";"):
    if type == "RefSeq":
        stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
    elif type == "OMIM":
        stream.write('%s\t\tVP:ID <%s/%s>;\n' % (tab,OMIM,id))
    elif type == "EntrezGeneID":
        stream.write('%s\t\tVP:ID <%s/%s>;\n' % (tab,EG,id))
    elif type == "EnzymeID":
        stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
    elif type == "EnsemblGeneID":
        stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
    elif type == "MouseGenomeID":
        stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
    elif type == "CCSDID":
        stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
    elif type == "VegaID":
        stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
    elif type == "UCSCID":
        stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
    elif type == "RatGenomeID":
        stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))


    return stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
def printGenericName(stream, type, id, source, tab = "",endWith = ";"):
    stream.write('%sVP:GenericNames[\n' % (tab))
    stream.write('%s\t\tVP:GenericName "%s"^^xsd:string;\n' % (tab,id))
    stream.write('%s\t\trdfs:label "%s"^^xsd:string;\n' % (tab,id))
    stream.write('%s\t\tVP:Source %s ;\n' % (tab, source))
    stream.write('%s\t]%s\n' % (tab,endWith ))

def printTradeName(stream, type, id, source, tab = "",endWith = ";"):
    stream.write('%sVP:TradeNames[\n' % (tab))
    stream.write('%s\t\tVP:TradeName "%s"^^xsd:string;\n' % (tab,id))
    stream.write('%s\t\trdfs:label "%s"^^xsd:string;\n' % (tab,id))
    stream.write('%s\t\tVP:Source %s ;\n' % (tab, source))
    stream.write('%s\t]%s\n' % (tab,endWith ))

def printAlternativeName(stream, type, id, source, tab = "",endWith = ";"):
    stream.write('%sVP:AlternateNames[\n' % (tab))
    stream.write('%s\t\tVP:AlternateName "%s"^^xsd:string;\n' % (tab,id))
    stream.write('%s\t\trdfs:label "%s"^^xsd:string;\n' % (tab,id))
    stream.write('%s\t\tVP:Source %s ;\n' % (tab, source))
    stream.write('%s\t]%s\n' % (tab,endWith ))

def smiles(str):
    newstr = str.replace("\\",'--')
    newstr = safe_str(newstr)
    return '"%s"^^xsd:string' % newstr

'[H]/N=C(\\N)/NCCC[C@@H](C(=O)N1CCC[C@H]1C(=O)NCC(=O)NCC(=O)NCC(=O)NCC(=O)N[C@@H](CC(=O)N)C(=O)NCC(=O)N[C@@H](CC(=O)O)C(=O)N[C@@H](CC2=CC=CC=C2)C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H]([C@@H](C)CC)C(=O)N3CCC[C@H]3C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H](CCC(=O)O)C(=O)N[C@@H](CC4=CC=C(C=C4)O)C(=O)N[C@@H](CC(C)C)C(=O)O)NC(=O)[C@@H]5CCCN5C(=O)[C@@H](CC6=CC=CC=C6)N'

RefSeq = "RefSeq"
PubMed = "PubMed"
EntrezGene_ID = "EntrezGeneID"
Ensembl_ID = "EnsemblGeneID"
Enzyme_ID = "EnzymeID"
OMIM_ID = "OMIM"
Vega_ID = "VegaID"


VP_GO = "VP:GO"
VP_RefSeq = "VP:RefSeq"
VP_HumanCycGene = "VP:HumanCycGene"
VP_Alfred = "VP:Alfred"
VP_CTD = "VP:CTD"
VP_Ensembl = "VP:Ensembl"
VP_EntrezGene = "VP:EntrezGene"
VP_Enzyme = "VP:Enzyme"
VP_GenAtlas = "VP:GenAtlas"
VP_GeneCard = "VP:GeneCard"
VP_GO = "VP:GO"
VP_HGNC = "VP:HGNC"
VP_HUGO = "VP:HUGO"
VP_SCT = "VP:SCT"
VP_OMIM = "VP:OMIM"
VP_PharmGKB = "VP:PharmGKB"
VP_PharmGKBGene = "VP:PharmGKBGene"
VP_PharmGKBDisease = "VP:PharmGKBDisease"
VP_PharmGKBDrug = "VP:PharmGKBDrug"
VP_ModBas = "VP:ModBas"
VP_MouseGenome = "VP:MouseGenome"
VP_Vega="VP:Vega"
VP_DBase = "VP:DBase"
VP_MutDb = "VP:MutDb"
VP_RefSeq = "VP:RefSeq"
VP_dbSNP = "VP:dbSNP"
VP_HUGE = "VP:HUGE"
VP_URL = "VP:URL"
VP_UniProtKb = "VP:UniProtKb"
VP_UCSCGenomeBrowser = "VP:UCSCGenomeBrowser"
VP_IupharReceptor = "VP:IupharReceptor"
VP_ClinVar = "VP:ClinVar"
VP_Mesh = "VP:Mesh"
VP_MedDRA = "VP:MedDRA"
VP_NDFRT = "VP:NDFRT"
VP_SnoMedCT = "VP:SnoMedCT"
VP_UMLS = "VP:UMLS"
VP_Unknown = "VP:Unknown"
VP_TTD = "VP:TTD"
VP_BindingDb = "VP:BindingDb"
VP_ChemSpider = "VP:ChemSpider"
VP_DrugBank = "VP:DrugBank"
VP_KeggCompound = "VP:KeggCompound"
VP_PubChemCompound = "VP:PubChemCompound"
VP_SubChemSubstance = "VP:SubChemSubstance"
VP_DailyMed = "VP:DailyMed"
VP_HET = "VP:HET"
VP_ClinicalTrials = "VP:ClinicalTrials"
VP_DPD = "VP:DPD"
VP_Chebi = "VP:Chebi"
VP_Genbank = "VP:Genbank"
VP_NDC = "VP:NDC"
VP_Iupharligand = "VP:Iupharligand"
VP_Keggdrug = "VP:Keggdrug"
VP_PDB = "VP:PDB"
VP_SMILES = "VP:SMILES"
VP_RefSeqProt = "VP:RefSeqProt"

def printCrossReference(stream, type, id, tab = "",endWith = ";"):
    stream.write ("#ERROR Deprecated printCrossReference %s %s %s\n" % (type,id))

def printCrossReference(stream, type, id, source, tab = "",endWith = ";"):
    try:
        stream.write('%sVP:hasReference [\n' % (tab))
        if type == VP_RefSeqProt:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_RefSeqProt))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_PDB:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_PDB))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_Keggdrug:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_Keggdrug))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_Iupharligand:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_Iupharligand))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_NDC:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_NDC))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_Genbank:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_Chebi))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_Chebi:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_Chebi))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_DPD:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_DPD))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_ClinicalTrials:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_ClinicalTrials))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_HET:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_HET))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_DailyMed:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_DailyMed))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_SubChemSubstance:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_SubChemSubstance))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_DrugBank:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_DrugBank))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_KeggCompound:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_KeggCompound))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_PubChemCompound:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_PubChemCompound))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))

        if type == VP_ChemSpider:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_ChemSpider))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_BindingDb:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_BindingDb))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_TTD:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_TTD))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_UMLS:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_UMLS))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_NDFRT:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_NDFRT))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_Mesh:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_Mesh))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_MedDRA:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_MedDRA))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_dbSNP:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_dbSNP))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_CTD:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_CTD))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_URL:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_URL))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_IupharReceptor:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_IupharReceptor))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_Alfred:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_Alfred))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_HumanCycGene:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_HumanCycGene))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_UCSCGenomeBrowser:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_UCSCGenomeBrowser))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_UniProtKb:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_UniProtKb))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_MutDb:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_MutDb))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_ModBas:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_ModBas))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_HGNC:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_HGNC))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_HUGO:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_HUGO))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_GenAtlas:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_GenAtlas))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        if type == VP_SCT or type == VP_SnoMedCT:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_SnoMedCT))
            stream.write('%s\t\tVP:ID <%s/%s>;\n' % (tab,URI_SnoMedCT, id))
        if type == VP_GeneCard:
            stream.write('%s\t\ta\t%s;\n' % (tab,VP_GeneCard))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))

        if type == "RefSeq" or type == VP_RefSeq:
            stream.write('%s\t\ta\tVP:RefSeq;\n' % (tab))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string;\n' % (tab,id))
        elif type == OMIM_ID or type == VP_OMIM:
            stream.write('%s\t\ta\tVP:OMIM;\n' % (tab))
            stream.write('%s\t\tVP:ID <%s/%s>;\n' % (tab,OMIM,id))
        elif type == EntrezGene_ID or type == VP_EntrezGene:
            stream.write('%s\t\ta\tVP:EntrezGene;\n' % (tab))
            stream.write('%s\t\tVP:ID <%s/%s>;\n' % (tab,URI_EG,id))

        elif type == Enzyme_ID or type == VP_Enzyme:
            stream.write('%s\t\ta\tVP:Enzyme;\n' % (tab))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
        elif type == Ensembl_ID or type == VP_Ensembl:
            stream.write('%s\t\ta\tVP:EnsemblGene;\n' % (tab))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
        elif type == "MouseGenomeID":
            stream.write('%s\t\ta\tVP:MouseGenome;\n' % (tab))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
        elif type == "CCSDID":
            stream.write('%s\t\ta\tVP:CCSDID;\n' % (tab))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
        elif type == Vega_ID:
            stream.write('%s\t\ta\tVP:Vega;\n' % (tab))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
        elif type == "UCSCID":
            stream.write('%s\t\ta\tVP:UCSCID;\n' % (tab))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
        elif type == "RatGenomeID":
            stream.write('%s\t\ta\tVP:RatGenomeID;\n' % (tab))
            stream.write('%s\t\tVP:ID "%s"^^xsd:string  ;\n' % (tab,id))
        elif type == VP_GO:
            stream.write('%s\t\ta\t%s;\n' % (tab, VP_GO))
            stream.write('%s\t\tVP:ID %s;\n' % (tab, urlGO("GO_" + id)))
        stream.write('%s\t\tVP:Source %s ;\n' % (tab, source))
        stream.write('%s\t\tVP:StringID "%s"^^xsd:string ; # %s\n' % (tab,id,type))

        stream.write('%s\t]%s\n' % (tab,endWith ))
    except:
        stream.write('# Error XREF - Type : >%s< id : >%s< source : >%s<\n'% (type,id,source))


def strip(str):
    return str.strip('" \n\t\"\'')

def ontologyClass (str):
    if str.lower() == "preferred":
        return "VP:Preferred"
    if str.lower() == "current":
        return "VP:Current"
    if str.lower() == "approve":
        return "VP:Approve"
    if str.lower() == "alternate":
        return "VP:Alternate"
    return "\"%s\"^^xsd:string" % str