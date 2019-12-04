#! /usr/bin/env python3
#### Linux Commands - v1.02
from .ps_modules import *

######
### File System Commands and Short-Cuts
######
def open_permissions(path):
    os.system("sudo chmod -R 777 " + path)

def search_fs(path, typ='list'):
    if typ.lower() in ['list', 'l']:
        return [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn]
    elif typ.lower() in ['set', 's']:
        return {os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn}
    else:
        sys.exit('Error: Type Must be List/Set!')

def rm_file(file_path, sudo):
    if sudo == True:
        if os.path.exists(file_path):
            os.system('sudo rm ' + file_path)
    elif sudo == False:
        if os.path.exists(file_path):
            os.system('rm ' + file_path)
    else:
        sys.exit('Error: Type Must be List/Set!')

def mkdir(dir, sudo):
    if sudo == True:
        if not os.path.exists(dir):
            os.system("sudo mkdir " + dir)
    elif sudo == False:
        if not os.path.exists(dir):
            os.system("mkdir " + dir)
    else:
        sys.exit('Error: Type Must be List/Set!')

def rm_dir(dir_path, sudo):
    if sudo == True:
        if os.path.exists(dir_path):
            os.system('sudo rm -r ' + dir_path)
    elif sudo == False:
        if not os.path.exists(dir):
            os.system('rm -r ' + dir_path)
    else:
        sys.exit('Error: Type Must be List/Set!')

def export_list(file_name, iterable):
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        for i in iterable:
            f.write("%s\n" % i) 

def read_list(file_name, typ='list'):
    if typ == 'list':
        l = list(open(file_name).read().splitlines()) 
    elif typ == 'set':
        l = set(open(file_name).read().splitlines()) 
    else: 
        sys.exit('Error: Type Must be List/Set!')
    return l

######
### Terminal Commands
######
def escape_bash(astr):
    return re.sub("(!| |\$|#|&|\"|\'|\(|\)|\||<|>|`|\\\|;)", r"\\\1", astr)

def os_distro():
    os_name = subprocess.check_output('cat /etc/os-release | grep PRETTY_NAME= | cut -c 13-', shell=True)
    return str(os_name)[2:-3]

def sed_replace(pattern, file_path):
    os.system("sed -e'" + pattern + "' -i " + file_path)

def uncomment_line_sed(pattern, file_path, sudo):
    if sudo == True:
        os.system("sudo sed -e'/" + pattern + "/s/^#//g' -i " + file_path)
    elif sudo == False:
        os.system("sed -e'/" + pattern + "/s/^#//g' -i " + file_path)

def comment_line_sed(pattern, file_path, sudo):
    if sudo == True:
        os.system("sudo sed -e'/" + pattern + "/s/^#*/#/g' -i " + file_path)
    elif sudo == False:
        os.system("sed -e'/" + pattern + "/s/^#*/#/g' -i " + file_path)

######
### Linux System Package Commands
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
    os.system("pacaur " + arg +  packages)


######
### Arch Linux Commands
######
def pacman_Q(replace_spaces=False):
    os.system("pacman -Q > /tmp/pacman_q.meta")
    l = read_list('/tmp/pacman_q.meta', typ='set')
    rm_file('/tmp/pacman_q.meta', sudo=True)
    if replace_spaces == True:
        rl = {s.strip().replace(' ', '-') for s in l}
        return rl
    else:
        return l 

def find_paccache():
    cache_list = search_fs('~/.cache', 'set')
    fs_list = set(search_fs('/var/cache/pacman', 'set') | {f for f in cache_list if f.endswith(".pkg.tar.xz")})
    return fs_list

def find_pacman_pkgs(pkg_list, fs_list):
    bulk_search = ('|'.join(list(re.escape(pkg) for pkg in pkg_list))) ### Packages like g++ need to be escaped
    found_pkgs = set()
    for f in fs_list:
        if re.findall(bulk_search, f.lower()):
            found_pkgs.add(f)
    return found_pkgs

