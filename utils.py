import datetime
import json
import logging


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
    try:
        if len(paths)==1:
            if paths[0]=='':
                return jjson
            elif jjson.has_key(paths[0]):

                return jjson[paths[0]]
            else:
                logging.warn( 'Jjson',json.dumps(jjson))
                logging.warn( 'No this Key:', paths[0])
                return None
        elif len(paths)>1:
            return getFile(jjson[paths[0]], paths[1:])
    except AttributeError ,e:
        logging.error(e.message)
        return None


