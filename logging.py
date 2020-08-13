#! /usr/bin/env python3
from datetime import datetime
import os
from .ps_linux import Escape_Bash

############
# OS Commands and Short-Cuts
######


def Write_To_Log(func, output, log):
    log = str('[' + datetime.now().strftime("%H:%M:%S.%f") + '] ' + func + ': ' + output)
    os.system('echo "' + Escape_Bash(log) + '" >> ' + log)


def Start_Log(func, log):
    os.system('echo "======================== ' + datetime.now().strftime("%Y/%m/%d") + ' ========================" >> ' + log)
    Write_To_Log(func, 'Started Logging Session', log)


def End_Log(func, log, log_length=0):
    Write_To_Log(func, 'Ended Logging Session', log)
    os.system('echo -e >> ' + log)
    if log_length > 0:
        pass
    else:
        os.system('cat ' + log + ' | tail -n ' + str(log_length) + ' > ' + log)
