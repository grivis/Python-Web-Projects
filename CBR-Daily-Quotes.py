import urllib.request  # импортируем модуль
import re

url = 'http://cbr.ru/currency_base/daily.aspx?date_req=21.10.2016'  # адрес страницы, которую мы хотим скачать
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  # хотим притворяться браузером

req = urllib.request.Request(url, headers={'User-Agent': user_agent})
# добавили в запрос информацию о том, что мы браузер Мозилла

with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

regPostTitle = re.compile('<table class="data">.*?</table>', flags=re.U | re.DOTALL)
titles = regPostTitle.findall(html)


#print(titles)

new_titles = []
regTDopen = re.compile('<td>', flags=re.U | re.DOTALL)
regTDClose = re.compile('</td>', flags=re.U | re.DOTALL)
regTRopen = re.compile('<tr>', flags=re.U | re.DOTALL)
regTRClose = re.compile('</tr>', flags=re.U | re.DOTALL)
regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)

for t in titles:
    t = t.replace('\r', '')
    clean_t = regTDopen.sub('', t)
    clean_t = regTDClose.sub(' ', clean_t)
    clean_t = regTRopen.sub('', clean_t)
    clean_t = regTRClose.sub(' ', clean_t)
    clean_t = regTag.sub("", clean_t)
    #print(clean_t)
    new_titles.append(clean_t)
print(new_titles)
#regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
# regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
# for t in titles:
#     clean_t = regSpace.sub("*", t)
#     clean_t = regTag.sub("*", clean_t)

#     new_titles.append(clean_t)