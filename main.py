import openai #OpenAI API library
import pyttsx3 #text-to-speech conversion
import speech_recognition as sr #speech-to-text conversion


# Retrieve api key from file
with open('apiKey.txt', 'r') as file:

    # Read the contents of the file
    openai.api_key = file.read()

#*******************************************
#*********FUNCTIONS DEFINITION**************
#*******************************************

#Function that accepts audio by microphone and convert into text
def listener():
    # Set error variable to 0
    error = 0

    # Create a recognizer object
    r = sr.Recognizer()

    # Set microphone as audio source
    with sr.Microphone() as source:
        print("Speak now:")
        audio = r.listen(source)

    # Convert audio to text
    try:
        prompt = r.recognize_google(audio, language='it-IT') # Set language to Italian
        
    except :
        prompt = "Generic Error"
        error = 1

    print (prompt)    
    return prompt, error

#Function that calls OpenAI service with a prompt and returns the response
def callCompletion(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=360,
        top_p=1,
        best_of=20,
        frequency_penalty=0.5,
        presence_penalty=0
            )
    
    response = response.choices[0].text
    print (response)   
    return response

#Function that converts text into audio
def textToAudio(text):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Set the text-to-speech engine properties
    engine.setProperty('rate', 150)  # Set the speaking rate (words per minute)
    engine.setProperty('volume', 1)  # Set the volume (0 to 1)
    # Speak the text
    engine.say(text)
    engine.runAndWait()

#*******************************************
#*****************MAIN**********************
#*******************************************

#Audio input from user's micrhophone
prompt, error = listener()


if error == 0:
    try:
        #Call OpenAI service with the prompt collected from user
        answerAI = callCompletion(prompt)
    except:
        answerAI= "Non sono in grado di rispondere"
else: 
    answerAI= "Non ho capito"

#Convert into audio the response from OpenAI
textToAudio(answerAI)
