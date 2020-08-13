# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
import json
import re
import pandas as pd
import time
import datetime

def get_html(url):
    #Gets status of request to a url.  If successful, html is pulled.
    status = requests.get(url)
    if status.status_code == 200:
        print('Connection valid.  Pulling html...')
        html = requests.get(url).text
        data = soup(html, 'html.parser')
        print('Scrape completed.')
    else:
        return('Connection failed.')
    return data 

def yahoo_current(html):
    #Gets stock name, price at close, and price off hours, and timestamp
    name = html.find('h1', {'class': "D(ib) Fz(18px)", "data-reactid":"7"}).text
    price = html.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    ts = datetime.datetime.now()
    print('{0} is trading at {1} at {2}'.format(name, price, ts))
    return name, price, ts

urls = ['https://finance.yahoo.com/quote/MSFT',
        'https://finance.yahoo.com/quote/AMD',
        'https://finance.yahoo.com/quote/FB']

update = True

names = []
prices = []
ts_list = []

while update:
    for url in urls:
        html = get_html(url)
        name, price, ts  = yahoo_current(html)
        names.append(name)
        prices.append(price)
        ts_list.append(ts)
        time.sleep(10)
    

    
