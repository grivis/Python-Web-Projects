from CBR_Daily_Quotes import *
from RBC_Q_Sort_Function import *
from tkinter import *
from time import *
#from metroFind_more import *
import tkinter.ttk
from metroFind_more_Class import *

metro_st = set(list(metroTMP))
win = NONE
cur = NONE
months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября',10: 'октября', 11: 'ноября', 12: 'декабря'}
cities = {0 : 'Москве' , 1 : 'Санкт-Петербурге'}
currency = {0 : 'USD' , 1 : 'EUR'}
deal_type = {0 : 'покупке' , 1 : 'продаже'}

def form_metrolst(metro_st):
    tempLst = []
    for i in metro_st:
        if i[-2:].isdigit():
            tempLst.append(i[:-2])
        else:
            tempLst.append(i[:-1])
    return tempLst

def CB_Quotes(day, cur_par):
    ticks = time()
    lt = localtime(ticks)

    ticks = ticks - 60 * 60 * 24 * day
    lt = localtime(ticks)

    dd_par = str(lt.tm_mday)
    mm_par = str(lt.tm_mon)
    yyyy_par = str(lt.tm_year)

    todayq_par = cbquotes(dd_par, mm_par, yyyy_par)

    name, krat, kurs, kod = todayq_par[cur_par]

    return kurs


def sortKey(item):
    return item[0]


# def findNearestMetro(mySt, lst):
#     print('lat = ', lst)
#     far_dic = []
#     for i in lst:
#         if i[-1] != '':
#             print(mySt, i[-1])
#             num = findWay(mySt, i[-1])
#             temp = (num, i)
#             far_dic.append(temp)
#
#     far_dic.sort(key=sortKey)
#     sort_lst = [i[1] for i in far_dic]
#     print('far_dic = ', far_dic)
#     return sort_lst

def findNearestMetro(mySt, lst):
    far_dic = []
    for i in lst:
        if i[-1] != '':
            num = findWay(mySt, i[-1])
            temp = (num, i)
            far_dic.append(temp)

    far_dic.sort(key=sortKey)
    #sort_lst = [i[1] for i in far_dic]
    #print('far_dic = ', far_dic)
    #return sort_lst
    return far_dic


def show(city, cur1, deal, metro1):
    global months, cities, currency, deal_type
    metro = metro1.get()
    city = city.get()
    cur = cur1.get()
    deal = deal.get()
    nquotes = 15

    win = Toplevel(root)
    win.minsize(width=600, height=580)
    win.maxsize(width=600, height=580)
    dateLb = Label(win, text='', font='Arial 9')
    dateLb.grid(column=0, row=0, padx=5, pady=5, sticky=W)
    dateLb1 = Label(win, text='', font='Arial 9')
    dateLb1.grid(column=0, row=1, padx=5, pady=5, sticky=W)
    dateLb2 = Label(win, text='', font='Arial 9')
    dateLb2.grid(column=0, row=2, padx=5, pady=5, sticky=W)
    dateLb3 = Label(win, text='', font='Arial 9')
    dateLb3.grid(column=0, row=3, padx=5, pady=5, sticky=W)
    dateLb4 = Label(win, text='', font='Arial 9')
    dateLb4.grid(column=0, row=4, padx=5, pady=5, sticky=W)
    dateLb5 = Label(win, text='', font='Arial 9')
    dateLb5.grid(column=0, row=5, padx=5, pady=5, sticky=W)

    lis = Listbox(win, selectmode=SINGLE, height=15, width=97)
    lis.grid(column=0, row=6, padx=5, pady=5, sticky=W)

    CB_today = CB_Quotes(0, currency[cur])
    #CB_today = '35.12'
    prBank6 = 'Курс ЦБ РФ сегодня: ' + str(CB_today)
    dateLb6 = Label(win, text=prBank6, font='Arial 9')
    dateLb6.grid(column=0, row=7, padx=5, pady=5, sticky=W)

    CB_15 = CB_Quotes(15, currency[cur])
    #CB_15 = '34.13'
    prBank7 = 'Курс ЦБ РФ 15 дней назад: ' + str(CB_15)
    dateLb7 = Label(win, text=prBank7, font='Arial 9')
    dateLb7.grid(column=0, row=8, padx=5, pady=5, sticky=W)

    CB_30 = CB_Quotes(30, currency[cur])
    #CB_30 = '36.19'
    prBank8 = 'Курс ЦБ РФ 30 дней назад: ' + str(CB_30)
    dateLb8 = Label(win, text=prBank8, font='Arial 9')
    dateLb8.grid(column=0, row=9, padx=5, pady=5, sticky=W)

    CB_90 = CB_Quotes(90, currency[cur])
    #CB_90 = '35.98'
    prBank9 = 'Курс ЦБ РФ 90 дней назад: ' + str(CB_90)
    dateLb9 = Label(win, text=prBank9, font='Arial 9')
    dateLb9.grid(column=0, row=10, padx=5, pady=5, sticky=W)


    #while True:
    ticks = time()
    lt = localtime(ticks)

    ddNow = str(lt.tm_mday)
    mmNow = str(lt.tm_mon)
    yyyyNow = str(lt.tm_year)
    hourNow = str(lt.tm_hour)
    minNow = str(lt.tm_min)

    tempDeal = 'buy' if deal == 0 else 'sell'
    tempCity = 'МСК' if city == 0 else 'СПБ'
    #qlist = rbcqread(tempCity, tempDeal, currency[cur], nquotes)
    qlist = ['12', 35.12345123, [['35', 'АКБ Банк', 'Марьино'], ['34,3', 'СБК Банк', 'Митино'], ['35,15', 'Альфа банк', 'Сокол'], ['33', 'Мой банк', 'Сокольники'], ['33', 'Твой банк', 'Фили'], ['33,7', 'Ваш банк', 'Библиотека имени Ленина']]]

    if metro != '':
        sort_by_metro_lst = findNearestMetro(metro, qlist[2])
    else:
        sort_by_metro_lst = qlist[2]


    dateNow = 'Сегодня ' + ddNow + ' ' + months[lt.tm_mon] + ' ' + yyyyNow
    prBank = 'Предложения банков в ' + cities[city] + ' на ' + hourNow + ' часов ' + minNow + ' минут(ы)'
    prBank1 = 60 * '* '
    prBank2 = 'Всего имеется {0} предложений'.format(qlist[0])
    prBank3 = 'Средний курс - {0:5.2f}'.format(qlist[1])
    prBank4 = 'Лучшие предложения по ' + deal_type[deal] + ' ' + currency[cur] + ':'

    dateLb.configure(text=dateNow)
    dateLb1.configure(text=prBank)
    dateLb2.configure(text=prBank1)
    dateLb3.configure(text=prBank2)
    dateLb4.configure(text=prBank3)
    dateLb5.configure(text=prBank4)

    lis.delete(0, END)

    # for item in qlist[2]:
    #     stringTowrite = str(item[0]) + ' ' + str(item[1]) + ' ' + str(item[2]) ####
    #     lis.insert(END, stringTowrite)

    for item in sort_by_metro_lst:
        stringTowrite = str(item[1][0]) + ' ' + str(item[1][1]) + ' ' + str(item[1][2]) + '   приблизительное время в пути = ' + str(item[0] * 2)
        lis.insert(END, stringTowrite)
    #
     #   sleep(10)
    #win.after(10000, lambda : show(varCity, varCur, varDeal))




root = Tk()
root.title('Котировки наличной валюты')
root.minsize(width= 530, height=170)
root.maxsize(width= 530, height=170)
img = Image("photo", file="dol_eur_4.png")
root.tk.call('wm', 'iconphoto', root._w, img)

metro_lst = form_metrolst(metro_st)
metro_lst.sort()

fra1 = Frame(root,width=200,height=200, bd = 5, relief=GROOVE)
fra1.grid(row = 0, column = 0, padx = 10, pady = 10)

fra2 = Frame(root,width=200,height=200, bd = 5, relief=GROOVE)
fra2.grid(row = 0, column = 1, padx = 10, pady = 10)

fra3 = Frame(root,width=200,height=200, bd = 5, relief=GROOVE)
fra3.grid(row = 0, column = 2, padx = 10, pady = 10)

fra4 = Frame(root,width=330,height=40, bd = 5, relief=GROOVE)
fra4.grid(row = 1, column = 0, padx = 0, pady = 0, columnspan = 2)

chCity = Label(fra1, text = 'Выберите город:', font = 'Arial 12')
chCity.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = W)

varCity = IntVar()
rad0 = Radiobutton(fra1, text="Москва", variable=varCity, value=0)
rad0.grid(column=0, row=1, sticky=W)
rad1 = Radiobutton(fra1, text="Санкт-Петербург", variable=varCity, value=1)
rad1.grid(column=0, row=2, sticky=W)

chCur = Label(fra2, text = 'Выберите валюту:', font = 'Arial 12')
chCur.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = W)

varCur = IntVar()
rad2 = Radiobutton(fra2, text="USD", variable=varCur, value=0)
rad2.grid(column=0, row=1, sticky=W)
rad3 = Radiobutton(fra2, text="EUR", variable=varCur, value=1)
rad3.grid(column=0, row=2, sticky=W)

chDeal = Label(fra3, text = 'Выберите сделку:', font = 'Arial 12')
chDeal.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = W)
varDeal = IntVar()
rad4 = Radiobutton(fra3, text="Покупка", variable=varDeal, value=0)
rad4.grid(column=0, row=1, sticky=W)
rad4 = Radiobutton(fra3, text="Продажа", variable=varDeal, value=1)
rad4.grid(column=0, row=2, sticky=W)

chMetro = Label(fra4, text = 'Ваша станция метро:', font = 'Arial 10')
chMetro.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = W)

varMetro = StringVar()
combobox = tkinter.ttk.Combobox(fra4,values = metro_lst ,height=20, textvariable=varMetro)
combobox.grid(column=1, row=0, sticky=W, padx = 15, pady = 5)

bt = Button(root, text = 'Показать', command=lambda : show(varCity, varCur, varDeal, varMetro))
bt.grid(column=2, row=1, sticky=E, padx = 12, pady = 10)


root.mainloop()