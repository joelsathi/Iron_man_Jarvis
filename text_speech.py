import pyttsx3 as p

engine = p.init()
voices = engine.getProperty("voices")
# The index 0 is for male voice and the index 1 is for female voice
engine.setProperty("voice", voices[1].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
"""
This will give the property of the volume
The range of the volume will be between 0 and 1
"""
# volume = engine.getProperty("volume")
# print(volume)

engine.say("How are you doing?")
engine.say("What would you like me to do for you?")
engine.runAndWait()

