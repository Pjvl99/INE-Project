from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import time



class INE:

    def __init__(self) -> None:
        self.start_chromedriver()
        self.get_headers()


    def start_chromedriver(self):
        chrome_options = Options()
        download_dir = os.path.dirname(os.path.realpath(__file__))
        prefs = {'download.default_directory' : download_dir}
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
        self.driver.get("https://datos.ine.gob.gt/dataset")
    
    def get_headers(self) -> None:
        headers = WebDriverWait(self.driver, 60).until(lambda header: header.find_elements(By.CSS_SELECTOR, '.dataset-heading > a'))
        print(len(headers))



def main():
    INE()

main()

