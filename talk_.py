#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    author='@rocky_roll,
#    license='GNU GPLv3'
#

import pyttsx3


def talk_pytts__(text):
    engine = pyttsx3.init()
    # para win 10
    voice = engine.getProperty('voices')
    # engine.setProperty('voices', voice[0].id)
    # para linux
    engine.setProperty('voice', 'spanish-latin-am+f2')
    # lo msmo para todos
    engine.setProperty('rate', 145)
    engine.say(text)
    engine.runAndWait()

# talk_pytts__("hola")
