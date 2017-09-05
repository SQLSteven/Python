#!/usr/bin/python3

import datetime as dt
while 1==1:
    DAYSINAYEAR = 365.26
    print('What is your name?')
    NAME = input()
    VALIDDATE = False
    while not VALIDDATE:
        print('What is your date of birth? (please use the format YYYY-MM-DD)')
        try:
            BIRTHDATE = dt.datetime.strptime(input(),'%Y-%m-%d')    
        except:
            print('Wrong format, please try again:')    
            continue
        VALIDDATE = True
    TODAY = dt.datetime.now()
    AGE = abs((TODAY-BIRTHDATE).days)
    print('Hello ' + NAME + '.')
    print('I see that you are ' + str(AGE/DAYSINAYEAR) + ' years old.')
    print('(e)xit or (c)ontinue')
    CHOICE = input()
    if CHOICE == 'e' or CHOICE == 'E':
        break
