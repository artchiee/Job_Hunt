import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper
import time
from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re

# indeed url only for 'morocco' jobs
global start_url
start_url = "https://ma.indeed.com"

# Options to force the window's size
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1000,3000")

# path for my chrome(driver)
driver = webdriver.Chrome(
    "C:\\Users\\footb\\Downloads\\chromedriver", options=options)

# search string
job_title = str(
    input("what job type you looking for?!! :  " + "\n" + 'job : '))

# fire (target url)
driver.get(start_url)
time.sleep(6)

# Switching languages
fr_language = driver.find_element_by_xpath(
    '/html/body/div/div[4]/div[1]/bidi/p/a[1]')
en_language = driver.find_element_by_xpath(
    '/html/body/div/div[4]/div[1]/bidi/p/a[2]')
if fr_language:
    time.sleep(3)
    fr_link = fr_language.get_attribute('href')
    fr_link.click()
    time.sleep(3)
    en_link = en_language.get_attribute('href')
    en_link.click()
else:
    # fr_link = fr_language.get_attribute('href')
    # fr_link.click()
    en_link = en_language.get_attribute('href')
    en_link.click()

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


def sort_by():
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

            # Exclude digits whene returning titles = Locations
            new_string = ''.join(re.findall("[a-zA-Z]+", string))
            all_locations.append(new_string)

        print('urls found : ', all_links, '\n')  # optional delete later
        print('Location\'s Lists :', all_locations, '\n')

        # Convert first letter to Uppercase() if user typed it lower
        choice = input(str('Fetch results by location : \n'))
        convert_choice = (choice.title())
        if choice != convert_choice:
            location_pattern = re.compile(convert_choice)
            new_return = list(filter(location_pattern.match, all_locations))
            print('location after convertion is   : ', new_return)

            # return href that has input user(Location's name)
            href_pattern = re.compile('=' + convert_choice + '&jlid')
            # link match retrieved
            new_href = list(filter(href_pattern.search, all_links))
            if new_href:
                print('url match !!  : ', new_href, '\n')
                # Copy this link to (indeed) url section
                current_url = driver.current_url
                print('Current url running :  ', current_url, '\n')

                slice_current_url = re.search(
                    r'https://\w+\.\w+\.com/', current_url)  # /\w+\?\w*\=\w+&\w*\=
                # group() will omit -->  <re.Match object; span=(0, 21)
                if slice_current_url:
                    clean_url = slice_current_url.group()
                # new_url = list(filter(slice_current_url.search, current_url))

                # this will take form index(22)=emploi until the end
                print('current url after slicing is  : ', clean_url)
                for i in new_href:
                    slice_new_href = i[22::]
                    print('new href after slicing : ', slice_new_href, '\n')

                # Combine the Two nw urls
                final_url = clean_url + slice_new_href
                if final_url:
                    time.sleep(3)
                    driver.get(final_url)
                    time.sleep(6)
                    # Dissmiss The popup window if showed
                    action = ActionChains(driver)
                    popup_foreground = driver.find_element_by_xpath(
                        '//*[@id="popover-foreground"]')
                    action.move_to_element(popup_foreground).perform()
                    popup_dismiss = driver.find_element_by_xpath(
                        '//*[@id="popover-close-link"]')
                    action.move_to_element(popup_dismiss).perform()
                    popup_dismiss.click()

                    # Sorting by available Contract types
                    # Check first if sorting by job contract exists or not
                    top_level_tag = driver.find_element_by_id("JOB_TYPE_rbo")
                    if top_level_tag:
                        contract_types = []
                        try:
                            next_ul = top_level_tag.find_element_by_tag_name(
                                'ul')
                            for i in next_ul.find_elements_by_tag_name('li'):
                                link = i.find_element_by_tag_name('a')
                                get_titles = link.get_attribute('title')
                                contract_types.append(get_titles)
                            print('Found types : ', contract_types, '\n')
                            my_type = input(str('Enter sorting type : '))
                            convert = re.compile(my_type, re.I)
                            if my_type != convert:
                                _filter = list(
                                    filter(convert.search, contract_types))
                                print('Found : ', _filter)
                                # take full path for city + job + contract type
                            else:
                                print('Nothin Match')

                            #     titles_only = ''.join(
                            #         re.findall(r"[a-zA-Z]+", get_titles))
                            #     contract_types.append(titles_only)
                            # print('Avaialble contract types are : ',
                            #       contract_types, '\n')
                            # sorting_choice = input(
                            #     str('Fetch results by Contract : '))
                            # # Ignore case Sensetive/ins..
                            # exception = ('cdi', 'cdd')
                            # if sorting_choice in exception:
                            #     convert = sorting_choice.upper()
                            #     case_sen = re.compile(convert, flags=re.IGNORECASE)
                            #     matchobj = list(
                            #         filter(case_sen.search, titles_only))
                            #     print('Found : ', matchobj)
                            # else:
                            #     print('Nothing Found..')
                        except:
                            Exception()
                    else:
                        print('No Contract Types Available')

                else:
                    print('Invalid Url')
            else:
                print('Nothing Match Your title in hrefs list  !!')
        else:
            print('Your choice was correct : ', choice)

    except:
        Exception()


# call the two functions
enter_clear_location()
sort_by()
