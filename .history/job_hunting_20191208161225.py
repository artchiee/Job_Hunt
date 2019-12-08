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

location_field = driver.find_element_by_xpath('//*[@id="text-input-where"]')

# def clear_location_field(self, location_filed):
#     location_field = driver.find_element_by_xpath(
#         '//*[@id="text-input-where"]')

#         # see if the form is filled by default 
#     if location_field == 'Agadir':
#         #location_field.send_keys(location)
#         location_field.send_keys(Keys.CLEAR)
#         location_field.send_keys(Keys.ENTER)

# # call the def 

#     clear_location_field(location_field)

