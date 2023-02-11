from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
import os
import stat
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

link = input("Input URL of source: ")
type = input("What type of citation? (MLA, APA, Chicago): ")
pages = input("If you have specific pages to cite, list them here, otherwise leave blank: ")

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(
  chrome_options=options,
  executable_path=
  r"C:\Users\sophc\Downloads\chromedriver_win32\chromedriver.exe",
)
driver.implicitly_wait(20)

today = date.today()
#link = "http://kpsl.tlcdelivers.com/?config=hs#section=resource&resourceid=132700809&currentIndex=0&view=fullDetailsDetailsTab"
driver.get(link)

# გორგა დილა GORGA SQL INJECTION
# for these variables- make if statement to check if element even exists, and then put it in the variables if it does
# Author
author = driver.find_element(By.XPATH,
                             '//[@id="detailsPageContent"]/header/h3')
# Title of source
source_title = driver.find_element(By.XPATH,
                                   '//[@id="detailsPageContent"]/header/h2')
# Publisher
publisher = driver.find_element(By.XPATH,
                                '//*[@id="fullDetails_marcData"]/ul[3]/li')

# Citation
citation = ""
if (author != ""):
  citation = citation + author.text + ". "
if(source_title != ""):
  citation = citation + """ + source_title.text + "." "
if(publisher != ""):
  citation = citation + publisher.text
if (pages != ""):
  if(type == "Chicago"):
    citation = citation + " " + pages + ". "
  else:
    citation = citation + " pp. " + pages + "."

citation = citation + " Accessed: " + today.strftime("%B %d, %Y") + "."

print(citation)