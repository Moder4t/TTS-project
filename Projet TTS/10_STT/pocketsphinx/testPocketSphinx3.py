import os
from pocketsphinx import *
import pyaudio

'''
Created on 28 mars 2019

@author: gills

https://pypi.org/project/pocketsphinx/

'''
model_path = "fr-FR/"
print model_path

config = Decoder.default_config()
config.set_string('-verbose', 'yes')
config.set_string('-hmm', os.path.join(model_path, 'french'))
config.set_string('-keyphrase', 'edgard')
config.set_string('-dict', os.path.join(model_path, 'fr.dict'))
config.set_float('-kws_threshold', 1e+20)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=20480)
stream.start_stream()

decoder = Decoder(config)
decoder.start_utt()

while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break

    if decoder.hyp() is not None:
        print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        print("Hotword Detected")
        break
        #decoder.end_utt()
        #start_speech_recognition()
        #decoder.start_utt()
