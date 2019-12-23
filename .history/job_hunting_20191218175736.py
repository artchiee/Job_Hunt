import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4
from Scrapp_info import Info_Scrapper
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


# defining url
global start_url

# indeed url only for 'morocco' jobs
start_url = "https://indeed.com"
# define a soup obj
soup = bs4.BeautifulSoup(urlopen(start_url), 'html.parser')

# path for my B.PC
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# search string
job_title = str(
    input("what job type you looking for?!! :  " + "\n" + 'job : '))

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


# Move on to the secont pa
locations_lists = []


def select_location():
    span_tag = driver.find_element_by_xpath(
        '//*[@id="rb_Location"]/div[1]/span')
    # div tag
    span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]')
    # ul tag
    element = span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]/ul')
    # li tag
    lists = element.find_elements_by_tag_name('li')
    print('\n' + 'Locations Available  are : ' + '\n')
    try:
        for items in lists:
            # a tag / # Get locations name
            a_tag = items.find_element_by_tag_name('a')
            string = a_tag.get_attribute('title')
            print('' + ''.join(string))
    except:
        raise ValueError('No Available Locations')

    # this list of [l1, l2 /] etc , are location's name aka cities/hrefs
    # l1 = lists.find_element_by_xpath(
    #     '//*[@id="LOCATION_rbo"]/ul/li[1]/a')
    # l2 = lists.find_element_by_xpath(
    #     '//*[@id="LOCATION_rbo"]/ul/li[2]/a')
    # l3 = lists.find_element_by_xpath(
    #     '//*[@id="LOCATION_rbo"]/ul/li[3]/a')
    # l4 = lists.find_element_by_xpath(
    #     '//*[@id="LOCATION_rbo"]/ul/li[4]/a')
    # l5 = lists.find_element_by_xpath(
    #     '//*[@id="LOCATION_rbo"]/ul/li[5]/a')
    # l6 = lists.find_element_by_xpath(
    #     '//*[@id="LOCATION_rbo"]/ul/li[6]/a')

    # using the beautifulsoup to scrap all hrefs
    for links in soup.find('div', {'id' : 'LOCATION_rbo'}).findAll('a')
            print link['href']

    # enter = input('Location : ')
    # try:
    #     if enter in ('aga', 'agadir'):
    #         l5.click()
    # except:
    #     pass


# call the two functions
enter_clear_location()
select_location()
