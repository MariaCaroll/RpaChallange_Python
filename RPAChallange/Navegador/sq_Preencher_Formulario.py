#Preenche o formulário do navegador
import pandas as pd
def preencher_formulario(var_strCaminhoArquivo,bot, by):
    try:
        print("Realizando leitura do arquivo excel..")
        var_dfArquivo = pd.read_excel(var_strCaminhoArquivo)
    except:
        print("Erro ao fazer leitura do aquivo.")
    '''
        encontrar elemento com xpath. 
    '''
    #Botão start
    bot.find_element(selector = "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button", by = by.XPATH).click()
    try:
        print("Preenchedo formulário...")
        for item in var_dfArquivo.index:
            #Campo Nome
            bot.find_element(selector = "input[ng-reflect-name='labelFirstName']", by=by.TAG_NAME).click()
            bot.paste(var_dfArquivo['First Name'][item])

            #Campo Sobrenome
            bot.find_element(selector = "input[ng-reflect-name='labelLastName']", by=by.TAG_NAME).click()
            bot.paste(var_dfArquivo['Last Name '][item])

            #Campo Comapny Name
            bot.find_element(selector = "input[ng-reflect-name='labelCompanyName']", by=by.TAG_NAME).click()
            bot.paste(var_dfArquivo['Company Name'][item])

            #Campo Role in Company
            bot.find_element(selector = "input[ng-reflect-name='labelRole']", by=by.TAG_NAME).click()
            bot.paste(var_dfArquivo['Role in Company'][item])

            #Campo Address
            bot.find_element(selector = "input[ng-reflect-name='labelAddress']", by=by.TAG_NAME).click()
            bot.paste(var_dfArquivo['Address'][item])

            #Campo Email
            bot.find_element(selector = "input[ng-reflect-name='labelEmail']", by=by.TAG_NAME).click()
            bot.paste(var_dfArquivo['Email'][item])

            #Campo Phone
            bot.find_element(selector = "input[ng-reflect-name='labelPhone']", by=by.TAG_NAME).click()
            bot.paste(str(var_dfArquivo['Phone Number'][item]))

            #botão 'SUBMIT'
            bot.find_element(selector = "//input[@type = 'submit']", by = by.XPATH).click()
    except:
        print("Erro ao preencher formulário.")

    print("Formulário Preenchido com sucesso.")
    #Resultado final
    var_listResultado = bot.find_elements(selector = "/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]", by = by.XPATH)
    #Iterar a lista do resultado para exibir o texto 
    for element in var_listResultado:
        print (element.text)

        
