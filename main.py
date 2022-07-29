import sys
import BdB_rc #Import Convert logo file
import logo_rc #Import Convert logo file
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PyQt5 import QtCore, QtGui, QtWidgets 
from PySide2.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox,QLineEdit,QLabel,QWidget,QPushButton
from selenium.webdriver.chrome.options import Options

#UIWindow
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        #set Icon
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        #lOAD UI FILE
        uic.loadUi("v2.ui", self)
        #define widgets
        self.nitText = self.findChild(QLineEdit, 'nitText')
        self.consultarButton = self.findChild(QPushButton, 'consultarButton')
        self.info= self.findChild(QLineEdit, 'info')
        
        #Do something(?)
        self.consultarButton.clicked.connect(self.click)
        
        #Show the app
        self.show()

        
    def click(self):
        #Start Scraping
        # define the website to scrape and path where the chromediver is located
        website = 'https://www.rues.org.co/'
        chromedriver_autoinstaller.install() #AutoUpdate chromedriver
        path = 'C:\\chromedriver\\chromedriver.exe' # write the path here
        #run in background
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")
        # define 'driver' variable
        #driver = webdriver.Chrome(executable_path = path, options=chrome_options)
        driver = webdriver.Chrome(executable_path = path)
        driver.maximize_window()
        driver.get(website)
        nit = self.nitText.text()
        #searchData
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="txtNIT"]'))).send_keys(nit)
        #clickonConsultar
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConsultaNIT"]'))).click()
        #button spanning
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rmTable2"]/tbody/tr/td[1]'))).click()
        #button Info
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rmTable2"]/tbody/tr/td[7]/a'))).click()
        #button representante legal
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div/div[2]/div[1]/div/button'))).click()
        #extractData
        resultado = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div/div[2]/div[1]/div/div')))
        self.info.setText(resultado.text)
        print (resultado.text) 
        
        #closeBrowser  
        driver.quit()
        
#initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()