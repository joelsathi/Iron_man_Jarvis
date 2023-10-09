import speech_recognition as sr
import pyttsx3 as p
from web_automation import music
from meaning_finder import info
from movie_review import movie
from weather import weather
from watch_movie import watch_movie
from whatsapp_messager import Whatsapp
from Google_It_JARVIS import Google_It
from open_apliction import Open_application
import time as t

# Hey guys this is Joel with creating a voice recognition system called JARVIS
# This is really cool!!!!



r = sr.Recognizer()
engine = p.init()
engine.say("Hello sir this is JARVIS!, How are you doing sir?")
engine.runAndWait()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

with sr.Microphone() as source:
    # This is to adjust the noise so that JARVIS could understand without any error
    r.adjust_for_ambient_noise(source, duration=1)
    # This is used to get the text from the user as voice
    text = r.listen(source)
    try:
        recognized_text = r.recognize_google(text)
        print(recognized_text)
        if "fine" in recognized_text.lower() or "good" in recognized_text.lower():
            engine.say("Very well sir!")
        else:
            engine.say("I hope you'll overcome what are facing sir! Because God will never let his children down sir!")
            engine.runAndWait()
    except Exception as e:
        print(e)
        engine.say("What would you like to do sir?")
        engine.runAndWait()
    while True:
        print("Say Something!")
        print("Eg: Play video\nWatch movie\nGoogle something\nWeather forecast details\nGet information\nGet movie review\nFind meaning\n\nSay Bye to exit!")
        text1 = r.listen(source)
        try:
            recognized_text1 = r.recognize_google(text1)
            print(recognized_text1)

            # This will play music
            if "music" in recognized_text1.lower() or "play video" in recognized_text1.lower():
                engine.say("Which music video you want me to play sir?")
                engine.runAndWait()
                text_music = r.listen(source)
                try:
                    recognized_text_music = r.recognize_google(text_music)
                    print(recognized_text_music)
                    bot_music = music()
                    bot_music.music(recognized_text_music)
                except Exception as e:
                    print(e)

            # This will search for movies to watch
            elif "watch movie" in recognized_text1.lower():
                bot_movie = watch_movie()
                bot_movie.movie_search()

            # This will show the movie review
            elif "review" in recognized_text1.lower():
                engine.say("Which movie review you want to know sir?")
                engine.runAndWait()
                text_movie = r.listen(source, timeout=15)
                try:
                    recognized_text_movie = r.recognize_google(text_movie)
                    print(recognized_text_movie)
                    bot_movie = movie()
                    bot_movie.get_review(recognized_text_movie)
                except Exception as e:
                    print(e)

            # This will get the weather info
            elif "weather" in recognized_text1.lower():
                engine.say("Which city's weather you want me to search sir?")
                engine.runAndWait()
                text_weather = r.listen(source, timeout=20)
                try:
                    recognized_text_weather = r.recognize_google(text_weather)
                    print(recognized_text_weather)
                    bot_weather = weather()
                    bot_weather.weather(recognized_text_weather)
                except Exception as e:
                    print(e)

            # This will find the information of the given phrase or word
            elif "information" in recognized_text1.lower():
                engine.say("Which information you want to get know sir?")
                engine.runAndWait()
                text_info = r.listen(source, timeout=20)
                try:
                    recognized_text_info = r.recognize_google(text_info)
                    print(recognized_text_info)
                    bot_info = info()
                    bot_info.get_info(recognized_text_info)
                except Exception as e:
                    print(e)

            # This will send messages through What'sapp  Keep your phone near you!
            elif "send message" in recognized_text1.lower():
                engine.say("Whom do you want to sent the message sir?")
                engine.runAndWait()
                text_name = r.listen(source, timeout=20)
                try:
                    recognized_text_name = r.recognize_google(text_name)
                    print(recognized_text_name)
                except Exception as e:
                    print(e)
                engine.say("What message you want to send sir?")
                engine.runAndWait()
                text_message = r.listen(source, timeout=120)
                try:
                    recognized_text_message = r.recognize_google(text_message)
                    print(recognized_text_message)
                except Exception as e:
                    print(e)
                engine.say("Please open your what'sapp in your mobile phone and open what'sapp web ,sir!")
                try:
                    bot_whatsapp = Whatsapp()
                    bot_whatsapp.Whatsapp_message(recognized_text_name, recognized_text_message)
                except Exception as e:
                    print(e)

            # This will search your query in google
            elif "google" in recognized_text1.lower() or "search" in recognized_text1.lower():
                engine.say("What do you want me to search in Google sir?")
                engine.runAndWait()
                text_query = r.listen(source, timeout=120)
                try:
                    recognized_text_google = r.recognize_google(text_query)
                    print(recognized_text_google)
                    bot_google = Google_It()
                    bot_google.Google_Jarvis(recognized_text_google)
                except Exception as e:
                    print(e)

            # This will open apps
            elif "apps" in recognized_text1.lower():
                engine.say("Which app do you want me to open sir?")
                engine.runAndWait()
                text_app_name = r.listen(source, timeout=120)
                try:
                    recognized_text_open = r.recognize_google(text_app_name)
                    print(recognized_text_open)
                    bot_open_application = Open_application()

                    # This will open up the calculator
                    if "calculator" in recognized_text_open.lower():
                        bot_open_application.Open_calculator()
                    # This will open up the calendar
                    elif "calendar" in recognized_text_open.lower():
                        bot_open_application.Open_calendar()
                    # This will open up the clock and alarms app
                    elif "clock" in recognized_text_open.lower():
                        bot_open_application.Open_clock()
                    # This will open the notepad
                    elif "notepad" in recognized_text_open.lower():
                        bot_open_application.Open_notepad()
                    # This will open up the Camera app say Cheese!!!!
                    elif "camera" in recognized_text_open.lower():
                        bot_open_application.Open_Camera()
                    # This will open up the mailbox
                    elif "email" in recognized_text_open.lower():
                        bot_open_application.Open_mail()
                    # This will open a new word document
                    elif "word" in recognized_text_open.lower():
                        bot_open_application.Open_word()
                    # This will open up a new Excel document
                    elif "excel" in recognized_text_open.lower():
                        bot_open_application.Open_excel()
                    # This will open up a new Power point document
                    elif "powerpoint" in recognized_text_open.lower():
                        bot_open_application.Open_powerpoint()
                    # This will open up Pycharm
                    elif "pycharm" in recognized_text_open.lower():
                        bot_open_application.Open_pycharm()
                    # This will open up the IDLE
                    elif "idle" in recognized_text_open.lower():
                        bot_open_application.Open_IDLE()
                    # This will open Telegram app
                    elif "telegram" in recognized_text_open.lower():
                        bot_open_application.Open_telegram()
                    # This will open the Zoom app
                    elif "zoom" in recognized_text_open.lower():
                        bot_open_application.Open_Zoom()
                    else:
                        engine.say("I'm not programmed yet to open the specific file sir!")

                except Exception as e:
                    print(e)

            # this will stop the bot
            elif "bye" in recognized_text1.lower():
                engine.say("Have a nice day sir!!")
                engine.runAndWait()
                break

            elif "what's your name" in recognized_text1.lower():
                engine.say("JARVIS")
                engine.runAndWait()

            elif "how are you" in recognized_text1.lower():
                engine.say("I am very well sir and thank you for asking sir!")
                engine.runAndWait()

            elif "who built you" in recognized_text1.lower():
                engine.say("I'm built by Joel")
                engine.runAndWait()

            elif "what can you do" in recognized_text1.lower():
                things = ["I can play video",
                          "I can google anything for you",
                          "I can search the weather for you",
                          "I can get movies for you to watch",
                          "I can get movie reviews",
                          "I can search information for you",
                          "I can send messages for you through Whatsapp",
                          "I can open apps for you",
                          "Almost everything I expect sir",]
                engine.say([phrase for phrase in things])
                print([phrase for phrase in things])
                t.sleep(2)
                engine.runAndWait()

            else:
                engine.say("Sorry sir I haven't yet programmed to that task!!")
                engine.runAndWait()


        except Exception as e:
            print(e)
