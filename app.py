from flask import Flask
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB('db.json')


@app.route('/')
def hello_world():
    tables = db.tables()

    html = """
    <html>
        <head>
            <title>Smartphones</title>
        </head>

        <body>
            <h1>List of Brands</h1>
            <ul>
    """
    for table in tables:
        html += f"<li>{table}</li>"

    html += """</ul>"""

    # tables of pruducts
    for table in tables:
        html += f"<h2>{table}</h2>"
        html += """<table border='1'>
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Image</th>
            </tr>
        """

        for product in db.table(table).all():
            html += f"""
                <tr>
                    <td>{product['name']}</td>
                    <td>{product['price']}</td>
                    <td><a href="{product['img_url']}">url<a/></td>
                </tr>
            """ 
        html += "</table>"
    return html


if __name__ == '__main__':
    app.run(debug=True)