from flask import Blueprint


gabby_blueprint = Blueprint('gabby', __name__)


@gabby_blueprint.route('/about')
def about():
    return 'gabby.about'
