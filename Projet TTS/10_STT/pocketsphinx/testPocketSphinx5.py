import os
from pocketsphinx import *
import pyaudio

'''
Created on 28 mars 2019

@author: gills

https://pypi.org/project/pocketsphinx/

'''
model_path = "fr-FR-1/"
print(model_path)

config = Decoder.default_config()
config.set_string('-verbose', 'no')
config.set_string('-hmm', os.path.join(model_path, 'acoustic-model'))
config.set_string('-lm', os.path.join(model_path, 'language-model.lm.bin'))
#config.set_string('-keyphrase', 'edgard')
config.set_string('-dict', os.path.join(model_path, 'pronounciation-dictionary.dict'))
#config.set_float('-kws_threshold', 1e+20)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=20480)
stream.start_stream()

decoder = Decoder(config)
decoder.start_utt()

for i in range(0, int(8000 / 1024 * 6)):
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break

decoder.end_utt()

liste = []
[liste.append(seg.word) for seg in decoder.seg()]
#[(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()]
print ("liste", liste)
        #start_speech_recognition()
        #decoder.start_utt()
