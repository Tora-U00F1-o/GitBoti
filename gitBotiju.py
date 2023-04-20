# -*- coding: utf-8 -*-
"""


@author: Tora-U00F1-o
"""
import subprocess
import sys
import os
import colorama
from Console import *
from PropertiesManager import *

# =============================================================================
# Aqui es donde sucede la magia
# =============================================================================

def executeGitActionWithParams(args, param):
    args.append(param)
    executeGitAction(args)
    args.pop(len(args)-1)
    
def executeGitAction(args):
    if(int(ask("> Ejecutar "+ str(args)+ " ? (0|1) >"))):
        result = __executeGitAction__(args)
        
        sayColor("> Code: "+str(result.returncode), colorama.Fore.YELLOW)
        # say("\t > "+str(result))
        say("> Done: ")
        
        sayColor((result.stdout if result.stdout else "No completed"), colorama.Fore.GREEN)
        
        say("> Error: ")
        sayColor((result.stderr if result.stderr else "No errors"), colorama.Fore.RED)



def __executeGitAction__(args):
    result = subprocess.run(args, capture_output=True, text=True)
    # print(result)
    return result
    
# =============================================================================
# Menu DEFAULT
# =============================================================================
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

# =============================================================================
# Menu New Repo
# =============================================================================
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
    
# =============================================================================
# Menu branches
# =============================================================================

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
    
    
# =============================================================================
# Menu Settings
# =============================================================================

def setSubmenuSettings():
    program.setMenu(menuSettings)

def logInAction():
    # email = getProperties()[gitEmailKey]
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

# =============================================================================
# Menu INIT
# =============================================================================
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

# =============================================================================
# UTILS
# =============================================================================

def loadPath():
    # Cambiar el directorio actual al repositorio de Git
    try:
        repo_path = getProperties()[dirPathKey]
        os.chdir(repo_path)
    except (FileNotFoundError, KeyError) as error:
        input("Explotó con la ruta. Pulsa para continuar...")
        settingsGeneratePropertiesAction()
        if(input("Generado gitboti.properties... Configura y pulsa (0|1) para continuar...")):
            loadPath()

# =============================================================================
# Main
# =============================================================================

colorama.init()

loadPath()
program = Program(menuDefault)
program.run()

colorama.deinit()