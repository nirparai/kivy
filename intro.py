import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2

		self.add_widget(Label(text="UserName : "))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="Password : "))
		self.password = TextInput(multiline=False, password=True)
		self.add_widget(self.password)

class SimpleKivy(App):
	def build(self):
		return LoginScreen()

if __name__ == "__main__":
	SimpleKivy().run()
