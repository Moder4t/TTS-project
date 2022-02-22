'''
Created on 8 avr. 2019

@author: gills

https://github.com/Delgan/loguru

'''

import inspect

DEBUG = True

class trace:
    @staticmethod
    def affiche(chaine):
        if DEBUG:
            caller = inspect.currentframe().f_back
            print(caller.f_globals['__name__'], chaine)
            

        
