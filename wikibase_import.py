'''
import.py
author: Kate Polley
last updated: 10-11-2020

'''

from wikidataintegrator import wdi_core, wdi_login
import os, pprint, json
import config as cfg

mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/api.php"
login_creds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)

local_q = {}

def json_to_dict(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data

def wiki_prop_statements(wiki_dict):
    statements = []
    for prop in wiki_dict.keys():
        if wiki_dict.get(prop)[0] in cfg.wiki_props_used:
            statements.append(prop) #ACTUALLY EXTRACT PROPERTY HERE
    return statements

def get_local_q(label):
    return local_q.get(label)

def get_item_statements(i_dict, type):
    statements = [wdi_core.WDItemID(cfg.object_ids.get(type), prop_nr="P1")]
    for prop in i_dict.keys():
        if prop in ["Q", "wiki", "label"]:
            continue
        else:
            pid = cfg.property_ids.get(prop)
            object = cfg.property_keys.index(prop) in cfg.multi_val_prop
            for value in i_dict.get(prop):
                if object:
                    qid = get_local_q(value)
                    state = wdi_core.WDItemID(qid, prop_nr=pid)
                else:
                    state = wdi_core.WDString(value, prop_nr=pid)
                statements.append(state)

    return statements

def import_items(dict, q_out, type):

    for item in dict.keys():
        # turn the item dictionary into statements
        item_statements = get_item_statements(dict.get(item), type)

        # create the item
        wbPage = wdi_core.WDItemEngine(data=item_statements, mediawiki_api_url=mw_api_url)

        # set the label and description (empty descriptions for subjects)
        wbPage.set_label(item, lang="en")
        wbPage.set_description(dict.get(item).get("description"), lang="en")

        local_q[item] = wbPage.wd_item_id

        # print results as a sanity check
        pprint.pprint(wbPage.get_wd_json_representation())

        # write the changes to wikibase with login credentials
        # wbPage.write(login_creds)


def import_all():
    subjects = json_to_dict("data/entities/subjects.json")
    countries = json_to_dict("data/entities/countries.json")
    events = json_to_dict("data/entities/events.json")
    names = json_to_dict("data/entities/names.json")
    bib_series = json_to_dict("data/entities/bib_series.json")
    collections = json_to_dict("data/entities/collections.json")
    series = json_to_dict("data/entities/countries.json")
    objects = json_to_dict("data/entities/objects.json")
    belfer = json_to_dict("data/entities/belfer.json")
    becker = json_to_dict("data/entities/becker.json")
    koppel = json_to_dict("data/entities/koppel.json")
    people = json_to_dict("data/entities/people.json")

    dicts = [subjects, countries, events, names, bib_series, collections,
             series, objects, belfer, becker, koppel, people]

    types = ["subject", "country", "event", "name", "bib_series", "collection",
             "series", "object", "item", "item", "item", "person"]

    with open("q_ids.json", "w") as q_out:
        for idx, dict in enumerate(dicts):
            import_items(dict, q_out, types[idx])
        json.dump(local_q, q_out)