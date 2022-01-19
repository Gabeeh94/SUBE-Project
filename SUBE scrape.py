from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import os
import time

#Set Firefox's preferences so that it automatically downloads the PDF 
op = Options()
#Save file to path defined for recent download with value 2
op.set_preference("browser.download.folderList",2)
#Disable display Download Manager window with false value
op.set_preference("browser.download.manager.showWhenStarting", False)
#Make download location the curent working directory
op.set_preference("browser.download.dir",os.getcwd())
#MIME set to save file to disk without asking file type to used to open file
op.set_preference ("browser.helperApps.neverAsk.saveToDisk", "application/pdf;text/plain;application/text;text/xml;application/xml")

#Set permissions to allow automatic download
op.set_preference("browser.download.useDownloadDir", True)

op.set_preference("browser.download.viewableInternally.enabledTypes", "")

op.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)

op.set_preference("pdfjs.disabled", True)


#Open Browser
driver = webdriver.Firefox(options=op)
#Go to the site
driver.get("https://tarjetasube.sube.gob.ar/SubeWeb/Webforms/Account/Views/login.aspx?msg=1")

#Store current window's id
main_page = driver.current_window_handle

#Find and fill credentials
DNI = driver.find_element_by_id("txtDocumento").send_keys("Insert DNI")

#Wait a second to fill the next credential to not alert the captcha
time.sleep(2)

password = driver.find_element_by_id("txtPassword").send_keys("Insert pass")

time.sleep(2)

#Scroll down
driver.execute_script("window.scrollBy(0,500)", "")

time.sleep(3)

#Finds the frame where the captcha is located and switch to it
frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)

#Clicks the captcha and then switches back to the page
driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()
driver.switch_to.default_content()

time.sleep(2)

#Clicks to enter
enter = driver.find_element_by_xpath('//button[normalize-space()="Ingresar"]').click()


#Wait until the other page loads. If it waits longer than 10s it closes the page
try:
    elem = WebDriverWait(driver, 10,poll_frequency=3).until(
        EC.presence_of_element_located((By.ID, "dateFrom")) #This is a dummy element
    )
except:
    driver.close()

#Scrolls down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(1)

#Open the PDF and downloads it
PDF = driver.find_element_by_xpath('//button[normalize-space()="Imprimir movimientos"]').click()

time.sleep(3)

#Close the browser
driver.close()
