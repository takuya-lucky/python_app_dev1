import work_calendar_app
import kivy
import japanize_kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import StringProperty , ListProperty
from kivy.uix.widget import Widget
from kivy.resources import resource_add_path
import cgi

# # ランダムに取得したカレンダーを表示する
# def buttonClicked():
#     # text = work_calendar_app.calendar_input(2020, 12, 1, 3)
#     text2 = 'パターンA'
#     # print(list_a)
#     return text2

# # カレンダーデータの取得
# def calendar_data():
#     text = work_calendar_app.calendar_input(2020, 12, 1, 3)
#     text = work_calendar_app.day_check(2020, 12, text, 3)
#     # text = work_calendar_app.day_check(2020, 12, text, 3)
#     return text

# # def calendar_data2():
# #     text = work_calendar_app.calendar_input(2020, 12, 1, 3)
# #     text = work_calendar_app.day_check(2020, 12, text, 3)
# #     return text


# class TextWidget(Widget):
#     # text = StringProperty()
#     text = ListProperty()
#     # list_a = ListProperty()
#     color = ListProperty([1,1,1,1])

#     def __init__(self, **kwargs):
#         super(TextWidget, self).__init__(**kwargs)
        # self.text = ''

    # def buttonClicked(self):
    #     # self.text = 'パターンB'
    #     self.text = self.ids["text_box"].text
    #     return self.text
    
# class WorkApp(App):
#     def __init__(self, **kwargs):
#         super(WorkApp,self).__init__(**kwargs)
#         self.title = '君のシフトは…'

#     def build(self):
#         return TextWidget()

# if __name__ == '__main__':
#     WorkApp().run()

    
#カレンダーの年数入力
val1 = input('年を入力してください。→')

#カレンダーの月を入力
val2 = input('月を入力してください。→')

#カレンダーの月を入力
val3 = input('日を入力してください。→')

#カレンダーの月を入力
val4 = input('１週間の労働日数を入力してください。→')

test = work_calendar_app.calendar_input(val1 , val2, val3, val4)
print(test)