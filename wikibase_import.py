'''
import.py
author: Kate Polley
last updated: 10-04-2020

'''

from wikidataintegrator import wdi_core, wdi_login
import os, pprint, json
import config as cfg
from get_wiki_data import get_local_q

mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/w/api.php"
login_creds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)

def json_to_dict(file):
    data = json.load(file)
    return data

def wiki_prop_statements(wiki_dict):
    statements = []
    for prop in wiki_dict.keys():
        if prop in cfg.wiki_props_used:
            statements.append(prop) #ACTUALLY EXTRACT PROPERTY HERE
    return statements

def get_item_statements(i_dict):
    statements = []
    for prop in i_dict.keys():
        pid = cfg.property_ids.get(prop)
        object = cfg.property_keys.index(prop) in cfg.multi_val_prop
        if prop == "Q":
            continue
        elif prop == "wiki":
            states = wiki_prop_statements(i_dict.get(prop))
            for s in states:
                statements.append(s)
        else:
            for value in i_dict.get(prop):
                if object:
                    qid = get_local_q(value)
                    state = wdi_core.WDItemID(qid, prop_nr=pid)
                else:
                    state = wdi_core.WDString(value, prop_nr=pid)
                statements.append(state)

    return statements

def import_items(dict):

    for item in dict.keys():
        # turn the item dictionary into statements
        item_statements = get_item_statements(dict.get(item))

        # create the item
        wbPage = wdi_core.WDItemEngine(data=item_statements, mediawiki_api_url=mw_api_url)

        # set the label and description (empty descriptions for subjects)
        wbPage.set_label(item, lang="en")
        wbPage.set_description(dict.get(item).get("description"), lang="en")

        # print results as a sanity check
        pprint.pprint(wbPage.get_wd_json_representation())

        # write the changes to wikibase with login credentials
        wbPage.write(login_creds)


def import_all():

    pass