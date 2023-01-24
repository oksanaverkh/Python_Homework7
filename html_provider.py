from data_display import show_phonebook

def create_html():
    style1 = 'style="font-size:42px;"'
    style2 = 'style="font-size:22px;"'
    style3 = 'style="font-size:28px;"'

    html = '<html>\n <head>    <p {}>{}</p></head>\n <body>\n'\
            .format(style1, 'Phonebook')
    count=1
    html +='<html>\n <head>    <p {}>{}</p></head>\n <body>\n'\
            .format(style3, f'Contact {count}')
    for i in range(len(show_phonebook())):
        data = (show_phonebook())[i]
        if not (i+1)%4:
            count+=1
            html +='<html>\n <head>    <p {}>{}</p></head>\n <body>\n'\
            .format(style3, f'Contact {count}')
        html +='    <p {}>{}</p>\n'\
            .format(style2, data)
    html += '   </body>\n</html'

    with open('index.html', 'w') as page:
        page.write(html)
    
    return html