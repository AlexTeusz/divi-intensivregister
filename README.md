# DIVI Intensivregister

This program extracts the clinic information of the [DIVI Intensivregister](https://www.divi.de/register/intensivregister?view=items) and stores it into a CSV file. 

**Legend: ICU / ECMO:**

- 1 (green)
- 2 (yellow)
- 3 (red)

## Run program

1. `pip install -r requirements.txt`
2. `python extract.py`

## Selenium Chromedriver

The program uses [Selenium](https://selenium-python.readthedocs.io/) to visit the webpage and select 'All' to see all clinics. If the program isn't running, it could be the case that you have to download another version of the chrome driver:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
