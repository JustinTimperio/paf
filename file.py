#! /usr/bin/env python3
import os
import sys
import hashlib
import multiprocessing


############
# File System Commands
######


def search_dir(path, typ='set'):
    '''
    Scans a path recursivly and returns a list of files.
    Uses os.path.join() and os.walk().
    '''
    if typ.lower() in ['list', 'l']:
        return [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn]
    elif typ.lower() in ['set', 's']:
        return {os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(path)) for f in fn}
    else:
        sys.exit('Error: Type Must be List/Set!')


def search_dirs(paths):
    '''
    '''
    files = set()
    for p in paths:
        files.update(search_dir(p, typ='set'))
    return files


def size_of_files(file_list):
    '''
    Returns byte sum of files in a list.
    '''
    size = 0
    for f in file_list:
        try:
            size += os.path.getsize(f)
        except Exception:
            OSError
    return size


############
# File Commands
######


def export_iterable(file_name, iterable):
    '''
    Export iterable to a file with each entry on a new line.
    '''
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'w') as f:
        for i in iterable:
            f.write("%s\n" % i)


def read_file(file_name, typ='list'):
    '''
    Reads file into set or list.
    '''
    if typ == 'list':
        fl = list(open(file_name).read().splitlines())
    elif typ == 'set':
        fl = set(open(file_name).read().splitlines())
    else:
        sys.exit('Error: Type Must be List/Set!')
    return fl


############
# Checksum Functions
######


def checksum_file(file_path):
    '''
    Checksums a file using hashlib.md5(). Reads the file in 250MB chunks.
    Checksum is slow as fuck on anything larger than 5GB so they are ignored.
    Returns a tuple with [0] == path and [1] == checksum.
    '''
    if not os.path.exists(file_path):
        return (file_path, 'MISSING!')
    else:
        try:
            size = os.path.getsize(file_path)
        except Exception:
            return (file_path, 'UNREADABLE!')

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


def checksum_file_list(paths, queue_depth=os.cpu_count(), output='Checksumming Files'):
    '''
    Checksum all files in paths using mp.pool then return results.
    Returns a set of tuples with paths and checksums.
    '''
    import tqdm

    with multiprocessing.Pool(queue_depth) as pool:
        sums = set(tqdm.tqdm(pool.imap(checksum_file, paths),
                             total=len(paths), desc=output))

    return sums
