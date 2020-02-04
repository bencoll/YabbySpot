from flask import Blueprint, request, render_template, flash

from models.post import Post

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
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        content = request.form['content']
        featured = True if request.form.get('featured', 'off') == 'on' else False
        Post(author=author, title=title, subtitle=subtitle,
             content=content, featured=featured).save_to_db()
        flash(f"Your new post has been saved; '{title}'.", "success")
    return render_template("new_post.html", post="Story")
