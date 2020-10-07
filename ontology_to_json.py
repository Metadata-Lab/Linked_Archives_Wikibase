'''
ontology_to_json.py
Author: Kate Polley
Last Modified: 10-04-2020

take data exported from Protege and convert to JSON
each JSON object will correspond to one entity to import to Wikibase
'''

import json
import config as cfg
from get_wiki_data import search_for_q, get_statements

'''
import ontology export, sort each line into appropriate category
category identifiers based on config.py
'''
def import_data():
    data = open("data/all_owl.txt", "r")

    # sort entries in file using configuration settings
    for line in data:
        #get rid of extra pipe at end of line, split into list
        line = line[:-1]
        entry = line.split('|')

        #look at iri to determine category
        entity = entry[0]

        #so here's this really weird case
        if "/person/Eisenmann Charles" in entity:
            cfg.subjects.append(entry)
            continue

        for key in cfg.iri_keys:
            if key in entity:
                cfg.iri_keys[key].append(entry)

'''
strip extra quotation marks around strings
@param str: the string to strip
@returns string without quotation marks
'''
def strip_quotes(str):
    new = str.strip("\"").strip("\'").strip("*")
    return new

'''
for strings containing multiple values
split the string into individual values
@param str: string with multiple values
@returns values as list
'''
def parse_values(str):
    v = strip_quotes(str)
    list = v.split('\t')
    for idx, value in enumerate(list):
        list[idx] = strip_quotes(value)
    return list

'''
create the proper label for the entity (edited for people)
@param dict: the item dictionary
@returns the label string
'''
def get_label(dict):

    #if it is a person (has name), reformat label to first, middle, last
    if "firstname" in dict.keys():
        label = dict["firstname"][0]
        if len(dict["firstname"][0]) == 1:
            label += "."
        if "middleinitial" in dict.keys():
            label += " " + dict["middleinitial"][0]
            if len(dict["middleinitial"][0]) == 1:
                label += "."
        if "lastname" in dict.keys():
            label += " " + dict["lastname"][0]
        label = label.replace("  ", " ").replace("Unknown", "").strip()

        if len(label) == 0:
            label = "Unknown"

    #keep the orginal label for non-person entities
    else:
        if "label" in dict.keys():
            label = dict["label"][0]
        else:
            iri = dict.get("IRI")[0]
            label = iri[ iri.rfind('/')+1: ]

    return label

'''
parse each entity into a python dictionary to save as json
@param dict: master dictionary of all items
@param list: list of all items to be parsed
@returns dictionary populated with all entity dictionaries
'''
def parse_entities(dict, list):
    for item in list:
        i_dict = {}

        #add all properties from ontology
        for idx, val in enumerate(item):

            #ignore value if
            if val == '': continue

            if idx in cfg.multi_val_prop:
                i_dict[cfg.property_keys[idx]] = parse_values(val)
            else:
                i_dict[cfg.property_keys[idx]] = [strip_quotes(val)]

        label = get_label(i_dict)
        print(label)

        #SEARCH WIKIDATA, ADD Q NUM TO DICT IF EXISTS
        q = search_for_q(label)
        if q is not None:
            i_dict["Q"] = q
            #ADD WIKIDATA PROPERTIES TO DICTIONARY
            i_dict["wiki"] = get_statements(i_dict["Q"])

        #put together multiple entries with same label
        if label in dict.keys():
            for idx, prop in enumerate(cfg.property_keys):
                if prop not in dict[label].keys(): continue
                if idx in cfg.multi_val_prop:
                    for val in dict[label][prop]:
                        if val not in i_dict[prop]:
                            i_dict[prop].append(val)
                else:
                    if i_dict[prop][0] not in dict[label][prop]:
                        for val in dict[label][prop]:
                            i_dict[prop].append(val)

        print(i_dict)

        #add new entry to dictionary
        dict[label] = i_dict

    return dict

def parse_category(config_var, outfile):
    dict = {}
    dict = parse_entities(dict, config_var)
    with open(outfile, 'w') as outfile:
        json.dump(dict, outfile)

def parse_all():
    import_data()
    parse_category(cfg.people, 'data/entities/people.json')
    parse_category(cfg.subjects, 'data/entities/subjects.json')
    parse_category(cfg.names, 'data/entities/names.json')
    parse_category(cfg.countries, 'data/entities/countries.json')
    parse_category(cfg.events, 'data/entities/events.json')
    parse_category(cfg.series, 'data/entities/series.json')
    parse_category(cfg.objects, 'data/entities/objects.json')
    parse_category(cfg.collections, 'data/entities/collections.json')
    parse_category(cfg.bib_series, 'data/entities/bib_series.json')
    parse_category(cfg.belfer, 'data/entities/belfer.json')
    parse_category(cfg.becker, 'data/entities/becker.json')
    parse_category(cfg.koppel, 'data/entities/koppel.json')