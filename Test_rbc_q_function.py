from RBC_Q_Sort_Function import *
from time import *

deal = 'buy'
city = 'МСК'
currency = 'USD'
nquotes = 15
while True:

    deal = 'buy'
    qlist = rbcqread(city, deal, currency, nquotes)


    print(nquotes, 'лучших мест в', city, 'чтобы', deal, currency)
    print('Всего имеется {0} предложений'.format(qlist[0]))
    print('Средняя цена - {0:5.2f} '.format(qlist[1]))
    for item in qlist[2]:
        print(item[2], item[0], item[1], item[5], sep=4 * '\t')

    print()

    deal = 'sell'
    qlist = rbcqread(city, deal, currency, nquotes)


    print(nquotes, 'лучших мест в', city, 'чтобы', deal, currency)
    print('Всего имеется {0} предложений'.format(qlist[0]))
    print('Средняя цена - {0:5.2f} '.format(qlist[1]))
    for item in qlist[2]:
        print(item[2], item[0], item[1], item[5], sep=4 * '\t')
    print()


    sleep(30)