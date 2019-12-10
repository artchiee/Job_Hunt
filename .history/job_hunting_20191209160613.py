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

# ask --> if you want to specify location or not yet


location_field = '' 


def clear_location_field(location_field):
    location_name = []
    location_field = driver.find_element_by_xpath(
        '//*[@id="text-input-where"]')
    
    # get text / value of that field
    location_field.text 


    # test if location_field is filled 
    if len(location_field) > 0:
        location_name.append(location_field)
        # delete input field insearted by default
        del location_name
        # location_field.send_keys(Keys.CONTROL + "a")
        # location_field.send_keys(Keys.DELETE)

    else:
        location = str(input("Do you want to give location or proccede to see all available jobs  ???" + "\n"))
        location_field.send_keys(location)
        location_field.send_keys(Keys.ENTER)

clear_location_field(location_field)
