# pip install selenium bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from time import sleep
all=[]
def adder(page):
    sap = BeautifulSoup(page, 'html.parser')
    div_tags = sap.find_all('div', {'class': 'tweet-content media-body'})
    for div_tag in div_tags:
        text = div_tag.get_text(strip=True)
        all.append(text)

# ---------------
# enter the keyword you need to search for
keyword = "python"
# ---------------

url = "https://nitter.net/search?f=tweets&q=%23"+ keyword +"&since=&until=&near"

# download chrome webdriver from   "https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.41/"
# Specify the path to the Chrome driver executable
driver_path = " " # put in the path with "\\" seperated directories

# Create a new Chrome browser instance
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

# -----------------------
for x in range(5):
    sleep(1.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page_source = driver.page_source 
    adder(page_source)
    try:
        load_more_button = driver.find_element(By.CLASS_NAME, "show-more")
        load_more_button.click()
        sleep(2.5)
    except:
        break
# -----------------------
driver.quit()

# pinting the list of the elements 
print(list(set(all)))  

