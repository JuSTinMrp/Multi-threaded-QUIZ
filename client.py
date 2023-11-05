#!/usr/bin/env python

import socket
import json
import os # for clearing screen

# banner

def banner():
    print('''
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓█▓▒▓█▓▒▓█░░░░░
            ░░░░░░░░░CREATED BY░░░░░░░░░░░░▓█▓▒▒░░▒░░░░░▒██▒░░
            ░░░░░░░░░░░@JuSTinMrp░░░░░░▒▓█▓░░░░░░░░░░░░░░██▓░░
            ░░░░░░░░░░░@Vishallas░░░░░░██▒░▓▓░░░░▒▓░░░░░░░██▒░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░▓█▓░░░░░░░░░░░░░░░░░▓█▓░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░██▒░░░▒░░░░░░░░░░░░░██▓░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░▓█▒░░░▒█▓▓██▒░░░░░░▒██░░
            ░░░░░░░░░░░▒▒▓▒▒▒▒▓▓▓▓▒░░░░██▒░░░░░░░░░░░░░░▒██░░░
            ░░░░░░░░░░▓▓▒▒▒▓▓▓▓▒▒▒▒▒░░░░▒██▓▒▒░░░░▒▒▓▓██▓░░░░░
            ░░░░░░░░░▒▓▒▒▒▒▒▓▓▓▓▒▒▒▒▒░░░░░░▒▒▒███▒▒▒▒░░░░░░░░░
            ░░░░░░░░░░░▒▒▓▓▒▒▓▓▒▒▒▒▓░░░░░░░░░░██▒░░░░░░░░░░░░░
            ░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▒▒░░░░░░░▒██░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░▒█▓▒▒░▒▓▓███▓▒▒▒▓█▓░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓███▓░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▒░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░▓█▓░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██▒░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░██▒░░░░░░░░░
''')
    
# screen clearing 
def clear_screen():
    # Clear the screen depending on the OS
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pprint(question):
    clear_screen()      # clearing and showing banner
    banner()
    print('\n1) %s\r' % question['question'])
    for i in range(4):
        print(f"[{i+1}] {question['choices'][i]}")

    choice = int(input('\nEnter the choice : ').strip())

    input('\nConfirm the Choice %d, press enter.' % choice)

    return choice

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1111
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))


while True:
    name_prompt = client_socket.recv(1024).decode()
    print(name_prompt, end='')
    
    try:
        name = input()
        client_socket.send(name.encode())
        NO_OF_QUES = int(client_socket.recv(1024).decode())
        for i in range(NO_OF_QUES):
            data = client_socket.recv(1024).decode()
            if data != '':
                question = json.loads(data)
                choice = pprint(question)
                client_socket.send(str(choice).encode())
        client_socket.close()
        print("You completed the test... :)")
        break
    except KeyboardInterrupt:
        print("\nYou exited the test... :(")
        client_socket.close()
        break