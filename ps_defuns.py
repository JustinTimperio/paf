#! /usr/bin/env python3
#### Core Functions - v1.0
from .ps_modules import *

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
    p = ("\u001b[33;1m{}\033[00m" .format(prompt)) 
    yn = input(prompt + ' (y/n):')
    if yn.lower().strip() in ['y','yes']: 
        return True
    elif yn.lower().strip() in ['no','n']:
        return False
    else: sys.exit('Input Must be Y/N!') 

def export_list(file_name, iterable):
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        for i in iterable:
            f.write("%s\n" % i) 

def read_list(file_name):
    l = list(open(file_name).read().splitlines()) 
    return l

def read_between(start, end, iterable, re_flag=False):
    lines = list()
    flag = None
    if re_flag == False:
        for l in iterable:
            if l == start:
                flag=True
            elif l == end:
                flag=False
            elif flag is None or flag == False:
                pass
            elif flag == True:
                lines.append(l)
        return lines
    
    elif re_flag == True:
        import re
        for l in iterable:
            if re.findall(re.escape(start.lower()), l.lower()):
                flag=True
            elif re.findall(re.escape(end.lower()), l.lower()):
                flag=False
            elif flag is None or flag == False:
                pass
            elif flag == True:
                lines.append(l)
        return lines

def convert_size(size_bytes): 
    import math
    if size_bytes == 0: 
        return "0B" 
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB") 
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i) 
    size = round(size_bytes / power, 2) 
    return "{} {}".format(size, size_name[i])
