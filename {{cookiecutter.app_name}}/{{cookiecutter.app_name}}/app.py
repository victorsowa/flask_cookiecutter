import os
import sys

import flask

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import {{cookiecutter.app_name}}.data.db_session as db_session

app = flask.Flask(__name__)


def main():
    configure()
    app.run(debug=True, port=5006)


def configure():
    print("Configuring Flask app:")

    register_blueprints()
    print("Registered blueprints")

    setup_db()
    print("DB setup completed.")
    print("", flush=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        '{{cookiecutter.app_name}}.sqlite')

    db_session.global_init(db_file)


def register_blueprints():
    from {{cookiecutter.app_name}}.views import home_views

    app.register_blueprint(home_views.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()
