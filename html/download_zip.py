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

# sorting by DESC to make sure West Virginia was displayed on first page
URL_SORT = "https://nrcs.app.box.com/v/soils/folder/64615474196?sortColumn=name&sortDirection=DESC"
HOST_NAME = "https://nrcs.app.box.com"
TARGET_FOLDER = "."
STATE = 'WV'   # West Virginia

def fetchHtmlForThePage(url, delay, block_name):
  browser = webdriver.Chrome('./chromedriver')
  
  browser.get(url)
  try:
    # Waiting for the javascirpt create the page content
    element_present = EC.presence_of_element_located((By.ID, block_name))
    WebDriverWait(browser, delay).until(element_present)
  except TimeoutException:
    pass

  html = browser.page_source
  browser.quit()
  return html


def downloadZipFile(url, state):
  html = fetchHtmlForThePage(url, 10, 'table-header')
  soup = BeautifulSoup(html, 'lxml')
  links = soup.find_all('a', attrs = {'data-resin-target': 'openfile'})
  for link in links:
    if link.text.endswith('_'+state+'.zip'):
      downloadPage = HOST_NAME + link['href']
      getZipFile(downloadPage)


def getZipFile(url):
  browser = webdriver.Chrome('./chromedriver')
  
  browser.get(url)

  try:
    # Waiting for the javascirpt create the page content
    element_present = EC.presence_of_element_located((By.ID, 'button'))
    WebDriverWait(browser, 5).until(element_present)
  except TimeoutException:
    pass
  
  browser.find_element_by_xpath('//button[text()="Download"]').click()
  
  try:
    # Waiting for the javascirpt create the page content
    element_present = EC.presence_of_element_located((By.ID, 'iframe'))
    WebDriverWait(browser, 5).until(element_present)
  except TimeoutException:
    pass
  
  html = browser.page_source
  browser.quit()
  soup = BeautifulSoup(html, 'lxml')
  iframe = soup.find('iframe')
  print(iframe['src'])


if __name__ == "__main__":
  downloadZipFile(URL_SORT, STATE)
  # For testing...
  # getZipFile('https://nrcs.app.box.com/v/soils/file/398770471572')
