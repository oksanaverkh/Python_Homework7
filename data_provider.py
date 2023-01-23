from random import randint
from datetime import datetime as dt
import logger as log

def import_contact_from_file(filename):
    with open('phonebook.txt', 'a') as file:
        with open(filename, 'r') as data:
            data = data.readlines()
            file.writelines(f'\n{data[0]}')
            file.writelines(data[1])
            file.writelines(data[2])
            file.writelines(f'{data[3]}\n')
    log.log_input_data('New contact imported from a file')

def add_contact_manually(contact_name):
    with open('phonebook.txt', 'a') as file:
        file.write(f'{contact_name}\n')
    log.log_input_data('New contact added')

def find_contact_in_phonebook(last_name):
    log.log_input_data('Info about contact requested by user')
    with open('phonebook.txt', 'r') as data:
            data = data.readlines()
            if last_name in data:
                return data

    log.log_input_data('Provided info about contact')