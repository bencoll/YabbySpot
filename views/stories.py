from flask import Blueprint, request, render_template

story_blueprint = Blueprint('stories', __name__)


@story_blueprint.route('/')
def index():
    """
    Collect list of stories and display them as cards to be selected
    :return: stories page with list of stories
    """
    # TODO: Stories landing page
    return 'stories.index'


@story_blueprint.route('/new', methods=['GET', 'POST'])
def new_story():
    if request.method == 'POST':
        pass
    return render_template("new_post.html", post="Story")
