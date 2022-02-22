import os
from pocketsphinx import LiveSpeech

'''
Created on 28 mars 2019

@author: gills

https://pypi.org/project/pocketsphinx/

'''
model_path = "fr-FR/"
print (model_path)

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=1024,
    no_search=False,
    full_utt=False,
    audio_device='2',
    hmm=os.path.join(model_path, 'french2'),
    lm=os.path.join(model_path, 'fr-small.lm.bin'),
    dict=os.path.join(model_path, 'fr.dict')
)

for phrase in speech:
    print(phrase)
