from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import string
import random

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, original_url TEXT, short_url TEXT)''')
        conn.commit()

# Generate a random short string
def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Add URL to database
def add_url_to_db(original_url, short_url):
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
        conn.commit()

# Retrieve URL from database
def get_original_url(short_url):
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
        result = c.fetchone()
        return result[0] if result else None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = generate_short_url()
        add_url_to_db(original_url, short_url)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    return 'URL not found', 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
