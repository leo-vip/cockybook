# coding: UTF-8


import os
import Config

import OpdsCore

__author__ = 'lei'


#base="/home/cocky"


class LocalFileSystem(FileSystem):
    def outErr(self):
        print("No Realyzed")

    def exists(self,path):
        return os.path.exists(path)

    def isfile(self,path):
        return os.path.isfile(path)

    def listdir(self,path):
        return os.listdir(path)

    def getdownloadurl(self,path,name):

        return OpdsCore.connect_path(OpdsCore.connect_path(Config.SITE_BOOK_DONWLOAD, path), name)

if __name__ == "__main__":
    # l = LocalOpdsProtocol()
    # l.listBooks("/")
    # getCreateDate("f:\\opds")
    # print("我擦。。。。")

    # for f in os.listdir(base):
    #     print(f.decode("gbk"))

        m={}
        m['sss']=["a","b"]
        m['aas']=["xx"]

        for ii in m.items():
            print m[ii]