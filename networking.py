#! /usr/bin/env python3

import socket
try:
    import requests
except Exception:
    pass


def download_url(url, file_path):
    '''
    Downloads a url to a filepath using requests module.
    '''
    r = requests.get(url, allow_redirects=True)
    open(file_path, 'wb').write(r.content)


def url_content_type(url):
    try:
        res = requests.head(url, timeout=(5, 5))
        status = res.status_code

        try:
            typ = res.headers['Content-Type']
        except Exception:
            typ = 'Unknown'

        try:
            length = res.headers['Content-Length']
        except Exception:
            length = 'Unknown'

        try:
            server = res.headers['Server']
        except Exception:
            server = 'Unknown'

        res.close()
        res_obj = (url, status, typ, length, server)
        del res, status, typ, length, server
        return res_obj

    except requests.exceptions.Timeout:
        return (url, 'Timeout', 'Nil', 'Nil', 'Nil')

    except requests.exceptions.RequestException:
        return (url, 'Request Error', 'Nil', 'Nil', 'Nil')

    except Exception:
        return (url, 'Unknown Error', 'Nil', 'Nil', 'Nil')


def local_ip():
    '''
    Returns the local IP of the system.
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
