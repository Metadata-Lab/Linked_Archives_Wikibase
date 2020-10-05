'''
import.py
author: Kate Polley
last updated: 10-04-2020

'''

from wikidataintegrator import wdi_core, wdi_login
import os, pprint, json

mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/w/api.php"
logincreds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)

def json_to_dict(file):
    data = json.load(file)
    return data

def get_local_q(label):
    return None

def import_items(dict):

    for item in dict.keys():
        # statements format - need to get actual p values for properties, q values for object items
        item_statements = [wdi_core.WDString(dict.get(item).get("iri"), prop_nr="P1"), wdi_core.WDItemID("Q11", prop_nr="P13")]

        # create the item
        wbPage = wdi_core.WDItemEngine(data=item_statements, mediawiki_api_url=mw_api_url)

        # set the label and description (empty descriptions for subjects)
        wbPage.set_label(item, lang="en")
        wbPage.set_description(dict.get(item).get("description"), lang="en")

        # print results as a sanity check
        pprint.pprint(wbPage.get_wd_json_representation())

        # write the changes to wikibase with login credentials
        wbPage.write(logincreds)

def import_people():
    pass

def import_all():
    pass