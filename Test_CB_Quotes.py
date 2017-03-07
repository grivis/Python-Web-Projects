'''
Тестируем функцию CB_Quotes, определенную в модуле CBR_Daily_Quotes.py
Эта функция возвращает "словарь словарей"
histquotes = {'0':{}, '15':{}, '30':{}, '90':{}}
'''
from CBR_Daily_Quotes import *

histquotes = CB_Quotes()


# print('Котировки сегодня')
# print(histquotes['0'])
# print('---')
#
# print('Котировки 15')
# print(histquotes['15'])
# print('---')
#
# print('Котировки 30')
# print(histquotes['30'])
# print('---')
#
# print('Котировки 90')
# print(histquotes['90'])
# print('---')

print('USD сегодня')
print(histquotes['0']['USD'][2])
print('---')

print('USD 15')
print(histquotes['15']['USD'][2])
print('---')

print('USD 30')
print(histquotes['30']['USD'][2])
print('---')

print('USD 90')
print(histquotes['90']['USD'][2])
print('---')


