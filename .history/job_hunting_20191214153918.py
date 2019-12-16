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

# path for my B.PC
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# search string
job_title = str(input("what job type you looking for?!! :  " + "\n"))

# fire (target url)
driver.get(start_url)

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)


global location_input

location_input = ''


def enter_location():
    location_field = driver.find_element_by_xpath(
        '//*[@id="text-input-where"]')
    global location_field

    try:
        if location_field == '':
            location_input = str(
                'enter location or see all available jobs ' + '\n')
            answer_me = str(
                input('yes --> give location  ||| ' + 'no --> see all'))

            print(location_input + answer_me)

            #answer is yes
            if answer_me == 'yes':
                ur_location = str(input('Enter location'))
                location_field.send_keys(ur_location)
                location_field.send_keys(Keys.ENTER)

            # answer == no
            else:
                time.sleep(2)
                location_field.send_keys(Keys.ENTER)

        # if location_field wes filled (by default)
        else:
            location_field.send_keys(Keys.CONTROL + "a")
            location_field.send_keys(Keys.DELETE)
            location_field.send_keys(Keys.ENTER)
            time.sleep(3)

            #print('give location now :' + "   ")
            give_location = input('Enter Location : ')
            location_field.send_keys(give_location)
            location_field.send_keys(Keys.ENTER)

    except:
        Exception()


# clear location_field if it was filled (by defalute)

# def clear_location_field():
#     location_field = driver.find_element_by_xpath(
#         '//*[@id="text-input-where"]')

#     location_field.send_keys(Keys.CONTROL + "a")
#     location_field.send_keys(Keys.DELETE)
#     location_field.send_keys(Keys.ENTER)


# Move on to the secont page


# call the two functions
enter_location()
