# ------------------------------- 
# -------    ../utils/Check.py     ----------- 
# ------------------------------- 
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
# ------------------------------- 
# -------    ../utils/Console.py     ----------- 
# ------------------------------- 
"""
Console utils 
@author: Tora-U00F1-o
"""
import colorama
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
# ------------------------------- 
# -------    ../utils/PropertiesManager.py     ----------- 
# ------------------------------- 
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

# ------------------------------- 
# -------    ../gitBotiju.py     ----------- 
# ------------------------------- 
import subprocess
import sys
import os
import configparser
import colorama
def executeGitActionWithParams(args, param):
    args.append(param)
    executeGitAction(args)
    args.pop(len(args)-1)
def executeGitAction(args):
    if(int(ask("> Ejecutar "+ str(args)+ " ? (0|1) >"))):
        result = __executeGitAction__(args)
        sayColor("> Code: "+str(result.returncode), colorama.Fore.YELLOW)
        say("> Done: ")
        sayColor((result.stdout if result.stdout else "No completed"), colorama.Fore.GREEN)
        say("> Error: ")
        sayColor((result.stderr if result.stderr else "No errors"), colorama.Fore.RED)
def __executeGitAction__(args):
    result = subprocess.run(args, capture_output=True, text=True)
    return result
def setMenuDefaultMenu():
        program.setMenu(menuDefault)
pullArgs = ['git', 'pull']
def pullAction():
    executeGitAction(pullArgs)
statusArgs = ['git', 'status']
def statusAction():
    executeGitAction(statusArgs)
addAllArgs = ['git', 'add', '*']
def addAllAction():
    executeGitAction(addAllArgs)
commitArgs = ['git', 'commit', '-m']
def commitWithMsgAction():
    param = ask("Msg for commit: ")
    executeGitActionWithParams(commitArgs, param)
pushArgs = ['git', 'push']
def pushAction():
    executeGitAction(pushArgs)
def setSubmenuNewRepo():
    program.setMenu(menuNewRepo)
cloneArgs = ['git', 'clone']
def nrCloneAction(): 
    param = ask("URL to clone: ")
    executeGitActionWithParams(cloneArgs, param)
    nameProy = param.split("/")
    nameProy = nameProy[len(nameProy)-1].split(".git")[0]
    editProperty( dirPathKey, "./"+nameProy+"/")
    loadPath()
def setSubmenuBranches():
    program.setMenu(menuBranches)
brancListArgs = ['git', 'branch']
def branchGetLocalListAction():
    executeGitAction(brancListArgs)
def branchGetRemoteListAction():
    executeGitActionWithParams(brancListArgs, '-r')
changeBranchArgs = ['git', 'checkout']
def branchChangeBranchAction(): 
    param = ask("Name of branch to change: ")
    executeGitActionWithParams(changeBranchArgs, param)
def branchCreateNewBranch():
    param = ask("Name of new branch: ")
    executeGitActionWithParams(brancListArgs, param)
    executeGitActionWithParams(changeBranchArgs, param)
    branchSaveArgs = ['git', 'push', '--set-upstream', 'origin']
    executeGitActionWithParams(branchSaveArgs, param)
def setSubmenuSettings():
    program.setMenu(menuSettings)
def logInAction():
    email = ask("Insert git email: ")
    gitConfig = ['git', 'config', 'user.email']
    executeGitActionWithParams(gitConfig, email.strip())
def settingsGeneratePropertiesAction():
    f = open("gitboti.properties", 'w')
    f.write("[DEFAULT] \n")
    f.write(dirPathKey+" = ./ \n")
    f.write(gitEmailKey+" = noEmail \n")
    f.write(gitNameKey+" = noName \n")
    f.close()
def settingsPrintGuideAction():
    say("Instalar git")
    sayColor(" - En win:", colorama.Fore.YELLOW)
    say("\t:Descarga el instalador de Git desde la página oficial: https://git-scm.com/download/win ")
    say("\t:Abrir una consola nueva para trabajar")
    sayColor(" - En Debian/Ubuntu:", colorama.Fore.YELLOW)
    say("\t: > sudo apt-get install git")
    say(" - Verificar instalacion > git --version")
menuDefault = [
        ["Exit", sys.exit],
        ["Pull", pullAction],
        ["Status", statusAction],
        ["Add", addAllAction],
        ["Commit", commitWithMsgAction],
        ["Push", pushAction],
        ["* New repo menu", setSubmenuNewRepo],
        ["* Branches menu", setSubmenuBranches],
        ["* Settings menu", setSubmenuSettings],
        ]
menuNewRepo = [
        ["Back", setMenuDefaultMenu],
        ["Clone", nrCloneAction],
        ]
menuBranches = [
        ["Back", setMenuDefaultMenu],
        ["Local list of branches", branchGetLocalListAction],
        ["Remote list of branches", branchGetRemoteListAction],
        ["Create a new branch", branchCreateNewBranch],
        ["Change to branch", branchChangeBranchAction],
        ]
menuSettings = [
        ["Back", setMenuDefaultMenu],
        ["Log-in in git", logInAction],
        ["Generate properties", settingsGeneratePropertiesAction],
        ["Print starting guide", settingsPrintGuideAction],
        ]
def loadPath():
    try:
        repo_path = getProperties()[dirPathKey]
        os.chdir(repo_path)
    except (FileNotFoundError, KeyError) as error:
        input("Explotó con la ruta. Pulsa para continuar...")
        settingsGeneratePropertiesAction()
        if(input("Generado gitboti.properties... Configura y pulsa (0|1) para continuar...")):
            loadPath()
colorama.init()
loadPath()
program = Program(menuDefault)
program.run()
colorama.deinit()
