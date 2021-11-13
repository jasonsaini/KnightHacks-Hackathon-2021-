import speech_recognition as sr
import pyttsx3

class SpeechHandler:
    #initalize text-to-speech engine
    ttsEngine = pyttsx3.init()
    
    def __init__():
        # Set voice to male
        voices = ttsEngine,getProperty('voices')
        ttsEngine.setProperty('voice', voices[0].id)

        """ 
        SET VOLUME
        volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
        engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
        
        
        SET RATE   
        rate = engine.getProperty('rate')   # getting details of current speaking rate
        engine.setProperty('rate', 125)     # setting up new voice rate
        
        """
    
    def speak(message):
        engine.say(message)
        engine.runAndWait()
        engine.stop()
        return
