from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("design.kv")

class MyLayout(Widget):
	pass

class HomePredictorApp(MDApp):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	HomePredictorApp().run()