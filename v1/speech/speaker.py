import pyttsx3

class Narattor:
	def __init__(self):
		self.engine = pyttsx3.init()
		self.engine.setProperty('rate', 160) # Speed
		self.engine.setProperty('volume', 1.0) # Volume

	def speak(self, text):
		self.engine.say(text)
		self.engine.runAndWait()