import pyttsx3

def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 180)
    print("  ")
    print(f"Bot : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("  ")





