#! /usr/bin/python
#### Core Functions - v1.0
import os, sys

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

def yn_frame(prompt, y_defun, n_defun):
    yn = input(prompt + '? (y/n):')
    if yn.lower() in ['y','yes']: 
        y_defun
    elif yn.lower() in ['no','n']:
        n_defun
    else: sys.exit('No usable argument given!') 

def export_list(file_name, list_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        for i in list_name:
            f.write("%s\n" % i) 

def read_list(file_name):
    list_name = list(open(file_name).read().splitlines()) 
    return list_name
