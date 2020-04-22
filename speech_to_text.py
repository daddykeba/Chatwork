import speech_recognition as sr
#language = 'fr'

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='fr-FR')
        print("You said: {}".format(text))
    except:
        print("Sorry could not recognize your voice")