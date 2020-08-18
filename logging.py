#! /usr/bin/env python3
import os
from datetime import datetime
from .file import read_file


############
# Logging Commands
######

def write_to_log(func, output, log_file):
    log = str('[' + datetime.now().strftime("%H:%M:%S.%f") + '] ' + func + ': ' + output)
    with open(log_file, 'a') as f:
        f.write("%s\n" % log)


def start_log(func, log_file):
    start = '======================== ' + datetime.now().strftime("%Y/%m/%d") + ' ========================'
    with open(log_file, 'a') as f:
        f.write("%s\n" % start)
    write_to_log(func, 'Started Logging Session', log_file)


def end_log(func, log_file, log_length=0):
    write_to_log(func, 'Ended Logging Session', log_file)
    if log_length == 0:
        pass
    else:
        os.system('cat ' + log_file + ' | tail -n ' + str(log_length) + ' | tee ' + log_file + ' > /dev/nul')
        write_to_log(func, 'Trimmed Log to ' + str(log_length) + ' Lines On Exit', log_file)
    os.system('echo -e >> ' + log_file)
