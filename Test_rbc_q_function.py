from RBC_Q_Sort_Function import *
from time import *

deal = 'buy'
city = 'МСК'
currency = 'USD'
nquotes = 5
while True:

    deal = 'buy'
    qlist = rbcqread(city, deal, currency, nquotes)

    print(nquotes, 'лучших мест в', city, 'чтобы', deal, currency)
    for item in qlist:
        print(item[2], item[0], item[1], sep=4 * '\t')

    print()

    deal = 'sell'
    qlist = rbcqread(city, deal, currency, nquotes)

    print(nquotes, 'лучших мест в', city, 'чтобы', deal, currency)
    for item in qlist:
        print(item[2], item[0], item[1], sep=4 * '\t')

    sleep(30)