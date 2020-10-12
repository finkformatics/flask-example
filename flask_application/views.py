from flask import redirect, render_template, request

from . import app

search_engines = {
    'Google': 'https://google.com',
    'Yahoo': 'https://yahoo.com',
    'DuckDuckGo': 'https://duckduckgo.com',
    'Yandex': 'https://yandex.com',
}


@app.route('/')
def index():
    return render_template('index.html', name='World', search_engines=search_engines)


@app.route('/add', methods=['POST'])
def add_search_engine():
    search_engines[request.form.get('search-engine-name')] = request.form.get('search-engine-url')

    return redirect('/')
