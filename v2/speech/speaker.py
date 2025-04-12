import pyttsx3

class Narrator:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)

        # Use sweet British female voice
        self.engine.setProperty("voice", "com.apple.voice.enhanced.en-GB.Kate")  
        print("[INFO] Voice set to: Kate (British English Female)")

    def speak(self, text):
        polite_text = f"{text.strip().capitalize()}."
        self.engine.say(polite_text)
        self.engine.runAndWait()
