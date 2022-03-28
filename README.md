
<h1 align="center">
<img src="https://img.shields.io/static/v1?label=PYSENHA%20POR&message=Bates&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center">PYSENHA </p> </h3>

<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> generator password with calendar </p>

>> <h3> How install </h3>

```
pip install pysenha==6.0.0

```
>> <h3> How Works </h3>

```
pysenha(recipient, d, old_password)


#recipient = This is a string and means the email of the recipient who will receive the message.
#d = This is a int and means The number of days, starting today, that you need to schedule yourself to #change your password
#old_password = This is a string and means your current password and it will be changed!

#As an exit you will receive the following message:
 ######################################
    CHEGOU O DIA DE TROCAR A SUA SENHA.
    #######################################
    SENHA ATUAL > {old_password}
    #######################################
    SENHA PARA TROCAR > {new_password}
    #######################################

```
    