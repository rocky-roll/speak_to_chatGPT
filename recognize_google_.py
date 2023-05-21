#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    author='@rocky_roll,
#    license='GNU GPLv3'
#

import os
import queue
import random

# from talk_ import talk_pytts__
import speech_recognition as sr

from chatGPT_ import *
from gtts_ import talk_gtts__

listener = sr.Recognizer()

q = queue.Queue()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")

            listener.adjust_for_ambient_noise(source, duration=0.1)
            audio = listener.listen(source)
    except Exception as e:
        pass
    return audio


def recognize_audio(audio):
    print("Procesando...")
    rec = listener.recognize_google(audio, language='es-AR')
    rec = rec.lower()
    # print(rec)
    return rec


def main():
    global q
    name = "chat gpt"
    filename = ('te escucho ', 'dime ', 'si ', 'pregunta ')
    counter = 0
    open_ = False
    while True:
        try:
            response = recognize_audio(listen())
            if name in response or "hola" in response and counter == 0:

                counter += 1
                open_ = True
                q.put_nowait(open_)
                numeros = random.randint(0, 3)
                # talk_pytts__(filename[numeros])
                talk_gtts__(filename[numeros])
                # response = response.replace(name, '')
                # response = response.strip()

            elif "cerrar" in response:
                print(response)
                response = response.replace("cerrar", '')
                response = response.strip()
                os._exit(0)

            elif "cancelar" in response and counter == 1:
                response = response.replace("cancelar", '')
                response = response.strip()
                # talk_pytts__('ok')
                talk_gtts__('ok')
                counter = 0
                open_ = False
                q.put_nowait(open_)
            elif open_ == True:
                print(response)
                # talk_pytts__(ChatGPT.main_GPT(response))
                talk_gtts__(ChatGPT.main_GPT(response))

                open_ = False
                q.put_nowait(open_)
                counter = 0
        except:
            pass


if __name__ == "__main__":
    main()
