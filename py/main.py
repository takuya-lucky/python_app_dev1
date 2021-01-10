import work_calendar_app
import work_member_app
import kivy
import japanize_kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import StringProperty , ListProperty
from kivy.uix.widget import Widget
from kivy.resources import resource_add_path
import cgi

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

# カレンダー情報の取得
shift = work_calendar_app.calendar_input()
# sorted_shift = sorted(shift, key=lambda s: s[0])
# print(sorted_shift)
print(shift)
