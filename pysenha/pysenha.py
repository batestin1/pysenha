
#############################################################################################################################
#   filename:pysenha.py                                                       
#   created: 2022-03-23                                                              
#   import your librarys below                                                    
#############################################################################################################################
import random
from datetime import datetime, date, timedelta
import win32com.client as client

#parametros serão: email, dias para avisar, senha antiga

        
def pysenha(recipient, d, old_password):
    try:
        #date
        datetomorrow = datetime.now() + timedelta(days = d)
        dateRemember = datetomorrow.strftime("%d/%m/%Y %H:%m")

        old = old_password
        old = old.replace("", "-")
        old = old.split('-')[1:18]
        new = []
        for i in range(len(old)):
            a = random.choice(old)
            new.append(a)

        new_password = ''.join(new)

        #sendMail
        #connect with outlook
        outlook = client.Dispatch("outlook.application")

        #create a newcalendar 

        call_item = outlook.CreateItem(1)

        #subject
        call_item.subject = "TROCA DE SENHA"
        #body
        call_item.body = f"""
        ######################################
        CHEGOU O DIA DE TROCAR A SUA SENHA.
        #######################################
        SENHA ATUAL > {old_password}
        #######################################
        SENHA PARA TROCAR > {new_password}
        #######################################

        """
        #location
        call_item.location = f"NOVA SENHA: {new_password}"
        #date and time
        call_item.start = dateRemember
        call_item.duration = 40
        #adicionando anexos
        #call_item.Attachments.Add("C:/Users/Bates/Documents/Repositorios/LIBS/meetPython/meetPython/module.json")
        #priority
        call_item.importance = 2
        #meeting status for validate
        call_item.MeetingStatus = 1

        #add peoples
        call_item.Recipients.add(recipient).Type = 1
        #call_item.display()
        call_item.send()
    except:
        print(f"Email enviado com sucesso para {recipient}")
    

