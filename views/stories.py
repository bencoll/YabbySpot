from flask import Blueprint


story_blueprint = Blueprint('stories', __name__)


@story_blueprint.route('/')
def index():
    return 'stories.index'
