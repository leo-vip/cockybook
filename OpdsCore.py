from xml.dom.minidom import Document, Text, Element
import datetime
import Config
import Const

__author__ = 'lei'

def setfeedNS(feed):
    feed.setAttribute("xmlns:app","http://www.w3.org/2007/app")
    feed.setAttribute("xmlns:opds","http://opds-spec.org/2010/catalog")
    feed.setAttribute("xmlns:opds",Config.SITE_URL)
    feed.setAttribute("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
    feed.setAttribute("xmlns","http://www.w3.org/2005/Atom")
    feed.setAttribute("xmlns:dcterms","http://purl.org/dc/terms/")
    feed.setAttribute("xmlns:thr","http://purl.org/syndication/thread/1.0")
    feed.setAttribute("xmlns:opensearch","http://a9.com/-/spec/opensearch/1.1/")

def getNow():
    return datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%SZ")

class Feed:
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
        self.addNode(self.feed, Const.updated,getNow())
        self.createLink(self.feed,"http://opds.cockybook.com/aa","aa","aa","application/atom+xml; profile=opds-catalog; kind=navigation")
        self.createLink(self.feed,"http://opds.cockybook.com/bb","bb","bb","application/atom+xml; profile=opds-catalog; kind=navigation")
        self.createLink(self.feed,"http://opds.cockybook.com/cc","cc","cc","application/atom+xml; profile=opds-catalog; kind=navigation")
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
        if isinstance(value,Element):
            element.appendChild(value)
        else:
            node = self.doc.createElement(key)
            node.appendChild(self.doc.createTextNode(value))
            element.appendChild(node)

    def toString(self):
        #return self.doc.toxml("utf-8")
        return self.doc.toprettyxml(encoding="utf-8")

    def createEntry(self, title=None, updated=None, idd=None, content=None, links={}):
        entry = self.doc.createElement(Const.entry)
        self.addNode(entry, Const.entry_title, title)
        self.addNode(entry, Const.entry_updated, updated)
        self.addNode(entry, Const.entry_id, idd)
        self.addNode(entry, Const.entry_content, content)
        for link in links:
            self.createLink(entry, link.href, link.rel, link.title, link.type)
        self.feed.appendChild(entry)

    def createLink(self, entry, href, rel, title, type):
        link = self.doc.createElement(Const.link)
        link.setAttribute("type", type)
        link.setAttribute("href", href)
        link.setAttribute("rel", rel)
        link.setAttribute("title", title)
        entry.appendChild(link)
        return link


class Link:
    """
    Link Entity
    """
    def __init__(self, href, rel, title, type):
        self.href = href
        self.rel = rel
        self.title = title
        self.type = type


class OpdsProtocol:

    """
    All Opds File System Must Realized this Class
    """
    def __init__(self,feed,path):
        self.feed=feed
        self.path=path

    def listBooks(self):
        print("No Realized")
        pass

    def dowloadBook(self):
        print("No Realized")
        pass

    def showhtml(self):
        print("No Realized")
        pass


# if __name__ == '__main__':
