from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import time

chrome_options = Options()
download_dir = os.path.dirname(os.path.realpath(__file__))
prefs = {'download.default_directory' : download_dir}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
driver.get("https://datos.ine.gob.gt/dataset")
time.sleep(10)