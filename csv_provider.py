from data_display import show_phonebook

def create_csv():
    with open('phonebook.csv', 'w') as file:
        for i in range(len(show_phonebook())):
            data = (show_phonebook())[i]
            file.write(data)
    
