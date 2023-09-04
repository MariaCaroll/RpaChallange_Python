# Abri a aba do navegador

def abri_Navegador(var_strUrl, bot, by):
    var_intContador = 0
    var_intLogo = 0
    while var_intContador < 3 and var_intLogo == 0:
        bot.browse(var_strUrl)
        #Verifica se a página carregou...
        var_imgLogo = bot.find_elements(
            f"/html/body/app-root/div[1]/nav/div/a", by.XPATH)
        var_intLogo = len(var_imgLogo)
        if var_intLogo == 0:
            print("Erro ao acessar o site")
            fechar_Navegador(var_strUrl, bot)
            var_intContador += 1
        print("Site está estável.")
    if var_intContador == 3:
        print("Erro ao acessar site.")


def fechar_Navegador(var_strUrl, bot):
    bot.stop_browser(var_strUrl)
