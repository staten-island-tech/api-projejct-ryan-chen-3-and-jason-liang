import os

from flask import Flask, render_template
from requests import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return render_template('index.html')

    @app.route('/pokemon/<pokemon>')
    def getpokemon(pokemon):
        for e in pokemon["__init__"]:
            if pokemon in e["name"]:
                return render_template("interest.html", pokemon=pokemon)
        return "try again!"

    return app