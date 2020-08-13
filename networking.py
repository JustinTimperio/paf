#! /usr/bin/env python3
# Network Commands - v1.0
import socket
import requests


def DL_URL(url, file_path):
    '''Downloads a url to a filepath using requests module.'''
    r = requests.get(url, allow_redirects=True)
    open(file_path, 'wb').write(r.content)


def Is_URL_Downloadable(url):
    '''Check if a url is downloadable by requests. Returns True if yes, False if no.'''
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def Local_IP():
    '''Returns the local IP of the system.'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
