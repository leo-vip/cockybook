from flask import Flask
from CockyMain import Feed, Link


__author__ = 'lei'

app = Flask(__name__)

@app.route("/")
def helo():

    #f = Feed()
    #f.addEntry("ttt", "uuu", "iddd", "content...",
    #           {Link("xxx", "xxx", "aaa", "jpg"), Link("mm", "mm", "mm", "xml")})

    return "xxxx" #f.toString()+"\n"

if __name__ == "__main__":
    app.run()

