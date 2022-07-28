import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller


#loadUI

        
#data Cedulas

nit = 901358032
# define the website to scrape and path where the chromediver is located
website = 'https://www.rues.org.co/'
chromedriver_autoinstaller.install() #AutoUpdate chromedriver
path = 'C:\\chromedriver\\chromedriver.exe' # write the path here

# define 'driver' variable
driver = webdriver.Chrome(executable_path = path)
#clear cached driver
#driver.get('chrome://settings/clearBrowserData')
#driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
# open Google Chrome with chromedriver
driver.minimize_window
driver.get(website)


#searchData
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txtNIT"]'))).send_keys(nit)

#clickonConsultar
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConsultaNIT"]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main[1]/div/div[6]/div/div/div/div/table/tbody/tr/td[7]/a'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div/div[2]/div[1]/div/button'))).click()


#extractData
data = nit
resultado = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txtFacultades"]')))
print (resultado.text)

#closeBrowser

