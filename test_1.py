import speech_recognition as sr
import pyttsx3 as p

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say Something")
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio), "\n")
        except Exception as e:
            print(e)
