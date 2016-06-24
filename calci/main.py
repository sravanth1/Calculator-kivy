import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.textinput import TextInput
import re
from kivy.logger import Logger
from kivy.resources import resource_find
from kivy.lang import Builder
from kivy.core.image import Image
from kivy.uix.image import AsyncImage
from kivy.properties import StringProperty


class My(App):
	def build(self):
		return Myapp()


class Myapp(FloatLayout):
	def callback(self,instance):
		if instance.text=='add':
			if not self.t1.text or not self.t2.text:
				self.t3.text="Nan"
			else:
				self.t3.text=str(kivy.parser.parse_float(self.t1.text)+kivy.parser.parse_float(self.t2.text))
		if instance.text=='multiply':
			if not self.t1.text or not self.t2.text:
				self.t3.text="Nan"
			else:
				self.t3.text=str(kivy.parser.parse_float(self.t1.text)*kivy.parser.parse_float(self.t2.text))
		if instance.text=='subtract':
			if not self.t1.text or not self.t2.text:
				self.t3.text="Nan"
			else:
				self.t3.text=str(kivy.parser.parse_float(self.t1.text)-kivy.parser.parse_float(self.t2.text))
		if instance.text=='division':
			if self.t1.text and self.t2.text:
				if self.t2.text!=0:
					self.t3.text=str(kivy.parser.parse_float(self.t1.text)/kivy.parser.parse_float(self.t2.text))
				else:
					self.t3.text="Nan"
			else:
				self.t3.text="Nan"

	def __init__(self, **kwargs):
		super(Myapp, self).__init__(**kwargs)
		btn1 = Button(text='add', size_hint=(.1,.1),pos_hint= {'x': .1,'top': .2})
		btn2 = Button(text='subtract', size_hint=(.1,.1),pos_hint= {'x': .3,'top': .2})
		btn3=Button(text='multiply',size_hint=(.1,.1),pos_hint= {'x': .5,'top': .2})
		btn4=Button(text='division',size_hint=(.1,.1),pos_hint= {'x': .7,'top': .2})
		self.add_widget(Label(text='calculator',pos_hint={'center_x': .5, 'center_y': 0.9},font_size=100))
		self.add_widget(Label(text='first',pos_hint= {'x': -0.375,'top': 1.05},font_size=14))
		self.add_widget(Label(text='second',pos_hint= {'x': -0.075,'top': 1.05},font_size=14))
		self.t1=TextInput(multiline=False,size_hint_x=.2, size_hint_y=.1,pos_hint= {'x': .1,'top': .5})
		self.t2=TextInput(multiline=False,size_hint_x=.2, size_hint_y=.1,pos_hint= {'x': .3,'top': .5})
		self.t3=TextInput(text='',size_hint_x=.2, size_hint_y=.1,pos_hint= {'x': .5,'top': .5})
		self.add_widget(self.t1)
		self.add_widget(self.t2)
		self.add_widget(self.t3)
		self.add_widget(btn1)
		self.add_widget(btn2)
		self.add_widget(btn3)
		self.add_widget(btn4)
		#print "111111111111111111111"
		btn1.bind(on_press=self.callback)
		btn2.bind(on_press=self.callback)
		btn3.bind(on_press=self.callback)
		btn4.bind(on_press=self.callback)
		#print "22222222222222222222"

		

if __name__=='__main__':
	print "sra"
	My().run()


