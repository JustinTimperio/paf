#! /usr/bin/python
#### A pure python implementation of parallel gzip compression using multiprocessing

import os, gzip, tarfile, shutil, argparse, tqdm
import multiprocessing as mp

#######################
### Base Functions 
###################
def search_fs(path):
    file_list = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn] 
    return file_list

def gzip_compress_file(path):
    with open(path, 'rb') as f:
        with gzip.open(path + '.gz', 'wb') as gz:
            shutil.copyfileobj(f, gz)
    os.remove(path)

def gzip_decompress_file(path):
    with gzip.open(path, 'rb') as gz:
        with open(path[:-3], 'wb') as f:
            shutil.copyfileobj(gz, f)
    os.remove(path)

def tar_dir(path):
    with tarfile.open(path + '.tar', 'w') as tar:
        for f in search_fs(path):
            tar.add(f, f[len(path):])

def untar_dir(path):
    with tarfile.open(path, 'r:') as tar:
        tar.extractall(path[:-4])

#######################
### Core gztar Commands
###################
def gztar_c(dir, queue_depth, rmbool):
    files = search_fs(dir)
    with mp.Pool(queue_depth) as pool:
        r = list(tqdm.tqdm(pool.imap(gzip_compress_file, files),
                           total=len(files), desc='Compressing Files'))
    print('Adding Compressed Files to TAR....')
    tar_dir(dir)
    if rmbool == True:
        shutil.rmtree(dir)
    
def gztar_d(tar, queue_depth, rmbool):
    print('Extracting Files From TAR....')
    untar_dir(tar)
    if rmbool == True:
        os.remove(tar)
    files = search_fs(tar[:-4])
    with mp.Pool(queue_depth) as pool:
        r = list(tqdm.tqdm(pool.imap(gzip_decompress_file, files),
                           total=len(files), desc='Decompressing Files'))

#######################
### Parse Args
###################
p = argparse.ArgumentParser(description='A pure python implementation of parallel gzip compression archives.')
p.add_argument('-c', '--compress', metavar='/DIR/TO/COMPRESS', nargs=1, help='Recursively gzip files in a dir then place in tar.')
p.add_argument('-d', '--decompress', metavar='/TAR/TO/DECOMPRESS.tar', nargs=1, help='Untar archive then recursively decompress gzip\'ed files')
p.add_argument('-t', '--throttle', action='store_true', help='Throttle compression to only 75%% of the available cores.')
p.add_argument('-r', '--remove', action='store_true', help='Remove TAR/Folder after process.')
arg = p.parse_args()
### Flags
if arg.throttle == True:
    qd = round(mp.cpu_count()*.75)
else:
    qd = mp.cpu_count()
### Main Args
if arg.compress:
    gztar_c(str(arg.compress)[2:-2], qd, arg.remove)
if arg.decompress:
    gztar_d(str(arg.decompress)[2:-2], qd, arg.remove)
