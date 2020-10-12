from flask import render_template

from . import app


@app.route('/')
def index():
    search_engines = {
        'Google': 'https://google.com',
        'Yahoo': 'https://yahoo.com',
        'DuckDuckGo': 'https://duckduckgo.com',
        'Yandex': 'https://yandex.com',
    }

    return render_template('index.html', name='World', search_engines=search_engines)
