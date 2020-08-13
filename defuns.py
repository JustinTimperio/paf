#! /usr/bin/env python3
import datetime as dt
import re
import math
import os
import sys


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


############
# File System Commands
######


def Search_FS(path, typ='list'):
    '''Uses os.path.join() and os.walk() to search through directories.'''
    if typ.lower() in ['list', 'l']:
        return [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn]
    elif typ.lower() in ['set', 's']:
        return {os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn}
    else:
        sys.exit('Error: Type Must be List/Set!')


def Size_Of_Files(file_list):
    '''Returns Size of Files in Bytes.'''
    size = 0
    for f in file_list:
        try: size += os.path.getsize(f)
        except Exception: OSError
    return size


############
# File Commands
######

def Export_List(file_name, iterable):
    '''Export list or set to file name.'''
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        for i in iterable:
            f.write("%s\n" % i)


def Read_List(file_name, typ='list'):
    '''Reads file into set or list.'''
    if typ == 'list':
        fl = list(open(file_name).read().splitlines())
    elif typ == 'set':
        fl = set(open(file_name).read().splitlines())
    else:
        sys.exit('Error: Type Must be List/Set!')
    return fl


def Read_Between(start, end, iterable, re_flag=False):
    '''
    Returns list of lines found between two strings/values.
    If re_flag is False, direct string comparison will be used.
    If re_flag is True, regex will be used to find start and end strings.
    '''
    lines = list()
    flag = None

    if re_flag is False:
        for line in iterable:
            if line is start:
                flag = True
            elif line is end:
                flag = False
            elif flag is None or flag is False:
                pass
            elif flag is True:
                lines.append(line)
        return lines

    elif re_flag is True:
        for line in iterable:
            if re.findall(re.escape(start.lower()), line.lower()):
                flag = True
            elif re.findall(re.escape(end.lower()), line.lower()):
                flag = False
            elif flag is None or flag is False:
                pass
            elif flag is True:
                lines.append(line)
        return lines
