import speech_recognition as sr
from deep_translator import GoogleTranslator
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()
translator = google_translator()

while True:
    with sr.Microphone() as source:
        print("speak now")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text == "exit":
                break
        except sr.UnknownValueError:
            print("could not understand")
        except sr.RequestError:
            print("could not request result from google")

        translated_text = translator.translate(speech_text, lang_tgt='fr')
        print(translated_text)

        voice = gTTS(translated_text, lang='fr')
        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")

'''Python Libraries to Install:

pip install SpeechRecognition
pip install pyaudio
pip install google-trans-new
pip install gTTS
pip install playsound'''

'''If you get the error:
"google_trans_new.google_trans_new.google_new_transError: 404 (Not Found) from TTS API. Probable cause: Unknown"

It is because of a bug and this is the solution:
1. search in the python library for the google_trans_new.py file.
"Lib\site-packages "google_trans_new_google_trans_new.py"
(I use virtual machine and it is easier for me to find it)

Open it and change the codes to these:

16 / URL_SUFFIX_DEFAULT = 'com'

90/ def __init__(self, url_suffix="com", timeout=5, proxies=None):

151/ response = (decoded_line).

233/ response = (decoded_line)

3. That should work, if it doesn't then google the error and you will get help in these cases:
google_trans_new.google_trans_new.google_new_transError: 404 (Not Found) from TTS API. Probable cause: Unknown

'''
#use pip install playsound==1.2.2