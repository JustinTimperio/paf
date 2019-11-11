#! /usr/bin/python
# This script builds bash commands that compress files in parallel
import os, argparse

def compress(dir):
    os.system('find ' + dir + ' -type f | parallel gzip -q && tar -cf '
              + os.path.basename(dir) + '.tar -C ' + dir + ' .')

def decompress(tar):
    d = os.path.splitext(tar)[0]
    os.system('mkdir ' + d + ' && tar -xf ' + tar + ' -C ' + d +
          ' && find ' + d + ' -name *.gz -type f | parallel gzip -qd') 

p = argparse.ArgumentParser()
p.add_argument('-c', '--compress', metavar='/DIR/TO/COMPRESS', nargs=1)
p.add_argument('-d', '--decompress', metavar='/TAR/TO/DECOMPRESS.tar', nargs=1)
args = p.parse_args()

if args.compress:
    compress(str(args.compress)[2:-2])
if args.decompress:
    decompress(str(args.decompress)[2:-2])
