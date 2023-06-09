from getpass import getpass
import os

def save_file(date):
    with open('data.txt', 'a', newline='') as file:
        file.write(date + os.linesep)   

def create_user():
    new_user = input('Type the new user: ')
    return new_user

def create_password(user):    
    user_password = getpass('Type password: ')
    while True:
        confirm_password = getpass('Confirm password: ')
        if confirm_password == user_password:
            save_file(user)
            save_file(user_password)
            break
        else:
            continue 

def is_login_valid(user, password):
    new_data = []
    with open('data.txt', 'r') as file:
        data = file.readlines()
        for date in data:
            new_data.append(date.replace('\n', ''))

        if user in new_data and password in new_data:
            return print(f'Successful login {user}')
        else:
            return print('Date invalid')
            
def do_login():
    user = input('Type user: ')
    password = getpass('Type password: ')
    is_login_valid(user, password)

def choose_option():
    option = input('|            Option:')
    return option

def delete_user(user):
    user_delete = user
    new_data = []
    with open('data.txt', 'r') as file:
        data = file.readlines()
        if user+'\n' in data:
            for date in data:
                new_data.append(date.replace('\n', ''))
        else:
            print('User invalid')
            return        
    try:
        if user in new_data:
            new_data.pop(new_data.index(user)+1)
            new_data.pop(new_data.index(user))

        with open('data.txt', 'w', newline='') as file:
            for data in new_data:
                file.write(data + os.linesep)
        print(f'{user_delete} deleted')        
    except:
        print(f'{user_delete} not found')        

def show_users():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    
    for i in range(0,len(data),2):
        print(data[i].rstrip('\n'))

def main(option):
    if option == '1':
        do_login()
    elif option == '2':
        new_user = create_user()
        create_password(new_user)
        print(f'User {new_user} was successfully created')
    elif option == '3':
        user = input('Type user for delete: ')
        delete_user(user)
    elif option == '4':
        show_users() 
    elif option == '5':
        exit()         
    else:
        print('🚫 Option invalid! 🚫')        
        main(choose_option())

while True:
    print('\nWelcome in this system - by Sautier Alexsander ')
    print('-----------------------------------------------')    
    print('|            Choose a option                  |')
    print('|            [1] - LogIn                      |')    
    print('|            [2] - Create New User            |')    
    print('|            [3] - Delete User                |')    
    print('|            [4] - Show Users                 |')    
    print('|            [5] - Exit                       |')    
    main(choose_option())
    input('Press "ENTER" to continue')
    os.system('clear')