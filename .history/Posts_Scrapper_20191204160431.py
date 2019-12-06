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
search_str = str(raw_input('type the target username the u want to look for :  '))

# fire (target url)
driver.get(start_url)

# associate the search with instagram search 

user_search  = driver.find_element_by_class_name('x3qfX')
user_search






