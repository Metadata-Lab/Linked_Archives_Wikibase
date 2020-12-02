from wikidataintegrator import wdi_core, wdi_login
from lib.wikibase_import import extract_wiki_statements
from lib.json_read_edit import json_to_dict

#prep for wikibase connection
mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/api.php"
login_creds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)


'''
STEP 4-1
if Ted Koppel related statements still import and cause error, use this function to redo that item
replace related to with only related to collection (not all items in collection)
and add the wikidata statements
'''
def fix_koppel():

    #get the ted koppel data
    file = "data/entities/people_edited.json"
    people = json_to_dict(file)
    koppel_dict = people.get("Ted Koppel")
    wiki_dict = koppel_dict.get("wiki")

    #reate item statements
    base_statement = wdi_core.WDItemID("Q290", prop_nr="P5")
    wiki_statements = extract_wiki_statements(wiki_dict)
    wiki_statements.append(base_statement)

    # create the item
    wbPage = wdi_core.WDItemEngine(wd_item_id="Q10123", data=wiki_statements, mediawiki_api_url=mw_api_url)

    # write the changes to wikibase with login credentials
    try:
        wbPage.write(login_creds)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    fix_koppel()