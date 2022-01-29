import pyautogui 
import speech_recognition as sr

# turn on internet before run the code
# the function is for take input of your voice

def takecommand():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

# this function is for type your text

def typer(inp):
    try:
        legnth = len(inp)
        print(legnth)
        a = 0
        print(inp)
        while True:
            index = inp[a]
            pyautogui.press(index)
            a = a+1
            if a >= legnth:
                break
    except:
        print("string not found")


# if you have no internet connection 
# then the function print NONE
# so please turn on internet

while True:
    query = takecommand()
    if 'exit' in query:
        break
    elif 'enter' in query:
        pyautogui.press("enter")
    
    typer(str(query))
