import urllib.request  # импортируем модуль
import re

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

f = open('Quotes.csv', 'w', encoding='utf-8')
inputStr = ''
for item in exlist:
    inputStr = ('\t').join(item)
    print(inputStr)
    f.write(inputStr+'\n')
f.close()

