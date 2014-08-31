# .\clinvar13.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-06-28 12:34:52.438000 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:05c09cde-fee2-11e3-b730-24fd52344a77')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: typeStatus
class typeStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'typeStatus')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 17, 1)
    _Documentation = None
typeStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeStatus, enum_prefix=None)
typeStatus.current = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'current', tag=u'current')
typeStatus.completed_and_retired = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'completed and retired', tag=u'completed_and_retired')
typeStatus.delete = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'delete', tag=u'delete')
typeStatus.in_development = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'in development', tag=u'in_development')
typeStatus.reclassified = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'reclassified', tag=u'reclassified')
typeStatus.reject = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'reject', tag=u'reject')
typeStatus.secondary = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'secondary', tag=u'secondary')
typeStatus.suppressed = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'suppressed', tag=u'suppressed')
typeStatus.under_review = typeStatus._CF_enumeration.addEnumeration(unicode_value=u'under review', tag=u'under_review')
typeStatus._InitializeFacetMap(typeStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'typeStatus', typeStatus)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 119, 3)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.laboratory = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'laboratory', tag=u'laboratory')
STD_ANON.locus_specific_database_LSDB = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'locus-specific database (LSDB)', tag=u'locus_specific_database_LSDB')
STD_ANON.consortium = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'consortium', tag=u'consortium')
STD_ANON.resource = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'resource', tag=u'resource')
STD_ANON.other = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 133, 4)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.current = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'current', tag=u'current')
STD_ANON_.replaced = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'replaced', tag=u'replaced')
STD_ANON_.removed = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'removed', tag=u'removed')
STD_ANON_.not_current = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'not current', tag=u'not_current')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 200, 6)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.RCV = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'RCV', tag=u'RCV')
STD_ANON_2.SCV = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'SCV', tag=u'SCV')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 212, 4)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.current = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'current', tag=u'current')
STD_ANON_3.replaced = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'replaced', tag=u'replaced')
STD_ANON_3.removed = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'removed', tag=u'removed')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 258, 11)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.ModeOfInheritance = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'ModeOfInheritance', tag=u'ModeOfInheritance')
STD_ANON_4.Penetrance = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'Penetrance', tag=u'Penetrance')
STD_ANON_4.AgeOfOnset = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'AgeOfOnset', tag=u'AgeOfOnset')
STD_ANON_4.Severity = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'Severity', tag=u'Severity')
STD_ANON_4.ClinicalSignificanceHistory = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'ClinicalSignificanceHistory', tag=u'ClinicalSignificanceHistory')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 314, 6)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.RCV = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'RCV', tag=u'RCV')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 324, 4)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.current = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'current', tag=u'current')
STD_ANON_6.replaced = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'replaced', tag=u'replaced')
STD_ANON_6.removed = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'removed', tag=u'removed')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 360, 11)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.ModeOfInheritance = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'ModeOfInheritance', tag=u'ModeOfInheritance')
STD_ANON_7.Penetrance = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'Penetrance', tag=u'Penetrance')
STD_ANON_7.AgeOfOnset = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'AgeOfOnset', tag=u'AgeOfOnset')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 405, 14)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.HGVS_genomic_top_level = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, genomic, top level', tag=u'HGVS_genomic_top_level')
STD_ANON_8.HGVS_genomic_RefSeqGene = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, genomic, RefSeqGene', tag=u'HGVS_genomic_RefSeqGene')
STD_ANON_8.HGVS_genomic_LRG = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, genomic, LRG', tag=u'HGVS_genomic_LRG')
STD_ANON_8.HGVS_genomic = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, genomic', tag=u'HGVS_genomic')
STD_ANON_8.HGVS_coding_RefSeq = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, coding, RefSeq', tag=u'HGVS_coding_RefSeq')
STD_ANON_8.HGVS_coding_LRG = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, coding, LRG', tag=u'HGVS_coding_LRG')
STD_ANON_8.HGVS_coding = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, coding', tag=u'HGVS_coding')
STD_ANON_8.HGVS_previous = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, previous', tag=u'HGVS_previous')
STD_ANON_8.HGVS_protein = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, protein', tag=u'HGVS_protein')
STD_ANON_8.HGVS_protein_RefSeq = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, protein, RefSeq', tag=u'HGVS_protein_RefSeq')
STD_ANON_8.HGVS_non_coding = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, non-coding', tag=u'HGVS_non_coding')
STD_ANON_8.HGVS_non_validated = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, non-validated', tag=u'HGVS_non_validated')
STD_ANON_8.HGVS_RNA = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, RNA', tag=u'HGVS_RNA')
STD_ANON_8.HGVS_uncertain = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS, uncertain', tag=u'HGVS_uncertain')
STD_ANON_8.HGVS = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'HGVS', tag=u'HGVS')
STD_ANON_8.NonHGVS = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'NonHGVS', tag=u'NonHGVS')
STD_ANON_8.Location = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'Location', tag=u'Location')
STD_ANON_8.MiscellaneousDescription = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'MiscellaneousDescription', tag=u'MiscellaneousDescription')
STD_ANON_8.Description = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'Description', tag=u'Description')
STD_ANON_8.FunctionalConsequence = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'FunctionalConsequence', tag=u'FunctionalConsequence')
STD_ANON_8.MolecularConsequence = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'MolecularConsequence', tag=u'MolecularConsequence')
STD_ANON_8.ProteinChange1LetterCode = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'ProteinChange1LetterCode', tag=u'ProteinChange1LetterCode')
STD_ANON_8.ProteinChange3LetterCode = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'ProteinChange3LetterCode', tag=u'ProteinChange3LetterCode')
STD_ANON_8.ActivityLevel = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'ActivityLevel', tag=u'ActivityLevel')
STD_ANON_8.GlobalMinorAlleleFrequency = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'GlobalMinorAlleleFrequency', tag=u'GlobalMinorAlleleFrequency')
STD_ANON_8.AlleleFrequency = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'AlleleFrequency', tag=u'AlleleFrequency')
STD_ANON_8.Suspect = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'Suspect', tag=u'Suspect')
STD_ANON_8.Allelic_Variant_previous = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'Allelic Variant, previous', tag=u'Allelic_Variant_previous')
STD_ANON_8.AbsoluteCopyNumber = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'AbsoluteCopyNumber', tag=u'AbsoluteCopyNumber')
STD_ANON_8.acceptor_splice_site = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'acceptor splice site', tag=u'acceptor_splice_site')
STD_ANON_8.donor_splice_site = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'donor splice site', tag=u'donor_splice_site')
STD_ANON_8.nucleotide_change = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'nucleotide change', tag=u'nucleotide_change')
STD_ANON_8.protein_change_historical = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'protein change, historical', tag=u'protein_change_historical')
STD_ANON_8.transcript_variant = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'transcript variant', tag=u'transcript_variant')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 481, 17)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.HGVS = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'HGVS', tag=u'HGVS')
STD_ANON_9.genotype = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'genotype', tag=u'genotype')
STD_ANON_9.gene_relationships = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'gene relationships', tag=u'gene_relationships')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 503, 9)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_10, enum_prefix=None)
STD_ANON_10.variant_in_gene = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'variant in gene', tag=u'variant_in_gene')
STD_ANON_10.co_occurring_variant = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'co-occurring variant', tag=u'co_occurring_variant')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 519, 6)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.Gene = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'Gene', tag=u'Gene')
STD_ANON_11.Variation = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'Variation', tag=u'Variation')
STD_ANON_11.Insertion = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'Insertion', tag=u'Insertion')
STD_ANON_11.Deletion = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'Deletion', tag=u'Deletion')
STD_ANON_11.single_nucleotide_variant = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'single nucleotide variant', tag=u'single_nucleotide_variant')
STD_ANON_11.Indel = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'Indel', tag=u'Indel')
STD_ANON_11.Duplication = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'Duplication', tag=u'Duplication')
STD_ANON_11.Structural_variant = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'Structural variant', tag=u'Structural_variant')
STD_ANON_11.copy_number_gain = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'copy number gain', tag=u'copy_number_gain')
STD_ANON_11.copy_number_loss = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'copy number loss', tag=u'copy_number_loss')
STD_ANON_11.protein_only = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'protein only', tag=u'protein_only')
STD_ANON_11.Microsatellite = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'Microsatellite', tag=u'Microsatellite')
STD_ANON_11.fusion = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'fusion', tag=u'fusion')
STD_ANON_11.inversion = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'inversion', tag=u'inversion')
STD_ANON_11.QTL = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'QTL', tag=u'QTL')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 552, 11)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.HGVS_genomic_top_level = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, genomic, top level', tag=u'HGVS_genomic_top_level')
STD_ANON_12.HGVS_genomic_RefSeqGene = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, genomic, RefSeqGene', tag=u'HGVS_genomic_RefSeqGene')
STD_ANON_12.HGVS_genomic_LRG = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, genomic, LRG', tag=u'HGVS_genomic_LRG')
STD_ANON_12.HGVS_coding_RefSeq = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, coding, RefSeq', tag=u'HGVS_coding_RefSeq')
STD_ANON_12.HGVS_coding_LRG = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, coding, LRG', tag=u'HGVS_coding_LRG')
STD_ANON_12.HGVS_coding = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, coding', tag=u'HGVS_coding')
STD_ANON_12.HGVS_previous = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, previous', tag=u'HGVS_previous')
STD_ANON_12.HGVS_protein = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, protein', tag=u'HGVS_protein')
STD_ANON_12.HGVS_protein_RefSeq = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, protein, RefSeq', tag=u'HGVS_protein_RefSeq')
STD_ANON_12.HGVS_nucleotide = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, nucleotide', tag=u'HGVS_nucleotide')
STD_ANON_12.HGVS_non_validated = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, non-validated', tag=u'HGVS_non_validated')
STD_ANON_12.HGVS_uncertain = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'HGVS, uncertain', tag=u'HGVS_uncertain')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 585, 3)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.Gene = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'Gene', tag=u'Gene')
STD_ANON_13.Variant = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'Variant', tag=u'Variant')
STD_ANON_13.gene_variant = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'gene-variant', tag=u'gene_variant')
STD_ANON_13.OMIM_record = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'OMIM record', tag=u'OMIM_record')
STD_ANON_13.Haplotype = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'Haplotype', tag=u'Haplotype')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 629, 3)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.Disease = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'Disease', tag=u'Disease')
STD_ANON_14.DrugResponse = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'DrugResponse', tag=u'DrugResponse')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 688, 6)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_15, enum_prefix=None)
STD_ANON_15.phenocopy = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'phenocopy', tag=u'phenocopy')
STD_ANON_15.Subphenotype = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'Subphenotype', tag=u'Subphenotype')
STD_ANON_15.co_occurring_condition = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'co-occurring condition', tag=u'co_occurring_condition')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 705, 3)
    _Documentation = None
STD_ANON_16._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_16, enum_prefix=None)
STD_ANON_16.Disease = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value=u'Disease', tag=u'Disease')
STD_ANON_16.DrugResponse = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value=u'DrugResponse', tag=u'DrugResponse')
STD_ANON_16.BloodGroup = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value=u'BloodGroup', tag=u'BloodGroup')
STD_ANON_16.Finding = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value=u'Finding', tag=u'Finding')
STD_ANON_16.NamedProteinVariant = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value=u'NamedProteinVariant', tag=u'NamedProteinVariant')
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 768, 4)
    _Documentation = None
STD_ANON_17._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_17, enum_prefix=None)
STD_ANON_17.number_of_occurrences = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value=u'number of occurrences', tag=u'number_of_occurrences')
STD_ANON_17.p_value = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value=u'p value', tag=u'p_value')
STD_ANON_17.odds_ratio = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value=u'odds ratio', tag=u'odds_ratio')
STD_ANON_17.variation_call = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value=u'variation call', tag=u'variation_call')
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 790, 4)
    _Documentation = None
STD_ANON_18._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_18, enum_prefix=None)
STD_ANON_18.submitter_generated = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value=u'submitter-generated', tag=u'submitter_generated')
STD_ANON_18.data_mining = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value=u'data mining', tag=u'data_mining')
STD_ANON_18.data_review = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value=u'data review', tag=u'data_review')
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 807, 11)
    _Documentation = None
STD_ANON_19._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_19, enum_prefix=None)
STD_ANON_19.Location = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value=u'Location', tag=u'Location')
STD_ANON_19.ControlsAppropriate = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value=u'ControlsAppropriate', tag=u'ControlsAppropriate')
STD_ANON_19.MethodAppropriate = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value=u'MethodAppropriate', tag=u'MethodAppropriate')
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 846, 9)
    _Documentation = None
STD_ANON_20._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_20, enum_prefix=None)
STD_ANON_20.literature_only = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value=u'literature only', tag=u'literature_only')
STD_ANON_20.reference_population = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value=u'reference population', tag=u'reference_population')
STD_ANON_20.case_control = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value=u'case-control', tag=u'case_control')
STD_ANON_20.clinical_testing = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value=u'clinical testing', tag=u'clinical_testing')
STD_ANON_20.in_vitro = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value=u'in vitro', tag=u'in_vitro')
STD_ANON_20.in_vivo = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value=u'in vivo', tag=u'in_vivo')
STD_ANON_20.inferred_from_source = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value=u'inferred from source', tag=u'inferred_from_source')
STD_ANON_20.research = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value=u'research', tag=u'research')
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 879, 11)
    _Documentation = None
STD_ANON_21._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_21, enum_prefix=None)
STD_ANON_21.Description = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'Description', tag=u'Description')
STD_ANON_21.VariantAlleles = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'VariantAlleles', tag=u'VariantAlleles')
STD_ANON_21.SubjectsWithVariant = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'SubjectsWithVariant', tag=u'SubjectsWithVariant')
STD_ANON_21.SubjectsWithDifferentCausativeVariant = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'SubjectsWithDifferentCausativeVariant', tag=u'SubjectsWithDifferentCausativeVariant')
STD_ANON_21.VariantChromosomes = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'VariantChromosomes', tag=u'VariantChromosomes')
STD_ANON_21.IndependentObservations = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'IndependentObservations', tag=u'IndependentObservations')
STD_ANON_21.SingleHeterozygote = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'SingleHeterozygote', tag=u'SingleHeterozygote')
STD_ANON_21.CompoundHeterozygote = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'CompoundHeterozygote', tag=u'CompoundHeterozygote')
STD_ANON_21.ObservedUnspecified = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'ObservedUnspecified', tag=u'ObservedUnspecified')
STD_ANON_21.AlleleFrequency = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'AlleleFrequency', tag=u'AlleleFrequency')
STD_ANON_21.GenotypeAndMOIConsistent = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'GenotypeAndMOIConsistent', tag=u'GenotypeAndMOIConsistent')
STD_ANON_21.UnaffectedFamilyMemberWithCausativeVariant = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'UnaffectedFamilyMemberWithCausativeVariant', tag=u'UnaffectedFamilyMemberWithCausativeVariant')
STD_ANON_21.HetParentTransmitNormalAllele = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'HetParentTransmitNormalAllele', tag=u'HetParentTransmitNormalAllele')
STD_ANON_21.CosegregatingFamilies = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'CosegregatingFamilies', tag=u'CosegregatingFamilies')
STD_ANON_21.InformativeMeioses = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value=u'InformativeMeioses', tag=u'InformativeMeioses')
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 935, 4)
    _Documentation = None
STD_ANON_22._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_22, enum_prefix=None)
STD_ANON_22.germline = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'germline', tag=u'germline')
STD_ANON_22.somatic = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'somatic', tag=u'somatic')
STD_ANON_22.de_novo = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'de novo', tag=u'de_novo')
STD_ANON_22.uncertain = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'uncertain', tag=u'uncertain')
STD_ANON_22.not_provided = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'not provided', tag=u'not_provided')
STD_ANON_22.inherited = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'inherited', tag=u'inherited')
STD_ANON_22.maternal = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'maternal', tag=u'maternal')
STD_ANON_22.paternal = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'paternal', tag=u'paternal')
STD_ANON_22.uniparental = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'uniparental', tag=u'uniparental')
STD_ANON_22.biparental = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'biparental', tag=u'biparental')
STD_ANON_22.not_reported = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'not-reported', tag=u'not_reported')
STD_ANON_22.tested_inconclusive = STD_ANON_22._CF_enumeration.addEnumeration(unicode_value=u'tested-inconclusive', tag=u'tested_inconclusive')
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 970, 8)
    _Documentation = None
STD_ANON_23._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_23, enum_prefix=None)
STD_ANON_23.days = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value=u'days', tag=u'days')
STD_ANON_23.months = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value=u'months', tag=u'months')
STD_ANON_23.years = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value=u'years', tag=u'years')
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 979, 8)
    _Documentation = None
STD_ANON_24._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_24, enum_prefix=None)
STD_ANON_24.minimum = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value=u'minimum', tag=u'minimum')
STD_ANON_24.maximum = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value=u'maximum', tag=u'maximum')
STD_ANON_24.single = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value=u'single', tag=u'single')
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 993, 4)
    _Documentation = None
STD_ANON_25._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_25, enum_prefix=None)
STD_ANON_25.yes = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value=u'yes', tag=u'yes')
STD_ANON_25.no = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value=u'no', tag=u'no')
STD_ANON_25.not_provided = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value=u'not provided', tag=u'not_provided')
STD_ANON_25.unknown = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1032, 4)
    _Documentation = None
STD_ANON_26._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_26, enum_prefix=None)
STD_ANON_26.male = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value=u'male', tag=u'male')
STD_ANON_26.female = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value=u'female', tag=u'female')
STD_ANON_26.mixed = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value=u'mixed', tag=u'mixed')
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1045, 4)
    _Documentation = None
STD_ANON_27._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_27, enum_prefix=None)
STD_ANON_27.submitter_generated = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value=u'submitter-generated', tag=u'submitter_generated')
STD_ANON_27.data_mining = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value=u'data mining', tag=u'data_mining')
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1113, 4)
    _Documentation = None
STD_ANON_28._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_28, enum_prefix=None)
STD_ANON_28.cis = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value=u'cis', tag=u'cis')
STD_ANON_28.trans = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value=u'trans', tag=u'trans')
STD_ANON_28.unknown = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_enumeration)

# Atomic simple type: ReviewStatusType
class ReviewStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The values of review status are used to build the 'star ratings' 
			displayed on the ClinVar public site.  
			0 stars:  a conflict or not classified by submitter
			1 star: classified by single submitter
			2 stars: classified by multiple submitters
			3 stars: reviewed by expert panel
			4 stars: reviewed by professional society"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReviewStatusType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1125, 1)
    _Documentation = u"The values of review status are used to build the 'star ratings' \n\t\t\tdisplayed on the ClinVar public site.  \n\t\t\t0 stars:  a conflict or not classified by submitter\n\t\t\t1 star: classified by single submitter\n\t\t\t2 stars: classified by multiple submitters\n\t\t\t3 stars: reviewed by expert panel\n\t\t\t4 stars: reviewed by professional society"
ReviewStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReviewStatusType, enum_prefix=None)
ReviewStatusType.not_classified_by_submitter = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value=u'not classified by submitter', tag=u'not_classified_by_submitter')
ReviewStatusType.classified_by_single_submitter = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value=u'classified by single submitter', tag=u'classified_by_single_submitter')
ReviewStatusType.classified_by_multiple_submitters = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value=u'classified by multiple submitters', tag=u'classified_by_multiple_submitters')
ReviewStatusType.reviewed_by_expert_panel = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value=u'reviewed by expert panel', tag=u'reviewed_by_expert_panel')
ReviewStatusType.reviewed_by_professional_society = ReviewStatusType._CF_enumeration.addEnumeration(unicode_value=u'reviewed by professional society', tag=u'reviewed_by_professional_society')
ReviewStatusType._InitializeFacetMap(ReviewStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ReviewStatusType', ReviewStatusType)

# Atomic simple type: AssertionTypeAttr
class AssertionTypeAttr (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssertionTypeAttr')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1143, 1)
    _Documentation = None
AssertionTypeAttr._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AssertionTypeAttr, enum_prefix=None)
AssertionTypeAttr.variation_to_disease = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value=u'variation to disease', tag=u'variation_to_disease')
AssertionTypeAttr.variation_in_modifier_gene_to_disease = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value=u'variation in modifier gene to disease', tag=u'variation_in_modifier_gene_to_disease')
AssertionTypeAttr.confers_sensitivity = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value=u'confers sensitivity', tag=u'confers_sensitivity')
AssertionTypeAttr.confers_resistance = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value=u'confers resistance', tag=u'confers_resistance')
AssertionTypeAttr.variant_to_named_protein = AssertionTypeAttr._CF_enumeration.addEnumeration(unicode_value=u'variant to named protein', tag=u'variant_to_named_protein')
AssertionTypeAttr._InitializeFacetMap(AssertionTypeAttr._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AssertionTypeAttr', AssertionTypeAttr)

# Atomic simple type: CommentTypeList
class CommentTypeList (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CommentTypeList')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1153, 1)
    _Documentation = None
CommentTypeList._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CommentTypeList, enum_prefix=None)
CommentTypeList.public = CommentTypeList._CF_enumeration.addEnumeration(unicode_value=u'public', tag=u'public')
CommentTypeList.ConvertedByNCBI = CommentTypeList._CF_enumeration.addEnumeration(unicode_value=u'ConvertedByNCBI', tag=u'ConvertedByNCBI')
CommentTypeList._InitializeFacetMap(CommentTypeList._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CommentTypeList', CommentTypeList)

# Atomic simple type: SeverityType
class SeverityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SeverityType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1160, 1)
    _Documentation = None
SeverityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SeverityType, enum_prefix=None)
SeverityType.mild = SeverityType._CF_enumeration.addEnumeration(unicode_value=u'mild', tag=u'mild')
SeverityType.moderate = SeverityType._CF_enumeration.addEnumeration(unicode_value=u'moderate', tag=u'moderate')
SeverityType.severe = SeverityType._CF_enumeration.addEnumeration(unicode_value=u'severe', tag=u'severe')
SeverityType._InitializeFacetMap(SeverityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SeverityType', SeverityType)

# Atomic simple type: AssertionTypeAttrSCVonly
class AssertionTypeAttrSCVonly (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssertionTypeAttrSCVonly')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1168, 1)
    _Documentation = None
AssertionTypeAttrSCVonly._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AssertionTypeAttrSCVonly, enum_prefix=None)
AssertionTypeAttrSCVonly.variation_to_included_disease = AssertionTypeAttrSCVonly._CF_enumeration.addEnumeration(unicode_value=u'variation to included disease', tag=u'variation_to_included_disease')
AssertionTypeAttrSCVonly._InitializeFacetMap(AssertionTypeAttrSCVonly._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AssertionTypeAttrSCVonly', AssertionTypeAttrSCVonly)

# Atomic simple type: ZygosityType
class ZygosityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ZygosityType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1192, 1)
    _Documentation = None
ZygosityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ZygosityType, enum_prefix=None)
ZygosityType.HomozygousVariant = ZygosityType._CF_enumeration.addEnumeration(unicode_value=u'HomozygousVariant', tag=u'HomozygousVariant')
ZygosityType.SingleHeterozygote = ZygosityType._CF_enumeration.addEnumeration(unicode_value=u'SingleHeterozygote', tag=u'SingleHeterozygote')
ZygosityType.CompoundHeterozygote = ZygosityType._CF_enumeration.addEnumeration(unicode_value=u'CompoundHeterozygote', tag=u'CompoundHeterozygote')
ZygosityType.not_provided = ZygosityType._CF_enumeration.addEnumeration(unicode_value=u'not provided', tag=u'not_provided')
ZygosityType._InitializeFacetMap(ZygosityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ZygosityType', ZygosityType)

# Atomic simple type: Methodtypelist
class Methodtypelist (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Methodtypelist')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1200, 1)
    _Documentation = None
Methodtypelist._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Methodtypelist, enum_prefix=None)
Methodtypelist.curation = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'curation', tag=u'curation')
Methodtypelist.literature_only = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'literature only', tag=u'literature_only')
Methodtypelist.reference_population = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'reference population', tag=u'reference_population')
Methodtypelist.case_control = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'case-control', tag=u'case_control')
Methodtypelist.clinical_testing = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'clinical testing', tag=u'clinical_testing')
Methodtypelist.in_vitro = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'in vitro', tag=u'in_vitro')
Methodtypelist.in_vivo = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'in vivo', tag=u'in_vivo')
Methodtypelist.research = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'research', tag=u'research')
Methodtypelist.not_provided = Methodtypelist._CF_enumeration.addEnumeration(unicode_value=u'not provided', tag=u'not_provided')
Methodtypelist._InitializeFacetMap(Methodtypelist._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Methodtypelist', Methodtypelist)

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1231, 3)
    _Documentation = None
STD_ANON_29._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_29, enum_prefix=None)
STD_ANON_29.current = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value=u'current', tag=u'current')
STD_ANON_29.previous = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value=u'previous', tag=u'previous')
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_enumeration)

# Union simple type: AssertionTypeAttrSCV
# superclasses pyxb.binding.datatypes.anySimpleType
class AssertionTypeAttrSCV (pyxb.binding.basis.STD_union):

    """Simple type that is a union of AssertionTypeAttr, AssertionTypeAttrSCVonly."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssertionTypeAttrSCV')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1173, 1)
    _Documentation = None

    _MemberTypes = ( AssertionTypeAttr, AssertionTypeAttrSCVonly, )
AssertionTypeAttrSCV._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AssertionTypeAttrSCV)
AssertionTypeAttrSCV._CF_pattern = pyxb.binding.facets.CF_pattern()
AssertionTypeAttrSCV.variation_to_disease = u'variation to disease'# originally AssertionTypeAttr.variation_to_disease
AssertionTypeAttrSCV.variation_in_modifier_gene_to_disease = u'variation in modifier gene to disease'# originally AssertionTypeAttr.variation_in_modifier_gene_to_disease
AssertionTypeAttrSCV.confers_sensitivity = u'confers sensitivity'# originally AssertionTypeAttr.confers_sensitivity
AssertionTypeAttrSCV.confers_resistance = u'confers resistance'# originally AssertionTypeAttr.confers_resistance
AssertionTypeAttrSCV.variant_to_named_protein = u'variant to named protein'# originally AssertionTypeAttr.variant_to_named_protein
AssertionTypeAttrSCV.variation_to_included_disease = u'variation to included disease'# originally AssertionTypeAttrSCVonly.variation_to_included_disease
AssertionTypeAttrSCV._InitializeFacetMap(AssertionTypeAttrSCV._CF_enumeration,
   AssertionTypeAttrSCV._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'AssertionTypeAttrSCV', AssertionTypeAttrSCV)

# Complex type CitationType with content type ELEMENT_ONLY
class CitationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CitationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CitationType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 58, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_CitationType_ID', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 60, 3), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'URL'), 'URL', '__AbsentNamespace0_CitationType_URL', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 74, 3), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element CitationText uses Python identifier CitationText
    __CitationText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'CitationText'), 'CitationText', '__AbsentNamespace0_CitationType_CitationText', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 75, 3), )

    
    CitationText = property(__CitationText.value, __CitationText.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CitationType_Type', pyxb.binding.datatypes.string)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 77, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 77, 2)
    
    Type = property(__Type.value, __Type.set, None, u"This maintained distinct from publication types in PubMed and established \n\t\t\t\t\tby GTR curators. The default is 'general'.")

    
    # Attribute Abbrev uses Python identifier Abbrev
    __Abbrev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Abbrev'), 'Abbrev', '__AbsentNamespace0_CitationType_Abbrev', pyxb.binding.datatypes.string)
    __Abbrev._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 83, 2)
    __Abbrev._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 83, 2)
    
    Abbrev = property(__Abbrev.value, __Abbrev.set, None, u'Corresponds to the abbreviation reported by GTR.')

    _ElementMap.update({
        __ID.name() : __ID,
        __URL.name() : __URL,
        __CitationText.name() : __CitationText
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Abbrev.name() : __Abbrev
    })
Namespace.addCategoryObject('typeBinding', u'CitationType', CitationType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 61, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute Source uses Python identifier Source
    __Source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Source'), 'Source', '__AbsentNamespace0_CTD_ANON_Source', pyxb.binding.datatypes.string, required=True)
    __Source._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 64, 7)
    __Source._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 64, 7)
    
    Source = property(__Source.value, __Source.set, None, u'If there is an identifier, what database\n\t\t\t\t\t\t\t\t\tprovides it.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Source.name() : __Source
    })



# Complex type PublicSetType with content type ELEMENT_ONLY
class PublicSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type PublicSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PublicSetType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 130, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ClinVarAssertion uses Python identifier ClinVarAssertion
    __ClinVarAssertion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ClinVarAssertion'), 'ClinVarAssertion', '__AbsentNamespace0_PublicSetType_ClinVarAssertion', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 10, 1), )

    
    ClinVarAssertion = property(__ClinVarAssertion.value, __ClinVarAssertion.set, None, None)

    
    # Element ReferenceClinVarAssertion uses Python identifier ReferenceClinVarAssertion
    __ReferenceClinVarAssertion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReferenceClinVarAssertion'), 'ReferenceClinVarAssertion', '__AbsentNamespace0_PublicSetType_ReferenceClinVarAssertion', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 16, 1), )

    
    ReferenceClinVarAssertion = property(__ReferenceClinVarAssertion.value, __ReferenceClinVarAssertion.set, None, None)

    
    # Element RecordStatus uses Python identifier RecordStatus
    __RecordStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'RecordStatus'), 'RecordStatus', '__AbsentNamespace0_PublicSetType_RecordStatus', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 132, 3), )

    
    RecordStatus = property(__RecordStatus.value, __RecordStatus.set, None, None)

    
    # Element ReplacedBy uses Python identifier ReplacedBy
    __ReplacedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ReplacedBy'), 'ReplacedBy', '__AbsentNamespace0_PublicSetType_ReplacedBy', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 142, 3), )

    
    ReplacedBy = property(__ReplacedBy.value, __ReplacedBy.set, None, None)

    
    # Element Replaces uses Python identifier Replaces
    __Replaces = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Replaces'), 'Replaces', '__AbsentNamespace0_PublicSetType_Replaces', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 143, 3), )

    
    Replaces = property(__Replaces.value, __Replaces.set, None, None)

    
    # Element Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Title'), 'Title', '__AbsentNamespace0_PublicSetType_Title', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 144, 3), )

    
    Title = property(__Title.value, __Title.set, None, u'The title is contructed from the concatenation of the description of the variation and the phenotype.\n\t\t\t\t\tIn the database it is extracted from the title of RCV accession')

    
    # Attribute DateLastUpdated uses Python identifier DateLastUpdated
    __DateLastUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateLastUpdated'), 'DateLastUpdated', '__AbsentNamespace0_PublicSetType_DateLastUpdated', pyxb.binding.datatypes.anySimpleType)
    __DateLastUpdated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 161, 2)
    __DateLastUpdated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 161, 2)
    
    DateLastUpdated = property(__DateLastUpdated.value, __DateLastUpdated.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_PublicSetType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __ClinVarAssertion.name() : __ClinVarAssertion,
        __ReferenceClinVarAssertion.name() : __ReferenceClinVarAssertion,
        __RecordStatus.name() : __RecordStatus,
        __ReplacedBy.name() : __ReplacedBy,
        __Replaces.name() : __Replaces,
        __Title.name() : __Title
    })
    _AttributeMap.update({
        __DateLastUpdated.name() : __DateLastUpdated,
        __ID.name() : __ID
    })
Namespace.addCategoryObject('typeBinding', u'PublicSetType', PublicSetType)


# Complex type ReleaseType with content type ELEMENT_ONLY
class ReleaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ReleaseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReleaseType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 163, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ClinVarSet uses Python identifier ClinVarSet
    __ClinVarSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ClinVarSet'), 'ClinVarSet', '__AbsentNamespace0_ReleaseType_ClinVarSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 3, 1), )

    
    ClinVarSet = property(__ClinVarSet.value, __ClinVarSet.set, None, u'The ClinVarSet is used to group the aggregate record (RCV accession)\n\t\t\twith the submissions underlying it (SCV accessions) \n\t\t\t')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_ReleaseType_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 171, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 171, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Dated uses Python identifier Dated
    __Dated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Dated'), 'Dated', '__AbsentNamespace0_ReleaseType_Dated', pyxb.binding.datatypes.date, required=True)
    __Dated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 172, 2)
    __Dated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 172, 2)
    
    Dated = property(__Dated.value, __Dated.set, None, None)

    _ElementMap.update({
        __ClinVarSet.name() : __ClinVarSet
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Dated.name() : __Dated
    })
Namespace.addCategoryObject('typeBinding', u'ReleaseType', ReleaseType)


# Complex type MeasureTraitType with content type ELEMENT_ONLY
class MeasureTraitType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MeasureTraitType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MeasureTraitType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 174, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ClinVarSubmissionID uses Python identifier ClinVarSubmissionID
    __ClinVarSubmissionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ClinVarSubmissionID'), 'ClinVarSubmissionID', '__AbsentNamespace0_MeasureTraitType_ClinVarSubmissionID', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 176, 3), )

    
    ClinVarSubmissionID = property(__ClinVarSubmissionID.value, __ClinVarSubmissionID.set, None, None)

    
    # Element ClinVarAccession uses Python identifier ClinVarAccession
    __ClinVarAccession = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ClinVarAccession'), 'ClinVarAccession', '__AbsentNamespace0_MeasureTraitType_ClinVarAccession', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 190, 3), )

    
    ClinVarAccession = property(__ClinVarAccession.value, __ClinVarAccession.set, None, None)

    
    # Element RecordStatus uses Python identifier RecordStatus
    __RecordStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'RecordStatus'), 'RecordStatus', '__AbsentNamespace0_MeasureTraitType_RecordStatus', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 211, 3), )

    
    RecordStatus = property(__RecordStatus.value, __RecordStatus.set, None, None)

    
    # Element ClinicalSignificance uses Python identifier ClinicalSignificance
    __ClinicalSignificance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance'), 'ClinicalSignificance', '__AbsentNamespace0_MeasureTraitType_ClinicalSignificance', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 220, 3), )

    
    ClinicalSignificance = property(__ClinicalSignificance.value, __ClinicalSignificance.set, None, None)

    
    # Element CustomAssertionScore uses Python identifier CustomAssertionScore
    __CustomAssertionScore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'CustomAssertionScore'), 'CustomAssertionScore', '__AbsentNamespace0_MeasureTraitType_CustomAssertionScore', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 221, 3), )

    
    CustomAssertionScore = property(__CustomAssertionScore.value, __CustomAssertionScore.set, None, u'\n\t\t\t\t\t\tUsed to represent the scoring matrix a submitter may use to \n\t\t\t\t\t\tevaluate clinical signficance. \n\t\t\t\t\t')

    
    # Element Assertion uses Python identifier Assertion
    __Assertion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Assertion'), 'Assertion', '__AbsentNamespace0_MeasureTraitType_Assertion', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 237, 3), )

    
    Assertion = property(__Assertion.value, __Assertion.set, None, None)

    
    # Element ExternalID uses Python identifier ExternalID
    __ExternalID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ExternalID'), 'ExternalID', '__AbsentNamespace0_MeasureTraitType_ExternalID', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 238, 3), )

    
    ExternalID = property(__ExternalID.value, __ExternalID.set, None, u'XrefType is used to identify data source(s) and their identifiers.\n\t\t\t\t\tOptional because not all sources have an ID specific to the assertion. \n\t\t\t\t\t')

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_MeasureTraitType_AttributeSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 245, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, u'AttributeSet is a package to represent a unit of information,\n\t\t\t\t\t\tthe source(s) of that unit, identifiers representing that unit, and comments.\n\t\t\t\t ')

    
    # Element ObservedIn uses Python identifier ObservedIn
    __ObservedIn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ObservedIn'), 'ObservedIn', '__AbsentNamespace0_MeasureTraitType_ObservedIn', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 278, 3), )

    
    ObservedIn = property(__ObservedIn.value, __ObservedIn.set, None, None)

    
    # Element MeasureSet uses Python identifier MeasureSet
    __MeasureSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MeasureSet'), 'MeasureSet', '__AbsentNamespace0_MeasureTraitType_MeasureSet', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 279, 3), )

    
    MeasureSet = property(__MeasureSet.value, __MeasureSet.set, None, None)

    
    # Element TraitSet uses Python identifier TraitSet
    __TraitSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TraitSet'), 'TraitSet', '__AbsentNamespace0_MeasureTraitType_TraitSet', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 280, 3), )

    
    TraitSet = property(__TraitSet.value, __TraitSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_MeasureTraitType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 281, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element StudyName uses Python identifier StudyName
    __StudyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'StudyName'), 'StudyName', '__AbsentNamespace0_MeasureTraitType_StudyName', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 282, 3), )

    
    StudyName = property(__StudyName.value, __StudyName.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_MeasureTraitType_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 283, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute DateCreated uses Python identifier DateCreated
    __DateCreated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateCreated'), 'DateCreated', '__AbsentNamespace0_MeasureTraitType_DateCreated', pyxb.binding.datatypes.date)
    __DateCreated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 285, 2)
    __DateCreated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 285, 2)
    
    DateCreated = property(__DateCreated.value, __DateCreated.set, None, None)

    
    # Attribute DateLastUpdated uses Python identifier DateLastUpdated
    __DateLastUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateLastUpdated'), 'DateLastUpdated', '__AbsentNamespace0_MeasureTraitType_DateLastUpdated', pyxb.binding.datatypes.date)
    __DateLastUpdated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 286, 2)
    __DateLastUpdated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 286, 2)
    
    DateLastUpdated = property(__DateLastUpdated.value, __DateLastUpdated.set, None, u'A modification date is independent of a version change. \n\t\t\t\tContent generated by NCBI may change without representing a change in the version.\n\t\t\t\t')

    
    # Attribute SubmissionDate uses Python identifier SubmissionDate
    __SubmissionDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SubmissionDate'), 'SubmissionDate', '__AbsentNamespace0_MeasureTraitType_SubmissionDate', pyxb.binding.datatypes.date)
    __SubmissionDate._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 293, 2)
    __SubmissionDate._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 293, 2)
    
    SubmissionDate = property(__SubmissionDate.value, __SubmissionDate.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_MeasureTraitType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __ClinVarSubmissionID.name() : __ClinVarSubmissionID,
        __ClinVarAccession.name() : __ClinVarAccession,
        __RecordStatus.name() : __RecordStatus,
        __ClinicalSignificance.name() : __ClinicalSignificance,
        __CustomAssertionScore.name() : __CustomAssertionScore,
        __Assertion.name() : __Assertion,
        __ExternalID.name() : __ExternalID,
        __AttributeSet.name() : __AttributeSet,
        __ObservedIn.name() : __ObservedIn,
        __MeasureSet.name() : __MeasureSet,
        __TraitSet.name() : __TraitSet,
        __Citation.name() : __Citation,
        __StudyName.name() : __StudyName,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __DateCreated.name() : __DateCreated,
        __DateLastUpdated.name() : __DateLastUpdated,
        __SubmissionDate.name() : __SubmissionDate,
        __ID.name() : __ID
    })
Namespace.addCategoryObject('typeBinding', u'MeasureTraitType', MeasureTraitType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 177, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute submitter uses Python identifier submitter
    __submitter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'submitter'), 'submitter', '__AbsentNamespace0_CTD_ANON__submitter', pyxb.binding.datatypes.string)
    __submitter._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 178, 5)
    __submitter._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 178, 5)
    
    submitter = property(__submitter.value, __submitter.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__AbsentNamespace0_CTD_ANON__title', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 179, 5)
    __title._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 179, 5)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute localKey uses Python identifier localKey
    __localKey = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'localKey'), 'localKey', '__AbsentNamespace0_CTD_ANON__localKey', pyxb.binding.datatypes.string, required=True)
    __localKey._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 180, 5)
    __localKey._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 180, 5)
    
    localKey = property(__localKey.value, __localKey.set, None, u'Of primary use to submitters, to facilitate\n\t\t\t\t\t\t\tidentification of records corresponding to their submissions.\n\t\t\t\t\t\t\t')

    
    # Attribute submitterDate uses Python identifier submitterDate
    __submitterDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'submitterDate'), 'submitterDate', '__AbsentNamespace0_CTD_ANON__submitterDate', pyxb.binding.datatypes.date)
    __submitterDate._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 187, 5)
    __submitterDate._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 187, 5)
    
    submitterDate = property(__submitterDate.value, __submitterDate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __submitter.name() : __submitter,
        __title.name() : __title,
        __localKey.name() : __localKey,
        __submitterDate.name() : __submitterDate
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
						Used to represent the scoring matrix a submitter may use to 
						evaluate clinical signficance. 
					"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 228, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_2_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 230, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_2_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 231, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_2_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 233, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 233, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Value'), 'Value', '__AbsentNamespace0_CTD_ANON_2_Value', pyxb.binding.datatypes.string)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 234, 5)
    __Value._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 234, 5)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Citation.name() : __Citation,
        __XRef.name() : __XRef
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Value.name() : __Value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """AttributeSet is a package to represent a unit of information,
						the source(s) of that unit, identifiers representing that unit, and comments.
				 """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 251, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_3_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 253, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_3_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 272, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_3_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 273, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_3_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 274, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })



# Complex type ReferenceAssertionType with content type ELEMENT_ONLY
class ReferenceAssertionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ReferenceAssertionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReferenceAssertionType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 296, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ClinVarAccession uses Python identifier ClinVarAccession
    __ClinVarAccession = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ClinVarAccession'), 'ClinVarAccession', '__AbsentNamespace0_ReferenceAssertionType_ClinVarAccession', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 298, 3), )

    
    ClinVarAccession = property(__ClinVarAccession.value, __ClinVarAccession.set, None, None)

    
    # Element RecordStatus uses Python identifier RecordStatus
    __RecordStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'RecordStatus'), 'RecordStatus', '__AbsentNamespace0_ReferenceAssertionType_RecordStatus', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 323, 3), )

    
    RecordStatus = property(__RecordStatus.value, __RecordStatus.set, None, None)

    
    # Element ClinicalSignificance uses Python identifier ClinicalSignificance
    __ClinicalSignificance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance'), 'ClinicalSignificance', '__AbsentNamespace0_ReferenceAssertionType_ClinicalSignificance', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 332, 3), )

    
    ClinicalSignificance = property(__ClinicalSignificance.value, __ClinicalSignificance.set, None, u'Either the value corresponding to the scoring system of the ACMG, or \n\t\t\t\t\ta value representing such concepts as drug response, risk factors, etc.')

    
    # Element Assertion uses Python identifier Assertion
    __Assertion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Assertion'), 'Assertion', '__AbsentNamespace0_ReferenceAssertionType_Assertion', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 338, 3), )

    
    Assertion = property(__Assertion.value, __Assertion.set, None, None)

    
    # Element ExternalID uses Python identifier ExternalID
    __ExternalID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ExternalID'), 'ExternalID', '__AbsentNamespace0_ReferenceAssertionType_ExternalID', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 339, 3), )

    
    ExternalID = property(__ExternalID.value, __ExternalID.set, None, u'Represents the public identifier a source may have for this record. \n\t\t\t\t\t')

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_ReferenceAssertionType_AttributeSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 345, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, u'Many concepts in the database are represented by what ClinVar terms an AttributeSet, \n\t\t\t\t\t\twhich is an open-ended structure providing the equivalent of a type of information, the value(s) for that data type, \n\t\t\t\t\t\tsubmitter(s), free text comment(s) describing that attribute, identifier(s) for that attribute, and \n\t\t\t\t\t\tcitation(s) related to that attribute.\n\t\t\t\t\t')

    
    # Element ObservedIn uses Python identifier ObservedIn
    __ObservedIn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ObservedIn'), 'ObservedIn', '__AbsentNamespace0_ReferenceAssertionType_ObservedIn', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 378, 3), )

    
    ObservedIn = property(__ObservedIn.value, __ObservedIn.set, None, None)

    
    # Element MeasureSet uses Python identifier MeasureSet
    __MeasureSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MeasureSet'), 'MeasureSet', '__AbsentNamespace0_ReferenceAssertionType_MeasureSet', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 379, 3), )

    
    MeasureSet = property(__MeasureSet.value, __MeasureSet.set, None, None)

    
    # Element TraitSet uses Python identifier TraitSet
    __TraitSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TraitSet'), 'TraitSet', '__AbsentNamespace0_ReferenceAssertionType_TraitSet', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 380, 3), )

    
    TraitSet = property(__TraitSet.value, __TraitSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_ReferenceAssertionType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 381, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_ReferenceAssertionType_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 382, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute DateCreated uses Python identifier DateCreated
    __DateCreated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateCreated'), 'DateCreated', '__AbsentNamespace0_ReferenceAssertionType_DateCreated', pyxb.binding.datatypes.date)
    __DateCreated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 384, 2)
    __DateCreated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 384, 2)
    
    DateCreated = property(__DateCreated.value, __DateCreated.set, None, None)

    
    # Attribute DateLastUpdated uses Python identifier DateLastUpdated
    __DateLastUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateLastUpdated'), 'DateLastUpdated', '__AbsentNamespace0_ReferenceAssertionType_DateLastUpdated', pyxb.binding.datatypes.date)
    __DateLastUpdated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 385, 2)
    __DateLastUpdated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 385, 2)
    
    DateLastUpdated = property(__DateLastUpdated.value, __DateLastUpdated.set, None, None)

    
    # Attribute SubmissionDate uses Python identifier SubmissionDate
    __SubmissionDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SubmissionDate'), 'SubmissionDate', '__AbsentNamespace0_ReferenceAssertionType_SubmissionDate', pyxb.binding.datatypes.date)
    __SubmissionDate._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 386, 2)
    __SubmissionDate._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 386, 2)
    
    SubmissionDate = property(__SubmissionDate.value, __SubmissionDate.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_ReferenceAssertionType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __ClinVarAccession.name() : __ClinVarAccession,
        __RecordStatus.name() : __RecordStatus,
        __ClinicalSignificance.name() : __ClinicalSignificance,
        __Assertion.name() : __Assertion,
        __ExternalID.name() : __ExternalID,
        __AttributeSet.name() : __AttributeSet,
        __ObservedIn.name() : __ObservedIn,
        __MeasureSet.name() : __MeasureSet,
        __TraitSet.name() : __TraitSet,
        __Citation.name() : __Citation,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __DateCreated.name() : __DateCreated,
        __DateLastUpdated.name() : __DateLastUpdated,
        __SubmissionDate.name() : __SubmissionDate,
        __ID.name() : __ID
    })
Namespace.addCategoryObject('typeBinding', u'ReferenceAssertionType', ReferenceAssertionType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Many concepts in the database are represented by what ClinVar terms an AttributeSet, 
						which is an open-ended structure providing the equivalent of a type of information, the value(s) for that data type, 
						submitter(s), free text comment(s) describing that attribute, identifier(s) for that attribute, and 
						citation(s) related to that attribute.
					"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 353, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_4_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 355, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_4_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 372, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_4_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 373, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_4_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 374, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 397, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_5_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 399, 9), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_5_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 449, 9), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_5_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 450, 9), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_5_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 451, 9), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 474, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_6_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 476, 12), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_6_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 493, 12), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 545, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_7_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 547, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_7_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 574, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_7_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 575, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_7_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 576, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 603, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_8_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 605, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_8_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 614, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_8_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 615, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_8_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 616, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, u'table_type = 38')

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 643, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_9_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 645, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_9_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 654, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_9_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 655, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_9_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 656, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 666, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_10_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 668, 9), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_10_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 677, 9), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_10_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 678, 9), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_10_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 679, 9), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })



# Complex type AttributeType with content type SIMPLE
class AttributeType (pyxb.binding.basis.complexTypeDefinition):
    """The attribute is a general element to represent a defined set of data
				qualified by an enumerated set of types. For each attribute element, the value will
				be a character string and is optional. Source shall be used to store identifiers for
				supplied data from source other than the submitter (e.g. SequenceOntology). The data
				submitted where Type="variation" shall be validated against sequence_alternation in
				Sequence Ontology http://www.sequenceontology.org/. This is to be a generic version
				of AttributeType and should be used with extension when it is used to specify Type
				and its enumerations. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributeType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 717, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute integerValue uses Python identifier integerValue
    __integerValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'integerValue'), 'integerValue', '__AbsentNamespace0_AttributeType_integerValue', pyxb.binding.datatypes.int)
    __integerValue._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 730, 4)
    __integerValue._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 730, 4)
    
    integerValue = property(__integerValue.value, __integerValue.set, None, None)

    
    # Attribute dateValue uses Python identifier dateValue
    __dateValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dateValue'), 'dateValue', '__AbsentNamespace0_AttributeType_dateValue', pyxb.binding.datatypes.date)
    __dateValue._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 731, 4)
    __dateValue._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 731, 4)
    
    dateValue = property(__dateValue.value, __dateValue.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __integerValue.name() : __integerValue,
        __dateValue.name() : __dateValue
    })
Namespace.addCategoryObject('typeBinding', u'AttributeType', AttributeType)


# Complex type SetElementSetType with content type ELEMENT_ONLY
class SetElementSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SetElementSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SetElementSetType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 735, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ElementValue uses Python identifier ElementValue
    __ElementValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ElementValue'), 'ElementValue', '__AbsentNamespace0_SetElementSetType_ElementValue', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 737, 3), )

    
    ElementValue = property(__ElementValue.value, __ElementValue.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_SetElementSetType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 746, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_SetElementSetType_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 747, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_SetElementSetType_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 748, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __ElementValue.name() : __ElementValue,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SetElementSetType', SetElementSetType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 738, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_11_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 741, 7)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 741, 7)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type SoftwareSet with content type EMPTY
class SoftwareSet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SoftwareSet with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SoftwareSet')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 751, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_SoftwareSet_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 752, 2)
    __name._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 752, 2)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__AbsentNamespace0_SoftwareSet_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 753, 2)
    __version._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 753, 2)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute purpose uses Python identifier purpose
    __purpose = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'purpose'), 'purpose', '__AbsentNamespace0_SoftwareSet_purpose', pyxb.binding.datatypes.string)
    __purpose._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 754, 2)
    __purpose._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 754, 2)
    
    purpose = property(__purpose.value, __purpose.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __version.name() : __version,
        __purpose.name() : __purpose
    })
Namespace.addCategoryObject('typeBinding', u'SoftwareSet', SoftwareSet)


# Complex type MethodType with content type ELEMENT_ONLY
class MethodType (pyxb.binding.basis.complexTypeDefinition):
    """ Details of a method used to generate variant calls or predict/report
                functional consequence. The name of the platform should represent a sequencer or an
                array, e.g. sequencing or array , e.g. capillary, 454, Helicos, Solexa, SOLiD. This
                structure should also be used if the method is 'Curation'. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MethodType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 756, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NamePlatform uses Python identifier NamePlatform
    __NamePlatform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'NamePlatform'), 'NamePlatform', '__AbsentNamespace0_MethodType_NamePlatform', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 764, 3), )

    
    NamePlatform = property(__NamePlatform.value, __NamePlatform.set, None, None)

    
    # Element TypePlatform uses Python identifier TypePlatform
    __TypePlatform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TypePlatform'), 'TypePlatform', '__AbsentNamespace0_MethodType_TypePlatform', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 765, 3), )

    
    TypePlatform = property(__TypePlatform.value, __TypePlatform.set, None, None)

    
    # Element Purpose uses Python identifier Purpose
    __Purpose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Purpose'), 'Purpose', '__AbsentNamespace0_MethodType_Purpose', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 766, 3), )

    
    Purpose = property(__Purpose.value, __Purpose.set, None, None)

    
    # Element ResultType uses Python identifier ResultType
    __ResultType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ResultType'), 'ResultType', '__AbsentNamespace0_MethodType_ResultType', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 767, 3), )

    
    ResultType = property(__ResultType.value, __ResultType.set, None, None)

    
    # Element MinReported uses Python identifier MinReported
    __MinReported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MinReported'), 'MinReported', '__AbsentNamespace0_MethodType_MinReported', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 777, 3), )

    
    MinReported = property(__MinReported.value, __MinReported.set, None, None)

    
    # Element MaxReported uses Python identifier MaxReported
    __MaxReported = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MaxReported'), 'MaxReported', '__AbsentNamespace0_MethodType_MaxReported', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 778, 3), )

    
    MaxReported = property(__MaxReported.value, __MaxReported.set, None, None)

    
    # Element ReferenceStandard uses Python identifier ReferenceStandard
    __ReferenceStandard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ReferenceStandard'), 'ReferenceStandard', '__AbsentNamespace0_MethodType_ReferenceStandard', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 779, 3), )

    
    ReferenceStandard = property(__ReferenceStandard.value, __ReferenceStandard.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_MethodType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 780, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_MethodType_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 781, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Description'), 'Description', '__AbsentNamespace0_MethodType_Description', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 782, 3), )

    
    Description = property(__Description.value, __Description.set, None, u' Free text to enrich the description of the method and to\n                        provide information not captured in specific fields. ')

    
    # Element Software uses Python identifier Software
    __Software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Software'), 'Software', '__AbsentNamespace0_MethodType_Software', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 788, 3), )

    
    Software = property(__Software.value, __Software.set, None, None)

    
    # Element SourceType uses Python identifier SourceType
    __SourceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SourceType'), 'SourceType', '__AbsentNamespace0_MethodType_SourceType', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 789, 3), )

    
    SourceType = property(__SourceType.value, __SourceType.set, None, None)

    
    # Element MethodType uses Python identifier MethodType
    __MethodType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MethodType'), 'MethodType', '__AbsentNamespace0_MethodType_MethodType', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 798, 3), )

    
    MethodType = property(__MethodType.value, __MethodType.set, None, None)

    
    # Element MethodAttribute uses Python identifier MethodAttribute
    __MethodAttribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MethodAttribute'), 'MethodAttribute', '__AbsentNamespace0_MethodType_MethodAttribute', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 799, 3), )

    
    MethodAttribute = property(__MethodAttribute.value, __MethodAttribute.set, None, None)

    
    # Element MethodResult uses Python identifier MethodResult
    __MethodResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MethodResult'), 'MethodResult', '__AbsentNamespace0_MethodType_MethodResult', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 822, 3), )

    
    MethodResult = property(__MethodResult.value, __MethodResult.set, None, u' MethodResult is used to represent results specific to a particular method.\n                        An example is a method used to validate the the variant call; the MethodResult would be pass/fail/inconclusive')

    _ElementMap.update({
        __NamePlatform.name() : __NamePlatform,
        __TypePlatform.name() : __TypePlatform,
        __Purpose.name() : __Purpose,
        __ResultType.name() : __ResultType,
        __MinReported.name() : __MinReported,
        __MaxReported.name() : __MaxReported,
        __ReferenceStandard.name() : __ReferenceStandard,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Description.name() : __Description,
        __Software.name() : __Software,
        __SourceType.name() : __SourceType,
        __MethodType.name() : __MethodType,
        __MethodAttribute.name() : __MethodAttribute,
        __MethodResult.name() : __MethodResult
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MethodType', MethodType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 800, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_12_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 802, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute
    })
    _AttributeMap.update({
        
    })



# Complex type ObservationSet with content type ELEMENT_ONLY
class ObservationSet (pyxb.binding.basis.complexTypeDefinition):
    """Documents in what populations or samples an allele or genotype has been observed 
				relative to the described trait. Summary observations can be registered per 
				submitted assertion, grouped by common citation, study type, origin, ethnicity, tissue, cell line,
				and species data. Not all options are valid per study type, but these will not be validated in the xsd.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ObservationSet')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 830, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Sample uses Python identifier Sample
    __Sample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Sample'), 'Sample', '__AbsentNamespace0_ObservationSet_Sample', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 839, 3), )

    
    Sample = property(__Sample.value, __Sample.set, None, None)

    
    # Element Method uses Python identifier Method
    __Method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Method'), 'Method', '__AbsentNamespace0_ObservationSet_Method', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 840, 3), )

    
    Method = property(__Method.value, __Method.set, None, None)

    
    # Element ObservedData uses Python identifier ObservedData
    __ObservedData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ObservedData'), 'ObservedData', '__AbsentNamespace0_ObservationSet_ObservedData', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 864, 3), )

    
    ObservedData = property(__ObservedData.value, __ObservedData.set, None, u'This is an AttributeSet, there will be 1 attribute supported by optional citations, xrefs and comment. \n\t\t\t\t\t\tThere must be at least one ObservedData Set, but can be any number.\n\t\t\t\t\t\tFor each ObservedData set the Attribute will be either decimal or string depending on type. \n\t\t\t\t\t\tThe value will be stored here, but decimals will be entered to the database as a string.\n\t\t\t\t\t')

    
    # Element Co-occurrenceSet uses Python identifier Co_occurrenceSet
    __Co_occurrenceSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Co-occurrenceSet'), 'Co_occurrenceSet', '__AbsentNamespace0_ObservationSet_Co_occurrenceSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 913, 3), )

    
    Co_occurrenceSet = property(__Co_occurrenceSet.value, __Co_occurrenceSet.set, None, None)

    
    # Element TraitSet uses Python identifier TraitSet
    __TraitSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TraitSet'), 'TraitSet', '__AbsentNamespace0_ObservationSet_TraitSet', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 914, 3), )

    
    TraitSet = property(__TraitSet.value, __TraitSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_ObservationSet_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 915, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_ObservationSet_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 916, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_ObservationSet_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 917, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __Sample.name() : __Sample,
        __Method.name() : __Method,
        __ObservedData.name() : __ObservedData,
        __Co_occurrenceSet.name() : __Co_occurrenceSet,
        __TraitSet.name() : __TraitSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ObservationSet', ObservationSet)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """This is an AttributeSet, there will be 1 attribute supported by optional citations, xrefs and comment. 
						There must be at least one ObservedData Set, but can be any number.
						For each ObservedData set the Attribute will be either decimal or string depending on type. 
						The value will be stored here, but decimals will be entered to the database as a string.
					"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 872, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Attribute uses Python identifier Attribute
    __Attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Attribute'), 'Attribute', '__AbsentNamespace0_CTD_ANON_13_Attribute', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 874, 6), )

    
    Attribute = property(__Attribute.value, __Attribute.set, None, None)

    
    # Element Severity uses Python identifier Severity
    __Severity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Severity'), 'Severity', '__AbsentNamespace0_CTD_ANON_13_Severity', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 905, 6), )

    
    Severity = property(__Severity.value, __Severity.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_13_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 906, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_13_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 907, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_13_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 908, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_13_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Attribute.name() : __Attribute,
        __Severity.name() : __Severity,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __ID.name() : __ID
    })



# Complex type FamilyInfo with content type EMPTY
class FamilyInfo (pyxb.binding.basis.complexTypeDefinition):
    """Complex type FamilyInfo with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FamilyInfo')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 920, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute NumFamilies uses Python identifier NumFamilies
    __NumFamilies = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'NumFamilies'), 'NumFamilies', '__AbsentNamespace0_FamilyInfo_NumFamilies', pyxb.binding.datatypes.int)
    __NumFamilies._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 921, 2)
    __NumFamilies._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 921, 2)
    
    NumFamilies = property(__NumFamilies.value, __NumFamilies.set, None, None)

    
    # Attribute FamilyHistory uses Python identifier FamilyHistory
    __FamilyHistory = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'FamilyHistory'), 'FamilyHistory', '__AbsentNamespace0_FamilyInfo_FamilyHistory', pyxb.binding.datatypes.string)
    __FamilyHistory._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 922, 2)
    __FamilyHistory._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 922, 2)
    
    FamilyHistory = property(__FamilyHistory.value, __FamilyHistory.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __NumFamilies.name() : __NumFamilies,
        __FamilyHistory.name() : __FamilyHistory
    })
Namespace.addCategoryObject('typeBinding', u'FamilyInfo', FamilyInfo)


# Complex type SampleType with content type ELEMENT_ONLY
class SampleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SampleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SampleType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 924, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SampleDescription uses Python identifier SampleDescription
    __SampleDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SampleDescription'), 'SampleDescription', '__AbsentNamespace0_SampleType_SampleDescription', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 926, 3), )

    
    SampleDescription = property(__SampleDescription.value, __SampleDescription.set, None, None)

    
    # Element Origin uses Python identifier Origin
    __Origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Origin'), 'Origin', '__AbsentNamespace0_SampleType_Origin', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 934, 3), )

    
    Origin = property(__Origin.value, __Origin.set, None, None)

    
    # Element Ethnicity uses Python identifier Ethnicity
    __Ethnicity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Ethnicity'), 'Ethnicity', '__AbsentNamespace0_SampleType_Ethnicity', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 952, 3), )

    
    Ethnicity = property(__Ethnicity.value, __Ethnicity.set, None, None)

    
    # Element GeographicfOrigin uses Python identifier GeographicfOrigin
    __GeographicfOrigin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'GeographicfOrigin'), 'GeographicfOrigin', '__AbsentNamespace0_SampleType_GeographicfOrigin', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 953, 3), )

    
    GeographicfOrigin = property(__GeographicfOrigin.value, __GeographicfOrigin.set, None, None)

    
    # Element Tissue uses Python identifier Tissue
    __Tissue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Tissue'), 'Tissue', '__AbsentNamespace0_SampleType_Tissue', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 954, 3), )

    
    Tissue = property(__Tissue.value, __Tissue.set, None, None)

    
    # Element CellLine uses Python identifier CellLine
    __CellLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'CellLine'), 'CellLine', '__AbsentNamespace0_SampleType_CellLine', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 955, 3), )

    
    CellLine = property(__CellLine.value, __CellLine.set, None, None)

    
    # Element Species uses Python identifier Species
    __Species = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Species'), 'Species', '__AbsentNamespace0_SampleType_Species', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 956, 3), )

    
    Species = property(__Species.value, __Species.set, None, None)

    
    # Element Age uses Python identifier Age
    __Age = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Age'), 'Age', '__AbsentNamespace0_SampleType_Age', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 965, 3), )

    
    Age = property(__Age.value, __Age.set, None, None)

    
    # Element Strain uses Python identifier Strain
    __Strain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Strain'), 'Strain', '__AbsentNamespace0_SampleType_Strain', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 991, 3), )

    
    Strain = property(__Strain.value, __Strain.set, None, None)

    
    # Element AffectedStatus uses Python identifier AffectedStatus
    __AffectedStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AffectedStatus'), 'AffectedStatus', '__AbsentNamespace0_SampleType_AffectedStatus', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 992, 3), )

    
    AffectedStatus = property(__AffectedStatus.value, __AffectedStatus.set, None, None)

    
    # Element NumberTested uses Python identifier NumberTested
    __NumberTested = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'NumberTested'), 'NumberTested', '__AbsentNamespace0_SampleType_NumberTested', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1002, 3), )

    
    NumberTested = property(__NumberTested.value, __NumberTested.set, None, u'Denominator, total individuals included in this observation\n\t\t\t\t\t\tset.')

    
    # Element NumberMales uses Python identifier NumberMales
    __NumberMales = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'NumberMales'), 'NumberMales', '__AbsentNamespace0_SampleType_NumberMales', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1008, 3), )

    
    NumberMales = property(__NumberMales.value, __NumberMales.set, None, u'Denominator, total males included in this observation\n\t\t\t\t\t\tset.')

    
    # Element NumberFemales uses Python identifier NumberFemales
    __NumberFemales = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'NumberFemales'), 'NumberFemales', '__AbsentNamespace0_SampleType_NumberFemales', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1014, 3), )

    
    NumberFemales = property(__NumberFemales.value, __NumberFemales.set, None, u'Denominator, total females included in this observation\n\t\t\t\t\t\tset.')

    
    # Element NumberChrTested uses Python identifier NumberChrTested
    __NumberChrTested = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'NumberChrTested'), 'NumberChrTested', '__AbsentNamespace0_SampleType_NumberChrTested', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1020, 3), )

    
    NumberChrTested = property(__NumberChrTested.value, __NumberChrTested.set, None, u'Denominator, total number chromosomes tested. Number affected\n\t\t\t\t\t\tand unaffected are captured in the element\n\t\t\t\t\t\tNumberObserved.')

    
    # Element Gender uses Python identifier Gender
    __Gender = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Gender'), 'Gender', '__AbsentNamespace0_SampleType_Gender', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1027, 3), )

    
    Gender = property(__Gender.value, __Gender.set, None, u'Gender should be used ONLY if explicit values are not available for number of males or females, and there is a need to indicate that the genders in the sample are known. \n                    ')

    
    # Element FamilyData uses Python identifier FamilyData
    __FamilyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'FamilyData'), 'FamilyData', '__AbsentNamespace0_SampleType_FamilyData', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1040, 3), )

    
    FamilyData = property(__FamilyData.value, __FamilyData.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_SampleType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1041, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_SampleType_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1042, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_SampleType_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1043, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element SourceType uses Python identifier SourceType
    __SourceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SourceType'), 'SourceType', '__AbsentNamespace0_SampleType_SourceType', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1044, 3), )

    
    SourceType = property(__SourceType.value, __SourceType.set, None, None)

    _ElementMap.update({
        __SampleDescription.name() : __SampleDescription,
        __Origin.name() : __Origin,
        __Ethnicity.name() : __Ethnicity,
        __GeographicfOrigin.name() : __GeographicfOrigin,
        __Tissue.name() : __Tissue,
        __CellLine.name() : __CellLine,
        __Species.name() : __Species,
        __Age.name() : __Age,
        __Strain.name() : __Strain,
        __AffectedStatus.name() : __AffectedStatus,
        __NumberTested.name() : __NumberTested,
        __NumberMales.name() : __NumberMales,
        __NumberFemales.name() : __NumberFemales,
        __NumberChrTested.name() : __NumberChrTested,
        __Gender.name() : __Gender,
        __FamilyData.name() : __FamilyData,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment,
        __SourceType.name() : __SourceType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SampleType', SampleType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 927, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Description'), 'Description', '__AbsentNamespace0_CTD_ANON_14_Description', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 929, 6), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_14_Citation', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 930, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __Citation.name() : __Citation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 957, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute TaxonomyId uses Python identifier TaxonomyId
    __TaxonomyId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TaxonomyId'), 'TaxonomyId', '__AbsentNamespace0_CTD_ANON_15_TaxonomyId', pyxb.binding.datatypes.int)
    __TaxonomyId._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 960, 7)
    __TaxonomyId._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 960, 7)
    
    TaxonomyId = property(__TaxonomyId.value, __TaxonomyId.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __TaxonomyId.name() : __TaxonomyId
    })



# Complex type Co-occurrenceType with content type ELEMENT_ONLY
class Co_occurrenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Co-occurrenceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Co-occurrenceType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1054, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Zygosity uses Python identifier Zygosity
    __Zygosity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Zygosity'), 'Zygosity', '__AbsentNamespace0_Co_occurrenceType_Zygosity', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1059, 3), )

    
    Zygosity = property(__Zygosity.value, __Zygosity.set, None, None)

    
    # Element AlleleDescSet uses Python identifier AlleleDescSet
    __AlleleDescSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AlleleDescSet'), 'AlleleDescSet', '__AbsentNamespace0_Co_occurrenceType_AlleleDescSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1060, 3), )

    
    AlleleDescSet = property(__AlleleDescSet.value, __AlleleDescSet.set, None, None)

    
    # Element Count uses Python identifier Count
    __Count = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Count'), 'Count', '__AbsentNamespace0_Co_occurrenceType_Count', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1061, 3), )

    
    Count = property(__Count.value, __Count.set, None, None)

    _ElementMap.update({
        __Zygosity.name() : __Zygosity,
        __AlleleDescSet.name() : __AlleleDescSet,
        __Count.name() : __Count
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Co-occurrenceType', Co_occurrenceType)


# Complex type ClinicalSignificanceType with content type ELEMENT_ONLY
class ClinicalSignificanceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ClinicalSignificanceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClinicalSignificanceType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1064, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ReviewStatus uses Python identifier ReviewStatus
    __ReviewStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ReviewStatus'), 'ReviewStatus', '__AbsentNamespace0_ClinicalSignificanceType_ReviewStatus', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1066, 3), )

    
    ReviewStatus = property(__ReviewStatus.value, __ReviewStatus.set, None, None)

    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Description'), 'Description', '__AbsentNamespace0_ClinicalSignificanceType_Description', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1067, 3), )

    
    Description = property(__Description.value, __Description.set, None, u'We are not providing an enumeration for the values we report for clinical significance within the xsd. \n\t\t\t\t\t\tThe values are maintained here: ftp://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Clinical_significance.txt. ')

    
    # Element Explanation uses Python identifier Explanation
    __Explanation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Explanation'), 'Explanation', '__AbsentNamespace0_ClinicalSignificanceType_Explanation', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1073, 3), )

    
    Explanation = property(__Explanation.value, __Explanation.set, None, u"Explanation is used only when the description is 'conflicting data from submitters'\n\t\t\t\t\tThe element summarizes the conflict.")

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_ClinicalSignificanceType_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1079, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_ClinicalSignificanceType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1080, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_ClinicalSignificanceType_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1081, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute DateLastEvaluated uses Python identifier DateLastEvaluated
    __DateLastEvaluated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateLastEvaluated'), 'DateLastEvaluated', '__AbsentNamespace0_ClinicalSignificanceType_DateLastEvaluated', pyxb.binding.datatypes.date)
    __DateLastEvaluated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1083, 2)
    __DateLastEvaluated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1083, 2)
    
    DateLastEvaluated = property(__DateLastEvaluated.value, __DateLastEvaluated.set, None, None)

    _ElementMap.update({
        __ReviewStatus.name() : __ReviewStatus,
        __Description.name() : __Description,
        __Explanation.name() : __Explanation,
        __XRef.name() : __XRef,
        __Citation.name() : __Citation,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __DateLastEvaluated.name() : __DateLastEvaluated
    })
Namespace.addCategoryObject('typeBinding', u'ClinicalSignificanceType', ClinicalSignificanceType)


# Complex type ClinicalSignificanceTypeSCV with content type ELEMENT_ONLY
class ClinicalSignificanceTypeSCV (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ClinicalSignificanceTypeSCV with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClinicalSignificanceTypeSCV')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1085, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ReviewStatus uses Python identifier ReviewStatus
    __ReviewStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ReviewStatus'), 'ReviewStatus', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_ReviewStatus', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1087, 3), )

    
    ReviewStatus = property(__ReviewStatus.value, __ReviewStatus.set, None, None)

    
    # Element Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Description'), 'Description', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_Description', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1088, 3), )

    
    Description = property(__Description.value, __Description.set, None, u'We are not providing an enumeration for the values we report for clinical significance within the xsd. \n\t\t\t\t\t\tThe values are maintained here: ftp://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Clinical_significance.txt. ')

    
    # Element Explanation uses Python identifier Explanation
    __Explanation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Explanation'), 'Explanation', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_Explanation', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1094, 3), )

    
    Explanation = property(__Explanation.value, __Explanation.set, None, u"Explanation is used only when the description is 'conflicting data from submitters'\n\t\t\t\t\tThe element summarizes the conflict.")

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1100, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1101, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1102, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute DateLastEvaluated uses Python identifier DateLastEvaluated
    __DateLastEvaluated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateLastEvaluated'), 'DateLastEvaluated', '__AbsentNamespace0_ClinicalSignificanceTypeSCV_DateLastEvaluated', pyxb.binding.datatypes.date)
    __DateLastEvaluated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1104, 2)
    __DateLastEvaluated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1104, 2)
    
    DateLastEvaluated = property(__DateLastEvaluated.value, __DateLastEvaluated.set, None, None)

    _ElementMap.update({
        __ReviewStatus.name() : __ReviewStatus,
        __Description.name() : __Description,
        __Explanation.name() : __Explanation,
        __XRef.name() : __XRef,
        __Citation.name() : __Citation,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __DateLastEvaluated.name() : __DateLastEvaluated
    })
Namespace.addCategoryObject('typeBinding', u'ClinicalSignificanceTypeSCV', ClinicalSignificanceTypeSCV)


# Complex type AlleleDescType with content type ELEMENT_ONLY
class AlleleDescType (pyxb.binding.basis.complexTypeDefinition):
    """This is to be used within co-occurrence set """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AlleleDescType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1106, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__AbsentNamespace0_AlleleDescType_Name', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1111, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element RelativeOrientation uses Python identifier RelativeOrientation
    __RelativeOrientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'RelativeOrientation'), 'RelativeOrientation', '__AbsentNamespace0_AlleleDescType_RelativeOrientation', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1112, 3), )

    
    RelativeOrientation = property(__RelativeOrientation.value, __RelativeOrientation.set, None, None)

    
    # Element Zygosity uses Python identifier Zygosity
    __Zygosity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Zygosity'), 'Zygosity', '__AbsentNamespace0_AlleleDescType_Zygosity', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1121, 3), )

    
    Zygosity = property(__Zygosity.value, __Zygosity.set, None, None)

    
    # Element ClinicalSignificance uses Python identifier ClinicalSignificance
    __ClinicalSignificance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance'), 'ClinicalSignificance', '__AbsentNamespace0_AlleleDescType_ClinicalSignificance', False, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1122, 3), )

    
    ClinicalSignificance = property(__ClinicalSignificance.value, __ClinicalSignificance.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __RelativeOrientation.name() : __RelativeOrientation,
        __Zygosity.name() : __Zygosity,
        __ClinicalSignificance.name() : __ClinicalSignificance
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AlleleDescType', AlleleDescType)


# Complex type XrefType with content type EMPTY
class XrefType (pyxb.binding.basis.complexTypeDefinition):
    """This structure is used to represent how an object described in the submission relates to objects in other databases.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'XrefType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 31, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute DB uses Python identifier DB
    __DB = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DB'), 'DB', '__AbsentNamespace0_XrefType_DB', pyxb.binding.datatypes.string, required=True)
    __DB._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 36, 2)
    __DB._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 36, 2)
    
    DB = property(__DB.value, __DB.set, None, u'The name of the database. When there is an overlap with sequence\n\t\t\t\tdatabases, that name is used.')

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_XrefType_ID', pyxb.binding.datatypes.string, required=True)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 42, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 42, 2)
    
    ID = property(__ID.value, __ID.set, None, u'The identifier used by the database.  Being exported\n\t\t\t\tas a string even though internally the database has rules for defining\n\t\t\t\twhich datases use integer identifers.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_XrefType_Type', pyxb.binding.datatypes.string)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 49, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 49, 2)
    
    Type = property(__Type.value, __Type.set, None, u'Used to differentiate between different types of identifers\n\t\t\t\tthat a database may provide.')

    
    # Attribute URL uses Python identifier URL
    __URL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'URL'), 'URL', '__AbsentNamespace0_XrefType_URL', pyxb.binding.datatypes.anyURI)
    __URL._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 55, 2)
    __URL._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 55, 2)
    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute Status uses Python identifier Status
    __Status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Status'), 'Status', '__AbsentNamespace0_XrefType_Status', typeStatus, unicode_default=u'current')
    __Status._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 56, 2)
    __Status._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 56, 2)
    
    Status = property(__Status.value, __Status.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DB.name() : __DB,
        __ID.name() : __ID,
        __Type.name() : __Type,
        __URL.name() : __URL,
        __Status.name() : __Status
    })
Namespace.addCategoryObject('typeBinding', u'XrefType', XrefType)


# Complex type CommentType with content type SIMPLE
class CommentType (pyxb.binding.basis.complexTypeDefinition):
    """A structure to support reporting unformatted content.
			"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CommentType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 89, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute DataSource uses Python identifier DataSource
    __DataSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DataSource'), 'DataSource', '__AbsentNamespace0_CommentType_DataSource', pyxb.binding.datatypes.string)
    __DataSource._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 96, 4)
    __DataSource._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 96, 4)
    
    DataSource = property(__DataSource.value, __DataSource.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CommentType_Type', CommentTypeList)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 97, 4)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 97, 4)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DataSource.name() : __DataSource,
        __Type.name() : __Type
    })
Namespace.addCategoryObject('typeBinding', u'CommentType', CommentType)


# Complex type DataSourceType with content type EMPTY
class DataSourceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DataSourceType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DataSourceType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 103, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute DataSource uses Python identifier DataSource
    __DataSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DataSource'), 'DataSource', '__AbsentNamespace0_DataSourceType_DataSource', pyxb.binding.datatypes.string, required=True)
    __DataSource._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 104, 2)
    __DataSource._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 104, 2)
    
    DataSource = property(__DataSource.value, __DataSource.set, None, u'A standard term for the source of the information')

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_DataSourceType_ID', pyxb.binding.datatypes.string)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 109, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 109, 2)
    
    ID = property(__ID.value, __ID.set, None, u'The identifier used by the data source')

    
    # Attribute SourceType uses Python identifier SourceType
    __SourceType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SourceType'), 'SourceType', '__AbsentNamespace0_DataSourceType_SourceType', STD_ANON)
    __SourceType._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 114, 2)
    __SourceType._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 114, 2)
    
    SourceType = property(__SourceType.value, __SourceType.set, None, u'Controlled terms to categorize the source of the\n\t\t\t\tinformation')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DataSource.name() : __DataSource,
        __ID.name() : __ID,
        __SourceType.name() : __SourceType
    })
Namespace.addCategoryObject('typeBinding', u'DataSourceType', DataSourceType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 191, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Acc uses Python identifier Acc
    __Acc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Acc'), 'Acc', '__AbsentNamespace0_CTD_ANON_16_Acc', pyxb.binding.datatypes.string, required=True)
    __Acc._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 192, 5)
    __Acc._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 192, 5)
    
    Acc = property(__Acc.value, __Acc.set, None, None)

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Version'), 'Version', '__AbsentNamespace0_CTD_ANON_16_Version', pyxb.binding.datatypes.integer, required=True)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 193, 5)
    __Version._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 193, 5)
    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_16_Type', STD_ANON_2, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 194, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 194, 5)
    
    Type = property(__Type.value, __Type.set, None, u"RCV accessions aggregate data from each submission.\n\t\t\t\t\t\t\t\tEach submission is assigned an accession of beginning with 'SCV'\n\t\t\t\t\t\t\t")

    
    # Attribute OrgID uses Python identifier OrgID
    __OrgID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'OrgID'), 'OrgID', '__AbsentNamespace0_CTD_ANON_16_OrgID', pyxb.binding.datatypes.int)
    __OrgID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 207, 5)
    __OrgID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 207, 5)
    
    OrgID = property(__OrgID.value, __OrgID.set, None, None)

    
    # Attribute DateUpdated uses Python identifier DateUpdated
    __DateUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateUpdated'), 'DateUpdated', '__AbsentNamespace0_CTD_ANON_16_DateUpdated', pyxb.binding.datatypes.date)
    __DateUpdated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 208, 5)
    __DateUpdated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 208, 5)
    
    DateUpdated = property(__DateUpdated.value, __DateUpdated.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Acc.name() : __Acc,
        __Version.name() : __Version,
        __Type.name() : __Type,
        __OrgID.name() : __OrgID,
        __DateUpdated.name() : __DateUpdated
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_17 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 254, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_17_Type', STD_ANON_4, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 257, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 257, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 299, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Acc uses Python identifier Acc
    __Acc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Acc'), 'Acc', '__AbsentNamespace0_CTD_ANON_18_Acc', pyxb.binding.datatypes.string, required=True)
    __Acc._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 300, 5)
    __Acc._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 300, 5)
    
    Acc = property(__Acc.value, __Acc.set, None, u'The accession assigned by ClinVar.')

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Version'), 'Version', '__AbsentNamespace0_CTD_ANON_18_Version', pyxb.binding.datatypes.integer, required=True)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 305, 5)
    __Version._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 305, 5)
    
    Version = property(__Version.value, __Version.set, None, u'A new version of an SCV accession is assigned with an update\n\t\t\t\t\t\t\tfrom the submitter.  A new version of an RCV accession is assigned when the\n\t\t\t\t\t\t\tset of ClinVarAssertions is changed, either by a change in version or by\n\t\t\t\t\t\t\taddition of a new submission.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_18_Type', STD_ANON_5, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 313, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 313, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute DateUpdated uses Python identifier DateUpdated
    __DateUpdated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DateUpdated'), 'DateUpdated', '__AbsentNamespace0_CTD_ANON_18_DateUpdated', pyxb.binding.datatypes.date)
    __DateUpdated._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 320, 5)
    __DateUpdated._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 320, 5)
    
    DateUpdated = property(__DateUpdated.value, __DateUpdated.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Acc.name() : __Acc,
        __Version.name() : __Version,
        __Type.name() : __Type,
        __DateUpdated.name() : __DateUpdated
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_19 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 356, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_19_Type', STD_ANON_7, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 359, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 359, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type MeasureSetType with content type ELEMENT_ONLY
class MeasureSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MeasureSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MeasureSetType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 389, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Measure uses Python identifier Measure
    __Measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Measure'), 'Measure', '__AbsentNamespace0_MeasureSetType_Measure', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 391, 3), )

    
    Measure = property(__Measure.value, __Measure.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__AbsentNamespace0_MeasureSetType_Name', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 542, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Symbol'), 'Symbol', '__AbsentNamespace0_MeasureSetType_Symbol', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 543, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_MeasureSetType_AttributeSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 544, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_MeasureSetType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 580, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_MeasureSetType_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 581, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_MeasureSetType_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 582, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_MeasureSetType_Type', STD_ANON_13, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 584, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 584, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_MeasureSetType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Measure.name() : __Measure,
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
Namespace.addCategoryObject('typeBinding', u'MeasureSetType', MeasureSetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 392, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__AbsentNamespace0_CTD_ANON_20_Name', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 394, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Symbol'), 'Symbol', '__AbsentNamespace0_CTD_ANON_20_Symbol', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 395, 6), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_CTD_ANON_20_AttributeSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 396, 6), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element CytogeneticLocation uses Python identifier CytogeneticLocation
    __CytogeneticLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'CytogeneticLocation'), 'CytogeneticLocation', '__AbsentNamespace0_CTD_ANON_20_CytogeneticLocation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 455, 6), )

    
    CytogeneticLocation = property(__CytogeneticLocation.value, __CytogeneticLocation.set, None, u'Cytogenetic location is maintained\n\t\t\t\t\t\t\t\tindependent of sequence location.')

    
    # Element SequenceLocation uses Python identifier SequenceLocation
    __SequenceLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SequenceLocation'), 'SequenceLocation', '__AbsentNamespace0_CTD_ANON_20_SequenceLocation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 461, 6), )

    
    SequenceLocation = property(__SequenceLocation.value, __SequenceLocation.set, None, None)

    
    # Element MeasureRelationship uses Python identifier MeasureRelationship
    __MeasureRelationship = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'MeasureRelationship'), 'MeasureRelationship', '__AbsentNamespace0_CTD_ANON_20_MeasureRelationship', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 462, 6), )

    
    MeasureRelationship = property(__MeasureRelationship.value, __MeasureRelationship.set, None, u'MeasureRelationship is used to represent relationships between \n\t\t\t\t\t\t\t\t\tthe type of measure being represented, and other object.\n\t\t\t\t\t\t\t\t\tThis can be gene/variant, protein/gene, etc., as in when a variation is reported to be within a gene.\n\t\t\t\t\t\t\t\t')

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_20_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 513, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_20_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 514, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_20_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 515, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Source'), 'Source', '__AbsentNamespace0_CTD_ANON_20_Source', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 516, 6), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_20_Type', STD_ANON_11, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 518, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 518, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_20_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __CytogeneticLocation.name() : __CytogeneticLocation,
        __SequenceLocation.name() : __SequenceLocation,
        __MeasureRelationship.name() : __MeasureRelationship,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_21 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 400, 10)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_21_Type', STD_ANON_8, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 403, 13)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 403, 13)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Change uses Python identifier Change
    __Change = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Change'), 'Change', '__AbsentNamespace0_CTD_ANON_21_Change', pyxb.binding.datatypes.anySimpleType)
    __Change._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 444, 13)
    __Change._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 444, 13)
    
    Change = property(__Change.value, __Change.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Change.name() : __Change
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """MeasureRelationship is used to represent relationships between 
									the type of measure being represented, and other object.
									This can be gene/variant, protein/gene, etc., as in when a variation is reported to be within a gene.
								"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 469, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__AbsentNamespace0_CTD_ANON_22_Name', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 471, 9), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Symbol'), 'Symbol', '__AbsentNamespace0_CTD_ANON_22_Symbol', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 472, 9), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_CTD_ANON_22_AttributeSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 473, 9), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element SequenceLocation uses Python identifier SequenceLocation
    __SequenceLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'SequenceLocation'), 'SequenceLocation', '__AbsentNamespace0_CTD_ANON_22_SequenceLocation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 497, 9), )

    
    SequenceLocation = property(__SequenceLocation.value, __SequenceLocation.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_22_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 498, 9), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_22_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 499, 9), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_CTD_ANON_22_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 500, 9), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_22_Type', STD_ANON_10, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 502, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 502, 8)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_22_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __SequenceLocation.name() : __SequenceLocation,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_23 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 477, 13)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_23_Type', STD_ANON_9, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 480, 16)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 480, 16)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_24 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 548, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_24_Type', STD_ANON_12, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 551, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 551, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Change uses Python identifier Change
    __Change = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Change'), 'Change', '__AbsentNamespace0_CTD_ANON_24_Change', pyxb.binding.datatypes.anySimpleType)
    __Change._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 569, 10)
    __Change._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 569, 10)
    
    Change = property(__Change.value, __Change.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Change.name() : __Change
    })



# Complex type TraitSetType with content type ELEMENT_ONLY
class TraitSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TraitSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TraitSetType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 597, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Trait uses Python identifier Trait
    __Trait = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Trait'), 'Trait', '__AbsentNamespace0_TraitSetType_Trait', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 599, 3), )

    
    Trait = property(__Trait.value, __Trait.set, None, None)

    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__AbsentNamespace0_TraitSetType_Name', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 600, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Symbol'), 'Symbol', '__AbsentNamespace0_TraitSetType_Symbol', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 601, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_TraitSetType_AttributeSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 602, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_TraitSetType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 624, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_TraitSetType_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 625, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_TraitSetType_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 626, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_TraitSetType_Type', STD_ANON_14, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 628, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 628, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_TraitSetType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Trait.name() : __Trait,
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
Namespace.addCategoryObject('typeBinding', u'TraitSetType', TraitSetType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_25 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 606, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_25_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 609, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 609, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type TraitType with content type ELEMENT_ONLY
class TraitType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TraitType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TraitType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 638, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__AbsentNamespace0_TraitType_Name', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 640, 3), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Symbol'), 'Symbol', '__AbsentNamespace0_TraitType_Symbol', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 641, 3), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_TraitType_AttributeSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 642, 3), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element TraitRelationship uses Python identifier TraitRelationship
    __TraitRelationship = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'TraitRelationship'), 'TraitRelationship', '__AbsentNamespace0_TraitType_TraitRelationship', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 660, 3), )

    
    TraitRelationship = property(__TraitRelationship.value, __TraitRelationship.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_TraitType_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 699, 3), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_TraitType_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 700, 3), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Comment'), 'Comment', '__AbsentNamespace0_TraitType_Comment', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 701, 3), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Source'), 'Source', '__AbsentNamespace0_TraitType_Source', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 702, 3), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_TraitType_Type', STD_ANON_16, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 704, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 704, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_TraitType_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __TraitRelationship.name() : __TraitRelationship,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Comment.name() : __Comment,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })
Namespace.addCategoryObject('typeBinding', u'TraitType', TraitType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_26 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 646, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_26_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 649, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 649, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 661, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__AbsentNamespace0_CTD_ANON_27_Name', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 663, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element Symbol uses Python identifier Symbol
    __Symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Symbol'), 'Symbol', '__AbsentNamespace0_CTD_ANON_27_Symbol', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 664, 6), )

    
    Symbol = property(__Symbol.value, __Symbol.set, None, None)

    
    # Element AttributeSet uses Python identifier AttributeSet
    __AttributeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'AttributeSet'), 'AttributeSet', '__AbsentNamespace0_CTD_ANON_27_AttributeSet', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 665, 6), )

    
    AttributeSet = property(__AttributeSet.value, __AttributeSet.set, None, None)

    
    # Element Citation uses Python identifier Citation
    __Citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Citation'), 'Citation', '__AbsentNamespace0_CTD_ANON_27_Citation', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 683, 6), )

    
    Citation = property(__Citation.value, __Citation.set, None, None)

    
    # Element XRef uses Python identifier XRef
    __XRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'XRef'), 'XRef', '__AbsentNamespace0_CTD_ANON_27_XRef', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 684, 6), )

    
    XRef = property(__XRef.value, __XRef.set, None, None)

    
    # Element Source uses Python identifier Source
    __Source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Source'), 'Source', '__AbsentNamespace0_CTD_ANON_27_Source', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 685, 6), )

    
    Source = property(__Source.value, __Source.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_27_Type', STD_ANON_15, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 687, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 687, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ID'), 'ID', '__AbsentNamespace0_CTD_ANON_27_ID', pyxb.binding.datatypes.positiveInteger)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    __ID._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1243, 2)
    
    ID = property(__ID.value, __ID.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __Symbol.name() : __Symbol,
        __AttributeSet.name() : __AttributeSet,
        __Citation.name() : __Citation,
        __XRef.name() : __XRef,
        __Source.name() : __Source
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __ID.name() : __ID
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_28 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 669, 10)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_28_Type', pyxb.binding.datatypes.string, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 672, 13)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 672, 13)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_29 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 803, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_29_Type', STD_ANON_19, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 806, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 806, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (MethodType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 841, 4)
    _ElementMap = MethodType._ElementMap.copy()
    _AttributeMap = MethodType._AttributeMap.copy()
    # Base type is MethodType
    
    # Element NamePlatform (NamePlatform) inherited from MethodType
    
    # Element TypePlatform (TypePlatform) inherited from MethodType
    
    # Element Purpose (Purpose) inherited from MethodType
    
    # Element ResultType (ResultType) inherited from MethodType
    
    # Element MinReported (MinReported) inherited from MethodType
    
    # Element MaxReported (MaxReported) inherited from MethodType
    
    # Element ReferenceStandard (ReferenceStandard) inherited from MethodType
    
    # Element Citation (Citation) inherited from MethodType
    
    # Element XRef (XRef) inherited from MethodType
    
    # Element Description (Description) inherited from MethodType
    
    # Element Software (Software) inherited from MethodType
    
    # Element SourceType (SourceType) inherited from MethodType
    
    # Element MethodType (MethodType) inherited from MethodType
    
    # Element MethodAttribute (MethodAttribute) inherited from MethodType
    
    # Element MethodResult (MethodResult) inherited from MethodType
    
    # Element Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_30_Type', True, pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 845, 8), )

    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        __Type.name() : __Type
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_31 (AttributeType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 875, 7)
    _ElementMap = AttributeType._ElementMap.copy()
    _AttributeMap = AttributeType._AttributeMap.copy()
    # Base type is AttributeType
    
    # Attribute integerValue inherited from AttributeType
    
    # Attribute dateValue inherited from AttributeType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_31_Type', STD_ANON_21, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 878, 10)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 878, 10)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.int
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 966, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.int
    
    # Attribute age_unit uses Python identifier age_unit
    __age_unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'age_unit'), 'age_unit', '__AbsentNamespace0_CTD_ANON_32_age_unit', STD_ANON_23, required=True)
    __age_unit._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 969, 7)
    __age_unit._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 969, 7)
    
    age_unit = property(__age_unit.value, __age_unit.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_CTD_ANON_32_Type', STD_ANON_24, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 978, 7)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 978, 7)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __age_unit.name() : __age_unit,
        __Type.name() : __Type
    })



# Complex type AssertionTypeRCV with content type EMPTY
class AssertionTypeRCV (pyxb.binding.basis.complexTypeDefinition):
    """Assertion is used to represent the type of relationship between the trait set and the measure set. This is stored in
						GTR.clinvar.measure_trait.relat_type.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssertionTypeRCV')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1176, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_AssertionTypeRCV_Type', AssertionTypeAttr, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1182, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1182, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
Namespace.addCategoryObject('typeBinding', u'AssertionTypeRCV', AssertionTypeRCV)


# Complex type SequenceLocationType with content type EMPTY
class SequenceLocationType (pyxb.binding.basis.complexTypeDefinition):
    """Used to report the assembly, chromosome, and location of the measure."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SequenceLocationType')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1213, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Assembly uses Python identifier Assembly
    __Assembly = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Assembly'), 'Assembly', '__AbsentNamespace0_SequenceLocationType_Assembly', pyxb.binding.datatypes.string, required=True)
    __Assembly._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1220, 2)
    __Assembly._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1220, 2)
    
    Assembly = property(__Assembly.value, __Assembly.set, None, None)

    
    # Attribute Chr uses Python identifier Chr
    __Chr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Chr'), 'Chr', '__AbsentNamespace0_SequenceLocationType_Chr', pyxb.binding.datatypes.string, required=True)
    __Chr._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1221, 2)
    __Chr._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1221, 2)
    
    Chr = property(__Chr.value, __Chr.set, None, None)

    
    # Attribute Accession uses Python identifier Accession
    __Accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Accession'), 'Accession', '__AbsentNamespace0_SequenceLocationType_Accession', pyxb.binding.datatypes.string)
    __Accession._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1222, 2)
    __Accession._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1222, 2)
    
    Accession = property(__Accession.value, __Accession.set, None, None)

    
    # Attribute outerStart uses Python identifier outerStart
    __outerStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'outerStart'), 'outerStart', '__AbsentNamespace0_SequenceLocationType_outerStart', pyxb.binding.datatypes.nonNegativeInteger)
    __outerStart._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1223, 2)
    __outerStart._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1223, 2)
    
    outerStart = property(__outerStart.value, __outerStart.set, None, None)

    
    # Attribute innerStart uses Python identifier innerStart
    __innerStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'innerStart'), 'innerStart', '__AbsentNamespace0_SequenceLocationType_innerStart', pyxb.binding.datatypes.nonNegativeInteger)
    __innerStart._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1224, 2)
    __innerStart._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1224, 2)
    
    innerStart = property(__innerStart.value, __innerStart.set, None, None)

    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__AbsentNamespace0_SequenceLocationType_start', pyxb.binding.datatypes.nonNegativeInteger)
    __start._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1225, 2)
    __start._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1225, 2)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute stop uses Python identifier stop
    __stop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'stop'), 'stop', '__AbsentNamespace0_SequenceLocationType_stop', pyxb.binding.datatypes.positiveInteger)
    __stop._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1226, 2)
    __stop._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1226, 2)
    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Attribute innerStop uses Python identifier innerStop
    __innerStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'innerStop'), 'innerStop', '__AbsentNamespace0_SequenceLocationType_innerStop', pyxb.binding.datatypes.positiveInteger)
    __innerStop._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1227, 2)
    __innerStop._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1227, 2)
    
    innerStop = property(__innerStop.value, __innerStop.set, None, None)

    
    # Attribute outerStop uses Python identifier outerStop
    __outerStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'outerStop'), 'outerStop', '__AbsentNamespace0_SequenceLocationType_outerStop', pyxb.binding.datatypes.positiveInteger)
    __outerStop._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1228, 2)
    __outerStop._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1228, 2)
    
    outerStop = property(__outerStop.value, __outerStop.set, None, None)

    
    # Attribute Strand uses Python identifier Strand
    __Strand = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Strand'), 'Strand', '__AbsentNamespace0_SequenceLocationType_Strand', pyxb.binding.datatypes.string)
    __Strand._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1229, 2)
    __Strand._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1229, 2)
    
    Strand = property(__Strand.value, __Strand.set, None, None)

    
    # Attribute AssemblyStatus uses Python identifier AssemblyStatus
    __AssemblyStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AssemblyStatus'), 'AssemblyStatus', '__AbsentNamespace0_SequenceLocationType_AssemblyStatus', STD_ANON_29)
    __AssemblyStatus._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1230, 2)
    __AssemblyStatus._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1230, 2)
    
    AssemblyStatus = property(__AssemblyStatus.value, __AssemblyStatus.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Assembly.name() : __Assembly,
        __Chr.name() : __Chr,
        __Accession.name() : __Accession,
        __outerStart.name() : __outerStart,
        __innerStart.name() : __innerStart,
        __start.name() : __start,
        __stop.name() : __stop,
        __innerStop.name() : __innerStop,
        __outerStop.name() : __outerStop,
        __Strand.name() : __Strand,
        __AssemblyStatus.name() : __AssemblyStatus
    })
Namespace.addCategoryObject('typeBinding', u'SequenceLocationType', SequenceLocationType)


# Complex type AssertionTypeSCV with content type EMPTY
class AssertionTypeSCV (pyxb.binding.basis.complexTypeDefinition):
    """Assertion is used to represent the type of relationship between the trait set and the measure set. This is stored in
						GTR.clinvar.measure_trait.relat_type.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssertionTypeSCV')
    _XSDLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1184, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Type'), 'Type', '__AbsentNamespace0_AssertionTypeSCV_Type', AssertionTypeAttrSCV, required=True)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1190, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1190, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
Namespace.addCategoryObject('typeBinding', u'AssertionTypeSCV', AssertionTypeSCV)


ReleaseSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReleaseSet'), ReleaseType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 2, 8))
Namespace.addCategoryObject('elementBinding', ReleaseSet.name().localName(), ReleaseSet)

ClinVarSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClinVarSet'), PublicSetType, documentation=u'The ClinVarSet is used to group the aggregate record (RCV accession)\n\t\t\twith the submissions underlying it (SCV accessions) \n\t\t\t', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 3, 1))
Namespace.addCategoryObject('elementBinding', ClinVarSet.name().localName(), ClinVarSet)

ClinVarAssertion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClinVarAssertion'), MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', ClinVarAssertion.name().localName(), ClinVarAssertion)

ReferenceClinVarAssertion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceClinVarAssertion'), ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', ReferenceClinVarAssertion.name().localName(), ReferenceClinVarAssertion)



CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ID'), CTD_ANON, scope=CitationType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 60, 3)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'URL'), pyxb.binding.datatypes.anyURI, scope=CitationType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 74, 3)))

CitationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CitationText'), pyxb.binding.datatypes.string, scope=CitationType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 75, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 60, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 74, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 75, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'ID')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 60, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'URL')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 74, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CitationType._UseForTag(pyxb.namespace.ExpandedName(None, u'CitationText')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 75, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CitationType._Automaton = _BuildAutomaton()




PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClinVarAssertion'), MeasureTraitType, scope=PublicSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 10, 1)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceClinVarAssertion'), ReferenceAssertionType, scope=PublicSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 16, 1)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'RecordStatus'), STD_ANON_, scope=PublicSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 132, 3), unicode_default=u'current'))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReplacedBy'), pyxb.binding.datatypes.string, scope=PublicSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 142, 3)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Replaces'), pyxb.binding.datatypes.string, scope=PublicSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 143, 3)))

PublicSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Title'), pyxb.binding.datatypes.string, scope=PublicSetType, documentation=u'The title is contructed from the concatenation of the description of the variation and the phenotype.\n\t\t\t\t\tIn the database it is extracted from the title of RCV accession', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 144, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 142, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 143, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 144, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 150, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'RecordStatus')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 132, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'ReplacedBy')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 142, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Replaces')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 143, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Title')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 144, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceClinVarAssertion')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 150, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PublicSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClinVarAssertion')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 157, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PublicSetType._Automaton = _BuildAutomaton_()




ReleaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClinVarSet'), PublicSetType, scope=ReleaseType, documentation=u'The ClinVarSet is used to group the aggregate record (RCV accession)\n\t\t\twith the submissions underlying it (SCV accessions) \n\t\t\t', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 3, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReleaseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClinVarSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 165, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReleaseType._Automaton = _BuildAutomaton_2()




MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ClinVarSubmissionID'), CTD_ANON_, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 176, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ClinVarAccession'), CTD_ANON_16, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 190, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'RecordStatus'), STD_ANON_3, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 211, 3), unicode_default=u'current'))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance'), ClinicalSignificanceTypeSCV, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 220, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CustomAssertionScore'), CTD_ANON_2, scope=MeasureTraitType, documentation=u'\n\t\t\t\t\t\tUsed to represent the scoring matrix a submitter may use to \n\t\t\t\t\t\tevaluate clinical signficance. \n\t\t\t\t\t', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 221, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Assertion'), AssertionTypeSCV, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 237, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ExternalID'), XrefType, scope=MeasureTraitType, documentation=u'XrefType is used to identify data source(s) and their identifiers.\n\t\t\t\t\tOptional because not all sources have an ID specific to the assertion. \n\t\t\t\t\t', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 238, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AttributeSet'), CTD_ANON_3, scope=MeasureTraitType, documentation=u'AttributeSet is a package to represent a unit of information,\n\t\t\t\t\t\tthe source(s) of that unit, identifiers representing that unit, and comments.\n\t\t\t\t ', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 245, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ObservedIn'), ObservationSet, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 278, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MeasureSet'), MeasureSetType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 279, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TraitSet'), TraitSetType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 280, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 281, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'StudyName'), pyxb.binding.datatypes.string, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 282, 3)))

MeasureTraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=MeasureTraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 283, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 221, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 238, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 245, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 281, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 282, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 283, 3))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'ClinVarSubmissionID')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 176, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'ClinVarAccession')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 190, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'RecordStatus')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 211, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 220, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'CustomAssertionScore')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 221, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'Assertion')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 237, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'ExternalID')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 238, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'AttributeSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 245, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'ObservedIn')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 278, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'MeasureSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 279, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'TraitSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 280, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 281, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'StudyName')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 282, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasureTraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 283, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeasureTraitType._Automaton = _BuildAutomaton_3()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 230, 6)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 231, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 230, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 231, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 230, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 231, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_4()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_17, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 253, 6)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 272, 6)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 273, 6)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 274, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 272, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 273, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 274, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 253, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 272, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 273, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 274, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_5()




ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ClinVarAccession'), CTD_ANON_18, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 298, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'RecordStatus'), STD_ANON_6, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 323, 3), unicode_default=u'current'))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance'), ClinicalSignificanceType, scope=ReferenceAssertionType, documentation=u'Either the value corresponding to the scoring system of the ACMG, or \n\t\t\t\t\ta value representing such concepts as drug response, risk factors, etc.', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 332, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Assertion'), AssertionTypeRCV, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 338, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ExternalID'), XrefType, scope=ReferenceAssertionType, documentation=u'Represents the public identifier a source may have for this record. \n\t\t\t\t\t', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 339, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AttributeSet'), CTD_ANON_4, scope=ReferenceAssertionType, documentation=u'Many concepts in the database are represented by what ClinVar terms an AttributeSet, \n\t\t\t\t\t\twhich is an open-ended structure providing the equivalent of a type of information, the value(s) for that data type, \n\t\t\t\t\t\tsubmitter(s), free text comment(s) describing that attribute, identifier(s) for that attribute, and \n\t\t\t\t\t\tcitation(s) related to that attribute.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 345, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ObservedIn'), ObservationSet, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 378, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MeasureSet'), MeasureSetType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 379, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TraitSet'), TraitSetType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 380, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 381, 3)))

ReferenceAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=ReferenceAssertionType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 382, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 332, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 339, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 345, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 378, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 381, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 382, 3))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'ClinVarAccession')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 298, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'RecordStatus')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 323, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 332, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Assertion')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 338, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'ExternalID')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 339, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'AttributeSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 345, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'ObservedIn')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 378, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'MeasureSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 379, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'TraitSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 380, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 381, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceAssertionType._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 382, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferenceAssertionType._Automaton = _BuildAutomaton_6()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_19, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 355, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 372, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 373, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 374, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 372, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 373, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 374, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 355, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 372, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 373, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 374, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_7()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_21, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 399, 9)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 449, 9)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 450, 9)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 451, 9)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 449, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 450, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 451, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 399, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 449, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 450, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 451, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_8()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_23, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 476, 12)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 493, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 493, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 476, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 493, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_9()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_24, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 547, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 574, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 575, 6)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 576, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 574, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 575, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 576, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 547, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 574, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 575, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 576, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_10()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_25, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 605, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 614, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 615, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_8, documentation=u'table_type = 38', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 616, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 614, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 615, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 616, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 605, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 614, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 615, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 616, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_11()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_26, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 645, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 654, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 655, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 656, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 654, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 655, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 656, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 645, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 654, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 655, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 656, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_12()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_28, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 668, 9)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 677, 9)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 678, 9)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 679, 9)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 677, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 678, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 679, 9))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 668, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 677, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 678, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 679, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_13()




SetElementSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ElementValue'), CTD_ANON_11, scope=SetElementSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 737, 3)))

SetElementSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=SetElementSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 746, 3)))

SetElementSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=SetElementSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 747, 3)))

SetElementSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=SetElementSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 748, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 746, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 747, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 748, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SetElementSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'ElementValue')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 737, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SetElementSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 746, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SetElementSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 747, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SetElementSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 748, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SetElementSetType._Automaton = _BuildAutomaton_14()




MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'NamePlatform'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 764, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TypePlatform'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 765, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Purpose'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 766, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ResultType'), STD_ANON_17, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 767, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MinReported'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 777, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MaxReported'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 778, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReferenceStandard'), pyxb.binding.datatypes.string, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 779, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 780, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 781, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Description'), pyxb.binding.datatypes.string, scope=MethodType, documentation=u' Free text to enrich the description of the method and to\n                        provide information not captured in specific fields. ', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 782, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Software'), SoftwareSet, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 788, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SourceType'), STD_ANON_18, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 789, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MethodType'), Methodtypelist, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 798, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MethodAttribute'), CTD_ANON_12, scope=MethodType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 799, 3)))

MethodType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MethodResult'), AttributeType, scope=MethodType, documentation=u' MethodResult is used to represent results specific to a particular method.\n                        An example is a method used to validate the the variant call; the MethodResult would be pass/fail/inconclusive', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 822, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 764, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 765, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 766, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 767, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 777, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 778, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 779, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 780, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 781, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 782, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 788, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 789, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 799, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 822, 3))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'NamePlatform')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 764, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'TypePlatform')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 765, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'Purpose')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 766, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'ResultType')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 767, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'MinReported')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 777, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'MaxReported')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 778, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferenceStandard')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 779, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 780, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 781, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'Description')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 782, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'Software')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 788, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'SourceType')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 789, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'MethodType')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 798, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'MethodAttribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 799, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(MethodType._UseForTag(pyxb.namespace.ExpandedName(None, u'MethodResult')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 822, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MethodType._Automaton = _BuildAutomaton_15()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_29, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 802, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 802, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_16()




ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Sample'), SampleType, scope=ObservationSet, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 839, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Method'), CTD_ANON_30, scope=ObservationSet, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 840, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ObservedData'), CTD_ANON_13, scope=ObservationSet, documentation=u'This is an AttributeSet, there will be 1 attribute supported by optional citations, xrefs and comment. \n\t\t\t\t\t\tThere must be at least one ObservedData Set, but can be any number.\n\t\t\t\t\t\tFor each ObservedData set the Attribute will be either decimal or string depending on type. \n\t\t\t\t\t\tThe value will be stored here, but decimals will be entered to the database as a string.\n\t\t\t\t\t', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 864, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Co-occurrenceSet'), Co_occurrenceType, scope=ObservationSet, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 913, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TraitSet'), TraitSetType, scope=ObservationSet, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 914, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=ObservationSet, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 915, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=ObservationSet, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 916, 3)))

ObservationSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=ObservationSet, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 917, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 840, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 913, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 914, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 915, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 916, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 917, 3))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'Sample')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 839, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'Method')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 840, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'ObservedData')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 864, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'Co-occurrenceSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 913, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'TraitSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 914, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 915, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 916, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ObservationSet._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 917, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObservationSet._Automaton = _BuildAutomaton_17()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Attribute'), CTD_ANON_31, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 874, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Severity'), SeverityType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 905, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 906, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 907, 6)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 908, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 905, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 906, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 907, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 908, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'Attribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 874, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'Severity')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 905, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 906, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 907, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 908, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_18()




SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SampleDescription'), CTD_ANON_14, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 926, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Origin'), STD_ANON_22, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 934, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Ethnicity'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 952, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'GeographicfOrigin'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 953, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Tissue'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 954, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CellLine'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 955, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Species'), CTD_ANON_15, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 956, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Age'), CTD_ANON_32, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 965, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Strain'), pyxb.binding.datatypes.string, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 991, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AffectedStatus'), STD_ANON_25, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 992, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'NumberTested'), pyxb.binding.datatypes.int, scope=SampleType, documentation=u'Denominator, total individuals included in this observation\n\t\t\t\t\t\tset.', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1002, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'NumberMales'), pyxb.binding.datatypes.int, scope=SampleType, documentation=u'Denominator, total males included in this observation\n\t\t\t\t\t\tset.', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1008, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'NumberFemales'), pyxb.binding.datatypes.int, scope=SampleType, documentation=u'Denominator, total females included in this observation\n\t\t\t\t\t\tset.', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1014, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'NumberChrTested'), pyxb.binding.datatypes.int, scope=SampleType, documentation=u'Denominator, total number chromosomes tested. Number affected\n\t\t\t\t\t\tand unaffected are captured in the element\n\t\t\t\t\t\tNumberObserved.', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1020, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Gender'), STD_ANON_26, scope=SampleType, documentation=u'Gender should be used ONLY if explicit values are not available for number of males or females, and there is a need to indicate that the genders in the sample are known. \n                    ', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1027, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'FamilyData'), FamilyInfo, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1040, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1041, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1042, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1043, 3)))

SampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SourceType'), STD_ANON_27, scope=SampleType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1044, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 926, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 952, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 953, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 954, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 955, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 956, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 965, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 991, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1002, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1008, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1014, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1020, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1027, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1040, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1041, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1042, 3))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1043, 3))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1044, 3))
    counters.add(cc_17)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'SampleDescription')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 926, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Origin')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 934, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Ethnicity')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 952, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'GeographicfOrigin')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 953, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Tissue')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 954, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'CellLine')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 955, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Species')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 956, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Age')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 965, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Strain')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 991, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'AffectedStatus')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 992, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'NumberTested')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1002, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'NumberMales')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1008, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'NumberFemales')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1014, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'NumberChrTested')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1020, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Gender')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1027, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'FamilyData')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1040, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1041, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1042, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1043, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(SampleType._UseForTag(pyxb.namespace.ExpandedName(None, u'SourceType')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1044, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SampleType._Automaton = _BuildAutomaton_19()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Description'), CommentType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 929, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 930, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 929, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 930, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, u'Description')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 929, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 930, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_20()




Co_occurrenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Zygosity'), ZygosityType, scope=Co_occurrenceType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1059, 3)))

Co_occurrenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AlleleDescSet'), AlleleDescType, scope=Co_occurrenceType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1060, 3)))

Co_occurrenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Count'), pyxb.binding.datatypes.int, scope=Co_occurrenceType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1061, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1059, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1060, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1061, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Co_occurrenceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Zygosity')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1059, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Co_occurrenceType._UseForTag(pyxb.namespace.ExpandedName(None, u'AlleleDescSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1060, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Co_occurrenceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Count')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1061, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Co_occurrenceType._Automaton = _BuildAutomaton_21()




ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReviewStatus'), ReviewStatusType, scope=ClinicalSignificanceType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1066, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Description'), pyxb.binding.datatypes.string, scope=ClinicalSignificanceType, documentation=u'We are not providing an enumeration for the values we report for clinical significance within the xsd. \n\t\t\t\t\t\tThe values are maintained here: ftp://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Clinical_significance.txt. ', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1067, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Explanation'), CommentType, scope=ClinicalSignificanceType, documentation=u"Explanation is used only when the description is 'conflicting data from submitters'\n\t\t\t\t\tThe element summarizes the conflict.", location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1073, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=ClinicalSignificanceType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1079, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=ClinicalSignificanceType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1080, 3)))

ClinicalSignificanceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=ClinicalSignificanceType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1081, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1066, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1067, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1073, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1079, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1080, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1081, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, u'ReviewStatus')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1066, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Description')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1067, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Explanation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1073, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1079, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1080, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceType._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1081, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClinicalSignificanceType._Automaton = _BuildAutomaton_22()




ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ReviewStatus'), ReviewStatusType, scope=ClinicalSignificanceTypeSCV, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1087, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Description'), pyxb.binding.datatypes.string, scope=ClinicalSignificanceTypeSCV, documentation=u'We are not providing an enumeration for the values we report for clinical significance within the xsd. \n\t\t\t\t\t\tThe values are maintained here: ftp://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Clinical_significance.txt. ', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1088, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Explanation'), CommentType, scope=ClinicalSignificanceTypeSCV, documentation=u"Explanation is used only when the description is 'conflicting data from submitters'\n\t\t\t\t\tThe element summarizes the conflict.", location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1094, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=ClinicalSignificanceTypeSCV, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1100, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=ClinicalSignificanceTypeSCV, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1101, 3)))

ClinicalSignificanceTypeSCV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=ClinicalSignificanceTypeSCV, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1102, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1087, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1088, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1094, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1100, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1101, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1102, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, u'ReviewStatus')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1087, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, u'Description')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1088, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, u'Explanation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1094, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1100, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1101, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClinicalSignificanceTypeSCV._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1102, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClinicalSignificanceTypeSCV._Automaton = _BuildAutomaton_23()




AlleleDescType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), pyxb.binding.datatypes.string, scope=AlleleDescType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1111, 3)))

AlleleDescType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'RelativeOrientation'), STD_ANON_28, scope=AlleleDescType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1112, 3)))

AlleleDescType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Zygosity'), ZygosityType, scope=AlleleDescType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1121, 3)))

AlleleDescType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance'), ClinicalSignificanceType, scope=AlleleDescType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1122, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1112, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1121, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1122, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AlleleDescType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1111, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlleleDescType._UseForTag(pyxb.namespace.ExpandedName(None, u'RelativeOrientation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1112, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlleleDescType._UseForTag(pyxb.namespace.ExpandedName(None, u'Zygosity')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1121, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AlleleDescType._UseForTag(pyxb.namespace.ExpandedName(None, u'ClinicalSignificance')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 1122, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AlleleDescType._Automaton = _BuildAutomaton_24()




MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Measure'), CTD_ANON_20, scope=MeasureSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 391, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), SetElementSetType, scope=MeasureSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 542, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Symbol'), SetElementSetType, scope=MeasureSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 543, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AttributeSet'), CTD_ANON_7, scope=MeasureSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 544, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=MeasureSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 580, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=MeasureSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 581, 3)))

MeasureSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=MeasureSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 582, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 542, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 543, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 544, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 580, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 581, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 582, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Measure')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 391, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 542, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Symbol')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 543, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'AttributeSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 544, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 580, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 581, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MeasureSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 582, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MeasureSetType._Automaton = _BuildAutomaton_25()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), SetElementSetType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 394, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Symbol'), SetElementSetType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 395, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AttributeSet'), CTD_ANON_5, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 396, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'CytogeneticLocation'), pyxb.binding.datatypes.string, scope=CTD_ANON_20, documentation=u'Cytogenetic location is maintained\n\t\t\t\t\t\t\t\tindependent of sequence location.', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 455, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SequenceLocation'), SequenceLocationType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 461, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'MeasureRelationship'), CTD_ANON_22, scope=CTD_ANON_20, documentation=u'MeasureRelationship is used to represent relationships between \n\t\t\t\t\t\t\t\t\tthe type of measure being represented, and other object.\n\t\t\t\t\t\t\t\t\tThis can be gene/variant, protein/gene, etc., as in when a variation is reported to be within a gene.\n\t\t\t\t\t\t\t\t', location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 462, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 513, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 514, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 515, 6)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Source'), DataSourceType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 516, 6)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 394, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 395, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 396, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 455, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 461, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 462, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 513, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 514, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 515, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 516, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 394, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'Symbol')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 395, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'AttributeSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 396, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'CytogeneticLocation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 455, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'SequenceLocation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 461, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'MeasureRelationship')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 462, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 513, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 514, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 515, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, u'Source')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 516, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_26()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), SetElementSetType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 471, 9)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Symbol'), SetElementSetType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 472, 9)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AttributeSet'), CTD_ANON_6, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 473, 9)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'SequenceLocation'), SequenceLocationType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 497, 9)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 498, 9)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 499, 9)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 500, 9)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 471, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 472, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 473, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 497, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 498, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 499, 9))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 500, 9))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 471, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, u'Symbol')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 472, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, u'AttributeSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 473, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, u'SequenceLocation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 497, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 498, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 499, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 500, 9))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_27()




TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Trait'), TraitType, scope=TraitSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 599, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), SetElementSetType, scope=TraitSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 600, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Symbol'), SetElementSetType, scope=TraitSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 601, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AttributeSet'), CTD_ANON_8, scope=TraitSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 602, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=TraitSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 624, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=TraitSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 625, 3)))

TraitSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=TraitSetType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 626, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 600, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 601, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 602, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 624, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 625, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 626, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Trait')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 599, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 600, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Symbol')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 601, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'AttributeSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 602, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 624, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 625, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TraitSetType._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 626, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TraitSetType._Automaton = _BuildAutomaton_28()




TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), SetElementSetType, scope=TraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 640, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Symbol'), SetElementSetType, scope=TraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 641, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AttributeSet'), CTD_ANON_9, scope=TraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 642, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TraitRelationship'), CTD_ANON_27, scope=TraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 660, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=TraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 699, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=TraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 700, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Comment'), CommentType, scope=TraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 701, 3)))

TraitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Source'), DataSourceType, scope=TraitType, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 702, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 641, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 642, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 660, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 699, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 700, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 701, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 702, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 640, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'Symbol')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 641, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'AttributeSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 642, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'TraitRelationship')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 660, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 699, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 700, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'Comment')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 701, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TraitType._UseForTag(pyxb.namespace.ExpandedName(None, u'Source')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 702, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TraitType._Automaton = _BuildAutomaton_29()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Name'), SetElementSetType, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 663, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Symbol'), SetElementSetType, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 664, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'AttributeSet'), CTD_ANON_10, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 665, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Citation'), CitationType, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 683, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'XRef'), XrefType, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 684, 6)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Source'), DataSourceType, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 685, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 663, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 664, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 665, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 683, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 684, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 685, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'Name')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 663, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'Symbol')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 664, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'AttributeSet')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 665, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 683, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 684, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, u'Source')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 685, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_30()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'Type'), STD_ANON_20, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 845, 8)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 841, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 764, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 765, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 766, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 767, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 777, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 778, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 779, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 780, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 781, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 782, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 788, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 789, 3))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 799, 3))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 822, 3))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 845, 8))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'NamePlatform')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 764, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'TypePlatform')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 765, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'Purpose')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 766, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'ResultType')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 767, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'MinReported')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 777, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'MaxReported')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 778, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'ReferenceStandard')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 779, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'Citation')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 780, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'XRef')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 781, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'Description')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 782, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'Software')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 788, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'SourceType')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 789, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'MethodType')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 798, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'MethodAttribute')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 799, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'MethodResult')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 822, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, u'Type')), pyxb.utils.utility.Location('D:/My Ontologies/ClinVar/clinvar_public_1.3.xsd', 845, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_31()

