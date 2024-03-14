from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.LookMeUp import expected_conditions as EC
import time

import selenium
print(selenium.__version__)
exit()

# path = "/home/wharmon/Documents/projects/chromedriver/chromedriver"
# driver = webdriver.Chrome(path)
service = Service(executable_path='path')
# service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://techwithtim.net")

print(driver.title)

search = driver.find_element_by_name("s")
search.clear()
search.send_keys("python")
search.send_keys(Keys.RETURN)
# print(driver.page_source)
# main = driver.find_element_by_id("main")
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
except:
    print("wait for 'main' failed: timeout")
    driver.quit()

# print main.text

articles = main.find_elements_by_tag_name("article")
for article in articles:
    header = article.find_element(
        by=By.CLASS_NAME,
        value="entry-summary",
    )
    print(header.text)

link = driver.find_element_by_link_text("Click here")
link.click()

same_driver_wait_code(
    EC.presence_of_element_located((By.LINK_TEXT, "Click here"))
)

time.sleep(5)

# driver.back()
# driver.forward()

time.sleep(5)

driver.close()  # just this tab
driver.quit()

