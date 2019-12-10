import requests
from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# defining url
global start_url

# indeed url only for 'morocco' jobs
start_url = "https://ma.indeed.com"

# path for chrome webdrive (change this path accordding to your pc)
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# search string
job_title = str(input("what job type you looking for?!! " + "\n"))

# fire (target url)
driver.get(start_url)

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)


location_field = ''


def clear_location_field(location_field):
    location_field = driver.find_element_by_xpath(
        '//*[@id="text-input-where"]')

    answer_me = str(input(' Yes --> give location' + '\n' + 'No --> See all' + '\n'))

    # VAlidate if location filed empty or not
    if location_field == '':
        location_input = str(input
            ("Do you want to give location or proccede to see all available jobs  ???" + "\n"))
        location_field.send_keys(location_input)
        location_field.send_keys(Keys.ENTER)

    else:
        location_field.send_keys(Keys.CONTROL + "a")
        location_field.send_keys(Keys.DELETE)
        time.sleep(3)

        # after deleting promte me to this string again
       
        print(location_input + '\n' + answer_me)

        if answer_me == 'yes':
            name = str(input('Enter location'))
            location_field.send_keys(name)
            location_field.send_keys(Keys.ENTER)
        else:
            time.sleep(2)
            location_field.send_keys(Keys.ENTER)


clear_location_field(location_field)
