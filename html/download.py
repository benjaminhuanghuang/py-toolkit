'''
  Setup:
    Install beautifulsoup4
      pip install beautifulsoup4
    Download webdriver for selenium from https://chromedriver.chromium.org/
'''

from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
 
URL = "https://nrcs.app.box.com/v/soils/folder/64615474196?page="
URL_SORT = "https://nrcs.app.box.com/v/soils/folder/64615474196?sortColumn=name&sortDirection=DESC"
TARGET_FOLDER = "."
STATE = 'WV'   # West Virginia
url = URL + '1'

totalPage = 3

def fetchHtmlForThePage(url, delay, block_name):
  browser = webdriver.Chrome('./chromedriver')
  
  browser.get(url)
  try:
    # Waiting for the javascirpt create the page content
    element_present = EC.presence_of_element_located((By.ID, block_name))
    WebDriverWait(browser, delay).until(element_present)
  except TimeoutException:
    print ("Loading took too much time!")

  html = browser.page_source
  browser.quit()
  return html

def getTotalPages():
  url = URL + '1'
  
  html = fetchHtmlForThePage(url, 5, 'table-header')
  soup = BeautifulSoup(html, 'lxml')
  span = soup.find('span', attrs = {'class' : 'btn-content'})
  sub_span = span.find('span')
  text = sub_span.text   # should be 1 of 3
  arr = text.split(' ')

  return int(arr[-1])

def getZipFile(url):
  
   html = urllib.request.urlopen(url).read()
   print(html)
   soup = BeautifulSoup(html, 'lxml')
   iframe = soup.find('iframe')
   print(iframe)
   
def downloadZipFiles(url, state):
    print("Download files from " + url)


if __name__ == "__main__":
  totalPage = getTotalPages()

  for x in range(totalPage):
    url = URL + str(x+1)
    downloadZipFiles(url, STATE)
