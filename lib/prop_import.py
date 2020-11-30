from selenium import webdriver
import csv, json

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
