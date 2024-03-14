from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)
now = datetime.now()
YYYYMMDD = now.strftime("%Y-%m-%d")    # maybe add hours, min, etc.

website = "https://google.com"

# path = "/home/wharmon/Documents/projects/chromedriver/chromedriver"
path = "../../../chromedriver/chromedriver"

# headless mode
options = Options()
options.headless = True

print("calling Service()")
service = Service(executable_path=path)
print("calling Chrome()")

# browser = webdriver.Chrome(executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe', service_args = ['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

driver = webdriver.Chrome(service=service, options=options)

print("calling get()")
driver.get(website)

print("calling find_element()")
xpath = '//div[@class="classname"]/text()'
containers = driver.find_elements(By="xpath", value=xpath)

for container in containers:
    t = container.find_element(By="xpath", value="./a/h2").text
    link = container.find_element(
        By="xpath",
        value="./a",
    ).get_attribute("href")
    # t = container.find_element(By="class", value="blue").text
    print(e)

df_data = pd.DataFrame({
    'title': ['x', 'y', 'z'],
    'subtitle': ['a', 'b', 'c'],
    'link': ['1', '2', '3'],
})

file_name = f'headline-{YYYYMMDD}.csv'
final_path = os.path.join(application_path, file_name)
df_data.to_csv(final_path)


print("calling sleep()")
time.sleep(1)

print("calling quit()")
driver.quit()

