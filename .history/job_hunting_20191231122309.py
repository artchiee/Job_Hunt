import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper
import time
from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.common.keys import Keys

# defining url
global start_url

# path for my B.PC
driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")

# indeed url only for 'moroco' jobs
start_url = "https://indeed.com"

# search string
job_title = str(
    input("what job type you looking for?!! :  " + "\n" + 'job : '))

# fire (target url)
driver.get(start_url)

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)

global location_input
global location_field
location_field = ''
location_input = ''


def enter_clear_location():
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

        # if location_field was filled (by default)
        else:
            location_field.send_keys(Keys.CONTROL + "a")
            location_field.send_keys(Keys.DELETE)
            time.sleep(2)
            location_field.send_keys(Keys.ENTER)

    except:
        Exception()


def select_location():
    span_tag = driver.find_element_by_xpath(
        '//*[@id="rb_Location"]/div[1]/span')
    # div tag
    span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]')
    # ul tag
    element = span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]/ul')
    # li tag
    lists = element.find_elements_by_tag_name('li')
    print('all Urls available :  \n ')

    # Printing all lists of hrefs / all locations
    all_links = []
    all_locations = []
    try:
        for items in lists:
            # a tag / # Get locations name
            a_tag = items.find_element_by_tag_name('a')
            link = a_tag.get_attribute('href')
            string = a_tag.get_attribute('title')
            all_links.append(link)
            all_locations.append(string)
        print('urls found : ', all_links, '\n')

        # test here 
        print(len(all_locations))
        print(all_locations.index(4))
        # print('Location\'s\ Lists :' ,  ','.join(all_locations), '\n')

        #test print index from list 


        # matching user input with titles stored in a list
        # try:
        #     #Focusing on the element first aka point the Cursor
        #    # driver.find_element_by_tag_name('body').click()
        #     choice = input(str('Fethc results by Locatoins : \n'))
        #     location_field.send_keys(Keys.NULL)
        #     time.sleep(2)
        #     location_field.send_keys(choice)
        #     location_field.send_keys(Keys.ENTER)
        # except KeyboardInterrupt:
        #     print('Interrupted')
  
    except:
        Exception()


# call the two functions
enter_clear_location()
select_location()
