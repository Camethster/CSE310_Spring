# %%
import seaborn
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# %%
DRIVER_PATH = 'C:\git\Portfolio\Smite\pullPro\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.smiteproleague.com/matches/4190')

# %%
#<a href="/scores">Scores</a>
'''scores = driver.find_element_by_xpath("//a[@href='/scores']").click()

time.sleep(5)
game =  driver.find_element_by_class_name("matchWrapper hidePreviousUpper").click()

game.click()  '''

stats = driver.find_element(By.CLASS_NAME,"grid-container").click()

# %%
time.sleep(10)
driver.quit()