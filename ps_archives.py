#! /usr/bin/python
#### Archive Commands - v1.0

import os, gzip, tarfile, shutil, argparse, tqdm
import multiprocessing as mp
import ps_linux

#######################
### Gzip and Tar Functions 
###################
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
def gztar_c(dir, queue_depth=round(mp.cpu_count()*.75), rmbool=True):
    files = search_fs(dir)
    with mp.Pool(queue_depth) as pool:
        r = list(tqdm.tqdm(pool.imap(gzip_compress_file, files),
                           total=len(files), desc='Compressing Files'))
    print('Adding Compressed Files to TAR....')
    tar_dir(dir)
    if rmbool == True:
        shutil.rmtree(dir)
    
def gztar_d(tar, queue_depth=round(mp.cpu_count()*.75), rmbool=True):
    print('Extracting Files From TAR....')
    untar_dir(tar)
    if rmbool == True:
        os.remove(tar)
    files = search_fs(tar[:-4])
    with mp.Pool(queue_depth) as pool:
        r = list(tqdm.tqdm(pool.imap(gzip_decompress_file, files),
                           total=len(files), desc='Decompressing Files'))

