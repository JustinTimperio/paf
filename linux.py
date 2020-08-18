#! /usr/bin/env python3
import re
import os
import sys
from .file import read_file


############
# File System Commands
######

def rm_file(file_path, sudo):
    '''
    Uses os.system() to remove files using standard nix commands.
    The main advatage over os submodule is support for sudo.
    '''
    if sudo is True:
        if os.path.exists(file_path):
            os.system('sudo rm ' + file_path)
    elif sudo is False:
        if os.path.exists(file_path):
            os.system('rm ' + file_path)
    else:
        sys.exit('Error: Sudo Must be True/False!')


def mk_dir(dir_path, sudo):
    '''
    Uses os.system() to make a directory using standard nix commands.
    The main advatage over os submodule is support for sudo.
    '''
    if sudo is True:
        if not os.path.exists(dir_path):
            os.system("sudo mkdir " + dir_path)
    elif sudo is False:
        if not os.path.exists(dir_path):
            os.system("mkdir " + dir_path)
    else:
        sys.exit('Error: Sudo Must be True/False!')


def rm_dir(dir_path, sudo):
    '''
    Uses os.system() to remove a directory using standard nix commands.
    The main advatage over os submodule is support for sudo.
    '''
    if sudo is True:
        if os.path.exists(dir_path):
            os.system('sudo rm -r ' + dir_path)
    elif sudo is False:
        if os.path.exists(dir_path):
            os.system('rm -r ' + dir_path)
    else:
        sys.exit('Error: Sudo Must be True/False!')


def change_permissions(path, perm_num):
    '''
    Change permissions recursively on path.
    '''
    os.system("sudo chmod -R " + perm_num + " " + path)


def basename(path):
    '''
    Provides faster file name trim than os.basename()
    '''
    return path.split('/')[-1]


def basenames(file_list):
    '''
    Returns a list of unique file names. Will remove duplicates names.
    Provides faster file name trim than looping with os.basename()
    '''
    return {p.split('/')[-1] for p in file_list}


############
# Terminal
######

def escape_bash_input(astr):
    '''
    Uses regex subsitution to safely escape bash input.
    '''
    return re.sub("(!| |\$|#|&|\"|\'|\(|\)|\||<|>|`|\\\|;)", r"\\\1", astr)


def sed_replace(pattern, file_path):
    os.system("sed -e'" + pattern + "' -i " + file_path)


def sed_uncomment_line(pattern, file_path, sudo):
    '''
    Uncomments lines using sed. This can safely be run over a file multiple
    times without adverse effects. This is ungodly helpful when modifing
    linux config files.
    '''
    if sudo is True:
        os.system("sudo sed -e'/" + pattern + "/s/^#//g' -i " + file_path)
    elif sudo is False:
        os.system("sed -e'/" + pattern + "/s/^#//g' -i " + file_path)
    else:
        sys.exit('Error: Sudo Must be True/False!')


def sed_comment_line(pattern, file_path, sudo):
    '''
    Comments lines using sed. This can safely be run over a file multiple
    times without adverse effects. This is ungodly helpful when modifing
    linux config files.
    '''
    if sudo is True:
        os.system("sudo sed -e'/" + pattern + "/s/^#*/#/g' -i " + file_path)
    elif sudo is False:
        os.system("sed -e'/" + pattern + "/s/^#*/#/g' -i " + file_path)
    else:
        sys.exit('Error: Sudo Must be True/False!')


############
# Linux System Commands
######

def am_i_root():
    '''
    Checks if python was run with sudo or as root.
    Returns True if root and False if userspace.
    '''
    if os.getuid() == 0:
        return True
    else:
        return False


def distro_name():
    '''
    Returns distrbution information from /etc/os-release.
    '''
    release = read_file('/etc/os-release')
    version = 'none'

    for line in release:
        if line.startswith('ID='):
            name = line[3:].replace('"', '')
        elif line.startswith('VERSION_ID='):
            version = line[11:].replace('"', '')

    del release
    return (name, version)


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


def yay_install(packages, arg='-S'):
    os.system("yay " + arg + packages)
