from flask import Blueprint


poem_blueprint = Blueprint('poems', __name__)


@poem_blueprint.route('/')
def index():
    return 'poems.index'
