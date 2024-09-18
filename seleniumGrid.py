from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.set_capability("browserName","safari")
chrome_options.set_capability("platformName","windows")




remote_url = "http://192.168.1.63:4444"
driver = webdriver.Remote(remote_url, options=chrome_options)
driver.get("https://www.credello.com/")