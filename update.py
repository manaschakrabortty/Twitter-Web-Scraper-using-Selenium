#little  change here
# # pip install selenium bs4
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service  # Import Service
# from bs4 import BeautifulSoup
# from time import sleep

# # List to store the tweets
# all = []

# # Function to parse page content and extract tweets
# def adder(page):
#     sap = BeautifulSoup(page, 'html.parser')
#     div_tags = sap.find_all('div', {'class': 'tweet-content media-body'})
#     for div_tag in div_tags:
#         text = div_tag.get_text(strip=True)
#         all.append(text)

# # Enter the keyword you need to search for
# keyword = "python"

# # Construct the URL
# url = f"https://nitter.net/search?f=tweets&q=%23{keyword}&since=&until=&near"

# # Specify the path to the Chrome driver executable
# driver_path = "C:\\WebDrivers\\chromedriver.exe"  # Replace with your actual ChromeDriver path

# # Set up the Chrome WebDriver using the Service object
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)

# # Open the Nitter search page
# driver.get(url)

# # Scroll and collect tweets
# for x in range(5):
#     sleep(1.5)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     page_source = driver.page_source
#     adder(page_source)
    
#     try:
#         # Find and click the "show more" button (if exists)
#         load_more_button = driver.find_element(By.CLASS_NAME, "show-more")
#         load_more_button.click()
#         sleep(2.5)
#     except:
#         # Break the loop if the button is not found or there are no more tweets
#         break

# # Close the WebDriver
# driver.quit()

# # Print the unique tweets
# print(list(set(all)))
