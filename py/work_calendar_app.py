# -*- coding: utf-8 -*-
import work_member_app
import calendar
import pprint
import random
import locale
from datetime import date, timedelta
import datetime

# 今日の日時を取得
today = datetime.date.today()

def calendar_input():
    #カレンダーの年数入力
    input_year = input('年を入力してください。→')

    #カレンダーの月を入力
    input_month = input('月を入力してください。→')

    #カレンダーの月を入力
    input_day = input('日を入力してください。→')

    # 入力値のチェック
    try:
        year = int(input_year)
        month = int(input_month)
        day = int(input_day)
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
    except ValueError:
        year = (today.year)
        month = (today.month)
        day = (today.day)
    
    # 年月日曜日をリストに追加
    fullmonth_num = (calendar.monthrange(year, month)[1])
    hiduke = datetime.date(year, month, 1)
    weeklist = []
    
    for x in range(fullmonth_num):
        monthdata = (hiduke.strftime('%Y/%m/%d/%A'))
        weeklist.insert(x,monthdata)
        hiduke = hiduke + datetime.timedelta(days=1)

    # ランダムに日にちを取得する
    result = day_check(year, month, weeklist)
    
    return result

def day_check(year, month, weeklist):
    # 指定月の日数の取得
    fullmonth_num = (calendar.monthrange(year, month)[1])

    # 定数
    oneweek_num = 7

    # 週の数でループ回数を決める
    week_loop = fullmonth_num / oneweek_num

    # ループの回数
    loop_count = 0

    # 日付リストの初期化
    attendance_date = []

    # 従業員データの入力
    worker = work_member_app.check_worker_num()

    # 従業員リストの初期化
    shift_member = []

    # 日ごとの必要人数
    need_worker = 3

    while loop_count < week_loop:

        # 1週間分の日にちを出す
        if(loop_count == 0):
            for x in range(oneweek_num):
                # １週間の日付ごとに必要な労働者のセット
                shift_member = random.sample(worker, need_worker)
                attendance_date.append([weeklist[x], shift_member])

        elif(loop_count >= 1 and fullmonth_num > (oneweek_num + (loop_count * oneweek_num))):
            # １週間を取り出し、ランダムに労働者をセットする
            for x in range(oneweek_num):
                shift_member = random.sample(worker, need_worker)
                attendance_date.append([weeklist[x + (1 + (oneweek_num * loop_count))],shift_member])

        elif (loop_count >= 1 and fullmonth_num < oneweek_num + (loop_count * oneweek_num)):
            # 残りの日数が一週間未満の時の処理
            range_num = fullmonth_num - (loop_count * oneweek_num + 1)
            if(range_num != 0):
                for x in range(range_num):
                    shift_member = random.sample(worker, need_worker)
                    attendance_date.append([weeklist[x + (1 + (oneweek_num * loop_count))],shift_member])
            else:
                pass

        # ループ回数のカウント
        loop_count += 1

    return attendance_date

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
