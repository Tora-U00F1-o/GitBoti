# -*- coding: utf-8 -*-
"""
Console utils 

@author: Tora-U00F1-o
"""
import colorama
from Check import *

# =============================================================================
# INPUT
# =============================================================================

"""Asks a string"""
def ask(mensaje):
    return input(str(mensaje))

"""Asks a string, if it is invalid asks again"""
def askString(mensaje):
    while(True):
        try:
            cadena = str(ask(mensaje))
            if isStringValid(cadena):
                return cadena
            else:
                raise ValueError
        except ValueError:
            continue


"""Asks an int, if it is invalid asks again"""
def askInt(mensaje):
    while(True):
        try:
            return int(ask(mensaje))
        except ValueError:
            continue

"""Asks an bool, if it is invalid asks again"""
def askBool():
    while(True):
        boolStr = str.lower(ask("(s)i o (n)o ? :"))
        if(boolStr.__eq__("s")):
            return True
        elif(boolStr.__eq__("n")):
            return False

        say(">> Opcion no reconocida")


# =============================================================================
# OUTPUT
# =============================================================================

"""Prints the msg"""
def say(mensaje):
    print(mensaje)
    
    
"""Prints the msg in color"""
def sayColor(mensaje, codeColorama):
    say(codeColorama +mensaje +colorama.Style.RESET_ALL)



"""Prints the menu (Array of Strings) formated"""
def showMenu(menu = []):
    sayColor("-----------------------------\n"
        +" MENU\n"
        +"-----------------------------", colorama.Fore.CYAN)

    for i in range(1, len(menu)):
        say("  "+str(i)+"_ "+menu[i])
        
    say("\n  0_ "+menu[0])
    sayColor("-----------------------------", colorama.Fore.CYAN)

"""Prints the menu and asks for an option and executes the option selected
Menu need to be [[Title action, funtion], [Title action, funtion],...].
First action must be exit action, with function has to be sys.exit
"""
def chooseOption(menu):
    option = -1
    optionsTitles = [fila[0] for fila in menu]
    while(option<0 or option>len(optionsTitles)-1):
        try:
            showMenu(optionsTitles)
            option = int(ask("> Opcion? :"))
        except:
            continue
    optionsActions = [fila[1] for fila in menu]

    optionsActions[option]()

    return option

"""Default template for program."""
class Program:
    def __init__(self, menuActual = ["Vacio", None]):
        self.menuActual = menuActual
        
    def run(self):
        say("Start")
        while(True):
            chooseOption(self.menuActual)
        say("Exit")
    
    def setMenu(self, menuActual = ["Vacio", None]):
        self.menuActual = menuActual