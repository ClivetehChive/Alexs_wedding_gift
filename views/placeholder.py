from flask import Flask, Blueprint

example_blueprint = Blueprint('example', __name__)

@example_blueprint.route('/<variable>', methods=['POST', 'GET'])
def test(variable):
    return variable