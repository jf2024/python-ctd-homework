# task3 here

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import csv

driver = webdriver.Chrome()
driver.maximize_window()

website = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver.get(website)

li_elements = driver.find_elements(By.CSS_SELECTOR, "li[class='row cp-search-result-item']")

results = []
for entry in li_elements:
    
    # title here
    title_element = entry.find_element(By.CLASS_NAME, 'title-content')
    title_text = title_element.text  # This extracts the actual text!

    # author
    author_elements = entry.find_elements(By.CLASS_NAME, 'author-link')
    author_names = [author.text for author in author_elements] 

    ## taking care of the multiple author case
    if len(author_names) == 0: 
        string_author = 'N/A'
    else:
        string_author = "; ".join(author_names)

    
    # format and year
    format_year_elem = entry.find_element(By.CLASS_NAME, 'display-info-primary')
    format_txt = format_year_elem.text


    book_dict = {
        'Title': title_text,
        'Author': string_author,
        'Format-Year': format_txt
    }
    
    results.append(book_dict)

df = pd.DataFrame(results)
print(df)

driver.quit()

#task4 starts here
df.to_csv('get_books.csv', index=False)
df.to_json('get_books.json', orient='records', indent=4)