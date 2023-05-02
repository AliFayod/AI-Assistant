import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import random
import Apps



# intialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)  # 0 = male , -1 = female
activationWord = 'computer'
your_name = 'Ali'
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
AppId = 'XVX5EP-7JGW8ULH2X'
wolframClient = wolframalpha.Client(AppId)
hilist = [f"oh!, good morning {your_name}...,I'm redy to serve you", f"Hi {your_name}..., how can I serve you!",
          f"hello {your_name} How are you?", f"hello!, Nice to hear your voice {your_name}...,give me your command!",
          f"Hi {your_name}, I hope you are doing well!..., can I help you!"]

donelist = ['any other command','do you want to ask me more',"it's done..., can I help you again!","the command is done my boos",f"lucky to serve you {your_name}...,anything else!"]

byelist = [f"oh,ok Goodbye {your_name}...,be sure I'm ready to serve you any time...,bye ", f"bye.. bye {your_name}",
          f"bye {your_name}..., I'll miss you", f"bye!...,that was nice to hear your voice {your_name}"]
welcomelist = [f'Welcome {your_name}..., how can I help you!',f'Nice..., you are here {your_name}..., What will we do today!',f"Hi {your_name}, how can I serve you."]


def talk(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():

    listener = sr.Recognizer()
    print('Listening for a command')
    with sr.Microphone() as source:
        # listener.adjust_for_ambient_noise(source)
        listener.pause_threshold = 1
        input_speech = listener.listen(source)
    try:

        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en-US')
        print(f'The input speech was:{query}')

    except Exception as exception:
        print("Oops! Didn't catch that")
        talk("Oops! Didn't catch that")
        print(exception)
        return "None"

    return query


def search_wikipedia(text=''):
    searchResults = wikipedia.search(text)
    if not searchResults:
        print('No wikipedia result')
        return 'No result received'
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']


def search_wolframalpha(query=''):
    response = wolframClient.query(query)
    if response['@success'] == 'false':
        return 'Could not compute'

    else:
        result = ''
        pod0 = response['pod'][0]
        pod1 = response['pod'][1]
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or (
                'definition' in pod1['@title'].lower()):
            result = listOrDict(pod1['subpod'])
            return result.split('(')[0]
        else:
            question = listOrDict(pod0['subpod'])
            return question.split("(")[0]


if __name__ == '__main__':
    talk(random.choice(welcomelist))
    while True:
        query = parseCommand().lower().split()

        #Stop AI_Assistant
        if query[0] == 'thank' or query[0] == 'okay' or query[0] == 'ok' or query[0] == 'no':
            if 'stop' in query or 'done' in query or ('thank' in query and 'you' in query) or 'thanks' in query:
                talk(random.choice(byelist))
                break
        #Say Hi
        if (query[0] == 'say'):
            if 'hi' in query or "hello" in query:
                talk(random.choice(hilist))
            else:
                query.pop(0)
                speech = ' '.join(query)
                talk(speech)

        #Open URL
        if query[0] == 'go' and query[1] == 'to':
            query = ' '.join(query[2:])
            webbrowser.get('chrome').open_new(query)
            talk('Opening...')
            talk(random.choice(donelist))

        #Wikipedia
        if query[0] == 'wikipedia':
            query = ' '.join(query[1:])
            talk('Searching ...')
            talk(search_wikipedia(query))

        #Caculation
        if query[0] == 'compute' or query[0] == 'calculate':
            query = ' '.join(query[1:])
            try:
                result = search_wolframalpha(query)
                talk('computing...')
                talk(result)
                talk(random.choice(donelist))
            except:
                talk('sorry unable to compute.')

        #Open Applications
        if (query[0] == 'open'):
            if 'application' in query:
                query.remove("application")
            if 'please' in query:
                query.remove('please')
            query = ' '.join(query[1:])

            try:
                talk("opening...")
                Apps.openApp(query)
                talk(random.choice(donelist))
            except:
                talk("I'am sorry couldn't find the application, any other command")
        #YouTube
        if (query[0] == 'find' or query[0] == 'look' or query[0] == 'search') and (
                query[1] == 'on' or query[1] == 'for' or query[1] == 'about') and ('youtube' in query):

            if 'search' in query:
                query.remove('search')
            if 'about' in query:
                query.remove('about')
            if 'find' in query:
                query.remove('find')
            if 'looking' in query:
                query.remove('looking')
            if 'youtube' in query:
                query.remove('youtube')
            if 'on' in query:
                query.remove("on")
            if 'for' in query:
                query.remove('for')
            if 'please' in query:
                query.remove('please')
            query = ' '.join(query)
            try:
                webbrowser.get('chrome').open_new(f'youtube.com/results?search_query={query}')
                talk('searching...')
                talk('enjoy on youtube...')
                talk(random.choice(donelist))
            except:
                talk('Unable to search.')

        #Close Application
        if query[0] == 'close':

            if 'please' in query:
                query.remove('please')
            if 'the' in query:
                query.remove('the')
            if 'application' in query:
                query.remove('application')

            query = ' '.join(query[1:])
            talk("colsing...")
            Apps.openApp(query,True)
