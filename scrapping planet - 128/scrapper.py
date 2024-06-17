from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd 
from selinium.webdriver.support.ui import WebDriverWait
from selinium.webdriver.support import exprcted_conditions as EC
import requests

start_url = 'https://science.nasa.gov/exoplanets/exoplanet-catalog/'
page = bs.find_all('tr')
stars_data = []

brouser = webdriver.Edge()
brouser.get(start_url)
time.sleep(2)

planet_data = []
def method_scrap():
    for i in range (0, 10):
        print(f"scrapping page {i + 1}")
        soupe= BeautifulSoup(brouser.page_source, 'html.parser')
        for planet in soupe.find_all('div', class_='hds-content-item'):
            planet_info=[]
            
            planet_info.append(planet.find('h3', class_='heading-22'.text.strip()))
            info_to_extract = ['name', 'Mass', 'radius', 'Distance']
            for info_name in info_to_extract:
                try:
                    planet_info.append(planet.select_one(f'span:- soup-contains("{info_name}")').find_next_sibling('span').text.strip())
                except:
                    planet_info.append('unknown')
            planet_data.append(planet_info)
        print(planet_data)
    stars_data.append(info_to_extract)
    stars_data = pd.DataFrame()
    stars_data.to_csv('scrapping.csv')
    