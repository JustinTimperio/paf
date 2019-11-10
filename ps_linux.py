#! /usr/bin/python
#### Linux Commands - 1.0

######
### File System Commands and Short-Cuts
######
def open_permissions(path):
    os.system("sudo chmod -R 777 " + path)

def search_fs(path):
    list_name = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn] 
    return list_name

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
### Linux System Commands
######
def bash_cpu_core_count():
    core_count = subprocess.check_output("cat /proc/cpuinfo | awk '/^processor/{print $3}' | wc -l", shell=True)
    return str(core_count)[2:-3]

def os_distro():
    os_name = subprocess.check_output('cat /etc/os-release | grep PRETTY_NAME= | cut -c 13-', shell=True)
    return str(os_name)[2:-3]

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

def pip_install(packages):
    os.system("sudo pip install " + packages)

def aurman_install(packages):
    os.system("aurman -S --needed " + packages)
