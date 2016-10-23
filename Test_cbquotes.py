'''
Эта программа тестирует функцию cbquotes(dd, mm, yyyy).
Функция скачивает курсы валют с сайта ЦБ РФ на указанную дату и возвращает все котировки в 
виде словаря {'XYZ':(Имя валюты, кратность, курс, цифровой код)}
'''
from CBR-Daily-Quotes.py import cbquotes

dd = '24'
mm = '10'
yyyy = '2016'

todayq = cbquotes(dd, mm, yyyy)

print(todayq)