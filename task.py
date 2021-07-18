from typing import Container
from bs4 import BeautifulSoup
import requests
import pandas as pd
url=requests.get("https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1")
stock_status=bool
if (stock_status==True):
   print('in-stock')
else: 
   print('out-stock')  
sp=BeautifulSoup(url.content,'html.parser')
price=sp.find_all('div', 'price')
title=sp.find_all('a','title')
stock=sp.find_all('span' ,'stock_status')
maftr=sp.find_all('a','maftr')
priceLoop=[prices.text for prices in price]
titleLoop=[titles.text for titles in title]
stockLoop=[stocks.text for stocks in stock]
maftrsLoop=[maftrs.text for maftrs in maftr]

data={
    'price':priceLoop,
    'Name_of_Console':titleLoop,
    'stock_material':stockLoop,
     'manifacturing_name':maftrsLoop  
 }
 
# fs=pd.DataFrame(data,columns=['price')
# # {     'price',
# #       'Name_of_Console',
# #       'stock_material',
# #        'manfacturing_name'    
# #  }
# # ])
print(data)

