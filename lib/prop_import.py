from selenium import webdriver
import csv, json

def add_new_properties():
    #driver_location = "H:/"
    #driver = webdriver.Firefox(driver_location)

    label = '//*[@id="ooui-php-3"]'
    desc = '//*[@id="ooui-php-4"]'
    type = '//*[@id="ooui-2"]'
    submit = '/html/body/div[3]/div[3]/div[4]/div[4]/form/fieldset/div/div/div[6]/span/button'
    string = '/html/body/div[5]/div[2]/div[12]/span[3]'

    next_q = 24
    output = {}

    with open("data/wiki_properties/props_for_import.csv") as props_file:
        reader = csv.reader(props_file)
        for row in reader:
            #driver.get('http://linkeddata.ischool.syr.edu/mediawiki/index.php/Special:NewProperty')

            prop_label = row[0]
            description = row[1]

            output[prop_label] = next_q
            next_q += 1

            # driver.find_element_by_xpath(label).send_keys(prop_label)
            # driver.find_element_by_xpath(desc).send_keys(description)
            #
            # driver.find_element_by_xpath(type).click()
            # driver.find_element_by_xpath(string).click()
            #
            # driver.find_element_by_xpath(submit).click()

    with open("data/wiki_props.json", "w") as json_file:
        json.dump(output, json_file)
