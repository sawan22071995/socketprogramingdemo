command=""
started=False
while(True):
    command=input('>').upper()
    if command=='HELP':
        print('''
start-to start the car
stop-to stop the car
quit-quit the car game''')
    elif command=='START':
        if started:
            print('the car is alredy started!!!')
        else:
             print('car stared....')
             started=True
    elif command=='STOP':
        if not started:
             print('the car is already stopped!!')
        else:
            started=False
            print('Car stopped')
    elif command=='QUIT':
        exit()
    else:
        print('i dont understand that!!!')
        print('please type "help" command to understand game!!')