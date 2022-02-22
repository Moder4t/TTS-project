# -*- coding: utf-8 -*-

'''
Created on 15 févr. 2019

@author: gills

Intallation de la librairie gTTS: sudo pip install gTTS
Inatalation de mpg321: sudo apt install mpg321

'''
from gtts import gTTS
import subprocess

tts = gTTS(u"Bonjour denis, il est 9 heures", lang="fr")
tts.save('out.mp3')
cmd = ['mpg321', '-q', 'out.mp3']
subprocess.call(cmd)
