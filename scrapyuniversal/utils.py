import os
import json
from os.path import realpath, dirname


def get_config(name):
    path = os.path.join(dirname(realpath(__file__)), 'configs', name+'.json')
    with open(path, 'r', encoding='utf-8') as fo:
        return json.loads(fo.read())
