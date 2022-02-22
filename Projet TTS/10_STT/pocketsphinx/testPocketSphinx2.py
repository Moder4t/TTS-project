import os
from pocketsphinx import AudioFile

'''
Created on 28 mars 2019

@author: gills

https://pypi.org/project/pocketsphinx/

'''
model_path = "pocketsphinx/fr-FR/"
print (model_path)

config = {
    'verbose': False,
    'audio_file': os.path.join("./", 'outAudio.wav'),
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'french'),
    'lm': os.path.join(model_path, 'fr-small.lm.bin'),
    'dict': os.path.join(model_path, 'fr.dict')
}

audio = AudioFile(**config)
for phrase in audio:
    print(phrase)
    
print ("fin")
print (config)

