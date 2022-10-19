from flask import Flask, jsonify, request
from db_func import get_articles, create_articles, create_connection

db = create_connection()
app = Flask(__name__)


@app.route('/')
def page_load():
    return jsonify({"Welcome Message ": "Hello There, visit 127.0.0.1:1234/articles"})


@app.route('/articles')
def load_all_articles():
    response = get_articles(db)
    if len(response) == 0:
        return jsonify({"Error": "Sorry could not find any articles"})
    else:
        return jsonify(response)


@app.route('/articles/<keyword>')
def load_articles_by_keyword(keyword):
    response = get_articles(db, keyword)
    print(response)
    if len(response) == 0:
        return jsonify({"Error": "Sorry could not find any articles with keyword " + keyword})
    else:
        return jsonify(response)


@app.route('/articles/crear', methods=["POST"])
def post_articles():
    response = create_articles(db, request.json['name'], request.json['link'], request.json['cosa'])
    print(response)
    if len(response) == 0:
        return jsonify({"Error": "Sorry could not find any articles with keyword POST"})
    else:
        return jsonify(response)
