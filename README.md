# GitBoti

Console app to perform git actions.

## Perform the following actions:
  - Basic actions:
    - status
    - add *
    - commit -m
    - push
  - New Repo
    - clone
  - Ramas
    - Listar las ramas locales
    - Listas las ramas remotas
    - Crear una nueva rama
    - Cambiar de rama 

## Modules used:

| Name | Description |
| ----------- | ----------- |
| gitBotiju.py | Main module |
| /utils/ | |
| Check.py | Validators for objects [Strings, ...]|
| Console.py | Console utils |
| PropertiesManager.py | Manage a properties file |
| /combined/ | |
| Ajuntador.py | Combines multiple files .py into one. Removes comments and white lines. ModuleResult name is gitBotijuCombined.py |


## External modules
Modules to install to use this app

  - Colorama: >`pip install colorama`
    - gitBotiju.py
    - Console.py
  - Configparser: >`pip install configparser`
    - PropertiesManager.py
