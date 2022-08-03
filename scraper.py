from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

#Selenium, on the other hand, is used
#famously used for automation testing,
#such as testing the functionality of a
#website (Login/Logout/etc.) but can
#be also used to interact with the page
#such as clicking a button, etc.
# Selenium opens up 
#the webpage in a browser.

#bs4 (BeautifulSoup) is a python
#module, which is famously used for
#parsing text as HTML and then
#performing actions in it, such as
#finding specific HTML tags with a
#particular class/id, or listing out all the
#li tags inside the ul tags.


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/nishantchinta/Downloads/Coding/c127/chromedriver.exe")
time.sleep(10)

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink", "planet-type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
planet_data = []
new_planet_data = []

def scrape():
    
    for i in range(0, 505):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "html.parser")

            #check the page number
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
            if current_page_num < i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
                
            elif current_page_num > i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
            
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

        
        
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
