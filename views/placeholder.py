from flask import Flask, Blueprint

example_blueprint = Blueprint('example', __name__)

@example_blueprint.route('/spotify')
def test():
    return "This is the blueprint"