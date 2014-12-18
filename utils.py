import datetime

__author__ = 'lei'



##connect path
def connect_path(base,name):
    if name.startswith('/'):
        name=name[1:]

    if base.endswith('/'):
        return base+name
    else:
        return base + '/' +name


def getNow():
    return datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%SZ")