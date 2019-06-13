#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, request, render_template, jsonify, redirect, url_for, make_response
from model import GameModel

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static')

model = GameModel(1)

@app.route('/')
def index():
    res = make_response(render_template('index.html', board=model.game.grid, size=model.game.dimension))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.route('/new/<difficulty>/<int:size>', methods=['GET'])
def new_game(difficulty, size):
    print('Initializing model with size {}'.format(size))
    model.new(size, difficulty)

    res = make_response(jsonify(model.game.grid))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.route('/swap', methods=['POST'])
def tile_swap():
    tile = (request.form['i'], request.form['j'])
    print('Swapping tile {}'.format(tile))

    # Sanitize input
    try:
        tile = tuple([int(c) for c in tile])
    except ValueError:
        res = make_response(jsonify(None))
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res

    if model.valid_swap(tile):
        model.swap(tile)
    else:
        res = make_response(jsonify(None))
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res

    json = {
        'won': model.game.win_state(),
        'model': model.game.grid
    }

    res = make_response(jsonify(json))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000, debug=True)