import requests
#from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# defining url 
start_url  = "https://www.instagram.com/cristiano/"

# path for chrome webdrive
driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")

# search string


search_field = str(input("what user you looking for?!! \n"))
# fire (target url)

driver.get(start_url)

# associate the search with instagram search 

user_search  = driver.find_element_by_class_name('x3qfX')
user_search.send_keys(search_field)
user_search.send_keys(u'\ue007')

# getting users posts

all_posts = []

def get







