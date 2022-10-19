from flask import Flask, jsonify, request
from db_func import get_articles, create_articles

mydb = None

app = Flask(__name__)

@app.route('/')
def pageLoad():
    return jsonify({"Welcome Message " :"Hello There, visit 127.0.0.1:1234/articles"})
@app.route('/articles')
def loadAllArticles():
    response = get_articles()
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any articles"})
    else:
        return jsonify(response)
@app.route('/articles/<keyword>')
def loadArticlesByKeyword(keyword):
    response = get_articles(keyword)
    print(response)
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any articles with keyword "+keyword})
    else:
        return jsonify(response)

@app.route('/articles/crear' , methods = ["POST"])
def loadArticlesByKeywordPost():
    response = create_articles(request.json['name'], request.json['link'], request.json['cosa'])
    print(response)
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any articles with keyword POST"})
    else:
        return jsonify(response)


