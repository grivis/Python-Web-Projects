
import urllib.request  # импортируем модуль
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://cbr.ru/currency_base/daily.aspx?date_req=25.10.2016')
bsobj = BeautifulSoup(html.read())
print(bsobj.h1)
for i in bsobj.table.tr.next_siblings:
    print(i)
