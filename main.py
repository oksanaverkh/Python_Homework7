import user_interface as ui
import controller as c
import logger as log

print('Choose an operation: ')
print('finding a contact - 1', 'addition of a new contact - 2', 'export of a phonebook - 3', 'logger journal looking - 4', sep='\n')
user_input = c.check_input_1()
if user_input =='1':
    next_input = input('Enter a surname: ')
elif user_input =='2':
    print('Choose an operation: manual addition - 1, import from a file - 2')
    next_input = c.check_input_2()
    if next_input =='1':
        ui.add_contact()
    else:
        ui.import_contact()
elif user_input =='3':
    print('Choose a view format: HTML - 1, CSV.file - 2')
    next_input = c.check_input_2()
    if next_input =='1':
        pass
    else:
        pass
elif user_input=='4':
    pass