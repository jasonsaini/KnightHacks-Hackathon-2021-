import speech_recognition as sr
import pyttsx3

#initalize text-to-speech engine
ttsEngine = pyttsx3.init()
#initalize speech-to-text engine
recognizer = sr.Recognizer()

# Set voice to male
voices = ttsEngine.getProperty('voices')
ttsEngine.setProperty('voice', voices[0].id)

# set volume
volume = ttsEngine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
ttsEngine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# set rate   
rate = ttsEngine.getProperty('rate')   # getting details of current speaking rate
ttsEngine.setProperty('rate', 165)     # setting up new voice rate

class SpeechHandler:
   
   # translates any text passed in to audio (speaking)
    def speak(message):
        ttsEngine.say(message)
        ttsEngine.runAndWait()
        ttsEngine.stop()
        return

    def listen():
        #print("Say something...")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration = 0.2)
            audio = recognizer.listen(source, timeout= None, phrase_time_limit= 5)
            # return transcribed audio as string
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""