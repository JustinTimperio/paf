#! /usr/bin/env python3
import os
import sys
import subprocess
import re


############
# File System Commands
######


def RM_File(file_path, sudo):
    '''Uses os.system calls to rm file. Allows sudo.'''
    if sudo is True:
        if os.path.exists(file_path):
            os.system('sudo rm ' + file_path)
    elif sudo is False:
        if os.path.exists(file_path):
            os.system('rm ' + file_path)
    else:
        sys.exit('Error: Sudo Must be True/False!')


def MK_Dir(dir_path, sudo):
    '''Uses os.system calls to mkdir dirs. Allows sudo.'''
    if sudo is True:
        if not os.path.exists(dir_path):
            os.system("sudo mkdir " + dir_path)
    elif sudo is False:
        if not os.path.exists(dir_path):
            os.system("mkdir " + dir_path)
    else:
        sys.exit('Error: Sudo Must be True/False!')


def RM_Dir(dir_path, sudo):
    '''Uses os.system calls to rm dirs. Allows sudo.'''
    if sudo is True:
        if os.path.exists(dir_path):
            os.system('sudo rm -r ' + dir_path)
    elif sudo is False:
        if os.path.exists(dir_path):
            os.system('rm -r ' + dir_path)
    else:
        sys.exit('Error: Sudo Must be True/False!')


def Change_Permissions(path, perm_num):
    '''Change Permissions Recursively on Path.'''
    os.system("sudo chmod -R " + perm_num + " " + path)


def Basename(file_list):
    '''Returns a trim\'ed list of unique file names. Will remove duplicates names.
    Provides faster file name trim than os.basename()'''
    trim = {p.split('/')[-1] for p in file_list}
    return trim


############
# Terminal Commands
######


def Escape_Bash(astr):
    '''Uses regex sub to escape bash input.'''
    return re.sub("(!| |\$|#|&|\"|\'|\(|\)|\||<|>|`|\\\|;)", r"\\\1", astr)


def Sed_Replace(pattern, file_path):
    os.system("sed -e'" + pattern + "' -i " + file_path)


def Uncomment_Line_Sed(pattern, file_path, sudo):
    if sudo is True:
        os.system("sudo sed -e'/" + pattern + "/s/^#//g' -i " + file_path)
    elif sudo is False:
        os.system("sed -e'/" + pattern + "/s/^#//g' -i " + file_path)


def Comment_Line_Sed(pattern, file_path, sudo):
    if sudo is True:
        os.system("sudo sed -e'/" + pattern + "/s/^#*/#/g' -i " + file_path)
    elif sudo is False:
        os.system("sed -e'/" + pattern + "/s/^#*/#/g' -i " + file_path)


############
# Linux System Package Commands
######


def Am_I_Root():
    '''Return True if Root, False if Userspace'''
    if os.getuid() == 0:
        return True
    else:
        return False


def Distro_Name():
    '''Returns Distro Name From /etc/os-release'''
    os_name = subprocess.check_output('cat /etc/os-release | grep PRETTY_NAME= | cut -c 13-', shell=True)
    pretty_name = str(os_name)[2:-3]
    return pretty_name


############
# Linux System Package Commands
######


def pacman(package, arg='-S'):
    os.system("sudo pacman " + arg + " " + package)


def yum(package, arg='install'):
    os.system("sudo yum " + arg + " " + package)


def apt(package, arg='install'):
    os.system("sudo apt-get " + arg + " " + package)


def zypper(package, arg='install'):
    os.system("sudo zypper " + arg + " " + package)


def pip_install(packages, arg='install'):
    os.system("sudo pip " + arg + " " + packages)


def pacaur_install(packages, arg='-S'):
    os.system("pacaur " + arg + packages)
