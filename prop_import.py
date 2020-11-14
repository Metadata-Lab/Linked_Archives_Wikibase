from selenium import webdriver



def main():
    driver_location = '/home/klpolley/geckodriver'
    driver = webdriver.Firefox(driver_location)
    driver.get('linkeddata.ischool.syr.edu/mediawiki/index.php/Special:NewProperty')

    label = '//*[@id="ooui-php-3"]'
    desc = '//*[@id="ooui-php-4"]'
    type = '//*[@id="ooui-2"]'
    submit = '/html/body/div[3]/div[3]/div[4]/div[4]/form/fieldset/div/div/div[6]/span/button'

    string = '/html/body/div[5]/div[2]/div[12]/span[3]'
    item = '/html/body/div[5]/div[2]/div[7]/span[3]'

    prop_label = "test property"
    description = "this is a selenium test"

    driver.find_element_by_xpath(label).send_keys(prop_label)
    driver.find_element_by_xpath(desc).send_keys(description)

    driver.find_element_by_xpath(string).click()

    driver.find_element_by_xpath(submit).click()


if __name__ == '__main__':
    main()