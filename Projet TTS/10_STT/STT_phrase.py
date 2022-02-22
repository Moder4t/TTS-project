# -*- coding: utf-8 -*-
'''
Created on 1 sept. 2021

@author: gills
'''
import io
import requests
import json
import pyaudio
import wave
import audioop

class STT_phrase:
    def __init__(self):
        self.wit_api = 'https://api.wit.ai/speech'
        self.wit_key = 'xxx'
        self.listenTime = 3 #12
        
    def wait(self):
        pa = pyaudio.PyAudio()
        
        RATE = 8000
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        '''
        Pour le déclanchement et la fin voir Speakerreconition.py
        La fonction Listen
        '''
        
        
        stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        frames = []
        
        for i in range(0, int(RATE / CHUNK * self.listenTime)):
            data = stream.read(CHUNK)
            frames.append(data)

        # stop Recording
        stream.stop_stream()
        stream.close()

        pa.terminate() 
        
        audioOut = io.BytesIO()
        waveFile = wave.open(audioOut, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(pa.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        audioData = audioOut.getvalue()
        waveFile.close() 
        
        HTTP_headers = {'authorization': 'Bearer ' + self.wit_key, 'Content-Type': 'audio/wav'}
        resp = requests.post(self.wit_api, headers = HTTP_headers, data = audioData)
        #print(resp.content)
        data = json.loads(resp.content)
        #print(data)
        text = data['text']
        return text

    def noiseLevel(self, temps):
        pa = pyaudio.PyAudio()
        
        RATE = 8000
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        
        niveauMoyen = 0;
             
        stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
      
        for i in range(0, int(RATE / CHUNK * temps)):
            data = stream.read(CHUNK)
            niveau = audioop.rms(data, 2) # 2 -> sur 16 bits
            niveauMoyen = 0.5 * niveauMoyen + 0.5 * niveau
 
        # stop Recording
        stream.stop_stream()
        stream.close()

        pa.terminate() 
        
        return niveauMoyen

if __name__ == "__main__":
    phrase = STT_phrase()
    print("-> go")
    text = phrase.wait()
    print(" -> fin: " + text)
    #print "Niveau moyen " + str(phrase.noiseLevel(3))
    #print(" -> fin: ")
    