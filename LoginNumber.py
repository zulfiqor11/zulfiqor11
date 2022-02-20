from telethon.sync import TelegramClient
from telethon import utils
import csv
from csv import reader
import configparser
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Style.BRIGHT + Fore.RESET + 'Welcome To jeevan Program\n')

with open('phone.csv','r')as f:
 str_list=[row[0]for row in csv.reader(f)]
 po=0
 for pphone in str_list:
  phone=utils.parse_phone(pphone)
  po+=1

  print(Style.BRIGHT + Fore.GREEN + f"Login {Style. RESET_ALL} {Style.BRIGHT+Fore.RESET} {phone}")
  client=TelegramClient(f"sessions/{phone}", 2392599, '7e14b38d250953c8c1e94fd7b2d63550')
  client.start(phone)
  client.disconnect()
  print()
 done=True
input(Style.BRIGHT + Fore.RESET + "All Number Login Done !" if done else "Error!")
print(Style.BRIGHT + Fore.YELLOW + "Press Enter to Exit")
