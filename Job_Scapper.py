from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  

import time 
import json
import os 


from web_driver_configs import (
    get_chrome_web_driver,
    get_web_driver_options,
    set_automation_as_head_less,
    set_ignore_certificate_error, 
    set_browser_as_incognito
)

options = get_web_driver_options()

# show browser when script is running 
#set_automation_as_head_less(options)

set_ignore_certificate_error(options)
set_browser_as_incognito(options)
driver = get_chrome_web_driver(options)


indeed_global_url = "https://www.indeed.com/worldwide"
driver.get(indeed_global_url)

# wait until element is loaded
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/table/tbody"))
    )
    print("table data element found , Resuming .. \n ")

except NoSuchElementException:
    print('element not found', Exception())


final_list = []
counter = 1
# save all location from table to .json file  
countries_file = "locations.json"

find_locations = driver.find_element_by_class_name('countries').find_elements_by_xpath('.//a')
# because we have two a tags, we need to checkc which one has title(.text) 
for a in find_locations:
    if a.text != "":
        # id is auto increment, and will be used instead of typing the locations title 
        final_list.append({"id" : counter, "title": a.text, "href": a.get_attribute('href')})
        counter += 1

# checking if location.json file is already exists
if not os.path.isfile(countries_file):
    print('.json file countries not found , creating it ... \n')
    with open(countries_file, 'w') as typing:
        json.dump(final_list, typing, indent=4)

else:
    print('.json file exists ... , Resuming \n')
    with open(countries_file, 'r') as r_file:
        read_dta = json.load(r_file)

# using input id to click on locations href
input_id = input('Please provide the input (id) from .json countries file exists in the project tree: ')
for check in read_dta:
    try:
        if check['id'] == int(input_id):
            location_link = check['href']
            title = check['title']
            print('redirecting to ' + title +' url ... \n ----------------------- ')
            driver.get(location_link)
    except ValueError:
        print('Input id must be existe in .json locations file')


try:
    search_fields = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[4]/div[1]"))
        )

    job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
    location_field = driver.find_element_by_xpath(
            '//*[@id="text-input-where"]')
except NoSuchElementException or TimeoutError:
    TimeoutError()


# check if both of these fields are already populated
if not job_field or location_field == "":
    location_field.send_keys(Keys.CONTROL + "a")
    location_field.send_keys(Keys.DELETE)
    job_field.send_keys(Keys.CONTROL + "a")
    job_field.send_keys(Keys.DELETE)

#print('both fields are Empty , Resuming ....')
input_city = input('Please provide city in which you want to search in :  ')
input_job = input('Please provide what job you\'re looking for  :  ')



location_field.send_keys(input_city)
job_field.send_keys(input_job)
location_field.send_keys(Keys.ENTER)

#Sorting (Last 7 days) # can be modified,but it's better to stick to latest search
try:
    date_posted = WebDriverWait(driver, 7).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="filter-dateposted"]'))
    )
    # last 7 days
    sort_by_latest = date_posted.find_element_by_xpath('.//li[3]/a').get_attribute('href')
    driver.get(sort_by_latest)
    time.sleep(6)
    popup_foreground = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,'//*[@id="popover-x"]'))
        ).click()

except NoSuchElementException:
    print('element not found')


pagination_available = driver.find_element_by_xpath('//*[@id="resultsCol"]/nav')
try:
    if pagination_available:
        print('pagination exists, Resuming Scrapping Jobs \n --------------')
        #pages_list = pagination_available.find_element_by_xpath('../div/ul').find_elements_by_tag_name('li[2]')
        # for page_num in pages_list:    
        #     click_next_url = page_num.find_element_by_tag_name('a').get_attribute('href').click()
    else:
        print('No pages available, Saving Jobs ...  ')

except:
    Exception()


NUMBER_OF_PAGES_TO_SEARCH = 60 #change this if you want to go over more pages

start_string = '&start='
base_url = driver.current_url
page = 10
# main information about the job 
job_title = ""
job_link = ""
company_name = ""
rating = ""
date_posted = ""
where = ""

final_job_list = []

# preventing start_string from insearting each time
should_add_start_string = True

while True:
    if page != 0 :
        try:
            driver.get(base_url + start_string + str(page))
                #FIXME : decremented number getting added beside the previous one                
        except:
            Exception()
        
        time.sleep(7)
        job_cards = driver.find_elements_by_xpath("//div[contains(@class,'clickcard')]")     
        for card in job_cards:
            job_title = card.find_element_by_xpath('.//h2[@class="title"]//a').text
            job_link = card.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute('href')
            
            # need to check if span has a nested  
            try:
                check_span = card.find_element_by_xpath('.//span[@class="company"]//a')
                if check_span:
                    company_name = check_span.text
                else:
                    company_name = card.find_element_by_xpath('.//span[@class="company"]').text
            except:
                Exception()

            # a few jobs may not have rating 
            try:
                rating = card.find_element_by_xpath('.//span[@class="ratingsContent"]').text
            except:
                rating = "rating not avialable"
            
            where = card.find_element_by_xpath('.//span[contains(@class, "location")]').text
            date_posted = card.find_element_by_xpath('.//div[@class="result-link-bar"]//span').text

            final_job_list.append(
                {
                'job_title' : job_title,
                'url' : job_link,
                'company_name' : company_name,
                'job_review': rating,
                'date_posted' : date_posted,
                'where' : where
            })

            saved_jobs_file = "saved_jobs.json"
            with open(saved_jobs_file, 'w') as w:
                json.dump(final_job_list, w, indent=4)
            
            
    page = page  + 10
    if page == NUMBER_OF_PAGES_TO_SEARCH:
        break

    print(page)

