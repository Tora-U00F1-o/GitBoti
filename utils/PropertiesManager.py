# -*- coding: utf-8 -*-
"""
@author: Tora-U00F1-o
"""

import configparser
import sys

fileNameProperties = "./gitboti.properties"
config = configparser.ConfigParser()
config.read(fileNameProperties)
    
dirPathKey = "dirpath"
gitEmailKey = "gitemail"
gitNameKey = "gitname"

def getProperties():
    config = configparser.ConfigParser()
    config.read(fileNameProperties)
    return config['DEFAULT']

def editProperty(nameProp, newValue):
    config = configparser.ConfigParser()
    config.read(fileNameProperties)
    
    config.set('DEFAULT', nameProp, newValue)
    with open(fileNameProperties, 'w') as config_file:
        config.write(config_file)
        
