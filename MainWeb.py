from xml.dom.minidom import Document
from flask import Flask
from CockyMain import Feed, Link


__author__ = 'lei'

app = Flask(__name__)

@app.route("/")
def helo():
    doc = Document()
    f = Feed(doc)
    #f.cleanDoc()
    f.addEntry("ttt", "uuu", "iddd", "content...",
               {Link("xxx", "xxx", "aaa", "jpg"), Link("mm", "mm", "mm", "xml")})

    return f.toString()+"\n"

if __name__ == "__main__":
    app.debug =True
    app.run()

