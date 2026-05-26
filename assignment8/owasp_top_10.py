from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import csv

driver = webdriver.Chrome()
driver.maximize_window()

website = 'https://owasp.org/Top10/2025/'
driver.get(website)

li_elements = driver.find_elements(By.XPATH, "//ol/li")
top_10_list = []

for vulns in li_elements:

    link_element = vulns.find_element(By.TAG_NAME, 'a')
    
    title_text = link_element.text  
    href_link = link_element.get_attribute('href')

    vuln_dict = {
        'Title': title_text,
        'Link': href_link
    }

    top_10_list.append(vuln_dict)

print(top_10_list)

df = pd.DataFrame(top_10_list)

df.to_csv('owasp_top_10.csv', index=False)

driver.quit()