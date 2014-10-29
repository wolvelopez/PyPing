import os
import easygui


print("Introduzca host: ")
host = input()
easygui.msgbox("This is a message!", title="simple gui")
i = 0
while i < 100000:
    ping = os.popen("ping -n 1 %s" % host)
    salidaPing = ping.readlines()
    for linea in salidaPing:
        print(linea)
        pos = linea.find('tiempo=')
        #Sumamos palabra tiempo + =
        pos = pos + 7
        tiempo = linea.find('ms', pos, len(linea))
        cadena = linea[pos:tiempo]
        print(cadena)
    i = i + 1
