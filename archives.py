#! /usr/bin/env python3
import os
import gzip
import shutil
import tarfile
import multiprocessing
from .file import search_dir


############
# Core Archive Functions
######

def gz_c(path, rm=False):
    with open(path, 'rb') as f:
        with gzip.open(path + '.gz', 'wb') as gz:
            shutil.copyfileobj(f, gz)
    if rm is True:
        os.remove(path)
    elif rm is False:
        pass


def gz_d(path, rm=False):
    with gzip.open(path, 'rb') as gz:
        with open(path[:-3], 'wb') as f:
            shutil.copyfileobj(gz, f)
    if rm is True:
        os.remove(path)
    elif rm is False:
        pass


def tar_dir(path, rm=False):
    with tarfile.open(path + '.tar', 'w') as tar:
        for f in search_dir(path):
            tar.add(f, f[len(path):])
    if rm is True:
        shutil.rmtree(path)
    elif rm is False:
        pass


def untar_dir(path, rm=False):
    with tarfile.open(path, 'r:') as tar:
        tar.extractall(path[:-4])
    if rm is True:
        os.remove(path)
    elif rm is False:
        pass


############
# Muti-Threaded Functions
######

def gztar_c(dir_path, queue_depth=round(os.cpu_count()*.75), rmbool=True):
    '''
    Compress files individually in a dir using mp.pool, then tar files.
    This compresses files BEFORE adding them to the tar.
    '''
    import tqdm

    files = search_dir(dir_path)
    with multiprocessing.Pool(queue_depth) as pool:
        list(tqdm.tqdm(pool.imap(gz_c, files), total=len(files), desc='Compressing Files'))

    print('Adding Compressed Files to TAR....')
    tar_dir(dir_path)

    if rmbool is True:
        shutil.rmtree(dir_path)


def gztar_d(tar_path, queue_depth=round(os.cpu_count()*.75), rmbool=True):
    '''
    Unpack a tar then individually decompress each file using mp.pool().
    This should be used in combo with GZTar_C().
    '''
    import tqdm

    print('Extracting Files From TAR....')
    untar_dir(tar_path)
    if rmbool is True:
        os.remove(tar_path)

    files = search_dir(tar_path[:-4])
    with multiprocessing.Pool(queue_depth) as pool:
        list(tqdm.tqdm(pool.imap(gz_d, files), total=len(files), desc='Decompressing Files'))
