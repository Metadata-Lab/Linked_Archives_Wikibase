from wikidataintegrator import wdi_core, wdi_login
import pprint

def main():
    mw_api_url = "http://linkeddata.ischool.syr.edu/mediawiki/api.php"
    # login_creds = wdi_login.WDLogin(user='Admin', pwd="metadata!master", mediawiki_api_url=mw_api_url)

    item_statements = [wdi_core.WDItemID("Q6", prop_nr="P1"), wdi_core.WDString("Test", prop_nr="P20"), wdi_core.WDString("Test Again", prop_nr="P20")]

    # create the item
    wbPage = wdi_core.WDItemEngine(data=item_statements, mediawiki_api_url=mw_api_url)

    # set the label and description (empty descriptions for subjects)
    wbPage.set_label('Test', lang="en")
    wbPage.set_description("Description Test", lang="en")

    # print results as a sanity check
    pprint.pprint(wbPage.get_wd_json_representation())

    # write the changes to wikibase with login credentials
    # wbPage.write(login_creds)


if __name__ == '__main__':
    main()