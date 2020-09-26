'''
ontology_to_json.py
Author: Kate Polley
Last Modified: 09/25/2020

take data exported from Protege and convert to JSON
each JSON object will correspond to one entity to import to Wikibase
'''

import pywikibot
import json
import config as cfg

'''
import ontology export, sort each line into appropriate category
category identifiers based on config.py
'''
def import_data():
    data = open("all_owl.txt", "r")

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
        label = dict["label"]

    return label

'''
find the wikidata q identifier if a page with the label exists
@param label: the label of the page to search for
@returns label string if page exists, None if it doesn't
'''
def search_wikidata(label):
    site = pywikibot.Site("en", "wikipedia")

    try:
        #search wikibase for item with label
        page = pywikibot.Page(site, label)
        item = pywikibot.ItemPage.fromPage(page)

        #if found, do some magic to turn item into proper string
        magic = {}
        magic["Q"] = str(item)
        q = magic["Q"]
        #make sure we only get the Q### part
        magic["Q"] = q[11:-2]
        return magic["Q"]

    except Exception as e:
        return None

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

        #SEARCH WIKIDATA, ADD Q NUM TO DICT IF EXISTS
        q = search_wikidata(label)
        if q is not None:
            i_dict["Q"] = q

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

        #add new entry to dictionary
        dict[label] = i_dict

    return dict

def parse_people():
    people_dict = {}
    people_dict = parse_entities(people_dict, cfg.people)
    with open('people.json', 'w') as outfile:
        json.dump(people_dict, outfile)

def main():
    import_data()
    parse_people()

if __name__ == '__main__':
    main()