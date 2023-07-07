#imports

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import time
import os
import wrangle as wra

#variables
user = os.getenv("githubUSER")
pswd = os.getenv("githubPSWD")
base_url = "https://github.com/"             

#functions

def open_selenium_session(url):
    user = os.getenv("githubUSER")
    pswd = os.getenv("githubPSWD")
    base_url = url

    # Create a webdriver object
    driver = webdriver.Chrome(service=Service())

    # Let's open up a website!
    driver.get(base_url + "login")
    
    # Wait for the program to continue running
    while True:
        time.sleep(1)
        
def dl_database_files(base_url, user, pswd, repo_name):    
    '''
    '''
    # Login
    # Enter username
    driver.find_element(By.NAME, "login").send_keys(user)
    
    # Enter password
    driver.find_element(By.NAME, "password").send_keys(pswd)
    
    # Locate and click the sign in button
    driver.find_element(By.NAME, "commit").click()
    
    # Navigate to repo
    # navigate to database-exercises repo
    driver.get(base_url+user+"/"+ repo_name)
    
    # Download sql file
    # Locate and click the sign in button
    driver.find_elements(By.XPATH, '''//a[@class="js-navigation-open Link--primary"]''')[1].click()
    
    # download the file
    driver.find_elements(By.XPATH, "//button[@data-component='IconButton']")[5].click()
    
