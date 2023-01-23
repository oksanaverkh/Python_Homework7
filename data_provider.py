from random import randint
from datetime import datetime as dt
import logger as log

def import_contact_from_file(filename):
    with open('phonebook.txt', 'a') as file:
        with open(filename, 'r') as data:
            data = data.readlines()
            file.writelines(f'{data[0]}')
            file.writelines(data[1])
            file.writelines(data[2])
            file.writelines(f'{data[3]}\n')
    log.log_input_data('New contact imported from a file')

def add_contact_manually(contact_name):
    with open('phonebook.txt', 'a') as file:
        file.write(f'{contact_name}\n')
    log.log_input_data('New contact added')

def find_contact_in_phonebook(last_name):
    with open('phonebook.txt', 'r') as data:
            data = data.read().split('\n')
            for i in range(len(data)):
                if f'Surname: {last_name}' in data[i]:
                    print(str('\n'+data[i]+'\n'+data[i+1]+'\n'+data[i+2]+'\n'+data[i+3]))
    log.log_input_data('Provided info about contact')  
          

    