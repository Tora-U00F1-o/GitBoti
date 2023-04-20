# -*- coding: utf-8 -*-
"""
Combines multiple files .py into one. Removes comments and \n
@author: Tora-U00F1-o
"""

fileNames = ["Check.py", "Console.py", "PropertiesManager.py", "gtiBotiju.py"]
# fileNames = ["Console.py","ejem.py"]

def appendFile(f):
    print("# -------    "+f.name  +"     ----------- \n")
    resultFile = open("result.py", 'a')
    resultFile.write("# ------------------------------- \n")
    resultFile.write("# -------    "+f.name  +"     ----------- \n")
    resultFile.write("# ------------------------------- \n")
    resultFile.write("# ------------------------------- \n")
    
    for line in f:
        if(len(line.strip()) == 0):
            continue
        if('#' in line and len(line.split('#')[0].strip()) == 0): # si es un comentario lo salta
            continue
        writeLine = True
        
        print("\t -> hasMoreimp: .", line, ".")
        if("import" in line):
            print("\t ->\t -> import in line ")
            args = line.split(" ")
            print("\t ->\t -> ", args)
            for arg in args:   
                for name in fileNames:  
                    print("\t ->\t ->\t -> ", name.split(".py")[0], " in ", arg)
                    if(name.split(".py")[0] in arg):
                        writeLine = False
                        print("\t ->\t ->\t ->\t -> no print ")
                
        print("\t -> wLine?", writeLine)
        if(writeLine):
            print("\t ->\t -> writed ")
            resultFile.write(line)
    resultFile.write("\n")
    resultFile.close()
    
    
for name in fileNames:
    f = open(name, 'r')
    appendFile(f)
    f.close()



    
