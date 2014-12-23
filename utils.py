import datetime
import json

__author__ = 'lei'

# #connect path
def connect_path(base, name):
    if name.startswith('/'):
        name = name[1:]

    if base.endswith('/'):
        return base + name
    else:
        return base + '/' + name


def getNow():
    return datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%SZ")


def getFile(jjson,paths):
    '''
    get json object
    :param jjson:   json object
    :param paths:   json path
    :return:        json object
    '''
    if len(paths)==1:
        if paths[0]=='':
            return jjson
        elif jjson.has_key(paths[0]):

            return jjson[paths[0]]
        else:
            print 'Jjson',json.dumps(jjson)
            print 'No this Key:', paths[0]
            return None
    elif len(paths)>1:
        #print(paths)
        return getFile(jjson[paths[0]], paths[1:])
