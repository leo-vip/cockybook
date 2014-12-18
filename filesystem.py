# coding: UTF-8


import os
import Config
import json
from qiniu import Auth, BucketManager
import utils

__author__ = 'lei'

#base="/home/cocky"
class FileSystem:
    def outErr(self):
        print("No Realyzed")

    def exists(self,path):
        self.outErr()
        pass
    def isfile(self,path):
        self.outErr()
        pass
    def listdir(self,path):
        self.outErr()
        return []
        pass
    def getdownloadurl(self,path,name):
        self.outErr()
        return ""

class LocalFileSystem(FileSystem):
    def outErr(self):
        print("No Realyzed")

    def exists(self,path):
        return os.path.exists(utils.connect_path(Config.base,path))

    def isfile(self,path):
        return os.path.isfile(utils.connect_path(Config.base,path))

    def listdir(self,path):
        return os.listdir(utils.connect_path(Config.base,path))

    def getdownloadurl(self,path,name):

        return utils.connect_path(utils.connect_path(Config.SITE_BOOK_DONWLOAD, path), name)

class QiniuFileSystem(FileSystem):
    q = Auth(Config.access_key,Config.secret_key)

    bucket = BucketManager(q)

    def outErr(self):
        print("No Realyzed")

    def exists(self,path):
        return True

    def isfile(self,path):
        if path.find('.')==-1:
            return False
        else:
            return True


    def listdir(self,path):
        if path=='' or path=='/':
            return Config.QiNiu_Book_types

        ret, eof, info =self.bucket.list(Config.bucket_name,prefix=path)
        #items_str=unicode(info.text_body)
        jjon=json.loads(info.text_body,encoding='utf8')
        return [en['key'][en['key'].find('/')+1:] for en in jjon['items']]


    def getdownloadurl(self,path,name):
        return utils.connect_path(utils.connect_path(Config.SITE_BOOK_DONWLOAD, path), name)

