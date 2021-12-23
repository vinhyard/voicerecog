#gate.io api
from __future__ import print_function
#randomizer
import random
#speech recognition
import speech_recognition as sr
#python text to speech
import pyttsx3
#time module
from time import ctime
import time
#webbrowser
import webbrowser
#yfinance
import yfinance as yf
#gate.io api
import gate_api
from gate_api.exceptions import ApiException, GateApiException
#regular expression
import re
#pywhatkit
import pywhatkit as kit
#for weather
import requests, json
#webscraping for shoes
import lxml
from lxml import html
import pyjokes
import datetime
import threading
from queue import Queue
queue = Queue() 
from english_dictionary.scripts.read_pickle import get_dict
english_dict = get_dict()
botname = 'chupapi'
#automate
from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "",
    key = "",
    secret = ""
)
api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.WalletApi(api_client)
currency = 'USD' # str | Currency unit used to calculate the balance amount. BTC, CNY, USD and USDT are allowed. USDT is the default. (optional) (default to 'USDT')


#initialize voice recognizer
listener = sr.Recognizer()

engine = pyttsx3.init()


#name
class person:
    name = ''
    def setName(self, name):
        self.name = name


#words stored inside voice data
def exists(words):
    for word in words:
        if word in voice_data:
            return True


#talk function 
def talk(text):
    engine.say(text)
    engine.runAndWait()

#info-fetch
def infoman():
   
    try:    
        if exists(['tell me about', 'give me info about']):
        
            mad = str(kit.info(voice_data, return_value=True))
            talk(mad)
    except:
        pass
api_key=''
base_url='http://api.openweathermap.org/data/2.5/weather?'
#weatherman
def weather():
    if exists(['temperature in','weather in']):
 
        city_name = voice_data.lower().split()[-1].strip()
        completeurl=f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        response1 = requests.get(completeurl)
        x=response1.json()
        temper = float(x['main']['temp'])
        fahrenheit = round((temper - 273.15) * 9/5 + 32, 2)
        descriptio = x['weather'][0]['description']
        
        talk(f'temperature in {city_name} is currently' + str(fahrenheit) + 'degrees fahrenheit with' 
        + str(descriptio) )

#what day is it
def day():
    if exists(['what day is it']):

        e = datetime.date.today().weekday()
        dk = {4:'fun Friday', 5:'Saturday',3:'Thursday',2:'Wednesday',1:'tipsy tuesday',0:'monday',6:'sunday'}
   
        talk(dk[e])

        time.sleep(1)
        if dk[e] == 6:
            talk('casino opens tomorrow')
        elif dk[e] == 4:
            talk('have a wonderful weekend')



#english-dictionary
def eng():
    try:
        if exists(['definition', 'define']):

            man = voice_data.lower().split()[-1].strip()

            talk(english_dict[man])
    except:
        pass













#help find places to eat via yelp
#not working
def yelp():
    if exists(['food', 'best','restaurant']):
        city = voice_data.lower().split()[-1].strip()
        descriptor = voice_data.lower().split()[1].strip()
        pager = requests.get(f'https://www.yelp.com/search?find_desc={descriptor}&find_loc={city}')
        treer = html.fromstring(pager.content)
        numba1 = treer.xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div[1]/div[1]/div[2]/div/ul/li[9]/div/div/div/div[2]/div[1]/div/div[1]/div/div/h4/span/a/text()')
        numba2 = treer.xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div[1]/div[1]/div[2]/div/ul/li[10]/div/div/div/div[2]/div[1]/div/div[1]/div/div/h4/span/a/text()')
        numba3 = treer.xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div[1]/div[1]/div[2]/div/ul/li[11]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/h4/span/a/text()')
        webbrowser.get().open(f'https://www.yelp.com/search?find_desc={descriptor}&find_loc={city}')
        talk(f'here are the best {descriptor} in {city}')



#jokes
def joker():
    if exists(['tell me a joke', 'tell me something funny','joke']):
        joking = pyjokes.get_joke(language='en', category='neutral')
        talk(joking)


#stockfunction
def stockspeed():
    search_term = voice_data.lower().split(" of ")[-1].strip() #strip removes whitespace after/before a term in string  
    stocks = {  
        "apple":"AAPL",  
        "microsoft":"MSFT",  
        "facebook":"FB",  
        "tesla":"TSLA",  
        "bitcoin":"BTC-USD",
        'palantir':'PLTR',
        'dogecoin':'DOGE-USD',
        'ethereum':'ETH-USD',
        'cardano':'ADA-USD', 'binance':'BNB-USD','tether':'USDT-USD',
        'litecoin':'LTC-USD', 'spy':'SPY','amd':'AMD','uber':'UBER', 'alibaba':'BABA'  
        }  
    try:  
        stock = stocks[search_term]  
        stock = yf.Ticker(stock)  
        price = stock.info["regularMarketPrice"]  
  
        talk(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
  
    except:  
        talk('oops, something went wrong')  

#shoe web scraper
def shoes():
    if exists(['shoe release', 'new shoes','shoe dates']):
        page = requests.get('https://sneakernews.com/release-dates/')

        tree = html.fromstring(page.content)
        availdate1 = tree.xpath('//*[@id="sneaker-release-main"]/div/section/div[2]/div/div[1]/a/div/span/text()')
        availdate11 = tree.xpath('//*[@id="sneaker-release-main"]/div/section/div[2]/div/div[1]/a/div/p/text()')
        availdate2 = tree.xpath('//*[@id="sneaker-release-main"]/div/section/div[2]/div/div[2]/a/div/span/text()')
        availdate22 = tree.xpath('//*[@id="sneaker-release-main"]/div/section/div[2]/div/div[2]/a/div/p/text()')
        availdate3 = tree.xpath('//*[@id="sneaker-release-main"]/div/section/div[2]/div/div[3]/a/div/span/text()')
        availdate33 = tree.xpath('//*[@id="sneaker-release-main"]/div/section/div[2]/div/div[3]/a/div/p/text()')
        talk(f'{availdate11[0]} will be released on {availdate1[0]}')
        time.sleep(1)
        talk(f'{availdate22[0]} will be released on {availdate2[0]}')
        time.sleep(1)
        talk(f'{availdate33[0]} will be released on {availdate3[0]}')
        time.sleep(1)


#tells top 5 trending stock news
def newspaper():
    if exists(['stock news','top news']):
        pager = requests.get('https://www.cnbc.com/stocks/')
        treer = html.fromstring(pager.content)
        news1 = treer.xpath('//*[@id="SectionWithoutNative-TrendingNowBreaker-8"]/div/div/ul/li[1]/div[2]/a/text()')
        new3_news = treer.xpath('//*[@id="SectionWithoutNative-TrendingNowBreaker-8"]/div/div/ul/li[2]/div[2]/a/text()')
        new4_news = treer.xpath('//*[@id="SectionWithoutNative-TrendingNowBreaker-8"]/div/div/ul/li[3]/div[2]/a/text()')
        new5_news = treer.xpath('//*[@id="SectionWithoutNative-TrendingNowBreaker-8"]/div/div/ul/li[4]/div[2]/a/text()')
        new6_news = treer.xpath('//*[@id="SectionWithoutNative-TrendingNowBreaker-8"]/div/div/ul/li[5]/div[2]/a/text()')
        new_news2 = re.sub('[^A-Za-z0-9]+', ' ', news1[0])
        new_news3 = re.sub('[^A-Za-z0-9]+', ' ', new3_news[0])
        new_news4 = re.sub('[^A-Za-z0-9]+', ' ', new4_news[0])
        new_news5 = re.sub('[^A-Za-z0-9]+', ' ', new5_news[0])
        new_news6 = re.sub('[^A-Za-z0-9]+', ' ', new6_news[0])
        talk(f'top 5 trending stock news:{new_news2} ')
        time.sleep(2)
        
        talk(new_news3)
        time.sleep(2)
        talk(new_news4)
        time.sleep(2)
        talk(new_news5)
        time.sleep(2)
        talk(new_news6)


# Hangman game

WORDLIST_FILENAME = "c:/Users/User1/Desktop/mit/Intro-to-Computer-Science-and-Programming-Using-Python/Problem Sets/Problem Set 3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
   
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = loadWords()
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
        
    for i in range(len(secretWord)):
      if secretWord[i] not in lettersGuessed:
        return False
        break
        
    

    return True
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    nio = secretWord
    for i in range(len(secretWord)):
      if secretWord[i] not in lettersGuessed:
        nio = nio.replace(secretWord[i], '_ ')

    return nio


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
 
    import string
    nio = string.ascii_lowercase
    for i in range(len(string.ascii_lowercase)):
      if string.ascii_lowercase[i] in lettersGuessed:
        nio = nio.replace(string.ascii_lowercase[i], '')
    return nio


def hangman(secretWord):
    mistakesMade = 8
    lettersGuessed = []
    matt = '_ '
    talk('Welcome to the game of Hangman!')
    time.sleep(.5)
    talk(f'I am thinking of a word that is {str(len(secretWord))} letters long')
    while mistakesMade >= 1 or isWordGuessed(secretWord, lettersGuessed) == False:
      print("-----------")
      print('You have', mistakesMade, 'guesses left')
      talk(f'You have {mistakesMade} guesses left. ')
      print('Available letters:', getAvailableLetters(lettersGuessed))
      chad = input('Please guess a letter:')
      
      chad.lower
      if str(chad) in secretWord:
        if str(chad) in lettersGuessed:
          print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
          lettersGuessed.append(str(chad))
          print(f'Good guess: {getGuessedWord(secretWord, lettersGuessed)}')
          talk('Great guess!')
          if matt not in getGuessedWord(secretWord, lettersGuessed):
            print("-----------") 
            print('Congratulations, you won!')
            talk('Wow! Good win')
            break
      elif str(chad) not in secretWord:
        print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
        mistakesMade -= 1
        if mistakesMade == 0: 
          print('-----------')
          print('Sorry, you ran out of guesses. The word was', secretWord,'.')
          talk('Sorry! Game over')
          break
      else: print('Oops! Try again')
      lettersGuessed.append(str(chad))


   


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

#get gate.io balance
def balance():
    try:
    # Retrieve user's total balances
        api_response = api_instance.get_total_balance(currency=currency)
        chad = str(api_response)
        chadamount = str(chad[-40:-34])
        talk('You have a balance of: ' + chadamount + 'dollars')

    except GateApiException as ex:
        talk("It did not work. Try again later")
    except ApiException as e:
        talk("Oh no. An error occured")
#coinflip
def coinflip1():
    if exists(['flip a coin','heads or tails','can you flip a coin']):
        coinflip = random.choice([1,2])
        if coinflip == 1:
            talk('heads')
        else:
            talk('tails')

#greeting
def greetings():
    if exists(['hey', 'hi', 'hello','howdy']):
        greeting = ["sup bitch, how can i help you", f'hey, what"s up? {person_obj.name}', f'hello, {person_obj.name}']
        randogreet = greeting[random.randint(0,len(greeting)-1)]
        talk(randogreet)

def name1():
    if exists(['who are you', 'tell me your name']):
        namer = [f'i go by {botname}', f'my name is {botname}', f'my friends call me {botname}']
        randoname = namer[random.randint(0,len(namer)-1)]
        if person_obj.name:
            talk(randoname)
        else:
            talk(f'my name is {botname}. what"s your name?')
    if exists(['my name is']):
        person_name = voice_data.split('is')[-1].strip()
        talk(f'okay, i will remember that {person_name}')
        person_obj.setName(person_name)  # remember name 

#google search
def googlesearch():
    if exists(["search for", 'look for']) and 'youtube' not in voice_data:  
        search_term = voice_data.split("for")[-1]
        print(search_term)  
        url = f"https://google.com/search?q={search_term}"  
        webbrowser.get().open(url)  
        talk(f'Here is what I found for {search_term} on google') 
#derivatives and antiderivative calculator and volumes

def derivativecalculator():
    l = {'antiderivative of sine':'negative cosine x plus constant', 
'derivative of sin': 'cosine x','antiderivative of tan':
'natural log of secant x', 'derivative of cosine': 'negative sine x',
'derivative of tan':'secant squared x', 'derivative of secant':'secant x tan x',
'derivative of inverse tan':'one over one plus x squared', 'derivative of cotan x':'negative cosecant x squared',
'derivative of natural log':'one over x','derivative of log':'one over x natural log a', 'antiderivative of one over x': 'natural log x', 'derivative of arc sine':'one over square root of one minus x squared',
'derivative of arc tan':'one over one plus x squared', 'volume by disk': 'pi times integral of radius x squared', 'volume by washer':'pi times integral of f x squared minus g x squared',


}
    try:
        if exists(l[voice_data]):
            talk(l[voice_data])
    except:
        pass

#play youtube
def yout():
    if exists(['youtube']):
        william = kit.playonyt(voice_data,use_api=True)
        talk(f'playing {voice_data[1:-3]} on youtube')
        

#time
def timewatch():
    if exists(['what"s the time', 'tell me the time', 'what time is it']):
        time = ctime().split(' ')[3].split(':')[0:2]
        if time[0] == '00':
            hours = '12'
        else:  
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        talk(time)

#listen for audio and convert to text:
def listen():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        listener.energy_threshold = 200
        voice = listener.listen(source)
        voice_data = ''    
        try:
            
            voice_data = listener.recognize_google(voice)
            


        except sr.UnknownValueError: #error: jarvis does not understand
            pass
        except sr.RequestError:
            talk('Sorry, the service is down') # error: recognizer not connected
        
        return voice_data.lower()

#response
def response(voice_data):
    
    #1.) Greeting
    greetings()

    #2.) name
    name1()

    #3.) Coinflip
    coinflip1()

    #4.) time
    timewatch()

    # 5: search google  
    googlesearch()

    # 6: gate.io balance
    if exists(['portfolio', 'crypto','balance']):
        balance()

    # 7: get stock price  
    if exists(["price of"]):  
        stockspeed()

    #8:derivative calculator
    derivativecalculator()

    #9:info fetch
    infoman()

    #10:weather
    weather()
    #11:youtube
    yout()
    #12: shoe release dates
    shoes()
    #13: financial stock news
    newspaper()
    #14: searches for restaurants
    yelp()
    #15:hangman game
    if exists(['lets play a game','want to play a game','wanna play hangman','hangman','play game']):
        secretWord = chooseWord(wordlist).lower()
        hangman(secretWord)
    #16:jokes
    joker()

    #17: day
    day()

    #eng dictionary
    eng()
    #quit
    if exists(["exit", "quit", "goodbye"]):  
        talk("going offline")  
        exit()



time.sleep(.75)

person_obj = person()
while (1):
    voice_data = listen()


    response(voice_data)
