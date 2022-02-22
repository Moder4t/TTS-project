'''
Created on 1 sept. 2021

@author: gills
'''
from STT_hotWord import *

if __name__ == "__main__":
    hotWord = STT_hotWord()
    print(hotWord.keywords)
    hotWord.wait()
    print("Le 'hotword' est detecte -> fin")