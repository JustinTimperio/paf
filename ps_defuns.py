#! /usr/bin/env python3
#### Core Functions - v2.0
import re, math

def prError(text): print("\u001b[31;1m{}\033[00m" .format(text))
def prSuccess(text): print("\u001b[32;1m{}\033[00m" .format(text))
def prWorking(text): print("\033[33m{}\033[00m" .format(text))
def prWarning(text): print("\033[93m{}\033[00m" .format(text))
def prChanged(text): print("\u001b[35m{}\033[00m" .format(text))
def prRemoved(text): print("\033[31m{}\033[00m" .format(text))
def prAdded(text): print("\033[94m{}\033[00m" .format(text))

######
## Basic Functions
######
def Date_To_Today(year, month, day):
    import datetime
    start_date = datetime.date(year, month, day)
    end_date = datetime.date.today() - datetime.timedelta(days=1)
    date_delta = abs((start_date - datetime.date.today()).days)
    date_list = [str(end_date - datetime.timedelta(days=x)) for x in range(0, date_delta)]
    return date_list

def YN_Frame(prompt):
    while True:
        yn = input(prompt + ' (y/n):')
        if yn.lower().strip() in ['y','yes']:
            return True
        elif yn.lower().strip() in ['no','n']:
            return False
        else:
           print('Please Respond With Yes/No!')

def Multi_Choice_Frame(options):
    ordered_list = list(options)
    counter = 1
    while True:
        for o in ordered_list:
            print('(' + str(counter) + ') ' + o)
            counter += 1
        selection = input('Enter Your Selection With an INT: ').strip()

        if re.findall(r'^([1-9]|0[1-9]|[1-9][0-9]|[1-9][1-9][0-9])$', selection):
            if int(selection) < counter:
                return ordered_list[int(selection) - 1]
        elif selection.strip() == 'exit' or 'quit':
            return False
        else:
            counter = 1
            print('No Validate INT Given!')

def Read_Between(start, end, iterable, re_flag=False):
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

def Convert_Size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return "{} {}".format(size, size_name[i])
