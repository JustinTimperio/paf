#! /usr/bin/env python3
# General Functions - v2.2.0
import datetime as dt
import re
import math
import os


def Write_To_Log(func, output, log_file):
    log = str('[' + dt.datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f") + '] ' + func + ' : ' + output)
    os.system('echo "' + log + '" >> ' + log_file)


def Start_Log(func, log_file):
    os.system('echo ================================ >> ' + log_file)
    Write_To_Log(func, 'Started Logging Session', log_file)


def End_Log(func, log_file):
    Write_To_Log(func, 'Ended Logging Session', log_file)


def Replace_Spaces(lst):
    '''Replaces all ` ` with `_` in each string in list.'''
    trim = {s.strip().replace(' ', '-') for s in lst}
    return trim


def Date_To_Today(year, month, day):
    '''Returns a list of dates between input date and today.'''
    start_date = dt.date(year, month, day)
    end_date = dt.date.today() - dt.timedelta(days=1)
    delta = abs((start_date - dt.date.today()).days)
    date_list = [str(end_date - dt.timedelta(days=x)) for x in range(0, delta)]
    return date_list


def YN_Frame(prompt):
    '''Standard Y/N input frame. Returns True for Yes, False for No.'''
    while True:
        yn = input('\033[1m' + prompt + ' (y/n):' + '\033[0m')
        if yn.lower().strip() in ['y', 'yes']:
            return True
        elif yn.lower().strip() in ['no', 'n']:
            return False
        else:
            print('Please Respond With Yes/No!')


def Multi_Choice_Frame(options):
    '''Lets a user select between arbitrary number of options.
    Returns value the user selects. Input `exit` or `quit` to return False.'''
    c_list = list(options)
    counter = 1
    while True:
        for o in c_list:
            print('(' + str(counter) + ') ' + o)
            counter += 1
        ans = input('\033[1m' + 'Enter Your Selection With an INT: ' + '\033[0m').strip()

        if re.findall(r'^([1-9]|0[1-9]|[1-9][0-9]|[1-9][1-9][0-9])$', ans) and int(ans) < counter:
            return c_list[int(ans) - 1]
        else:
            counter = 1
            print('No Validate INT Given!')


def Read_Between(start, end, iterable, re_flag=False):
    '''Returns list of lines found between two strings/values.
    If re_flag is False, direct string comparison will be used.
    If re_flag is True, regex will be used to find start and end strings.'''
    lines = list()
    flag = None

    if re_flag is False:
        for l in iterable:
            if l is start:
                flag = True
            elif l is end:
                flag = False
            elif flag is None or flag is False:
                pass
            elif flag is True:
                lines.append(l)
        return lines

    elif re_flag is True:
        for l in iterable:
            if re.findall(re.escape(start.lower()), l.lower()):
                flag = True
            elif re.findall(re.escape(end.lower()), l.lower()):
                flag = False
            elif flag is None or flag is False:
                pass
            elif flag is True:
                lines.append(l)
        return lines


def Convert_Size(size_bytes):
    '''Converts raw bytes input into human readable format.'''
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return "{} {}".format(size, size_name[i])


def max_threads(thread_target):
    '''Returns the max # of threads availble for a target process pool.'''
    cores = os.cpu_count()
    if cores >= thread_target:
        return thread_target
    else:
        return cores


# Color Print Output
def prError(text):
    print("\u001b[31;1m{}\033[00m" .format(text))

def prSuccess(text):
    print("\u001b[32;1m{}\033[00m" .format(text))

def prWarning(text):
    print("\u001b[33;1m{}\033[0m" .format(text))

def prBold(text):
    print("\u001b[37;1m{}\u001b[0m" .format(text))

def prChanged(text):
    print("\u001b[35m{}\033[00m" .format(text))

def prRemoved(text):
    print("\033[31m{}\033[00m" .format(text))

def prAdded(text):
    print("\033[94m{}\033[00m" .format(text))
