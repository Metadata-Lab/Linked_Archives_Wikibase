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

def import_batch(dicts, types, start_q, batch_file, missed_statements_file, missed_objects_file):
    with open(batch_file, "w") as q_out:
        for idx, dict in enumerate(dicts):
            start_q = import_items(dict, types[idx], start_q)
        json.dump(local_q, q_out)

    with open(missed_statements_file, "w") as add:
        for statement in not_added:
            str = ""
            for value in statement:
                str += value + ","
            add.write(str + "\n")

    with open(missed_objects_file, "w") as error_out:
        for item in import_error:
            error_out.write(item + "\n")


def import_first_batch():
    subjects = json_to_dict("data/entities/subjects.json")
    countries = json_to_dict("data/entities/countries.json")
    events = json_to_dict("data/entities/events.json")
    names = json_to_dict("data/entities/names.json")
    bib_series = json_to_dict("data/entities/bib_series.json")

    dicts = [subjects, countries, events, names, bib_series]
    types = ["subject", "country", "event", "name", "bib_series"]

    curr_q = 11
    import_batch(dicts, types, curr_q, "data/q_batch_one.json", "data/to_add.txt", "data/error_items.txt")


def import_second_batch():
    import_local_q("data/q_batch_one.json")

    #collections = json_to_dict("data/entities/collections.json") -- ADD MANUALLY
    series = json_to_dict("data/entities/series.json")
    objects = json_to_dict("data/entities/objects.json")


    dicts = [series, objects]
    types = ["series", "object"]

    curr_q = 299
    import_batch(dicts, types, curr_q, "data/q_batch_two.json", "data/to_add_2.txt", "data/error_items_2.txt")


def import_third_batch():
    import_local_q("data/q_batch_two.json")

    belfer = json_to_dict("data/entities/belfer.json")
    becker = json_to_dict("data/entities/becker.json")
    koppel = json_to_dict("data/entities/koppel.json")
    people = json_to_dict("data/entities/people.json")

    dicts = [belfer, becker, koppel, people]
    types = ["item", "item", "item", "person"]

    curr_q = 289
    import_batch(dicts, types, curr_q, "data/q_batch_three.json", "data/to_add_3.txt", "data/error_items_3.txt")


def import_people():
    import_local_q("data/q_batch_two.json")
    people = json_to_dict("data/entities/people.json")
    dicts = [people]
    types = ["person"]
    curr_q = 10110
    import_batch(dicts, types, curr_q, "data/q_batch_people.json", "data/to_add_p.txt", "data/error_items_p.txt")