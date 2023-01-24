from datetime import datetime as dt

def log_input_data(text):
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    with open('log.txt', 'a') as file:
        file.write('{}:{}\n'
                        .format(time, str(text)))

def log_output_data_term():
    with open('log.txt', 'r') as data:
        print(*data.readlines())

def log_output_data_csv():
    with open('log.csv', 'w') as file:
        with open('log.txt', 'r') as data:
            data = data.readlines()
            # for i in range(len(data)):
            #     data = data[i]
            file.writelines(data)
