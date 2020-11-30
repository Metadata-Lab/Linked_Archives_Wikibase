from wikidataintegrator import wdi_core, wdi_login
import json, pprint
import config as cfg

from lib.json_read import json_to_dict

#prep for wikibase connection
mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/api.php"
login_creds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)

#collect identifiers and errors
local_q = {}
props_missed = []
items_missed = []

'''
imports previously exported q identifiers by label
@param batch_file name of file with the q ids
side effect: local_q is updated with q values
'''
def import_local_q(batch_file):
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
    if type is not None: statements = [wdi_core.WDItemID(cfg.object_ids.get(type), prop_nr="P1")]
    else: statements = []

    for prop in i_dict.keys():
        #ignore the wikidata q value and label
        #wikidata property statements will be imported later
        if prop in ["Q", "wiki", "label"]:
            continue
        elif prop == "is_related_to" and i_dict.get("label")[0] == "Koppel Ted":
            continue #this weird case that causes internal server error
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
                    if len(value) > 400: value = value[:395] + "..."
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
side effect - items are written to wikibase
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

        if "description" in dict.get(item).keys():
            desc = dict.get(item).get("description")[0]
            if len(desc) > 250: wbPage.set_description(desc[:245] + '...', lang="en")
            else: wbPage.set_description(desc, lang="en")
        else:
            wbPage.set_description("", lang="en")

        #track q ids
        if local_q.get(item):
            with open("data/results/disambiguate.txt", "w") as dis:
                dis.write(item + "\n")
        local_q[item] = q
        q += 1

        # print results as a sanity check
        #pprint.pprint(wbPage.get_wd_json_representation())

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
    q = start_q
    #import items from each dictionary
    with open(batch_file, "w") as q_out:
        for idx, dict in enumerate(dicts):
            print(types[idx])
            q = import_items(dict, types[idx], q)
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

    return q

'''
import first batch of entities - everything except people and collection items
@returns the q id to start at with next import 
'''
def import_main():
    subjects = json_to_dict("data/entities/subjects_edited.json")
    countries = json_to_dict("data/entities/countries_edited.json")
    events = json_to_dict("data/entities/events_edited.json")
    names = json_to_dict("data/entities/names_edited.json")
    bib_series = json_to_dict("data/entities/bib_series_edited.json")
    collections = json_to_dict("data/entities/collections_edited.json")
    series = json_to_dict("data/entities/series_edited.json")
    objects = json_to_dict("data/entities/objects_edited.json")


    dicts = [subjects, countries, events, names, bib_series, collections, series, objects]
    types = ["subject", "country", "event", "name", "bib_series", "collection", "series", "object"]

    curr_q = 11 #after manual import of base properties and items
    return import_batch(dicts, types, curr_q, "data/q_ids.json",
                 "data/results/prop_import_errors.txt", "data/results/entity_import_errors.txt")

'''
import people to wikibase
@param next_q q id where import starts
@returns q id to start next import
'''
def import_people(next_q):
    import_local_q("data/q_ids.json")
    people = json_to_dict("data/entities/people_edited.json")
    return import_batch([people], ["person"], next_q, "data/q_ids.json",
                        "data/results/prop_import_errors_people.txt", "data/results/entity_import_errors_people.txt")

def import_collections(next_q):
    #generate file paths, import q ids
    files = ['becker', 'belfer', 'koppel']
    for idx, val in enumerate(files): files[idx] = 'data/entities/' + val + '.json'
    import_local_q("data/q_ids.json")
    errors = {}

    #loop through all three collections
    for file in files:
        collection = json_to_dict(file)

        #loop through each item in the collection
        for item in collection.keys():
            #get item statements
            states = get_item_statements(collection.get(item), None)
            #get the id of the item if it exists
            id = get_local_q(item)
            q = "Q" + str(id)

            if id is None:
                #if the item was not imported as an object, create a new item to import
                wbPage = wdi_core.WDItemEngine(data=states, mediawiki_api_url=mw_api_url)
                local_q[item] = next_q
                next_q += 1
                wbPage.set_label(item, lang="en")
            else:
                #if item exists, retrieve from wikibase
                wbPage = wdi_core.WDItemEngine(wd_item_id=q, data=states, mediawiki_api_url=mw_api_url)

            #set item description so it is not longer than the 250 character limit
            desc = collection.get(item).get("description")[0]
            if desc is not None:
                if len(desc) > 250: wbPage.set_description(desc[:245] + '...', lang="en")
                else: wbPage.set_description(desc, lang="en")
            else:
                wbPage.set_description("", lang="en")

            #pprint.pprint(wbPage.get_wd_json_representation())

            #write to wiki or record error
            try:
                wbPage.write(login_creds)
            except Exception as e:
                errors[item] = e

    #output ids and errors to files
    with open("data/results/collection_import_errors.json", "w") as error_out:
        json.dump(errors, error_out)
    with open ("data/q_ids.json", "w") as outfile:
        json.dump(local_q, outfile)

'''
get the item statements that came from wikidata
@param wiki_dict the dictionary of wikidata properties that was part of the item dictionary
@returns item statements to be written to wikibase
'''
def extract_wiki_statements(wiki_dict):
    statements = []
    #import the property ids
    prop_ids = json_to_dict("data/wiki_props.json")
    for prop in wiki_dict.keys():
        # take only the properties that we have decided to import
        if prop in prop_ids.keys(): # or prop is "instance of": - instance of not handled because of type conflict
            for value in wiki_dict.get(prop)[1].keys():
                #if the value is a date, get rid of the junk time data at the end
                if prop in cfg.wiki_date_props:
                    end = value.find("T")
                    value = value[:end]
                state = wdi_core.WDString(value, prop_nr=prop_ids.get(prop))
                statements.append(state)
    return statements

'''
add statements taken from wikidata to item pages
'''
def add_wikidata_statements():
    #import q ids to add statements to proper itesm
    import_local_q("data/q_ids.json")

    #generate file paths
    batch = ['people', 'bib_series', 'collections', 'countries', 'events', 'names', 'objects', 'series', 'subjects']
    for idx, val in enumerate(batch): batch[idx] = 'data/entities/' + val + '_edited.json'

    for file in batch:
        items = json_to_dict(file)
        for i in items.keys():
            #get the dictionary of wiki properties
            if "wiki" in items.get(i).keys():
                item_statements = extract_wiki_statements(items.get(i).get("wiki"))
                #get the q id for import
                q = "Q" + str(get_local_q(i))
                wbPage = wdi_core.WDItemEngine(wd_item_id=q, data=item_statements, mediawiki_api_url=mw_api_url)
                #pprint.pprint(wbPage.get_wd_json_representation())
                try:
                    wbPage.write(login_creds)
                except:
                    with open("data/results/wiki_prop_errors.txt", "w") as error_out:
                        error_out.write(i + "\n")




