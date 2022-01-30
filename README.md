# SUBE personal data scraper and cleaner

A Python scraper that downloads the PDF with all the SUBE's (Buenos Aires's public transportation system) data of a particular person and a script that uses OCR to create a csv from the images. This file was then used to do some basic analysis and visualizations in PowerBi.

## How it works

The scrape is done using python's Selenium module which opens the browser, fill the credentials and then downloads the pdf. It allows a much faster collection of the data than by doing it by hand and is intended to be ran at periodical intervals to track the person's public transport use. The only donwside is that it sometimes alerts the captcha and you have to run it again.

After you get the PDF you can run the "PDF to csv" script. It uses the pdf2image module to convert the pages into workable images which are then edited and preprocessed using the module Pillow to finally use pytesseract to get the text. The process consist in an iteration where the code goes through every line of data, cropping the image to just show a particular concept, applying OCR and then appending the resulting text to a list which stores the coresponding concept. After that it's just a matter of creating a csv with the csv module.

## How to use it

- It is required to have installed geckodriver for Selenium to be able to interact with Firefox, as well as the modules used by the scripts.

   https://github.com/mozilla/geckodriver/releases

- You need a user and password to a linked SUBE card. You can link an existing SUBE card in this link: https://tarjetasube.sube.gob.ar/SubeWeb/Webforms/Account/Views/login.aspx?msg=1

- The credentials have to be replaced in the "SUBE scrape.py" file as shown here:

   ![Write your user and password](images/Credentials.jpg)

- After you ran the scraper, the you can use the pdf to csv script and you will end up with a .csv file and the PDF

## Power Bi

![Power Bi example](images/SUBE-Power-Bi.jpg)
