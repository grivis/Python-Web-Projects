'''
  rbcqread(city, deal, currency, nquotes)

  deal - buy или sell
  currency - USD, EUR, GBP, ..
  nquotes - сколько котировок в отсортированном списке

  returns

  список из nquotes предложений

'''
def rbcqread(city, deal, currency, nquotes):
    '''
      rbcqread(city, deal, currency, nquotes)

      city - МСК или СПБ
      deal - buy или sell
      currency - USD, EUR, GBP, ..
      nquotes - сколько котировок в отсортированном списке

      returns

      список из nquotes предложений

    '''


    import urllib.request  # импортируем модуль
    import re


    def itemsort(item):
        return item[2]

    currdic = {'USD':'3', 'EUR':'2', 'GBP':'321'}

    if city == 'МСК':
        city = '1'
    else:
        city = '2'

    crbc = currdic.get(currency, '3')

    url = 'http://quote.rbc.ru/cash/?currency=' + crbc+ '&city=' + city + '&deal='+ deal + '&amount=100'  # адрес страницы, которую мы хотим скачать
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

    if deal == 'buy':
        rr = False
    else:
        rr = True


    exlist_num.sort(key=itemsort, reverse= rr)

    average = 0
    TotalQ = len(exlist_num)
    for i in range(TotalQ):
        average += exlist_num[i][2]
    average /= TotalQ


    if nquotes > TotalQ -1:
        nquotes = TotalQ - 1

    return TotalQ, average, exlist_num[:nquotes]
