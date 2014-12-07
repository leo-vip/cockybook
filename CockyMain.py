from xml.dom.minidom import Document
import Const

__author__ = 'lei'


class Feed():
    def __init__(self, doc=Document()):
        """
        Root Element
        :param doc:  Document()
        :return:
        """
        self.doc = doc
        self.feed = self.doc.createElement("feed")
        self.addNode(self.feed, Const.id, "http://opds.cockybook.com")
        self.addNode(self.feed, Const.author, "yinlei212@gmail.com")
        self.addNode(self.feed, Const.title, "CockyBook")
        self.doc.appendChild(self.feed)
        pass

    def addNode(self, element, key, value, link=None):
        """
        add A node to element
        :param element:
        :param key:
        :param value:
        :param link:  if is link ,this field is Not None.
        :return:
        """
        node = self.doc.createElement(key)
        node.appendChild(self.doc.createTextNode(value))
        element.appendChild(node)

    def toString(self):
        return self.doc.toxml("utf-8")
        #return self.doc.toprettyxml(encoding="utf-8")

    def addEntry(self, title=None, updated=None, idd=None, content=None, links={}):
        entry = self.doc.createElement(Const.entry)
        self.addNode(entry, Const.entry_title, title)
        self.addNode(entry, Const.entry_updated, updated)
        self.addNode(entry, Const.entry_id, idd)
        self.addNode(entry, Const.entry_content, content)
        for link in links:
            self.__addLink4Entry(entry, link.href, link.rel, link.title, link.type)
        self.feed.appendChild(entry)

    def __addLink4Entry(self, entry, href, rel, title, type):
        link = self.doc.createElement(Const.link)
        link.setAttribute("type", type)
        link.setAttribute("href", href)
        link.setAttribute("rel", rel)
        link.setAttribute("title", title)
        entry.appendChild(link)
        return link


class Link:
    def __init__(self, href, rel, title, type):
        self.href = href
        self.rel = rel
        self.title = title
        self.type = type



if __name__ == '__main__':
    for ii in range(10):
        doc = Document()
        f = Feed(doc)
        f.addEntry("ttt", "uuu", "iddd", "content...", {Link("xxx", "xxx", "aaa", "jpg"), Link("mm", "mm", "mm", "xml")})
        print f.toString()