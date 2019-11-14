#! /usr/bin/python
#### Archive Commands - v1.0
import os, gzip, tarfile, shutil

#######################
### Gzip and Tar Functions 
###################
def gz_c(path, rm=False):
    with open(path, 'rb') as f:
        with gzip.open(path + '.gz', 'wb') as gz:
            shutil.copyfileobj(f, gz)
    if rm == True:
        os.remove(path)
    if rm == False:
        return

def gz_d(path, rm=False):
    with gzip.open(path, 'rb') as gz:
        with open(path[:-3], 'wb') as f:
            shutil.copyfileobj(gz, f)
    if rm == True:
        os.remove(path)
    if rm == False:
        return

def tar_dir(path, rm=False):
    with tarfile.open(path + '.tar', 'w') as tar:
        for f in search_fs(path):
            tar.add(f, f[len(path):])
    if rm == True:
        shutil.rmtree(path)
    if rm == False:
        return

def untar_dir(path, rm=False):
    with tarfile.open(path, 'r:') as tar:
        tar.extractall(path[:-4])
    if rm == True:
        os.remove(path)
    if rm == False:
        return

#######################
### Core gztar Commands
###################
def gztar_c(dir, queue_depth=round(os.cpu_count()*.75), rmbool=True):
    import multiprocessing, tqdm 
    files = search_fs(dir)
    with multiprocessing.Pool(queue_depth) as pool:
        r = list(tqdm.tqdm(pool.imap(gzip_compress_file, files),
                           total=len(files), desc='Compressing Files'))
    print('Adding Compressed Files to TAR....')
    tar_dir(dir)
    if rmbool == True:
        shutil.rmtree(dir)
    
def gztar_d(tar, queue_depth=round(os.cpu_count()*.75), rmbool=True):
    import multiprocessing, tqdm 
    print('Extracting Files From TAR....')
    untar_dir(tar)
    if rmbool == True:
        os.remove(tar)
    files = search_fs(tar[:-4])
    with multiprocessing.Pool(queue_depth) as pool:
        r = list(tqdm.tqdm(pool.imap(gzip_decompress_file, files),
                           total=len(files), desc='Decompressing Files'))

