# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:51:10 2023

@author: Admin
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


##Extracting Maximum Temperatures

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
website_url = 'https://www.imdpune.gov.in/cmpg/Griddata/Max_1_Bin.html'  # Replace with the actual URL of the website
driver.get(website_url)


dropdown_element = driver.find_element(By.XPATH, '//*[@id="maxtemp"]') #Xpath from inspect element
select = Select(dropdown_element)

start_year = 1951
end_year = 2022 #Vary according to the year
path =  'file_path'

for year in range(start_year, end_year + 1):
    select.select_by_value(str(year))
    download_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/input') #Xpath from inspect element
    download_button.click()
    time.sleep(5)  

driver.quit()


##Minimum Temperature


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
website_url = 'https://www.imdpune.gov.in/cmpg/Griddata/Min_1_Bin.html'  # Replace with the actual URL of the website
driver.get(website_url)

dropdown_element = driver.find_element(By.XPATH, '//*[@id="mintemp"]')
select = Select(dropdown_element)

start_year = 1951
end_year = 2022

for year in range(start_year, end_year + 1): 
    select.select_by_value(str(year))
    download_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/input')
    download_button.click()
    time.sleep(5)  

driver.quit()


##Following code renames the filenames as required for code.py

#Max Files
import os

folder_path = "path\max"  # Replace with the actual path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".GRD"):
        file_parts = filename.split("_")
        if len(file_parts) == 3 and file_parts[0] == "Maxtemp" and file_parts[1] == "MaxT":
            year = file_parts[2].split(".")[0]
            new_filename = year + ".GRD"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

#Min Files
folder_path = "path\min"  # Replace with the actual path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".GRD"):
        file_parts = filename.split("_")
        if len(file_parts) == 3 and file_parts[0] == "Mintemp" and file_parts[1] == "MinT":
            year = file_parts[2].split(".")[0]
            new_filename = year + ".GRD"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

