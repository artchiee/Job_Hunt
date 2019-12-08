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

# fire (target url)
driver.get(start_url)

# associate the search with indeed search

job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)

# inside LOcation field (delete location if it was already insertead by default)
location_field = driver.find_element_by_xpath(
    '//*[@id="text-input-where"]').clear()

# befor hitting enter pause for 2
time.sleep(2)
job_field.send_keys(Keys.ENTER)


# getting users posts

# all_posts == []

# def Scrapp_posts(post_link):
# 	# locate tag with number of followers
# 	soup = BeautifulSoup(start_url, 'html.parser')
# 	data = soup.text
# 	find_attribute = data.find_all('meta', attrs={'property': 'og:description'})
# 	followers = find_attribute[0]

# 	#giving spesific number to small profiles
# 	#small_profile = 100
# 	# mediocre_profile = 500
# 	# viral_profile = 1000

# 	find_posts  = driver.find_element_by_class_name('v1Nh3')
# 	find_posts.find_element_by_css_selector('a').get_attribute('href')

# 	driver = webdrive.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")
