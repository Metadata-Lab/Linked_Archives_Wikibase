'''
import.py
author: Kate Polley
last updated: 10-23-2020

import ontology items (from json) into wikibase
'''

from wikidataintegrator import wdi_core, wdi_login
import os, pprint, json
import config as cfg

#prep for wikibase connection
mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/api.php"
login_creds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)

#collect identifiers and errors
local_q = {}
props_missed = []
items_missed = []

'''
import json file into dictionary
@param file file name to import
@returns dictionary of all data
'''
def json_to_dict(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data
'''
imports previously exported q identifiers by label
@param batch_file name of file with the q ids
side effect: local_q is updated with q values
'''
def import_local_q(batch_file):
    collections = {
        "Ronald G. Becker collection of Charles Eisenmann photographs": 296,
        "Ted Koppel Collection": 297,
        "Belfer Cylinders Collection": 298
    }
    local_q.update(collections)
    with open(batch_file) as batch:
        data = json.load(batch)
        local_q.update(data)

'''
retrieve the q identifier for the label
@param label the item label
@returns the q identifier from the local wikibase
'''
def get_local_q(label):
    return local_q.get(label)

'''
extract statements from item dictionary, formatted for wikibase import
@param i_dict item dictionary with all properties
@param type the type of item being imported (for instance of prop)
'''
def get_item_statements(i_dict, type):
    statements = [wdi_core.WDItemID(cfg.object_ids.get(type), prop_nr="P1")]
    for prop in i_dict.keys():
        #ignore the wikidata q value and label
        #wikidata property statements will be imported later
        if prop in ["Q", "wiki", "label"]:
            continue
        else:
            #get the information about the property
            pid = cfg.property_ids.get(prop)
            object = cfg.property_keys.index(prop) in cfg.object_prop
            #make statements for each value of the property
            for value in i_dict.get(prop):
                if object:
                    #get the q identifier of the object if applicable
                    qid = get_local_q(value)
                    if qid is None:
                        props_missed.append([i_dict.get("label")[0], pid, value])
                        continue
                    state = wdi_core.WDItemID(qid, prop_nr=pid)
                else:
                    state = wdi_core.WDString(value, prop_nr=pid)
                #add statement to the list
                statements.append(state)
    return statements

'''
import all items from a dictionary into wikibase
@param dict dictionary of items
@param type type of object being imported
@param curr_q q value of next import
@returns next q value to import
side effect - itmes are written to wikibase
'''
def import_items(dict, type, curr_q):
    q = curr_q
    for item in dict.keys():
        # turn the item dictionary into statements
        item_statements = get_item_statements(dict.get(item), type)

        # create the item
        wbPage = wdi_core.WDItemEngine(data=item_statements, mediawiki_api_url=mw_api_url)

        # set the label and description (empty descriptions for subjects)
        wbPage.set_label(item, lang="en")

        #description needs to be less than 250 characters
        desc = dict.get(item).get("description")
        if desc is not None:
            if len(desc) > 250: wbPage.set_description(desc[:245] + '...', lang="en")
            wbPage.set_description(desc, lang="en")
        else:
            wbPage.set_description("", lang="en")

        #track q ids
        local_q[item] = q
        q += 1

        # print results as a sanity check
        pprint.pprint(wbPage.get_wd_json_representation())

        # write the changes to wikibase with login credentials
        try:
            wbPage.write(login_creds)
        except Exception as e:
            #log items that don't get written to wikibase
            items_missed.append(item)
            print(e)
    return q

'''
import a batch of dictionaries to wikibase, log results
@param dicts list of dictionaries in order to be imported
@param types types of items in dictionaries listed above, in order
@param start_q the q id for the first item to be imported
@param batch_file file to export q ids of all imported items
@param missed_statements_file to export statements not imported
@param missed_objects_file to export items not imported
side effect - items in dictionaries imported to wikibase (excluding errors)
'''
def import_batch(dicts, types, start_q, batch_file, missed_statements_file, missed_objects_file):
    #import items from each dictionary
    with open(batch_file, "w") as q_out:
        for idx, dict in enumerate(dicts):
            start_q = import_items(dict, types[idx], start_q)
        json.dump(local_q, q_out)

    #print out statements that weren't imported - object not found
    with open(missed_statements_file, "w") as add:
        for statement in props_missed:
            str = ""
            for value in statement:
                str += value + ","
            add.write(str + "\n")

    #print out labels of items not imported - error on writing
    with open(missed_objects_file, "w") as error_out:
        for item in items_missed:
            error_out.write(item + "\n")

'''
import subjects, countries, events, names, and bib_series to wikibase
requires ontology properties and classes manually added to wikibase
'''
def import_first_batch():
    subjects = json_to_dict("data/entities/subjects.json")
    countries = json_to_dict("data/entities/countries.json")
    events = json_to_dict("data/entities/events.json")
    names = json_to_dict("data/entities/names.json")
    bib_series = json_to_dict("data/entities/bib_series.json")

    dicts = [subjects, countries, events, names, bib_series]
    types = ["subject", "country", "event", "name", "bib_series"]

    curr_q = 11
    import_batch(dicts, types, curr_q, "data/q_batch_one.json",
                 "data/results/error_props_1.txt", "data/results/error_items_1.txt")

'''
add series and objects (collection items without statements - to be added later)
requires collections being imported manually to wikibase
'''
def import_second_batch():
    import_local_q("data/q_batch_one.json")

    #collections = json_to_dict("data/entities/collections.json") -- ADD MANUALLY
    series = json_to_dict("data/entities/series.json")
    objects = json_to_dict("data/entities/objects.json")


    dicts = [series, objects]
    types = ["series", "object"]

    curr_q = 299
    import_batch(dicts, types, curr_q, "data/q_batch_two.json",
                 "data/results/error_props_2.txt", "data/results/error_items_2.txt")

'''
import people to wikibase, after batch two
'''
def import_people():
    import_local_q("data/q_batch_two.json")
    people = json_to_dict("data/entities/people.json")
    dicts = [people]
    types = ["person"]
    curr_q = 10110
    import_batch(dicts, types, curr_q, "data/q_batch_people.json",
                 "data/results/error_props_p.txt", "data/results/error_items_p.txt")


def extract_wiki_statements(wiki_dict):
    statements = []
    for prop in wiki_dict.keys():
        if prop in cfg.property_ids.keys():
            for value in wiki_dict.get(prop)[1].keys():
                state = wdi_core.WDString(value, prop_nr=cfg.property_ids.get(prop))
                statements.append(state)
    return statements

'''
add props from wikidata into the wikibase
'''
def import_wikidata_props():
    import_local_q("data/q_batch_people.json")
    people = json_to_dict("data/entities/people.json")

    for person in people.keys():
        print(person)
        if "wiki" in people.get(person).keys():
            item_statements = extract_wiki_statements(people.get(person).get("wiki"))
            q = "Q" + str(get_local_q(person))
            wbPage = wdi_core.WDItemEngine(wd_item_id=q, data=item_statements, mediawiki_api_url=mw_api_url)
            pprint.pprint(wbPage.get_wd_json_representation())
            wbPage.write(login_creds)
