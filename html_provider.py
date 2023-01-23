from data_display import show_phonebook

def create():
    style1 = 'style="font-size:42px;"'
    style2 = 'style="font-size:22px;"'

    html = '<html>\n <head>Phonebook</head>\n <body>\n'\
            .format(style1, 'Phonebook')
    for i in range(len(show_phonebook())):
        data = (show_phonebook())[i]
        html +='    <p {}>{}</p>\n'\
            .format(style2, data+'\n')
        html +='\n'
    html += '   </body>\n</html'

    with open('index.html', 'w') as page:
        page.write(html)
    
    return html