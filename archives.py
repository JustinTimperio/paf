#! /usr/bin/env python3
import os
import gzip
import shutil
import tarfile
from .file import find_files


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
        for f in find_files(path):
            tar.add(f, f[len(path):])
    if rm is True:
        shutil.rmtree(path)
    elif rm is False:
        pass


def untar_dir(path, rm=False):
    with tarfile.open(path, 'r:') as tar:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, path[:-"4"])
    if rm is True:
        os.remove(path)
    elif rm is False:
        pass
