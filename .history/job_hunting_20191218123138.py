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

enter = ''


def enter_clear_location():
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

    except:
        Exception()

# Move on to the secont page


locations_lists = []

def select_location():
    span_tag = driver.find_element_by_xpath(
        '//*[@id="rb_Location"]/div[1]/span')
    # div tag
    span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]')
    # ul tag
    element = span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]/ul')
    lists = element.find_elements_by_tag_name('li')
    for items in lists:
        a_tag = items.find_element_by_xpath('//*[@id="LOCATION_rbo"]/ul/li[1]/a')
        string = a_tag.get_attribute('title')
        print(string)


    #locations_lists = element.find_elements_by_tag_name('li')
    # locate a tag and it's hrefs
    # for link in locations_lists.find_elements_by_tag_name('a'):
    # links = locations_lists.find_elements_by_tag_name('a')
    # try:
    #          # this list of [l1, l2 /] etc , are location's name aka cities
    #     l1 = link.find_element_by_xpath(
    #                 '//*[@id="LOCATION_rbo"]/ul/li[1]/a')
    #     l2 = link.find_element_by_xpath(
    #                 '//*[@id="LOCATION_rbo"]/ul/li[2]/a')
    #     l3 = link.find_element_by_xpath(
    #                 '//*[@id="LOCATION_rbo"]/ul/li[3]/a')
    #     l4 = link.find_element_by_xpath(
    #                 '//*[@id="LOCATION_rbo"]/ul/li[4]/a')
    #     l5 = link.find_element_by_xpath(
    #                 '//*[@id="LOCATION_rbo"]/ul/li[5]/a')
    #     6 = link.find_element_by_xpath(
    #                 '//*[@id="LOCATION_rbo"]/ul/li[6]/a')
    #             # Get locations name
    #     for item in links:
    #         text = item.text
    #         print(', '.join(text))

    #         enter = input('location : ')
    #         if enter == 'casa ':
    #             casa.click()
    #             time.sleep(3)
    #         # in casee of a popup aka alert windows (Dismissed it)
    #         # Switch to the popup windows & locate it's xpath
    #             popup = driver.find_element_by_xpath('//*[@id="popover-close-link"]')
    #             popup.click()
    #             else:
    #                 break

    # except:
    #     Exception()


# call the two functions
enter_clear_location()
select_location()
