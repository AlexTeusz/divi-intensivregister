from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.divi.de/register/intensivregister/')

def extract(): 

    # create the intiial CSV file and write the header row
    with open('divi_clinic_list.csv', 'w', encoding='utf-8') as defaultFile:
        csv.writer(defaultFile).writerow([
            'title',
            'contact',
            'state',
            'icuLowCare',
            'icuHighCare',
            'ecmo',
            'date',
            'time'
        ])

    # select 'Alle' to see all clinics in the list
    time.sleep(1)
    browser.find_element_by_xpath("//select[@id='list_limit']/option[text()='Alle']").click()

    # get HTML from website
    html = browser.page_source
    soup = BeautifulSoup(html)

    # get the clinic table
    time.sleep(2)
    clinicTable = soup.find_all('table')[0].tbody
   
   # get each row from the table and extract the information
    for tr in clinicTable.find_all('tr'):
        title = tr.find_all('td')[0].contents[0].strip()
        contact = tr.find_all('td')[1].contents[0].strip()
        state = tr.find_all('td')[2].contents[0].strip()
        icuLowCare = getICULevel(tr.find_all('td')[3].contents[1].get('class')[0])
        icuHighCare = getICULevel(tr.find_all('td')[4].contents[1].get('class')[0])
        ecmo = getICULevel(tr.find_all('td')[5].contents[1].get('class')[0])
        date = tr.find_all('td')[6].contents[0].strip()
        dateTime = tr.find_all('td')[6].contents[2].strip()

        # for each clinic, store the information in the CSV file
        with open('divi_clinic_list.csv', 'a', encoding='utf-8') as f:
            csv.writer(f).writerow([
                title,
                contact,
                state,
                icuLowCare,
                icuHighCare,
                ecmo,
                date,
                dateTime
            ])


def getICULevel(icuClassName: str):
    """
    Get the icu / ecmo level from divi html class name.
    Legend:
        1 -> green
        2 -> yellow
        3 -> red
    """

    if icuClassName == 'hr-icon-green':
        return 1
    elif icuClassName == 'hr-icon-yellow':
        return 2
    elif icuClassName == 'hr-icon-red':
        return 3

 
if __name__ == "__main__":
    extract()