
#############################################################################################################################
#   filename:pysenha.py                                                       
#   created: 2022-03-23                                                              
#   import your librarys below                                                    
#############################################################################################################################
import random
import yagmail
from datetime import datetime, date, timedelta

#parametros serão: email, senhadoemail, dias para avisar, senha antiga

        
def pysenha(sender,sender_password,recipient, d, old_password):

    #date
    datetomorrow = datetime.now() + timedelta(days = d)
    dateRemember = datetomorrow.strftime("%d/%m")
       
    old = old_password
    old = old.replace("", "-")
    old = old.split('-')[1:18]
    new = []
    for i in range(len(old)):
        a = random.choice(old)
        new.append(a)

    new_password = ''.join(new)

    #sendMail
    
    mailServer = yagmail.SMTP(sender, sender_password)
    toFrom = recipient
    
    
    mailServer.send(toFrom, subject = "Time to Change Password",
    contents = f"""

<p> It's time to change your password for security reasons. </p>
<p> Your current password is currently: <h3> <b> "{old_password }" </b> </h3> </p>
<p> We recommend switching to: <h3> <b> "{new_password}" </b> </h3> </p>
<p> The final date to exchange is é <b> {dateRemember} </b> from this year. </p>
<p> Do this in less than 15 days from now, otherwise your access will be more difficult. </p> """)

   

    print(f"Email sent to {recipient} successfully!")

    
