from webbrowser import get
from flask import Flask, jsonify, request
import csv
from contentfiltering import get_recommendations
from demfiltering import articles as art

articles_list = []

with open('articles.csv', newline='', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        articles_list.append(row)

articles_list.pop(0)

like = []
dislike = []
# not_watched = []

app = Flask(__name__)

@app.route('/get-articles')

def get_articles():
    return jsonify({
        "data": articles_list,
        "status": 'Success'
    }, 200)

@app.route('/liked-articles', methods=['POST'])

def liked_articles():
    articles = articles_list[0]

    for row in articles_list:
        if articles_list['title'] == articles:
            like.append(row)

    return jsonify({
        "data": like,
        "status": 'Success'
    }, 200)

@app.route('/disliked-articles', methods=['POST'])

def disliked_articles():
    articles = articles_list[0]
    
    for row in articles_list:
        if articles_list['title'] == articles:
            dislike.append(row)

    return jsonify({
        "data": dislike,
        "status": 'Success'
    }, 200)

@app.route('/first-article', methods=['GET'])

def first_article():
    articles = articles_list[0]

    return jsonify({
        "data": articles,
        "status": 'Success'
    }, 200)

@app.route('/get-rec', methods=['GET'])

def get_rec():
    recommendations = get_recommendations()

    return jsonify({
        "data": recommendations,
        "status": 'Success'
    }, 200)

@app.route('/popular', methods=['GET'])

def popular():
    popular_articles = art

    return jsonify({
        "data": popular_articles,
        "status": 'Success'
    }, 200)


if __name__ == "__main__":
    app.run(debug=True)

