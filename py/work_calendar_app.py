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

# 定数
oneweek_num = 7

# 仕事の開始日のリスト
# 仕事の開始日を月初めの三日以内に設定するためのリスト
start_work_day = [0,1,2,3,4]

# 就業日(3日連続する)
attend_work = 3

# 休みの日(2日を基準とする)
# 例外を作る処理は必要であれば考える
holiday = 2

# シフト一覧
shift_list = ['朝勤務', '昼勤務' , '夜勤務']
shift_list_rookie = ['朝勤務', '昼勤務']

# 仕事の初日の初期化
# 3日仕事をして、2日休みなので、5日ずつ加算されていく
work_day = 0

# 指定月のカレンダーの情報を取得する
def calendar_input():
    #カレンダーの年数入力
    input_year = input('年を入力してください。→')

    #カレンダーの月を入力
    input_month = input('月を入力してください。→')

    #カレンダーの月を入力
    # input_day = input('日を入力してください。→')

    # シフトを作る週の数の入力
    input_need_week = input('欲しい週分の数値を入力してください')

    # 入力値のチェック
    try:
        year = int(input_year)
        month = int(input_month)
        weekly = int(input_need_week)
        # day = int(input_day)
        if(year > 9999):
            year = (today.year)
        else:
            pass
        if (month > 12):
            month = (today.month)
        else:
            pass
        # if (day > 31):
        #     day = (today.day)
        # else:
        #     pass
    except ValueError:
        year = (today.year)
        month = (today.month)
        weekly = 7
        # day = (today.day)
    
    # 1か月の日数を取得
    fullmonth_num = (calendar.monthrange(year, month)[1])
    fullmonth_oneweek_num = fullmonth_num + oneweek_num
    hiduke = datetime.date(year, month, 1)
    weeklist = []
    
    for x in range(fullmonth_oneweek_num):
        monthdata = (hiduke.strftime('%Y/%m/%d/%A'))
        weeklist.insert(x,monthdata)
        hiduke = hiduke + datetime.timedelta(days=1)

    # ランダムに日にちを取得する
    result = day_check(year, month, weeklist, weekly)
    
    return result

# 取得した日にちに勤務者を割り当てて、シフトを作成する
def day_check(year, month, weeklist, weekly):
   
    # ループの回数
    loop_count = 0

    # 日付リストの初期化
    attendance_date = []

    # 従業員データの入力
    worker = work_member_app.check_worker_num()

    # 従業員の人数の取得
    worker_num = len(worker)

    # 従業員リストの初期化
    shift_member = []

    # 仕事の開始日を重複させない為にランダムで選んだ開始日を保存しておくリスト
    check_work_day = []
        
    # シフトに入る労働者の選出
    for x in range(len(worker)):
        # シフトの作成回数
        shift_count = 0
        box = []
        # 順番に社員にシフトを入れるために選出
        shift_member = worker[x]

        # 仕事の開始日をランダムに割り当てる
        # 二人目以降は一日の必要人数以上にならないように、開始日を見て調整する
        if loop_count == 1:
            work_day = get_random_day(check_work_day)
            check_work_day.append(work_day)
        else:
            work_day = random.choice(start_work_day)
            check_work_day.append(work_day)

        # 日に従業員を割り当てる
        # シフトの欲しい週分ループをさせる
        for y in range(weekly):
           
            # 朝、昼、夜のシフトの割り当て
            shift_time = get_random_shift(shift_member, box, weeklist, work_day, year, month)

            # リストにシフトデータを追加する
            for x in range(attend_work):
                    attendance_date.append([[[weeklist[work_day + x]], shift_time ,shift_member]])
                    box.append([[[weeklist[work_day + x]], shift_time]])

            # 仕事をした最終日から、休み分（デフォルトは2日）を加えて、次の週のシフトのスタートにする
            work_day += attend_work + holiday

            # シフトの作成回数を増やす
            shift_count += 1

        loop_count = 1
    return attendance_date

def get_random_day(check_day):
    # 開始日からランダムに1日取り出す
    work_day = random.choice(start_work_day)

    # ランダムに取り出した日が一日に必要な人数を超えていれば、取り直す
    if check_day.count(work_day) >= 2:
        return get_random_day(check_day)
    else:
        return work_day

def get_random_shift(shift_member, box, weeklist, work_day, year , month):
    if 1 in shift_member:
        return random.choice(shift_list_rookie)
    else:
        return random.choice(shift_list)

        
# 指定の月の日数を取得する
def get_firts_day(year,month):
    return (calendar.monthrange(year, month)[1])

# 月の末日を取得
def get_last_day(year, month):
    return datetime.date(year, month, calendar.monthrange(year, month)[1])

