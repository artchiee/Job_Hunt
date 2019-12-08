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
driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")

# search string 
job_title = str(input("what job type you looking for?!! " + "\n"))

# fire (target url) 
driver.get(start_url)

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)

# ask --> if you want to specify location or not yet
# location = str(
#     input("Do you want to give location or proccede to see all available jobs  ???" + "\n"))


def clear_location_field():
    location_field = driver.find_element_by_xpath('//*[@id="text-input-where"]')

    # delete input field insearted by default 
    location_field.send_keys(Keys.CONTROL + "a")
    location_field.send_keys(Keys.DELETE)

    location_field.send_keys(Keys.ENTER)

    clear_location_field()


