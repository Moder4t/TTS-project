# -*- coding: utf-8 -*-
'''
Created on 16 févr. 2019

@author: gills

Installer le packetage: python-pyaudio
'''
import pyaudio
import wave

pa = pyaudio.PyAudio()

# Afficher les informations sur la carte audio
print(pa.get_device_count())
for i in range(pa.get_device_count()):
    print(pa.get_device_info_by_index(i))
  
# Enregistrer du son
RECORD_SECONDS = 5
RATE = 16000
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
DEV_INDEX = 12 # device index found by p.get_device_info_by_index(i)

stream = pa.open(format=FORMAT, channels=CHANNELS, input_device_index = DEV_INDEX, rate=RATE, input=True, frames_per_buffer=CHUNK)

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# stop Recording
stream.stop_stream()
stream.close()

pa.terminate() 

#waveFile = io.BytesIO()
waveFile = wave.open('outAudio.wav', 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(pa.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
#wav_data = waveFile.getvalue()
waveFile.close() 
