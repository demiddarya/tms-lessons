import sqlite3
from dataclasses import dataclass
from flask import Flask, abort, redirect, session, request
from flask_session import Session
import sqlite3


@dataclass
class Product:
    id: int
    name: str
    description: str
    category_id: int


@dataclass
class Category:
    id: int
    name: str


def load_products() -> list[Product]:
    storage = []
    with sqlite3.connect("internet-shop.db") as connection:
        full_list = connection.execute("Select id, name ,description,category_id from product")
        for i in full_list.fetchall():
            element = Product(*i)
            storage.append(element)
        return storage


def information_of_produtc(product_id: int) -> Product:
    with sqlite3.connect("internet-shop.db") as connection:
        result = connection.execute("Select id, name, description, category_id from product where id=?", (product_id,))
        rows = result.fetchall()
        if len(rows) != 1:
            raise ValueError(f"This id not found {product_id}")
        return Product(*rows[0])


def category_of_produtc(category_idd:int) -> Product:
    with sqlite3.connect("internet-shop.db") as connection:
        result = connection.execute("Select id, name, description, category_id from product where category_id=?", (category_idd,))
        rows = result.fetchall()
        if len(rows) != 1:
            raise ValueError(f"This id not found {category_idd}")
        return Product(*rows[0])


def join_config()->list[Category]:
    storage = []
    with sqlite3.connect("internet-shop.db") as connection:
        full_list = connection.execute("Select id, name from category")
        for i in full_list.fetchall():
            element = Category(*i)
            storage.append(element)
        return storage


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)


@app.route('/')
@app.route('/products')
def all_products():
    products = load_products()
    category_list=join_config()
    products_html = "\n".join(f"<li><a href='/product/{product.id}'>{product.name}</li>" for product in products)
    category_html = "\n".join(f"<li><a href='/category/{object.id}'>{object.name}</li>" for object in category_list )
    return f"""
    <html>
        <head>
            <title> Product shop </title>
        </head>
        <body>
            <h7>Favorite products:</h7>
            <a href="/product_list"><img src="data:image/png;base64,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"/></a>
            <h1> Category: </h1>
            <h3> {category_html} </h3>
            <h1> Product List </h1>
            <ul>
                {products_html}
            </ul>
        </body>
    </html>
    """


@app.route('/product/<int:product_id>')
def list_of_product(product_id: int):
    try:
        product = information_of_produtc(product_id)
    except ValueError as e:
        abort(404, e)
    star = ""
    favarite_products=session.get('favorite_products', set())
    if product.id in favarite_products :
        star = "&#9989"
    return f'''
    <html>
        <head>
            <title> {product.name} </title>
        </head>
        <body>
            <a href="/products"> Main page</a>
            <h1> Name:{product.name} {star} </h1>
            <h2> Description:{product.description} </h2>
            <h3> Category:{product.category_id} </h3>
            <h3> {count_favorites_products}
            <form method="post" action="/product/favorites_products">
                <input type="hidden" name="products_id" value="{product.id}"/>
                <input type="submit" value="Add favorites products "/>
            </form>
        </body>
    </html>
    '''


@app.route("/product/favorites_products", methods=["POST"])
def count_favorites_products():
    product_id = int(request.form["products_id"])
    product = information_of_produtc(product_id)
    favorite_products = session.setdefault('favorite_products', set())
    if product.id in favorite_products:
        favorite_products.remove(product.id)

    else:
        favorite_products.add(product.id)
    return redirect(f'/product/{product.id}')


@app.route("/product_list")
def generate_html_list():
    basket_list=[]
    favorite_product=session.get('favorite_products', set())
    for i in favorite_product:
        basket_list.append(information_of_produtc(i))
    products_html = "\n".join(f"<li><a href='/product/{product.id}'>{product.name}</li>" for product in basket_list)
    return f"""
    <html>
        <head>
            <title> Favorite Products </title>
        </head
        <body>
            <h1> Favorite Products: </h1>
            <ul>
                {products_html}
            </ul>
        </body>
    </html>
    """


@app.route("/category/<int:category_id>")
def list_category(category_id):
    try:
        products = category_of_produtc(category_id)
    except ValueError as e:
        abort(404, e)
    products_html = "\n".join(f"<li><a href='/product/{product.id}'>{product.name}</li>" for product in products)
    return f'''
        <html>
            <head>
                <title> Category list </title>
            </head>
            <body>
                <a href="/products"> Main page</a>
                <h1> Favorite Products: </h1>
                <h1> Name:{products.name} </h1>
                <ul>
                    {products_html}
                </ul>
            </body>
        </html>

'''


if __name__ == "__main__":
    app.run(port=2202, debug=True)
