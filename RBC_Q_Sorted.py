import urllib.request  # импортируем модуль
import re

def itemsort(item):
     return item[2]

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][2]<alist[i+1][2]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

'''
  rbcqread(deal, currency, nquotes)

  deal - buy или sell
  currency - USD, EUR, GBP, ..
  nquotes - сколько котировок в отсортированном списке

  returns

  список из nquotes предложений

'''

url = 'http://quote.rbc.ru/cash/?currency=3&city=1&deal=sell&amount=100'  # адрес страницы, которую мы хотим скачать
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  # хотим притворяться браузером

req = urllib.request.Request(url, headers={'User-Agent': user_agent})
# добавили в запрос информацию о том, что мы браузер Мозилла

with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

regPostTitle = re.compile(
    '<div class="quote__office__one js-one-office">.*?<div class="quote__office__cell quote__office__one__phone2">',
    flags=re.U | re.DOTALL)
titles = regPostTitle.findall(html)


new_titles = []
regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
for t in titles:
    clean_t = regSpace.sub("*", t)
    clean_t = regTag.sub("*", clean_t)
    clean_t = clean_t.replace('%', '')
    new_titles.append(clean_t)

exlist = []
for t in new_titles[:-1]:
    tl = t.split('*')
    for i in range(len(tl)):
        try:
            tl.remove('')
        except ValueError:
            break
    exlist.append(tl)

exlist_num = []
for item in exlist:
    it = item
    it[2] = float(it[2])
    it[3] = float(it[3])
    exlist_num.append(it)

#exlist_s = bubbleSort(exlist_num)
exlist_num.sort(key=itemsort, reverse=True)

print('Пять самых лучших мест, где можно ПРОДАТЬ валюту\n')
for item in exlist_num[:5]:
    print(item[5], item[2], item[0], item[1], sep=4*'\t')



