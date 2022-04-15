import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
from database import get_answer_from_memory



listener= sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Welcome to the BAIUST help point. if you have any query. Just ask me")





def takeCommand():
    # It takes microphone input from the user and returns string output

    try:
        with sr.Microphone() as source:

            print("Listening...")

            audio = listener.listen(source)

            query = listener.recognize_google(audio)
            query = query.lower()

            print(query)

    except Exception as e:
        pass

    return query


if __name__ == "__main__":
        wishMe()
   # while True:
        # if 1:
        query = takeCommand()
        print(get_answer_from_memory(query))
        speak(get_answer_from_memory(query))

        ans = get_answer_from_memory(query)

        if 'Here is all faculty members of Department of Computer Science & Engineering.' in ans:
            webbrowser.open("https://cse.baiust.edu.bd/academic_personnel")

        elif 'Here is all faculty members of Department of Electric & Electronic Engineering.' in ans:
            webbrowser.open("https://eee.baiust.edu.bd/academic_personnel")

        elif 'Here is all faculty members of Department of Civil Engineering.' in ans:
            webbrowser.open("https://ce.baiust.edu.bd/academic_personnel")

        elif 'Here is all faculty members of Department of Business Administration.' in ans:
             webbrowser.open("https://dba.baiust.edu.bd/academic_personnel")

        elif 'Here is all faculty members of Department of English.' in ans:
            webbrowser.open("https://eng.baiust.edu.bd/academic_personnel")

        elif 'Here is all faculty members of Department of law.' in ans:
            webbrowser.open("https://law.baiust.edu.bd/academic_personnel")

        elif 'how many department' in query:
            speak('There are 6 departments in BAIUST. Department of Computer Science & Engineering, Department of Electric & Electronic Engineering, Department of Civil Engineering, Department of Business Administration, Department of English, & Department of law')

        elif 'student portal' in query:
            webbrowser.open("https://iumss.baiust.edu.bd/")
            speak('Here is the student portal of BAIUST. you can find all of your academic information by signing in')

        elif 'location' in query:
            speak("Here is the exact location of BAIUST. Follow the map, and you will be the BAIUST campus ")
            webbrowser.open("https://www.google.com/maps/place/Bangladesh+Army+International+University+of+Science+and+Technology+(BAIUST)/@23.4773671,91.1112492,17z/data=!4m5!3m4!1s0x37547b8b07235dcd:0x1f168ba787f7f6d2!8m2!3d23.4770929!4d91.1136854")


        else:
            speak("Sorry!! I don't get it. Ask me anything else.")





