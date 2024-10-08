# Programa que demana la data de neixament.

dia=int(input("Dia?"))
mes=int(input("Mes?"))
any=int(input("Any?"))

#Validar les dades

from datetime import datetime

current_second = datetime.now().second
current_minute = datetime.now().minute
current_hour = datetime.now().hour

current_dat = datetime.now().day
current_month = datetime.now().hour
current_year = datetime.now().year

if any>current_year:
    print("Any incorrecte")
    print("Programa Finalitzat")

if mes>12 or mes<1:
    print("Mes incorrecte")
    print("Programa Finalitzat")

if dia>31 or dia<1:
    print("Dia incorrecte")
    print("Programa Finalitzat")

#Procesar les dades
#todo calcular edat
print("Programa Finalitzat")