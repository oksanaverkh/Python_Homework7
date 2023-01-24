from datetime import datetime as dt

def log_input_data(text):
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    with open('log.txt', 'a') as file:
        file.write('{}:{}\n'
                        .format(time, str(text)+'\n'))

def log_output_data():
    with open('log.txt', 'r') as data:
        print(data.readlines())