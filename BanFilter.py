from telethon.sync import TelegramClient
from telethon import functions, types
import csv
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Style.BRIGHT + Fore.RESET + 'Welcome To jeevan Program\n')
import subprocess, requests, time, os
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/xxxxxxxx')

try:#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if hwid in r.text:
        pass
    else:#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        print(Style.BRIGHT + Fore.RED + 'Your Software Are Not Activated By jeevan')
        print(f'Activation Key: {hwid}') 
        time.sleep(30)#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        os._exit()
except:
    print(Style.BRIGHT + Fore.YELLOW + 'Please Contact To jeevan For Activation')
    time.sleep(50) #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    os._exit() 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print(Style.BRIGHT + Fore.GREEN + 'Your Software Activated Successfully By jeevan\n')
with open('api.csv' , 'r' , encoding='utf-8') as f:
    users1=csv.reader(f)
    api=[i for i in users1]

with open('phone.csv' , 'r' , encoding='utf-8') as f:
    users1=csv.reader(f)
    phone=[i for i in users1]

bannumber=[]
f=open('BanNumber.csv', 'a',newline='',encoding='utf-8')
writer = csv.writer(f)
f1=open('BanApi.csv', 'a',newline='',encoding='utf-8')
writer1 = csv.writer(f1)

for i in range(len(phone)):
    client = TelegramClient(f"sessions/{phone[i][0]}", api[i][0], api[i][1])
    try:
        client.connect()
        if client.is_user_authorized():        
            print(Style.BRIGHT + Fore.RESET + f"SUCCESS")
            client.disconnect()
        else:
            print(Style.BRIGHT + Fore.RED + "Number Banned")
            fields=[phone[i][0]]
            writer.writerow(fields)
            fields=[api[i][0], api[i][1]]
            writer1.writerow(fields)
            bannumber.append(i)


    except telethon.errors.rpcerrorlist.ApiIdInvalidError:
        print("INVALID API")

    except telethon.errors.rpcerrorlist.PhoneNumberBannedError:
        print(f"{phone} is banned")
        fields=[phone[i][0]]
        writer.writerow(fields)
        fields=[api[i][0], api[i][1]]
        writer1.writerow(fields)
        bannumber.append(i)
    
    except:
        print(f'check detail of {phone}')

f.close()
f1.close()
bannumber.sort(reverse=True)
for i in bannumber:
    del api[i]
    del phone[i]

f=open('api.csv', 'w',newline='',encoding='utf-8')
writer = csv.writer(f)
for i in range(len(api)):
    fields=[api[i][0], api[i][1]]
    writer.writerow(fields)
f.close()
f=open('phone.csv', 'w',newline='',encoding='utf-8')
writer = csv.writer(f)
for i in range(len(phone)):
    fields=[phone[i][0]]
    writer.writerow(fields)
f.close()

print(Style.BRIGHT + Fore.GREEN + 'Task completed')
print(Style.BRIGHT + Fore.YELLOW + "Enter any key to exit")
input()