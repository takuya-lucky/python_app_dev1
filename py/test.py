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
import random

list_a = [['a'], ['b'],['c'],['d']]
list_b = [['a'], ['d']]
list_c = ['2021/01/04/Monday','朝勤務'], [['2021/01/05/Monday'], '昼勤務']
list_d = [1,2,3,4,5,6,1]
list_e = [['a',1],['c',3],['z',2]]
a = 1
y = 0
# for x in range(1):
#     list_w = list_c[1]
list_e.sort()
list_e = sorted(list_e, key=lambda s: s[1])
# print(list_e)
# print(list_c)
# if (['2021/01/04/Monday','朝勤務']) in list_c:
#     a = list_c.count(['2021/01/04/Monday','朝勤務'])
#     print(list_c)
key = '2021/01/04/Monday'
l_even = [i for i in list_c if key in i]
print(l_even)