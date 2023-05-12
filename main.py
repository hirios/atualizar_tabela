from flask import Flask, render_template, request, url_for, redirect, session, jsonify,after_this_request
import json


app = Flask(__name__)


def readJason():
    with open('chat.json') as json_file:
         return json.load(json_file)


@app.route('/', methods=["POST", "GET"])
def home():
	if request.method == "GET":	
		return render_template('index.html')


@app.route('/json', methods=["POST", "GET"])
def api():
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    if request.method == "GET":
        return jsonify(readJason())

        #return render_template('index.html')


app.run(host='0.0.0.0', port=5000, debug=True)


# @app.route('/', methods=["POST", "GET"])
# def home():
# 	if request.method == "POST":
# 		manga_title = request.form["manga_title"]
# 		return redirect(url_for("results", manga_title=manga_title))

# 	return render_template('pesquisa.html')