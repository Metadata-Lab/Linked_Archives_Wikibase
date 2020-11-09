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
global wiki_props
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
}

wiki_props = {
    'sex or gender':'P24',
    'occupation':'P25',
    'date of birth':'P26',
    'country of citizenship':'P27',
    'place of birth':'P28',
    'educated at':'P29',
    'languages spoken; written or signed':'P30',
    'date of death':'P31',
    'award received':'P32',
    'place of death':'P33',
    'political party':'P34',
    'employer':'P35',
    'name in native language':'P36',
    'position held':'P37',
    'cause of death':'P38',
    'sport':'P39',
    'spouse':'P40',
    'religion':'P41',
    'manner of death':'P42',
    'member of':'P43',
    'work location':'P44',
    'child':'P45',
    'member of sports team':'P46',
    'birth name':'P47',
    'ethnic group':'P48',
    'place of burial':'P49',
    'residence':'P50',
    'military branch':'P51',
    'instrument':'P52',
    'position played on team / speciality':'P53',
    'father':'P54',
    'genre':'P55',
    'conflict':'P56',
    'number of children':'P57',
    'country for sport':'P58',
    'field of work':'P59',
    'sibling':'P60',
    'nominated for':'P61',
    'height':'P62',
    'mother':'P63',
    'writing language':'P64',
    'mass':'P65',
    'participant in':'P66',
    'record label':'P67',
    'military rank':'P68',
    'notable work':'P69',
    'native language':'P70',
    'candidacy in election':'P71',
    'medical condition':'P72',
    'copyright status as a creator':'P73',
    'academic degree':'P74',
    'significant event':'P75',
    'pseudonym':'P76',
    'voice type':'P77',
    'student of':'P78',
    'league':'P79',
    'convicted of':'P80',
    'has works in the collection':'P81',
    'unmarried partner':'P82',
    'copyright representative':'P83',
    'relative':'P84',
    'movement':'P85',
    'influenced by':'P86',
    'nickname':'P87',
    'doctoral advisor':'P88',
    'owner of':'P89',
    'drafted by':'P90',
    'student':'P91',
    'honorific prefix':'P92',
    'allegiance':'P93',
    'handedness':'P94',
    'place of detention':'P95',
    'doctoral student':'P96',
    'has written for':'P97',
    'eye color':'P98',
    'sports discipline competed in':'P99',
    'name in kana':'P100',
    'hair color':'P101',
    'net worth':'P102',
    'time in space':'P103',
    'astronaut mission':'P104',
    'floruit':'P105',
    'political ideology':'P106',
    'sexual orientation':'P107',
    'affiliation':'P108',
    'blood type':'P109',
    'consecrator':'P110',
    'noble title':'P111',
    'lifestyle':'P112',
    'sport number':'P113',
    'victory':'P114',
    'religious order':'P115',
    'partner in business or sport':'P116',
    'represented by':'P117',
    'killed by':'P118',
    'second family name in Spanish name':'P119',
    'honorific suffix':'P120',
    'professorship':'P121',
    'named after':'P122',
    'coach of sports team':'P123',
    'head coach':'P124',
    'significant person':'P125',
    'generational suffix':'P126',
    'amateur radio callsign':'P127',
    'preferred pronoun':'P128',
    'ancestral home':'P129',

    'instance of': 'P130',
    'subclass of': 'P131',
    'described by source': 'P132',
    'inception': 'P133',
    'practiced by': 'P134',
    'anthem': 'P135',
    'area': 'P136',
    'capital': 'P137',
    'continent': 'P138',
    'country': 'P139',
    'currency': 'P140',
    'executive body': 'P141',
    'head of government': 'P142',
    'health specialty': 'P143',
    'language used': 'P144',
    'legislative body': 'P145',
    'located in time zone': 'P146',
    'native label': 'P147',
    'nominal GDP per capita': 'P148',
    'office held by head of government': 'P149',
    'official language': 'P150',
    'population': 'P151',
    'short name': 'P152',
    'country of origin': 'P153',
    'head of state': 'P154',
    'highest judicial authority': 'P155',
    'office held by head of state': 'P156',
    'official name': 'P157',
    'shares border with': 'P158',
    'basic form of government': 'P159',
    'culture': 'P160',
    'diplomatic relation': 'P161',
    'Human Development Index': 'P162',
    'located on terrain feature': 'P163',
    'motto text': 'P164',
    'patron saint': 'P165',
    'replaces': 'P166'
}





















wiki_date_props = ["date of birth", "date of death", "inception"]