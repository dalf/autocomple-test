from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', q=request.args.get('q', None))

@app.route("/autocomplete")
def autocomplete():
    q = request.args.get('q', '')
    return jsonify([ q + 'a', q + 'b', q + 'c', q + 'd', q + 'e', q + 'f'])

if __name__ == "__main__":
    app.run()
