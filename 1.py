#1) to create a flask that displays"hello world" on home page

from flask import Flask, request
app= Flask(__name__)

@app.route("/")
def Hello_World():
    return "Hello World"

    if __name__== '__main__':
        app.run(host="0.0.0.0")








