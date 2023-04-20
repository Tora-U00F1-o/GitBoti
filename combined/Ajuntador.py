# -*- coding: utf-8 -*-
"""
Combines multiple files .py into one. Removes comments and white lines
@author: Tora-U00F1-o

Im not removing the prints (witch i used for debugging) because i dont care.
And its cool to see 5 secs of words running light speed in the console
"""

filesToCombinePaths = ["../utils/Check.py", "../utils/Console.py", "../utils/PropertiesManager.py", "../gitBotiju.py"]

# get fileNames (remove paths and extension)
fileNames = []
for path in filesToCombinePaths:
    nameArr = path.split("/")
    name = nameArr[len(nameArr)-1]
    fileNames.append(name.split(".py")[0])
    
resultFileName = "gitBotijuCombined.py"

def appendFile(fileToAppend, resultFile):
    print("# -------    "+fileToAppend.name  +"     ----------- \n")
    resultFile.write("# ------------------------------- \n")
    resultFile.write("# -------    "+fileToAppend.name  +"     ----------- \n")
    resultFile.write("# ------------------------------- \n")
    
    for line in fileToAppend:
        if(len(line.strip()) == 0):
            continue
        if('#' in line and len(line.split('#')[0].strip()) == 0): # si es un comentario lo salta
            continue
        writeLine = True
        
        print("\t -> hasMoreimp: .", line, ".")
        if("import" in line):
            print("\t ->\t -> import in line ")
            argsImport = line.split(" ")
            print("\t ->\t -> ", argsImport)
            for arg in argsImport:   
                for name in fileNames:  
                    print("\t ->\t ->\t -> ", name, " in ", arg)
                    if(name in arg):
                        writeLine = False
                        print("\t ->\t ->\t ->\t -> no print ")
                
        print("\t -> wLine?", writeLine)
        if(writeLine):
            print("\t ->\t -> writed ")
            resultFile.write(line)
    resultFile.write("\n")
    
resultFile = open(resultFileName, 'w')
for name in filesToCombinePaths:
    fileToAppend = open(name, 'r')
    appendFile(fileToAppend, resultFile)
    fileToAppend.close()

resultFile.close()

    
