import requests
#from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper

from selenium import webdrive


# defining url 
start_url  = "https://www.instagram.com/cristiano/"

# ignore chrome options 

driver = webdrive.chrome("C:\\Users\\nouamane\\Downloads\\chromedriver_win32")

driver.get(start_url)