# coding: UTF-8
import calendar
import pprint

#カレンダーの年数入力
val1 = input('年を入力してください。→')
#カレンダーの月を入力
val2 = input('月を入力してください。→')
def calender_input(x , y):
    c = calendar.Calendar(firstweekday=0)
    try:
        year = int(x)
        date = int(y)
    except ValueError:
        year = 2020
        date = 1 
    #入力した値に応じたカレンダーを表示する
    print(calendar.month(year,date, w=2,l=1))
    #週ごとに日を格納する
    pprint.pprint(calendar.monthcalendar(year,date))
    pprint.pprint(c.yeardayscalendar(year),depth=5)
calender_input(val1 , val2)

#HTML形式でのカレンダーの出力
# def calender_html(z, w):
#     hc = calendar.HTMLCalendar()
#     try:
#         year = int(z)
#         date = int(y)
#     except ValueError:
#         year = 1993
#         date = 11
#     print(hc.formatmonth(year,date))
# calender_html(val1, val2)