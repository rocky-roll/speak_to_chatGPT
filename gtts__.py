import time
from io import BytesIO

from gtts import gTTS
from pygame import mixer


def wait():
    while mixer.get_busy():
        time.sleep(1)


def speak(texto):
    mp3_fo = BytesIO()
    tts = gTTS(text=texto, lang='es', tld='us')
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    mixer.init()
    sound = mixer.Sound(mp3_fo)
    sound.play()
    wait()


# speak("hola mundo")
