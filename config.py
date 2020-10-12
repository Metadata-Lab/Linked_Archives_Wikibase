global subjects
global people
global names
global countries
global events
global series
global objects
global collections
global bib_series
global belfer
global becker
global koppel

global collection_lists
global iri_keys
global property_keys
global multi_val_prop

global property_ids
global wiki_props_used

subjects = []
people = []
names = []
countries = []
events = []
series = []
objects = []
collections = []
bib_series = []
belfer = []
becker = []
koppel = []

collection_lists = [belfer, becker, koppel]

iri_keys = {
    "/subject": subjects,
    "227.": belfer,
    "140.": becker,
    "185.": koppel,
    "/person": people,
    "/names": names,
    "/countries": countries,
    "/event": events,
    "/series": series,
    "/object": objects,
    "/collection": collections,
    "/bib_series": bib_series
}

property_keys = [
    "IRI",
    "hasAppearance",
    "hasBib_series",
    "hasComposer",
    "hasHost",
    "hasHumanSubject",
    "hasInterviewee",
    "hasObject",
    "hasPerformer",
    "hasPhotographer",
    "hasReporter",
    "hasSubject",
    "is_part_of",
    "is_related_to",
    "is_created_by",
    "firstname",
    "lastname",
    "middleinitial",
    "role",
    "coverage",
    "date",
    "description",
    "identifier",
    "publisher",
    "rights",
    "subject",
    "title",
    "title_alt",
    "type",
    "type/mediaType",
    "mediaType",
    "comment",
    "label"
]

multi_val_prop = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
]

property_ids = {

}

wiki_props_used = [
    'P569', 'P27', 'P19', 'P1412', 'P570', 'P20', 'P1559', 'P1477', 'P742'
]