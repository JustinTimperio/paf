#! /usr/bin/env python3
#### Network Commands - v1.0
import requests, socket

######
### Network and Web Fuctions
######

def dl_url(url, file_name):
    r = requests.get(url, allow_redirects=True)
    open(file_name, 'wb').write(r.content)

def is_url_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def get_local_ip():
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
