from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

driver =Chrome()
teamDropDown = (By.ID, "teamDropDown")

indiaTeam = (By.LINK_TEXT, 'India')
stats = (By.LINK_TEXT, 'Stats')
avgArray = (By.XPATH,"//div[@id='teamStatsTable']//td[5]")
playerName = (By.XPATH, "//div[@id='teamStatsTable']//a")

driver.get("https://www.cricbuzz.com/")
driver.maximize_window()
driver.implicitly_wait(2)
element= driver.find_element(*teamDropDown)
actionchain = ActionChains(driver)
actionchain.move_to_element(element).perform()
element = driver.find_element(*indiaTeam)
element.click()
element = driver.find_element(*stats)
element.click()

playerElement = driver.find_elements(*playerName)
avgArray = driver.find_elements(*avgArray)
dct={}
for i in range(len(avgArray)):
    dct[playerElement[i].text] = avgArray[i].text
print(dct)










