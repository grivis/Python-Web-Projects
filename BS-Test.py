
import urllib.request  # импортируем модуль
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://cbr.ru/currency_base/daily.aspx?date_req=30.10.2016')
bsobj = BeautifulSoup(html.read())
#print(bsobj.h2.get_text())
#print(bsobj.table.get_text())
quotes = []
for i in bsobj.table.tr.next_siblings:
    il = str(i)
    quotes.append(il)

for i in range(len(quotes)):
    try:
        quotes.remove('\n')
    except ValueError:
        break

regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
for item in quotes:
    clean_item = regTag.sub("", item)
    clean_item_lst = clean_item.split('\n')
    print(clean_item_lst)
