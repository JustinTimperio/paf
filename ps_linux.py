#! /usr/bin/env python3
#### Linux Commands - v1.02
import os, sys, subprocess

######
### File System Commands and Short-Cuts
######
def open_permissions(path):
    os.system("sudo chmod -R 777 " + path)

def search_fs(path, fs_type='list'):
    fs = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn] 
    if fs_type is 'list':
        return fs
    if fs_type is 'set':
        return set(fs)

def rm_file(file_path, sudo):
    if sudo == True:
        if os.path.exists(file_path):
            os.system('sudo rm ' + file_path)
    elif sudo == False:
        if os.path.exists(file_path):
            os.system('rm ' + file_path)
    else:
        return print('Error: Sudo Must be True/False!')

def mkdir(dir, sudo):
    if sudo == True:
        if not os.path.exists(dir):
            os.system("sudo mkdir " + dir)
    elif sudo == False:
        if not os.path.exists(dir):
            os.system("mkdir " + dir)
    else:
        return print('Error: Sudo Must be True/False!')

def rm_dir(dir_path, sudo):
    if sudo == True:
        if os.path.exists(dir_path):
            os.system('sudo rm -r ' + dir_path)
    elif sudo == False:
        if not os.path.exists(dir):
            os.system('rm -r ' + dir_path)
    else:
        return print('Error: Sudo Must be True/False!')

######
### Terminal Commands
######
def os_distro():
    os_name = subprocess.check_output('cat /etc/os-release | grep PRETTY_NAME= | cut -c 13-', shell=True)
    return str(os_name)[2:-3]

def sed_replace(pattern, file_path):
    os.system("sed -e'" + pattern + "' -i " + file_path)

def uncomment_line_sed(pattern, file_path, sudo):
    if sudo == True:
        os.system("sudo sed -e'/" + pattern + "/s/^#//g' -i " + file_path)
    if sudo == False:
        os.system("sed -e'/" + pattern + "/s/^#//g' -i " + file_path)

def comment_line_sed(pattern, file_path, sudo):
    if sudo == True:
        os.system("sudo sed -e'/" + pattern + "/s/^#*/#/g' -i " + file_path)
    if sudo == False:
        os.system("sed -e'/" + pattern + "/s/^#*/#/g' -i " + file_path)

######
### Linux System Package Commands
######
def pacman(package, arg='-S'):
    os.system("sudo pacman " + arg + " " + package + " --needed")

def yum(package, arg='install'):
    os.system("sudo yum " + arg + " " + package)

def apt(package, arg='install'):
    os.system("sudo apt-get " + arg + " " + package)

def zypper(package, arg='install'):
    os.system("sudo zypper " + arg + " " + package)

def pip_install(packages, arg='install'):
    os.system("sudo pip " + arg + " " + packages)

def aurman_install(packages, arg='-S'):
    os.system("aurman " + arg + " --needed " + packages)
