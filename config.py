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
global object_prop

global object_ids
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
    "IRI", #0
    "hasAppearance", #N/A 1
    "hasBib_series", #N/A 2
    "hasComposer", #N/A 3
    "hasHost", #N/A 4
    "hasHumanSubject", #N/A 5
    "hasInterviewee", #N/A 6
    "hasObject", #N/A 7
    "hasPerformer", #N/A 8
    "hasPhotographer", #N/A 9
    "hasReporter", #N/A 10
    "hasSubject", #11
    "is_part_of", #12
    "is_related_to", #13
    "is_created_by", #14
    "firstname", #15
    "lastname", #16
    "middleinitial", #17
    "role", #18
    "coverage", #19
    "date", #20
    "description", #21
    "identifier", #22
    "publisher", #23
    "rights", #24
    "subject", #25
    "title", #26
    "title_alt", #27
    "type", #28
    "type/mediaType", #29
    "mediaType", #30
    "comment", #31
    "label" #32
]

multi_val_prop = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 25, 28
]

object_prop = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
]

object_ids = {
    "collection": "Q1",
    "object": "Q2",
    "item": "Q3",
    "person": "Q4",
    "name": "Q5",
    "subject": "Q6",
    "event": "Q7",
    "country": "Q8",
    "series": "Q9",
    "bib_series": "Q10"
}

property_ids = {
    #P1 = instance of
    "IRI": "P2",
    "hasSubject": "P3",
    "is_part_of": "P4",
    "is_related_to": "P5",
    "is_created_by": "P6",
    "firstname": "P7",
    "lastname": "P8",
    "middleinitial": "P9",
    "role": "P10",
    "coverage": "P11",
    "date": "P12",
    "description": "P13",
    "identifier": "P14",
    "publisher": "P15",
    "rights": "P16",
    "subject": "P17",
    "title": "P18",
    "title_alt": "P19",
    "type": "P20",
    "type/mediaType": "P21",
    "mediaType": "P22",
    "comment": "P23",
    #"label": "NONE"
    "date of birth": "P24",
    "place of birth": "P25",
    "country of citizenship": "P26",
    "languages spoken, written or signed": "P27",
    "date of death": "P28",
    "place of death": "P29",
    "name in native language": "P30",
    "birth name": "P31",
    "pseudonym": "P32"
}

wiki_props_used = [
    'P569', 'P27', 'P19', 'P1412', 'P570', 'P20', 'P1559', 'P1477', 'P742'
]