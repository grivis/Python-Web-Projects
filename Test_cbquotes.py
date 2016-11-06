'''
Эта программа тестирует функцию cbquotes(dd, mm, yyyy).
Функция скачивает курсы валют с сайта ЦБ РФ на указанную дату и возвращает все котировки в 
виде словаря {'XYZ':(Имя валюты, кратность, курс, цифровой код)}
'''
from CBR_Daily_Quotes import *
import time
#import CBR_Daily_Quotes

ticks = time.time()
lt = time.localtime(ticks)

ddNow = str(lt.tm_mday)
mmNow = str(lt.tm_mon)
yyyyNow = str(lt.tm_year)

ticks_15 = ticks - 60*60*24*15
lt_15 = time.localtime(ticks_15)

dd_15 = str(lt_15.tm_mday)
mm_15 = str(lt_15.tm_mon)
yyyy_15 = str(lt_15.tm_year)

ticks_30 = ticks - 60*60*24*30
lt_30 = time.localtime(ticks_30)

dd_30 = str(lt_30.tm_mday)
mm_30 = str(lt_30.tm_mon)
yyyy_30 = str(lt_30.tm_year)

ticks_90 = ticks - 60*60*24*90
lt_90 = time.localtime(ticks_90)

dd_90 = str(lt_90.tm_mday)
mm_90 = str(lt_90.tm_mon)
yyyy_90 = str(lt_90.tm_year)

# dd = '3'
# mm = '11'
# yyyy = '2016'

todayq = cbquotes(ddNow, mmNow, yyyyNow)
todayq_15 = cbquotes(dd_15, mm_15, yyyy_15)
todayq_30 = cbquotes(dd_30, mm_30, yyyy_30)
todayq_90 = cbquotes(dd_90, mm_90, yyyy_90)

name, krat, kurs, kod = todayq['USD']
name_15, krat_15, kurs_15, kod_15 = todayq_15['USD']
name_30, krat_30, kurs_30, kod_30 = todayq_30['USD']
name_90, krat_90, kurs_90, kod_90 = todayq_90['USD']

print('Курс на сегодня:')
print(krat, name, 'за', kurs, 'рублей')

print(20*'-')
print('Курс 15 дней назад:')
print(krat_15, name_15, 'за', kurs_15, 'рублей')

print(20*'-')
print('Курс 30 дней назад:')
print(krat_30, name_30, 'за', kurs_30, 'рублей')

print(20*'-')
print('Курс 90 дней назад:')
print(krat_90, name_90, 'за', kurs_90, 'рублей')


#сегодня, -15, -30, -90
