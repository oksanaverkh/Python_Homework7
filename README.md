Options available for the user while working with this phonebook:

1. View info about contact: user needs to enter a surname 
2. Addition of a new contact: 
    * my manual enter of info
    * by uploading a .txt file, info must be in the same format as in the phonebook
3. Opening the whole phonebook:
    * in browser (as html-page)
    * in .csv file
    * in terminal
4. View logging journal:
    * in .csv file
    * in terminal

Modules:
* module 'main' runs the program, user should choose necessary operation to do with phonebook
* module 'user_interface' contains functions for which user's info must be provided: finding, adding contacts
* module 'check_input' runs verification of user's choice in module 'main'
* module 'data_provider' contains functions for filling the phonebook
* module 'data_display' contains functions for display necessary info: finding contact, browsing of the phonebook
* module 'logger' creates, writes and displays logging journal
* modules 'html-' and 'csv-provider' describes functions for unloading the phonebook in web-page and .csv file