#! /usr/bin/env python3
import os
import gzip
import tarfile
import shutil
import hashlib
import multiprocessing
from .ps_linux import Search_FS


def GZ_C(path, rm=False):
    with open(path, 'rb') as f:
        with gzip.open(path + '.gz', 'wb') as gz:
            shutil.copyfileobj(f, gz)
    if rm is True:
        os.remove(path)
    elif rm is False:
        pass


def GZ_D(path, rm=False):
    with gzip.open(path, 'rb') as gz:
        with open(path[:-3], 'wb') as f:
            shutil.copyfileobj(gz, f)
    if rm is True:
        os.remove(path)
    elif rm is False:
        pass


def Tar_Dir(path, rm=False):
    with tarfile.open(path + '.tar', 'w') as tar:
        for f in Search_FS(path):
            tar.add(f, f[len(path):])
    if rm is True:
        shutil.rmtree(path)
    elif rm is False:
        pass


def Untar_Dir(path, rm=False):
    with tarfile.open(path, 'r:') as tar:
        tar.extractall(path[:-4])
    if rm is True:
        os.remove(path)
    elif rm is False:
        pass


def Checksum_File(file_path):
    '''
    Checksums a file using hashlib.md5(). Reads the file in 250MB chunks.
    Checksum is slow as fuck on anything larger than 5GB so they are ignored.
    Hopefully I'll fix this later by using raw linux commands
    '''
    if not os.path.exists(file_path):
        return (file_path, 'FILE MISSING!')
    else:
        size = os.path.getsize(file_path)

    if size == 0:
        return (file_path, '0')

    elif size > 5368709120:
        return (file_path, 'TOO LARGE!')

    else:
        with open(file_path, 'rb') as fh:
            m = hashlib.md5()
            while True:
                data = fh.read(268435456)
                if not data:
                    break
                m.update(data)
            return (file_path, str(m.hexdigest()))


def GZTar_C(dir_path, queue_depth=round(os.cpu_count()*.75), rmbool=True):
    '''
    Compress files individually in a dir using mp.pool, then tar files.
    This compresses files BEFORE adding them to the tar.
    '''
    import tqdm

    files = Search_FS(dir_path)
    with multiprocessing.Pool(queue_depth) as pool:
        list(tqdm.tqdm(pool.imap(GZ_C, files), total=len(files), desc='Compressing Files'))

    print('Adding Compressed Files to TAR....')
    Tar_Dir(dir_path)

    if rmbool is True:
        shutil.rmtree(dir_path)


def GZTar_D(tar_path, queue_depth=round(os.cpu_count()*.75), rmbool=True):
    '''
    Unpack a tar then individually decompress each file using mp.pool().
    This should be used in combo with GZTar_C().
    '''
    import tqdm

    print('Extracting Files From TAR....')
    Untar_Dir(tar_path)
    if rmbool is True:
        os.remove(tar_path)

    files = Search_FS(tar_path[:-4])
    with multiprocessing.Pool(queue_depth) as pool:
        list(tqdm.tqdm(pool.imap(GZ_D, files), total=len(files), desc='Decompressing Files'))
