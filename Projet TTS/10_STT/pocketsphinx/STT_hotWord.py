'''
Created on 9 avr. 2019

@author: gills
'''
import os
from pocketsphinx import *
import pyaudio
from Trace import trace

class STT_hotWord:
    def __init__(self, model):
        model_path = "fr-FR/"
        trace.affiche(model_path)

        config = Decoder.default_config()
        config.set_string('-verbose', 'yes')
        config.set_string('-hmm', os.path.join(model_path, 'french'))
        config.set_string('-keyphrase', model)
        config.set_string('-dict', os.path.join(model_path, 'fr.dict'))
        config.set_float('-kws_threshold', 1e+20)
        
        self.hotWord = model
        self.decoder = Decoder(config)

    def wait(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=20480)
        stream.start_stream()
        
        self.decoder.start_utt()

        while True:
            buf = stream.read(1024)
            if buf:
                self.decoder.process_raw(buf, False, False)
            else:
                break

            if self.decoder.hyp() is not None:
                trace.affiche([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in self.decoder.seg()])
                trace.affiche("Hotword Detected")
                self.decoder.end_utt()
                break
        
if __name__ == "__main__":
    hotword = STT_hotWord("edgard")
    trace.affiche(hotword.hotWord)
    hotword.wait()
    trace.affiche("Le 'hotword' est detecte -> fin")
    