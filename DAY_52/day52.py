from flask import Flask, request, redirect, render_template
import string
import random

app = Flask(__name__)
url_map = {}

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form.get('url')
        short_code = generate_short_code()
        url_map[short_code] = original_url
        short_url = request.host_url + short_code
        return render_template('about.html', short_url=short_url)
    return render_template('about.html')

@app.route('/<short_code>')
def redirect_url(short_code):
    if short_code in url_map:
        return redirect(url_map[short_code])
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)