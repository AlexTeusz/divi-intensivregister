from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.divi.de/register/intensivregister/')

def extract(): 

    time.sleep(2)
    browser.find_element_by_xpath("//select[@id='list_limit']/option[text()='Alle']").click()
    time.sleep(1)

    clinicTable = browser.find_element_by_css_selector('tbody/tr')
    print(clinicTable)


if __name__ == "__main__":
    extract()