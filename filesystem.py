# coding: UTF-8
import logging

import os
import requests
import Config
import json

from utils import connect_path, getFile

__author__ = 'lei'

# base="/home/cocky"
class FileSystem:
    def outErr(self):
        logging.error("No Realyzed")

    def exists(self, path):
        self.outErr()
        pass

    def isfile(self, path):
        self.outErr()
        pass

    def listdir(self, path):
        self.outErr()
        return []
        pass

    def getdownloadurl(self, path, name):
        self.outErr()
        return ""


class LocalFileSystem(FileSystem):
    """
    config the #Config.base
    """
    def exists(self, path):
        return os.path.exists(connect_path(Config.base, path))

    def isfile(self, path):
        return os.path.isfile(connect_path(Config.base, path))

    def listdir(self, path):
        return os.listdir(connect_path(Config.base, path))

    def getdownloadurl(self, path, name):
        return connect_path(connect_path(Config.SITE_BOOK_DONWLOAD, path), name)

class LocalMetadataFileSystem(FileSystem):
    #q = Auth(Config.access_key, Config.secret_key)

    #bucket = BucketManager(q)
    def __init__(self):
        ff=open('metadata.json','r')

        self.book_trees = json.load(ff)

    def exists(self, path):
        files=getFile(self.book_trees,self.getTruePaths(path))
        return len(files)!=0

    def isfile(self, path):
        if path.find('_-_') == -1:
            return False
        else:
            return True

    def listdir(self, path):
        paths=self.getTruePaths(path)

        if len(paths)!=0:
            return getFile(self.book_trees, paths)
        else:
            return self.book_trees

    def getTruePaths(self,tmp):
        """
        :param tmp:
        :return:
        """
        paths=tmp.split('/')
        paths=[p for p in paths if p!='']
        return paths

    def getdownloadurl(self, path, name):
        tmp = connect_path(path,name)

        files=getFile(self.book_trees,self.getTruePaths(tmp))

        return [connect_path(Config.SITE_BOOK_DONWLOAD,connect_path(path, ee)) for ee in files]

class QiniuFileSystem(FileSystem):
    #q = Auth(Config.access_key, Config.secret_key)

    #bucket = BucketManager(q)
    def __init__(self):
        ff=requests.get(connect_path(Config.SITE_BOOK_DONWLOAD,'metadata.json'))
        if ff.status_code ==200:
            self.book_trees = json.loads(ff.text)

    def outErr(self):
        logging.error("No Realyzed")

    def exists(self, path):
        files=getFile(self.book_trees,self.getTruePaths(path))
        #logging.info(len(files)!=0)
        return len(files)!=0

    def isfile(self, path):
        if path.find('_-_') == -1:
            return False
        else:
            return True

    def listdir(self, path):
        paths=self.getTruePaths(path)

        if len(paths)!=0:
            return getFile(self.book_trees, paths)
        else:
            return self.book_trees

    def getTruePaths(self,tmp):
        """
        :param tmp:
        :return:
        """
        paths=tmp.split('/')
        paths=[p for p in paths if p!='']
        return paths

    def getdownloadurl(self, path, name):
        tmp = connect_path(path,name)

        files=getFile(self.book_trees,self.getTruePaths(tmp))

        return [connect_path(Config.SITE_BOOK_DONWLOAD,connect_path(path, ee)) for ee in files]

if __name__ =='__main__':
    pass