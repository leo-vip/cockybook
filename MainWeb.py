from flask import Flask
from CockyMain import Feed, Link


__author__ = 'lei'

app = Flask(__name__)
f = Feed()
@app.route("/")
def helo():
    #f.cleanDoc()
    f.addEntry("ttt", "uuu", "iddd", "content...",
               {Link("xxx", "xxx", "aaa", "jpg"), Link("mm", "mm", "mm", "xml")})

    return f.toString()+"\n"

if __name__ == "__main__":
    app.debug =True
    app.run()

