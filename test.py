from wikidataintegrator import wdi_core, wdi_login
import pprint

def main():
    mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/api.php"
    login_creds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)

    item_statements = [wdi_core.WDString("Test", prop_nr="P2")]

    # create the item
    wbPage = wdi_core.WDItemEngine(wd_item_id="Q1", data=item_statements, mediawiki_api_url=mw_api_url)
   
    # print results as a sanity check
    pprint.pprint(wbPage.get_wd_json_representation())

    # write the changes to wikibase with login credentials
    wbPage.write(login_creds)


if __name__ == '__main__':
    main()