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
not_added = []
import_error = []

def json_to_dict(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data

def import_local_q():
    with open("data/q_batch_one.json") as json_file:
        data = json.load(json_file)
        local_q = data


def get_local_q(label):
    return local_q.get(label)

def get_item_statements(i_dict, type):
    statements = [wdi_core.WDItemID(cfg.object_ids.get(type), prop_nr="P1")]
    for prop in i_dict.keys():
        if prop in ["Q", "wiki", "label"]:
            continue
        else:
            pid = cfg.property_ids.get(prop)
            object = cfg.property_keys.index(prop) in cfg.object_prop
            for value in i_dict.get(prop):
                if object:
                    qid = get_local_q(value)
                    if qid is None:
                        not_added.append([i_dict.get("label")[0], pid, value])
                        continue
                    state = wdi_core.WDItemID(qid, prop_nr=pid)
                else:
                    state = wdi_core.WDString(value, prop_nr=pid)
                statements.append(state)

    return statements

def import_items(dict, type, curr_q):

    q = curr_q

    for item in dict.keys():
        # turn the item dictionary into statements
        item_statements = get_item_statements(dict.get(item), type)

        # create the item
        wbPage = wdi_core.WDItemEngine(data=item_statements, mediawiki_api_url=mw_api_url)

        # set the label and description (empty descriptions for subjects)
        wbPage.set_label(item, lang="en")

        desc = dict.get(item).get("description")
        if desc is not None:
            if len(desc) > 250: wbPage.set_description(desc[:245] + '...', lang="en")
            wbPage.set_description(desc, lang="en")
        else:
            wbPage.set_description("", lang="en")

        local_q[item] = q
        q += 1

        # print results as a sanity check
        pprint.pprint(wbPage.get_wd_json_representation())

        # write the changes to wikibase with login credentials
        try:
            wbPage.write(login_creds)
        except Exception as e:
            import_error.append(item)
            print(e)

    return q

def import_first_batch():
    subjects = json_to_dict("data/entities/subjects.json")
    countries = json_to_dict("data/entities/countries.json")
    events = json_to_dict("data/entities/events.json")
    names = json_to_dict("data/entities/names.json")
    bib_series = json_to_dict("data/entities/bib_series.json")

    dicts = [subjects, countries, events, names, bib_series]
    types = ["subject", "country", "event", "name", "bib_series"]

    curr_q = 11
    with open("data/q_batch_one.json", "w") as q_out:
        for idx, dict in enumerate(dicts):
            curr_q = import_items(dict, types[idx], curr_q)
        json.dump(local_q, q_out)

    with open("data/to_add.txt", "w") as add:
        for statement in not_added:
            str = ""
            for value in statement:
                str += value + ","
            add.write(str + "\n")

    with open("data/error_items.json", "w") as error_out:
        for item in import_error:
            error_out.write(item + "\n")

def import_second_batch():
    import_local_q()

    collections = json_to_dict("data/entities/collections.json")
    series = json_to_dict("data/entities/countries.json")
    objects = json_to_dict("data/entities/objects.json")
    belfer = json_to_dict("data/entities/belfer.json")
    becker = json_to_dict("data/entities/becker.json")
    koppel = json_to_dict("data/entities/koppel.json")
    people = json_to_dict("data/entities/people.json")

    dicts = [collections, series, objects, belfer, becker, koppel, people]
    types = ["collection", "series", "object", "item", "item", "item", "person"]

    curr_q = 289
    with open("data/q_batch_two.json", "w") as q_out:
        for idx, dict in enumerate(dicts):
            curr_q = import_items(dict, types[idx], curr_q)
        json.dump(local_q, q_out)

    with open("data/to_add_2.txt", "w") as add:
        for statement in not_added:
            str = ""
            for value in statement:
                str += value + ","
            add.write(str + "\n")

    with open("data/error_items_2.json", "w") as error_out:
        for item in import_error:
            error_out.write(item + "\n")