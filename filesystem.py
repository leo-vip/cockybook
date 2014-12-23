# coding: UTF-8


import os
import requests
import Config
import json

from utils import connect_path, getFile

__author__ = 'lei'

# base="/home/cocky"
class FileSystem:
    def outErr(self):
        print("No Realyzed")

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
    def outErr(self):
        print("No Realyzed")

    def exists(self, path):
        return os.path.exists(connect_path(Config.base, path))

    def isfile(self, path):
        return os.path.isfile(connect_path(Config.base, path))

    def listdir(self, path):
        return os.listdir(connect_path(Config.base, path))

    def getdownloadurl(self, path, name):
        return connect_path(connect_path(Config.SITE_BOOK_DONWLOAD, path), name)


class QiniuFileSystem(FileSystem):
    #q = Auth(Config.access_key, Config.secret_key)

    #bucket = BucketManager(q)
    def __init__(self):
        ff=requests.get(connect_path(Config.SITE_BOOK_DONWLOAD,'metadata.xml'))
        if ff.status_code ==200:
            self.book_trees = json.loads(ff.text)

    def outErr(self):
        print("No Realyzed")

    def exists(self, path):
        return True

    def isfile(self, path):
        if path.find('_-_') == -1:
            return False
        else:
            return True

    def listdir(self, path):
        # if path == '' or path == '/':
        #     return Config.QiNiu_Book_types
        #
        # ret, eof, info = self.bucket.list(Config.bucket_name, prefix=path)
        # #items_str=unicode(info.text_body)
        # jjon = json.loads(info.text_body, encoding='utf8')
        # return [en['key'][en['key'].find('/') + 1:] for en in jjon['items']]

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
        #print(tmp)

        files=getFile(self.book_trees,self.getTruePaths(tmp))

        return [connect_path(Config.SITE_BOOK_DONWLOAD,connect_path(path, ee)) for ee in files]
        #return connect_path(connect_path(Config.SITE_BOOK_DONWLOAD, path), name)

if __name__ =='__main__':
    # ff=requests.get(connect_path(Config.SITE_BOOK_DONWLOAD,'metadata.xml'))
    # if ff.status_code ==200:
    #     trees = json.loads(ff.text)
    filesys=QiniuFileSystem()
    # for ii in connect_path(u"/科技",u"黑客与画家_-_保罗·格雷厄姆").split('/'):
    #     print(ii)
    ll = filesys.listdir("Noval");

    for l in ll:
        print(l)

    print 'Over...'