import requests
from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# defining url 
global start_url
start_url  = "https://www.instagram.com/cristiano/"

# path for chrome webdrive
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# search string


search_field = str(input("what user you looking for?!! "+ "\n"))
# fire (target url)

driver.get(start_url)

# associate the search with instagram search 

user_search  = driver.find_element_by_class_name('x3qfX')
user_search.send_keys(search_field)

# befor hitting enter pause for 3
time.sleep(3)
user_search.send_keys(Keys.ENTER)w	
#pause for anothe 2s
time.sleep(2)
user_search.send_keys(Keys.ENTER)
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









