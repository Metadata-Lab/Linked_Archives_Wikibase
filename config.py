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
global wiki_date_props

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
    "country of citizenship": "P25",
    "place of birth": "P26",
    "educated at": "P27",
    "languages spoken, written or signed": "P28",
    "date of death": "P29",
    "place of death": "P30",
    "political party": "P31",
    "name in native language": "P32",
    "employer": "P33",
    "position held": "P34",
    "cause of death": "P35",
    "sport": "P36",
    "religion": "P37",
    "manner of death": "P38",
    "work location": "P39",
    "birth name": "P40",
    "member of sports team": "P41",
    "place of burial": "P42",
    "instrument": "P43",
    "military branch": "P44",
    "position played on team / speciality": "P45",
    "father": "P46",
    "conflict": "P47",
    "number of children": "P48",
    "country for sport": "P49",
    "sibling": "P50",
    "nominated for": "P51",
    "height": "P52",
    "mother": "P53",
    "writing language": "P54",
    "mass": "P55",
    "record label": "P56",
    "military rank": "P57",
    "notable work": "P58",
    "native language": "P59",
    "candidacy in election": "P60",
    "copyright status as a creator": "P61",
    "medical condition": "P62",
    "related category": "P63",
    "academic degree": "P64",
    "archives at": "P65",
    "pseudonym": "P66",
    "competition class": "P67",
    "voice type": "P68",
    "discography": "P69",
    "student of": "P70",
    "league": "P71",
    "has works in the collection": "P72",
    "convicted of": "P73",
    "unmarried partner": "P74",
    "copyright representative": "P75",
    "relative": "P76",
    "filmography": "P77",
    "influenced by": "P78",
    "movement": "P79",
    "doctoral advisor": "P80",
    "drafted by": "P81",
    "handedness": "P82",
    "honorific prefix": "P83",
    "student": "P84",
    "allegiance": "P85",
    "place of detention": "P86",
    "has written for": "P87",
    "eye color": "P88",
    "name in kana": "P89",
    "sports discipline competed in": "P90",
    "hair color": "P91",
    "net worth": "P92",
    "family": "P93",
    "time period": "P94",
    "floruit": "P95",
    "time in space": "P96",
    "astronaut mission": "P97",
    "sexual orientation": "P98",
    "political ideology": "P99",
    "list of works": "P100"
}

wiki_date_props = ["date of birth", "date of death"]