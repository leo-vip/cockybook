# coding: UTF-8
import datetime
import Config
import Const
from OpdsCore import OpdsProtocol, Entry, Link
import os, sys

__author__ = 'lei'

base = "f:\\opds"



def getCreateDate(file_path):
    #return datetime.datetime.now(os.path.getctime(file_path)).strftime("%Y-%m-%dT%I:%M:%SZ")
    return datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%SZ")


def create_entry(file_path, path, name):
    entry = Entry()
    entry.id = os.path.join(Config.SITE_BOOK_DONWLOAD+"/"+path, name)
    entry.content = name
    entry.title = name

    entry.updated = getCreateDate(file_path)
    #TODO add Another Links
    entry.links = [Link(entry.id, Const.book_link_rel_subsection, name, _get_book_entry_type(name))]
    return entry


def _get_book_entry_type(name):
    """
    get link type
    """
    if name.endswith(".pdf"):
        return Const.book_type_pdf
    elif name.endswith(".epub"):
        return Const.book_type_epub
    elif name.endswith(".jpg"):
        return Const.book_type_picture
    elif name.endswith(".mobi"):
        return Const.book_type_mobi
    else:
        # No subifx
        return Const.book_type_entry_catalog


class LocalOpdsProtocol(OpdsProtocol):
    """
    All Opds File System Must Realized this Class
    """

    def listBooks(self, path):
        """
        :return: {entiry ...}
        """
        l = []

        if (path != "/"):
            distPath = os.path.join(base, path)
        else:
            distPath = base
            #not exist!
        if (not os.path.exists(distPath)):
            print("dest Path [%s] is Not Exist." % distPath)
            return l

        if (os.path.isfile(distPath)):
            print("dest Path is a File Not Right." % distPath)
            return l

        for name in os.listdir(distPath):
            name = name.decode("gbk")
            file_path = os.path.join(distPath, name)
            if (os.path.isfile(file_path)):
                print("file: " + file_path)
                l.append(create_entry(file_path, path, name))
            else:
                print("Dir: " + file_path)
                l.append(create_entry(file_path, path, name))

        return l

    def dowloadBook(self, path):
        """
        file
        :param path:
        :return: file
        """

        file=open(os.path.join(base, path))


        return file
        pass

    def showhtml(self):
        return ("No Realized")
        pass


if __name__ == "__main__":
    # l = LocalOpdsProtocol()
    # l.listBooks("/")
    # getCreateDate("f:\\opds")
    # print("我擦。。。。")

    for f in os.listdir(base):
        print(f.decode("GBK"))