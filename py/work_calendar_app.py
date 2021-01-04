# -*- coding: utf-8 -*-
import calendar
import pprint
import random
import locale
from datetime import date, timedelta
import datetime

# 今日の日時を取得
today = datetime.date.today()

def calendar_input(input_year , input_month, input_day, input_attend):
    c = calendar.Calendar(firstweekday=0)
    # 入力値のチェック
    try:
        year = int(input_year)
        month = int(input_month)
        day = int(input_day)
        attend = int(input_attend)
        if(year > 9999):
            year = (today.year)
        else:
            pass
        if (month > 12):
            month = (today.month)
        else:
            pass
        if (day > 31):
            day = (today.day)
        else:
            pass
        if(attend > 7):
            attend = 7
        else:
            pass
    except ValueError:
        year = (today.year)
        month = (today.month)
        day = (today.day)
        attend = 3
    
    # 年月日曜日をリストに追加
    fulmonth_num = (calendar.monthrange(year, month)[1])
    hiduke = datetime.date(year, month, 1)
    weeklist = []
    loop = 0
    em = 0
    # while loop < fulmonth_num:
        # weeklist.insert(em,[])
        # for x in range(7):
        #     monthdata = (hiduke.strftime('%Y/%m/%d/%A'))
        #     weeklist.insert(x,monthdata)
        #     hiduke = hiduke + datetime.timedelta(days=1)
    for x in range(fulmonth_num):
        monthdata = (hiduke.strftime('%Y/%m/%d/%A'))
        weeklist.insert(x,monthdata)
        hiduke = hiduke + datetime.timedelta(days=1)

    # ランダムに日にちを取得する
    result = day_check(year, month, weeklist, attend)
    return result

def day_check(year, month, weeklist, attend):
    # 指定月の日数の取得
    fulmonth_num = (calendar.monthrange(year, month)[1])

    # 定数
    oneweek_num = 5

    # 週の数でループ回数を決める
    week_loop = fulmonth_num / oneweek_num

    # ループの回数
    loop_count = 0

    # 曜日の集計ポイント（土、日が入ると通常よりもポイントが増えるのでそれにより分岐させる）
    work_point = 0

    # リストの初期化
    weeklist3 = []

    while loop_count < week_loop:
        # リストの初期化
        weeklist2 = []
        # 1週間分の日にちを出す
        if(loop_count == 0):
            for x in range(oneweek_num):
                weeklist2.append(weeklist[x])
        elif(loop_count >= 1 and fulmonth_num > (oneweek_num + (loop_count * oneweek_num))):
            for x in range(oneweek_num):
                weeklist2.append(weeklist[x + (1 + (oneweek_num * loop_count))])
        elif (loop_count >= 1 and fulmonth_num < oneweek_num + (loop_count * oneweek_num)):
            range_num = fulmonth_num - (loop_count * oneweek_num + 1)
            if(range_num != 0):
                for x in range(range_num):
                    weeklist2.append(weeklist[x + (1 + (oneweek_num * loop_count))])
            else:
                pass
        
        # 日にちを取り出す
        get_day_count = fulmonth_num - (loop_count * oneweek_num + 1)
        
        # 週から3日ランダムに取り出すので、3日以下の場合の処理
        if(get_day_count >= 3):
            get_day_count = 3
            random_day = (random.sample(weeklist2,3))
        elif(get_day_count == 2):
            random_day = (random.sample(weeklist2,2))
        elif(get_day_count == 1):
            random_day = weeklist2
        else:
            pass
        
        # 平日と休日でポイントを振り、翌週のシフトに連続して、休日が来ないようにする
        if(get_day_count > 0):
            for x in range(get_day_count):
                rand = (random_day[x])
                # if('Saturday' in rand):
                #     work_point += 2
                # elif('Sunday' in rand):
                #     work_point += 2
                # else:
                #     work_point += 1
                weeklist3.append(rand)

        # ランダム取得した日数情報の初期化
        # weeklist2 = []
        # print(weeklist3)
        # ループ回数のカウント
        loop_count += 1

        # 週でランダム取得した日の曜日ポイントの合計値
        # 現在は合計しているが、週ごとに集計して、翌週には土日に入らないように分岐を入れたりする予定
        # print(work_point)
        # work_point = 0
    return weeklist3

# 月の末日を取得
def get_last_day(year, month):
    return datetime.date(year, month, calendar.monthrange(year, month)[1])

#HTML形式でのカレンダーの出力
def calender_html(z, w):
    hc = calendar.HTMLCalendar()
    try:
        year = int(z)
        month = int(y)
    except ValueError:
        year = (today.year)
        month = (today.month)
    print(hc.formatmonth(year,month))
