#! /usr/bin/env python3
#### Core Functions - v1.0
import os, sys, termcolor

######
## Basic Functions
######
def date_to_today(year, month, day, set_name):
    import datetime
    start_date = datetime.date(year, month, day)
    end_date = datetime.date.today() - datetime.timedelta(days=1)
    date_delta = abs((start_date - datetime.date.today()).days)
    list_name = {str(end_date - datetime.timedelta(days=x)) for x in range(0, date_delta)}
    return set_name

def yn_frame(prompt):
    p = ("\033[93m {}\033[00m" .format(promt)) 
    yn = input(prompt + ' (y/n):')
    if yn.lower() in ['y','yes']: 
        return True
    elif yn.lower() in ['no','n']:
        return False
    else: sys.exit('Input Must be Y/N!') 

def export_list(file_name, list_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        for i in list_name:
            f.write("%s\n" % i) 

def read_list(file_name):
    l = list(open(file_name).read().splitlines()) 
    return l
