#coding: UTF-8
from xml.dom.minidom import Document, Text, Element
import datetime
import Config
import Const
from Config import fs
from filesystem import FileSystem, LocalFileSystem

__author__ = 'lei'


def setfeedNS(feed):
    feed.setAttribute("xmlns:app", "http://www.w3.org/2007/app")
    feed.setAttribute("xmlns:opds", "http://opds-spec.org/2010/catalog")
    feed.setAttribute("xmlns:opds", Config.SITE_URL)
    feed.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    feed.setAttribute("xmlns", "http://www.w3.org/2005/Atom")
    feed.setAttribute("xmlns:dcterms", "http://purl.org/dc/terms/")
    feed.setAttribute("xmlns:thr", "http://purl.org/syndication/thread/1.0")
    feed.setAttribute("xmlns:opensearch", "http://a9.com/-/spec/opensearch/1.1/")


def getNow():
    return datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%SZ")
##connect path
def connect_path(base,name):
    if name.startswith('/'):
        name=name[1:]

    if base.endswith('/'):
        return base+name
    else:
        return base + '/' +name


def getCreateDate(file_path):
    #return datetime.datetime.now(os.path.getctime(file_path)).strftime("%Y-%m-%dT%I:%M:%SZ")
    return datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%SZ")


def create_entry(file_path, isFile, path, name):
    entry = Entry()
    if isFile :
        entry.id = fs.getdownloadurl(path,name)
        #
    else:
        entry.id = connect_path(connect_path(Config.SITE_BOOK_LIST, path), name)
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
    elif name.endswith(".txt"):
        return Const.book_type_text
    elif name.find('.')!=-1:
        return Const.book_type_content
    else:
        # No subifx
        return Const.book_type_entry_catalog


class FeedDoc:
    def __init__(self, doc):
        """
        Root Element
        :param doc:  Document()
        :return:
        """
        self.doc = doc
        self.feed = self.doc.createElement("feed")
        setfeedNS(self.feed)
        self.addNode(self.feed, Const.id, Config.SITE_URL)
        self.addNode(self.feed, Const.author, Config.SITE_EMAIL)
        self.addNode(self.feed, Const.title, Config.SITE_TITLE)
        self.addNode(self.feed, Const.updated, getNow())
        self.createLink(self.feed, Config.SITE_URL, "Home", "Home",
                        "application/atom+xml; profile=opds-catalog; kind=navigation")

        self.doc.appendChild(self.feed)
        pass

    def addNode(self, element, key, value, link=None):
        """
        add A node to element
        :param element:
        :param key:
        :param value:   can be str & Element
        :param link:  if is link ,this field is Not None.
        :return:
        """
        if isinstance(value, Element):
            element.appendChild(value)
        else:
            node = self.doc.createElement(key)
            node.appendChild(self.doc.createTextNode(value))
            element.appendChild(node)

    def toString(self):
        # return self.doc.toxml("utf-8")
        return self.doc.toprettyxml()

    def createEntry(self, entry):
        entryNode = self.doc.createElement(Const.entry)

        self.addNode(entryNode, Const.entry_title, entry.title)
        self.addNode(entryNode, Const.entry_updated, entry.updated)
        self.addNode(entryNode, Const.entry_id, entry.id)
        self.addNode(entryNode, Const.entry_content, entry.content)
        for link in entry.links:
            self.createLink(entryNode, link.href, link.rel, link.title, link.type)
        self.feed.appendChild(entryNode)

    def createLink(self, entry, href, rel, title, type):
        link = self.doc.createElement(Const.link)
        link.setAttribute("href", href)
        link.setAttribute("rel", rel)
        link.setAttribute("title", title)
        link.setAttribute("type", type)
        entry.appendChild(link)
        return link

class Entry:
    def __init__(self, title=None, updated=None, id=None, content=None, links=[]):
        self.links = links
        self.content = content
        self.id = id
        self.updated = updated
        self.title = title



class Link:
    """
    Link Entity
    """

    def __init__(self, href, rel, title, type):
        self.href = href
        self.rel = rel
        self.title = title
        self.type = type


#########################



class OpdsProtocol:
    """
    All Opds File System Must Realized this Class
    """

    def listBooks(self, path):
        """
        :return: {entiry ...}
        """
        rslist = []

        if (path != "/"):
            distPath = connect_path(Config.base, path)
        else:
            distPath = Config.base
            #not exist!
        if (not fs.exists(distPath)):
            print("dest Path [%s] is Not Exist." % distPath)
            return rslist

        if (fs.isfile(distPath)):
            print("dest Path is a File Not Right." % distPath)
            return rslist

        bookmap={}
        for name in fs.listdir(distPath):
            try:
                name = name.decode("utf-8")
            except Exception:
                try:
                    name=name.decode("gbk")
                except Exception as e:
                    pass

            file_path = connect_path(distPath, name)
            if (fs.isfile(file_path)):
                #print("file: " + file_path)
                rslist.append(create_entry(file_path, True, path, name))
            else:
                #print("Dir: " + file_path)
                rslist.append(create_entry(file_path, False, path, name))
        return rslist


    def dowloadBook(self, path):
        """
        file
        :param path:
        :return: file
        """

        return connect_path(Config.base, path)


    def showhtml(self):
        return ("No Realized")
        pass

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