# Function JulianDate (givendate: Gdate) : LongInt;
# var
# a, y, m : integer;
# begin
# a := (14-givendate.month) div 12;
# y := givendate.year + 4800 - a;
# m := givendate.month + 12*a - 3;
# JulianDate := givendate.day + ((153*m+2) div 5) + 365*y +(y div 4) -
# (y div 100) + (y div 400) - 32045;
# end;
#
# Function CalendarDate(JDN : LongInt) : GDate;
# var
# a, b, c, d, e, m : integer;
#
# begin
# a := JDN + 32044;
# b := (4*a+3) div 146097;
# c := a - (146097*b) div 4;
# d := (4*c+3) div 1461;
# e := c - (1461*d) div 4;
# m := (5*e+2) div 153;
# CalendarDate.day := e - ((153*m+2) div 5) + 1;
# CalendarDate.month := m + 3 - 12*(m div 10);
# CalendarDate.year := 100*b + d - 4800 + (m div 10);
# end;

def JulianDate(year, month, day):
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12*a - 3
    return day + (153*m+2)//5 + 365*y +(y // 4) - (y // 100) + (y // 400) - 32045

def CalendarDate(JDN):
    a = JDN + 32044
    b = (4*a+3) // 146097
    c = a - (146097*b) // 4
    d = (4*c+3) // 1461
    e = c - (1461*d) // 4
    m = (5*e+2) // 153
    day = e - ((153 * m + 2) // 5) + 1
    month = m + 3 - 12*(m // 10)
    year = 100*b + d - 4800 + (m // 10)
    return year, month, day

year = 2016
month = 11
day = 6

JDN = JulianDate(year, month, day)

print('Юлианская дата сегодня', JDN)

JDN10 = JDN - 10

year10, month10, day10 = CalendarDate(JDN10)

print('Юлианская дата 10 дней назад', year10, month10, day10 )