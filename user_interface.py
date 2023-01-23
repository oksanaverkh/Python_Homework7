import logger as log    
import data_provider as dp

# def get_data():
#     a = input('Enter a number: ')
#     op = input('Enter an operator: ')
#     b = input('Enter a number: ')
#     log.logger(a+op+b)

#     if 'j' in a:
#         a = complex(a)
#     if 'j' in b:
#         b = complex(b)
#     else:
#         a = int(a)
#         b = int(b)
#     # log.input_logger(a, b, op)

#     return a, b, op

def add_contact():
    log.log_input_data('Contact addition requested by user')
    surname = input('Enter a surname: ')
    name = input('Enter a name: ')
    telephone = input('Enter a phone number: ')
    description = input('Enter description: ')
    contact = 'Surname: '+surname+'\n'+'Name: '+name +'\n'+'Telephone: '+telephone+'\n'+'Comment: '+description+'\n'
    dp.add_contact_manually(contact)
    return contact

def import_contact():
    log.log_input_data('Contact import from file requested by user')
    print('Enter a path to file: ')
    name_file = input()
    dp.import_contact_from_file(name_file)

def show_contact():
    surname = input('Enter a surname: ')
    print(dp.find_contact_in_phonebook(surname))