import json
import requests
import pyjokes
from dadjokes import Dadjoke
from pyowm import OWM

# initalize OWM weather API & token
owm = OWM('10fe228afe45ed36923e6bb66c185efa')
mgr = owm.weather_manager()


class DadBot:

    # finds location from weather command message
    def parseLocation(message):
        location = ""
        # split message string into array 
        wordArr = message.split(" ")
        # initialize word count
        wordCount = 0;

        # iterate through string array for keywords ("in" and "?")
        for i in wordArr:
            # track word count
            wordCount += 1
            # if current word is in, location string should be after
            if i == "in":
                location = wordArr[wordCount]
            # if message contains '?', location is behind it
            if '?' in location:
                location = location[:-1]
    
        return location
    # returns a weather info messaage based on location
    def getWeather(location):
        observation = mgr.weather_at_place(location)
        w = observation.weather
        # get detailed weather status
        weather = w.detailed_status
        
        # get temperature
        tempDictionary = w.temperature('fahrenheit')
        temperature = tempDictionary.get('temp')
        
        # create weather dictionary
        location = location.capitalize()
        weatherDict = {'location' : location, 'temperature' : temperature, 'weather': weather}
        
        # return formatted message
        return (f"{weatherDict['weather']} and it's {weatherDict['temperature']}\xb0F in {weatherDict['location']} today!")
    
    def getJoke():
        # retrieve joke string from Dadjoke API
        dadjoke = Dadjoke()
        return dadjoke.joke
    
    def getGeekyJoke():
        geekyJoke = pyjokes.get_joke(language= 'en', category= 'neutral')
        return geekyJoke

    def getHiJoke(message):
        # split message into array by spaces
        wordArr = message.split(" ")
        # remove "I'm" from word array
        if message.startswith("i\'m"):
            wordArr.pop(0)
        elif message.startswith("I am"):
            wordArr.pop(0)
            wordArr.pop(0)
        s = ' '.join(wordArr)
        # return Hi quip
        return (f"Hi {s.capitalize()}! I'm DadBot!")
    
    def getQuote():
        # retrieve data from zenquotes API
        response = requests.get("https://zenquotes.io/api/random")
        jsonData = json.loads(response.text)
        
        # returns message as "[quote] - [author]"
        #return (jsonData[0]['q'] + "..." + jsonData[0]['a'] );
        return ("Here's a quote by " + jsonData[0]['a'] + " ... " + jsonData[0]['q'])

    def getHelpMsg():
        #build string (for neatness)
        helpMsg = "Say hi to Your Dad Bot by saying Hi or Hello\n"
        helpMsg += "Ask for the weather. (Ex: What's the weather like in Orlando?)\n"
        helpMsg += "Ask me to tell a joke!\n"
        helpMsg += "Ask me for life advice/quotes!\n"
        helpMsg += "Start a sentence with \"I\'m\""
        return helpMsg
