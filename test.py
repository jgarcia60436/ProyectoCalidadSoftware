#Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\dChrome\\chromedriver.exe'

driver = webdriver.Chrome(driver_path,chrome_options=options)

#inicializar navegador
driver.get('https://www.demoblaze.com/')