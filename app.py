import os
from flask import Flask, render_template

from common.decorators import requires_writer
from views.gabby import gabby_blueprint
from views.poems import poem_blueprint
from views.stories import story_blueprint
from views.users import user_blueprint

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

app.register_blueprint(gabby_blueprint, url_prefix='/gabby')
app.register_blueprint(poem_blueprint, url_prefix='/poems')
app.register_blueprint(story_blueprint, url_prefix='/stories')
app.register_blueprint(user_blueprint, url_prefix='/users')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new')
@requires_writer
def new_post():
    return render_template('post.html')


if __name__ == '__main__':
    app.run(debug=True)
