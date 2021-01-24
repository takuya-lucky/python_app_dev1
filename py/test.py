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

list_a = [['a'], ['b']]
if ['b'] in list_a:
    print('true')
else:
    print('false')