

def cbquotes(dd, mm, yyyy):
    import urllib.request  # импортируем модуль
    import re

    urlbase = 'http://cbr.ru/currency_base/daily.aspx?date_req='  # базовый адрес страницы котировок
    url = urlbase + dd +'.' + mm + '.' + yyyy
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  # хотим притворяться браузером

    req = urllib.request.Request(url, headers={'User-Agent': user_agent})
    # добавили в запрос информацию о том, что мы браузер Мозилла

    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')

    regPostTitle = re.compile('<table class="data">.*?</table>', flags=re.U | re.DOTALL)
    titles = regPostTitle.findall(html)


    regTDopen = re.compile('<td>', flags=re.U | re.DOTALL)
    regTDClose = re.compile('</td>', flags=re.U | re.DOTALL)
    regTRopen = re.compile('<tr>', flags=re.U | re.DOTALL)
    regTRClose = re.compile('</tr>', flags=re.U | re.DOTALL)
    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)

    for t in titles:
        t = t.replace('\r', '')
        t = t.replace('\n', '')
        clean_t = regTDopen.sub('', t)
        clean_t = regTDClose.sub('#', clean_t)
        clean_t = regTRopen.sub('', clean_t)
        clean_t = regTRClose.sub('*', clean_t)
        clean_t = regTag.sub("", clean_t)
        currlst = clean_t.split('*')

    allquotes = []
    for currency in currlst:
        clst = currency.split('#')
        allquotes.append(clst)

    allquotes = allquotes[1:-1]

    quotdic = {}
    #{'XYZ':(Имя валюты, кратность, курс, цифровой код)}

    for i in allquotes:
        quotdic[i[1]] = (i[3] , int(i[2]) , float(i[4].replace(',', '.')), i[0])


    return quotdic




