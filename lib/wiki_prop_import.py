from selenium import webdriver
from wikidataintegrator import wdi_core, wdi_login
import csv, json, config as cfg

from lib.json_read_edit import json_to_dict

#prep for wikibase connection
mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/api.php"
login_creds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)

'''
add properties from wikidata to wikibase using selenium to automatically fill in form
'''
def add_new_properties():
    #get the driver location on the remote desktop
    driver_location = "H:/"
    driver = webdriver.Firefox(driver_location)

    # the xpath for each of the form elements to be used
    label = '//*[@id="ooui-php-3"]'
    desc = '//*[@id="ooui-php-4"]'
    type = '//*[@id="ooui-2"]'
    submit = '/html/body/div[3]/div[3]/div[4]/div[4]/form/fieldset/div/div/div[6]/span/button'
    string = '/html/body/div[5]/div[2]/div[12]/span[3]'

    next_p = 24
    output = {}

    with open("data/wiki_properties/props_for_import.csv") as props_file:
        #raed in properties from import into csv file
        reader = csv.reader(props_file)
        for row in reader:
            #go to the form page
            driver.get('http://linkeddata.ischool.syr.edu/mediawiki/index.php/Special:NewProperty')

            #get the property label and description from the csv file
            prop_label = row[0]
            description = row[1]

            #record property ids
            output[prop_label] = next_p
            next_p += 1

            #type in property and description to form
            driver.find_element_by_xpath(label).send_keys(prop_label)
            driver.find_element_by_xpath(desc).send_keys(description)

            #use clicks to select property type as string
            driver.find_element_by_xpath(type).click()
            driver.find_element_by_xpath(string).click()

            #click submit
            driver.find_element_by_xpath(submit).click()

    #output property ids
    with open("data/wiki_props.json", "w") as json_file:
        json.dump(output, json_file)


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
    with open("data/q_ids.json") as qids:
        local_q = json.load(qids)

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
                q = "Q" + str(local_q.get(i))
                wbPage = wdi_core.WDItemEngine(wd_item_id=q, data=item_statements, mediawiki_api_url=mw_api_url)
                #pprint.pprint(wbPage.get_wd_json_representation())
                try:
                    wbPage.write(login_creds)
                except:
                    with open("data/results/wiki_prop_errors.txt", "w") as error_out:
                        error_out.write(i + "\n")
