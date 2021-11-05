from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
Path = "D:\Coders_club\Python_\Selenium\Driver\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_elements_by_xpath("//*[@id='search-2']/form/label/input")
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()


