from flask import Flask, render_template

app = Flask(__name__)

# داده‌های محصولات
products = [
    {"id": 1, "name": "Product 1", "price": 10.99, "image": "static/images/imag1.jpg"},
    {"id": 2, "name": "Product 2", "price": 12.99, "image": "images/imag2.jpg"},
    {"id": 3, "name": "Product 3", "price": 8.99, "image": "images/imag3.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)