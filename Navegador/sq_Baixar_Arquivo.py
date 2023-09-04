# Salva o arquivo na pasta do robo
def baixar_arquivo(bot, by, not_found, var_strCaminho):
    print("Fazendo download do arquivo atual....")

    # Verifica se a página carregou...
    var_btnDownload = bot.find_elements(
        by.XPATH, selector=r"//button[text() = ' Download Excel ']")
    print(var_btnDownload)

    '''if not bot.find("btnDownload", matching=0.97, waiting_time=10000):
        not_found("btnDownload")
    bot.rigth_click()

    if not bot.find("btnSubmit", matching=0.97, waiting_time=10000):
        not_found("btnSubmit")
    bot.click()

    if not bot.find("btnStart", matching=0.97, waiting_time=10000):
        not_found("btnStart")
    bot.click()'''

    bot.whait(5000)

    bot.paste(var_strCaminho)
    bot.enter()
