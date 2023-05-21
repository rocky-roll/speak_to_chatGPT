import os
import tempfile
import time
from gtts import gTTS
from pygame import mixer

def talk_gtts__(texto):
    temp_file = tempfile.mkdtemp()
    filename = os.path.join(temp_file, 'temp.mp3')
    #print(filename)
    tts = gTTS(texto, lang='es', tld='us')
    tts.save(filename)
    mixer.init()
    mixer.music.load(filename)
    audio_duration = mixer.Sound(filename).get_length()
    mixer.music.play()
    time.sleep(audio_duration)
#talk_gtts__("texto")