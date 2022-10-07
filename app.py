from flask import Flask, jsonify
import mysql.connector
from pprint import PrettyPrinter

mydb = None


def createConnection():
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="basebasica"
    )
    print(mydb)


createConnection()


def get_articles(keyword=''):
    cursor = mydb.cursor()
    cursor.execute("Select * from articles where name like '%"+keyword+"%'")
    articles = cursor.fetchall()
    jsonResult = []
    for article in articles:
        jsonResult.append({
            'ArticleName':article[1],
            'ArticleCosa': article[2],
            'ArticleLink':article[3]
        })
    return jsonResult


pp = PrettyPrinter()
pp.pprint(get_articles())

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


