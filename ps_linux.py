#! /usr/bin/python
#### Linux Commands - v1.01
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
    if sudo == 'r':
        if os.path.exists(file_path):
            os.system('sudo rm ' + file_path)
    if sudo == 'u':
        if os.path.exists(file_path):
            os.system('rm ' + file_path)

def mkdir(dir, sudo):
    if sudo == 'r':
        if not os.path.exists(dir):
            os.system("sudo mkdir " + dir)
    if sudo == 'u':
        if not os.path.exists(dir):
            os.system("mkdir " + dir)

def rm_dir(dir_path, sudo):
    if sudo == 'r':
        if os.path.exists(dir_path):
            os.system('sudo rm -r ' + dir_path)
    if sudo == 'u':
        if not os.path.exists(dir):
            os.system('rm -r ' + dir_path)

######
### Terminal Commands
######
def os_distro():
    os_name = subprocess.check_output('cat /etc/os-release | grep PRETTY_NAME= | cut -c 13-', shell=True)
    return str(os_name)[2:-3]

def sed_replace(pattern, file_path):
    os.system("sed -e'" + pattern + "' -i " + file_path)

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