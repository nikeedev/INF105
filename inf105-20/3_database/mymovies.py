from flask import Flask, request, render_template, make_response
from markupsafe import escape

from pathlib import Path
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>Hello, go to the <a href="/movie/">movie list</a>!</p>'


@app.route('/movie/')
def movielist():
    return render_template('movielist.html', list=build_list())


@app.route('/movie/<id>')
def single_movie(id=None):
    id = escape(id)
    path = Path("movies") / (id + '.json')

    if not path.exists:
            return f'Unknown movie {id}. <a href="/movie">Return to list</a>', 404

    info = get_movie_info(path)
    return render_template('movie.html', **info)
        


def build_list():
    all_jsons = Path("movies").glob("*.json")
    movie_list = []
    for path in all_jsons:
        id = path.stem
        info = get_movie_info(path)
        movie_list.append((info['year'], info['name'], id))
    return movie_list



def get_movie_info(path):
    with open(path) as f:
        info = json.load(f)
    return info    
