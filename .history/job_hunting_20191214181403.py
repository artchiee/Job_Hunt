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

l           ocation_input = ''


def enter_location():
    global location_field
    location_field = driver.find_element_by_xpath(
        '//*[@id="text-input-where"]')

    try:
        if location_field == '':
            location_input = str(
                'enter location or see all available jobs ' + '\n')
            answer_me = str(
                input('yes --> give location  ||| ' + 'no --> see all'))

            print(location_input + answer_me)

            # answer is yes
            if answer_me in ('y', 'yes', 'ye'):
                ur_location = str(input('Enter location'))
                location_field.send_keys(ur_location)
                location_field.send_keys(Keys.ENTER)

            # answer == no
            if answer_me in ('n', 'no', 'nope'):
                time.sleep(2)
                location_field.send_keys(Keys.ENTER)

        # if location_field wes filled (by default)
        else:
            location_field.send_keys(Keys.CONTROL + "a")
            location_field.send_keys(Keys.DELETE)
            time.sleep(2)
            location_field.send_keys(Keys.ENTER)

            # print('give location now :' + "   ")

            # Access 'Lieu --> location' xpath
            #all_locations = []
            for i in driver.find_element_by_xpath('//*[@id="rb_Location"]/div[1]/span'):
                     # div tag
                i.find_element_by_xpath('//*[@id="LOCATION_rbo"]')
                # ul tag
                element = i.find_element_by_xpath(
                    '//*[@id="LOCATION_rbo"]/ul')
                element.find_elements_by_tag_name('li')
                # locate a tag and it's hrefs
                for link in element.find_elements_by_tag_name('a'):
                    try:
                        casa = link.find_element_by_xpath(
                            '//*[@id="LOCATION_rbo"]/ul/li[1]/a')
                        enter = input('location : ')
                        if enter == casa:
                            casa.click()
                    except:
                        Exception()

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
