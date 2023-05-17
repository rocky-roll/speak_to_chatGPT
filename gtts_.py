#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    author='@rocky_roll,
#    license='GNU GPLv3'
#

import tempfile
import time

from gtts import gTTS
from pygame import mixer


def talk_gtts__(texto):
    with tempfile.NamedTemporaryFile('w+t') as temp:

        filename = temp.name
        # print(filename)
        tts = gTTS(texto, lang='es', tld='us')
        tts.save(filename)
        mixer.init()
        mixer.music.load(filename)
        audio_duration = mixer.Sound(filename).get_length()
        mixer.music.play()
        time.sleep(audio_duration)


# talk_gtts__("texto")
