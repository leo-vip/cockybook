#coding: UTF-8

from xml.dom.minidom import Document
from flask import Flask,url_for,send_file
import Const
from OpdsCore import FeedDoc, Link, OpdsProtocol, Entry, getNow
from Protocols import LocalOpdsProtocol
import Config


__author__ = 'lei'

app = Flask(__name__)


@app.route("/")
def helo():
    f = FeedDoc(Document())

    entry = Entry()
    entry.id=Config.SITE_BOOK_LIST
    entry.content="all Books List By Type"
    entry.title="Book List"

    entry.updated=getNow()
    #TODO add Another Links
    entry.links=[Link(entry.id,Const.book_link_rel_subsection,"Book List",Const.book_type_entry_catalog)]
    f.createEntry(entry)
    return f.toString()

    #f.createEntry("halo,OPds", "2014-12-11T07:10:23Z", "1234567890", "This is halo Opds Describe...",
     #             {Link("http://www.baidu.com", "xxx", "aaa",
     #                   "application/atom+xml;profile=opds-catalog;kind=acquisition"),
     #              Link("http://163.com", "mm", "mm", "application/atom+xml;profile=opds-catalog;kind=acquisition")})

    return f.toString() + "\n"

@app.route('/list')
def listbookroot():
    return listbooks('/')


@app.route('/list/<path:path>')
def listbooks(path):
    feed = FeedDoc(Document())
    #TODO add *** to feed.toString()
    l=getOpdsProtocol().listBooks(path)

    for entry in l:
        feed.createEntry(entry)

    #print(feed.toString().encode("utf-8"))
    return feed.toString()

@app.route('/download/<path:path>')
def download(path):
    """
    download book

    """
    filePath=getOpdsProtocol().dowloadBook(path)

    return send_file(filePath)


@app.route('/show/<path:path>')
def showhtml(path):
    return "show file:" + path


def getOpdsProtocol():
    return LocalOpdsProtocol()


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

