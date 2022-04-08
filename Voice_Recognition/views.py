from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

#Import Libraries
import speech_recognition as sr
import os

def mic(request):
    r = sr.Recognizer()
    r.energy_threshold=4000
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source) 
    try:
        txt = r.recognize_google(audio)
        Voice_To_Text = txt.capitalize()
        print("You said:", Voice_To_Text+".")
        context= {'You Said': Voice_To_Text}
        print(context)
        return JsonResponse(context)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except OSError:
        print("Speech not found.")
        