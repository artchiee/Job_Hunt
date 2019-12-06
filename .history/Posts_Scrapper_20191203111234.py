import requests
#from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper

from selenium import webdriver
from bs4 import BeautifulSoup

# defining url 
start_url  = "https://www.instagram.com/cristiano/"

# ignore chrome options 

driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")

driver.get(start_url)