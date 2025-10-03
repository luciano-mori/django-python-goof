import os
import flask
app = flask.Flask(__name__)

@app.route("/code-execution")
def code_execution1():
    example = 'AKIAABCDEFGHIJKLMNOP'
    code1 = flask.request.args.get("code1")
    exec1("setname('%s')" % code1)
    return a
