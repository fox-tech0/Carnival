from colorama import *
import os
from time import sleep as wait

init(autoreset=True)

print(Fore.LIGHTRED_EX + "Carnival")

print("""-> Options
Which would you like to select?""")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(Fore.LIGHTBLUE_EX + '1. ' + Fore.RESET + 'Github Repo')
print(Fore.LIGHTBLUE_EX + '2. ' + Fore.RESET + 'Repl.it Repo')
print('')
choice = input("Enter a Choice Number: ")
if(choice == "1"):
  os.system('clear')
  print('Username: ')
  username = input()
  print('Repo Name: ')
  name = input()
  os.system('clear')
  print('The Repo URL will look like this: ')
  url = "https://github.com/" + username +"/"+name 
  print(url)
  wait(5)
  os.system('clear')
  reciept = ""
  reciept += "URL: "+ url +"\n"
  reciept += "Name: " + name+ "\n"
  reciept += "By: "+ username
  print(reciept)
elif(choice == "2"):
  os.system('clear')
  print('Username: ')
  username = input()
  print('Repo Name: ')
  name = input()
  print('File Extension: ')
  extensions = input()
  print('File Name: (main, index): ')
  type = input()
  os.system('clear')
  print('The Repo URL will look like this: ')
  url = "https://repl.it/@" + username +"/"+name+"#"+ type + extensions
  print(url)
  wait(5)
  os.system('clear')
  reciept = ""
  reciept += "URL: "+ url +"\n"
  reciept += "Name: " + name+ "\n"
  reciept += "By: "+ username
  print(url)
