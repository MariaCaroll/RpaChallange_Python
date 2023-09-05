# Salva o arquivo na pasta do robo
def baixar_arquivo(bot, by, os, var_strCaminho):
    try:
        if os.path.isfile(var_strCaminho):
            #-----FAZER DOWNLOAND AQUIVO ATUALIZADO -----#
            os.remove(var_strCaminho)
            print("Fazendo download do arquivo atualizado....")
            bot.find_element(selector = '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a', by=by.XPATH).click()
            print("Download realizado com sucesso.")
            bot.wait(3000)
    except:
        print("Erro ao fazer download do arquivo.")