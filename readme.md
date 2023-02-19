# AI Speech Recognition and Response using OpenAI
This is a Python script that uses OpenAI to recognize voice input and generate a text-based response, which is then converted to speech and played back to the user.

## Features
* Speech-to-text conversion using the Google Cloud Speech-to-Text API.
* Text generation using OpenAI's GPT-3 language model.
* Text-to-speech conversion using the pyttsx3 library.
* Easy-to-use command-line interface.
## Requirements
* Python 3.6 or later.
* An OpenAI API key (free or paid).
* Copy and paste OpenAI API Key in apiKey.txt file

To install the required Python packages, run the following command:


```pip install -r requirements.txt```

## Usage
To run the script, simply execute the following command:


```python main.py```

You will be prompted to speak, and the AI will respond with a text-based answer that is spoken out loud.

## Limitations
* The quality of the speech recognition and response is dependent on the quality of the user's microphone and the OpenAI language model.
* The script is currently configured to work only with Italian language, but can be adapted for other languages.
## Notes
* Make sure you have a valid OpenAI API key before running the program.
* Make sure the required libraries are installed
