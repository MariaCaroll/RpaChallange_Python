#Preenche o formulário do navegador
def preencher_formulario(var_dtAquivo,bot, by,):
    print("Chegamos..")

    '''
        encontrar elemento com xpath. 
    '''

    for item in var_dtAquivo:
        #Campo Nome
        bot.find_element(selector = "input[ng-reflect-name='labelFirstName']", by=by.TAG_NAME).click()
        bot.paste(item[0])

         #Campo Sobrenome
        bot.find_element(selector = "input[ng-reflect-name='labelLastName']", by=by.TAG_NAME).click()
        bot.paste(item[1])

         #Campo Comapny Name
        bot.find_element(selector = "input[ng-reflect-name='labelCompanyName']", by=by.TAG_NAME).click()
        bot.paste(item[2])

         #Campo Role in Company
        bot.find_element(selector = "input[ng-reflect-name='labelRole']", by=by.TAG_NAME).click()
        bot.paste(item[3])

         #Campo Address
        bot.find_element(selector = "input[ng-reflect-name='labelAddress']", by=by.TAG_NAME).click()
        bot.paste(item[4])

         #Campo Email
        bot.find_element(selector = "input[ng-reflect-name='labelEmail']", by=by.TAG_NAME).click()
        bot.paste(item[5])

         #Campo Phone
        bot.find_element(selector = "input[ng-reflect-name='labelPhone']", by=by.TAG_NAME).click()
        bot.paste(item[6])

        #botão 'SUBMIT'
        bot.find_element(selector = "//input[@type = 'submit']", by = by.XPATH).click()

        
