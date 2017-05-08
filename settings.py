import os
DEBUG = True
root = os.path.dirname(__file__)
DATA = os.path.join(root, 'data')
LOG = os.path.join(root, 'log')
THREAD = 10

SSH = {
    'host': 'localhost',
    'port': 22,
    'username': 'user',
    'timeout': 30,
    'banner_timeout':30,
    'pkey_path': 'path/to/id_rsa/'
}

REMOTE_DIR = '/directory/to/file'
LOCAL_DIR = '/direcotry/to/store/file/locally'
LOCAL_TEMP = '/direcotry/to/store/file/temporarily'