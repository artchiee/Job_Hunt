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

# path for chrome webdrive (change this path accordding to my pc)
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# search string
job_title = str(input("what job type you looking for?!! " + "\n"))

# ask --> if you want to specify location or not yet
location = str(
    input('Do you want to give location or proccede to see all ???' + '\n'))

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)

location_field = driver.find_element_by_xpath('//*[@id="text-input-where"]')
location_field.send_keys(location)

# performe the test here
if location == location_field:
    find_jobs_btn = driver.find_element_by_xpath(
        '//*[@id="whatWhere"]/div/div/form/div[3]/button')
    find_jobs_btn.click()

    # fire (target url)
    driver.get(start_url)

else:
    Exception()
