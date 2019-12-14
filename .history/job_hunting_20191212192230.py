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
start_url = "https://indeed.com"

# path for chrome webdrive (change this path accordding to your pc)
driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")

# search string
job_title = str(input("what job type you looking for?!! " + "\n"))

# fire (target url)
driver.get(start_url)

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)

# test here 
location_field = driver.find_element_by_xpath('//*[@id="text-input-where"]')
location_field.send_keys(Keys.CONTROL + "a")
location_field.send_keys(Keys.DELETE)

def enter_location(location_field):

    location_field = driver.find_element_by_xpath('//*[@id="text-input-where"]')
    try:
        if location_field == '':
            location_input = str(
                input('enter location or see all available jobs ' + '\n'))
            answer_me = str(
                input('yes --> give location  ||| ' + 'no --> see all'))
            
            print(location_input  +  answer_me)

            #answer is yes
            if answer_me == 'yes':
                enter_location = str(input('Enter location'))
                location_field.send_keys(enter_location)
                location_field.send_keys(Keys.ENTER)

            # answer == no
            else:
                time.sleep(2)
                location_field.send_keys(Keys.ENTER)

        # if location_field wes filled call the function bellow()
        else:
            clear_location_field()

    except:
        Exception()

# clear location_field if it was filled (by defalute)

def clear_location_field():
    location_field = driver.find_element_by_xpath(
        '//*[@id="text-input-where"]')

    location_field.send_keys(Keys.CONTROL + "a")
    location_field.send_keys(Keys.DELETE)
    location_field.send_keys(Keys.ENTER)



# call the two functions
enter_location(location_field)
