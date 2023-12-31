"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""


# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from configuracao import var_dirDriveItem, var_strCaminhoArquivo
from Navegador.sq_Abrir_Navegador import abri_Navegador
from Navegador.sq_Baixar_Arquivo import baixar_arquivo
from Navegador.sq_Preencher_Formulario import preencher_formulario

import os

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    desktop_bot = DesktopBot()

    # Execute operations with the DesktopBot as desired
    # desktop_bot.control_a()
    # desktop_bot.control_c()
    # value = desktop_bot.get_clipboard()

    webbot = WebBot()

    # Configure whether or not to run on headless mode
    webbot.headless = False

    # Uncomment to change the default Browser to Firefox
    # webbot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    webbot.driver_path = var_dirDriveItem

    # Implement here your logic...
    abri_Navegador("https://rpachallenge.com/", webbot, By)
    baixar_arquivo(webbot, By, os, var_strCaminhoArquivo)  
    preencher_formulario (var_strCaminhoArquivo, webbot, By)
    # Wait 3 seconds before closin

    webbot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    #webbot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()  
