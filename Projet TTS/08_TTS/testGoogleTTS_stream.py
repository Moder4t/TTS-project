'''
Created on 30 août 2021

@author: gills
'''
import pygame
from io import BytesIO
from gtts import gTTS
import subprocess

print(u"Bonjour Stéphane")

tts = gTTS(u"bonjour Stéphane", lang="fr")

fp = BytesIO()
tts.write_to_fp(fp) #tts.save('out.mp3')
fp.seek(0)
pygame.mixer.init()
pygame.mixer.music.load(fp)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
