# -*- coding: utf-8 -*-
"""
Validators caseros 

@author: Tora-U00F1-o
"""

"""Return if string is valid"""
def isStringValid(string):
    if(string == None):
        return False

    if(len(string.strip()) == 0):
        return False

    return True

"""Throws ValueError if string is not valid"""
def checkString(string, msg):
    if(not isStringValid(string)):
        raise ValueError(msg)

"""Throws ValueError if element is None"""
def checkNotNone(element, msg):
    if(element == None):
        raise ValueError(msg)