from flask import Flask, jsonify, request
from db_func import get_articles, create_articles, create_connection
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

db = create_connection()
app = Flask(__name__)

app.json_encoder = LazyJSONEncoder

swagger_template = dict(
info = {
    'title': LazyString(lambda: 'Ongoing creation of Swagger UI document'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'This document depicts a sample Swagger UI document and implements Hello World functionality after executing GET.'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'articles',
            "route": '/articles.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docu/"
}
swagger = Swagger(app, template=swagger_template,
                  config=swagger_config)


@swag_from("swagger.yml", methods=['GET'])
@app.route('/')
def page_load():
    return jsonify({"Welcome Message ": "Hello There, visit 127.0.0.1:5000/articles"})


@app.route('/articles')
@swag_from("swagger.yml", methods=['GET'])
def load_all_articles():
    response = get_articles(db)
    if len(response) == 0:
        return jsonify({"Error": "Sorry could not find any articles"})
    else:
        return jsonify(response)


@app.route('/articles/<keyword>')
@swag_from("swagger.yml", methods=['GET'])
def load_articles_by_keyword(keyword):
    response = get_articles(db, keyword)
    print(response)
    if len(response) == 0:
        return jsonify({"Error": "Sorry could not find any articles with keyword " + keyword})
    else:
        return jsonify(response)


@app.route('/articles/crear', methods=["POST"])
@swag_from("swagger.yml", methods=['POST'])
def post_articles():
    response = create_articles(db, request.json['name'], request.json['link'], request.json['cosa'])
    print(response)
    if len(response) == 0:
        return jsonify({"Error": "Sorry could not find any articles with keyword POST"})
    else:
        return jsonify(response)
