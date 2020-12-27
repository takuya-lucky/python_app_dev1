import home
import cgi

# def input_day_data():
    
#カレンダーの年数入力
val1 = input('年を入力してください。→')

#カレンダーの月を入力
val2 = input('月を入力してください。→')

#カレンダーの月を入力
val3 = input('日を入力してください。→')

#カレンダーの月を入力
val4 = input('１週間の労働日数を入力してください。→')

test = home.calendar_input(val1 , val2, val3, val4)
# print(test)