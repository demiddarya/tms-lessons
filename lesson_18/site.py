from dataclasses import dataclass
import sqlite3
from flask import Flask, abort, request, session, redirect
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str
    like_count: int


def get_all_articles() -> list[Article]:
    with sqlite3.connect('site.db') as connection:
        cur = connection.execute('SELECT id, title, text, author, like_count FROM article')
        result = []
        for data in cur.fetchall():
            article = Article(data[0], data[1], data[2], data[3], data[4])
            result.append(article)
        return result


def get_article(article_id) -> Article:
    with sqlite3.connect('site.db') as connection:
        cur = connection.execute('SELECT id, title, text, author, like_count FROM article WHERE id = ?', (article_id,))
        rows = cur.fetchall()
        if len(rows) != 1:
            raise ValueError(f'Expected 1 object with id {article_id}, got {len(rows)}')
    return Article(*rows[0])


def save_article(article: Article):
    with sqlite3.connect('site.db') as connection:
        data = (article.title, article.text, article.author, article.like_count, article.id)
        connection.execute('UPDATE article '
                           'SET title = ?, text = ?, author = ?, like_count = ? '
                           'WHERE id = ?', data)


@app.route('/')
@app.route('/articles')
def articles():
    all_articles = get_all_articles()
    all_titles = []
    for article in all_articles:
        all_titles.append(f'<li><a href="/article/{article.id}">{article.title}</li>')
    all_titles_str = '<br>'.join(all_titles)
    return f'''
    <html>
        <head>
            <title>Articles APP</title>
        </head>
        <body>
           <h1>All articles</h1>
           <ul>
                {all_titles_str}
           </ul
        </body>
    </html>
    '''


@app.route('/article/<int:article_id>')
def view_article(article_id: int):
    try:
        article = get_article(article_id)
    except ValueError as e:
        abort(404, e)
    return f'''
    <html>
        <head>
            <title>Articles APP</title>
        </head>
        <body>
            <a href="/articles">Go to home page</a>
            <h1>{article.title}</h1>
            <h3>Author: {article.author}</h3>
            <p>{article.text}</p>
            <p>Like count: {article.like_count}</p>
            <form method="post" action="/article/like">
                <input type="hidden" name="article_id value="{article_id}"/>
                <input type="submit" value="Like"/>
            </form>
        </body>
    </html>
    '''


@app.route('/article/like', methods=['POST'])
def like_article():
    article_id = int(request.form['article_id'])
    article = get_article(article_id)
    liked_articles = session.setdefault('liked_articles', set())
    if article.id in liked_articles:
        article.like_count -= 1
        liked_articles.remove(article.id)
    else:
        article.like_count += 1
        liked_articles.add(article.id)
    save_article(article)
    return redirect(f'/article/{article.id}')


if __name__ == '__main__':
    app.run(port=8080, debug=True)


