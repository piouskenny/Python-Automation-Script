from selenium import webdriver
from bs4 import BeautifulSoup
import re

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Optional: Run Chrome in headless mode

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

url = 'https://piouskenny.netlify.app/'
driver.get(url)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

word_to_count = 'businesses'
word_count = len(re.findall(r'\b{}\b'.format(word_to_count), soup.get_text(strip=True), flags=re.IGNORECASE))

print(f"The word '{word_to_count}' is used {word_count} times on the webpage.")

