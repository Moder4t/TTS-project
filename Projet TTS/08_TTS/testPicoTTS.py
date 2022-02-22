'''
Created on 1 sept. 2021

@author: gills
'''
from PicoTTS import TTS_engine

if __name__ == "__main__":
    tts = TTS_engine();
    tts.say(u"Bonjour denis, il est 9 heures")
    print("fin")