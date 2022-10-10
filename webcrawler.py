from os import stat
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import chromedriver_binary 

driver = webdriver.Chrome("/usr/bin/chromedriver")
names =[]
statuss =[]
mailings = []
principals = []
dates = []

driver.get("https://sosbiz.idaho.gov/search/business")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'div-table-cell interactive'}):
    name = a.find('div', attrs={'class':'cell'})
    status = a.find('div', attrs={'class':'cell_'})
    mailing = a.find('div', attrs={'class':'value'})
    principal = a.find('div', attrs={'class':'value_'})
    date = a.find('div', attrs={'class':'value'})
    names.append(name.text)
    statuss.append(status.text)
    mailings.append(mailing.text)
    principals.append(principal.text)
    dates.append(date.text)

df = pd.DataFrame({'Entity Name':names,'Status':statuss,'Mailing Address':mailings, 'Principal Address':principals,'Initial Filing Date':dates})
df.to_csv('webcrawler.csv', index=False, encoding='utf-8')