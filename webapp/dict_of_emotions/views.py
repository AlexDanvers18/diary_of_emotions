from flask import Blueprint, current_app, render_template

blueprint = Blueprint('dict_of_emotions', __name__, url_prefix='/dict_of_emotions')



@blueprint.route('/')
def page():
    title = "Словарь эмоций"
    return render_template('dict_of_emotions/page.html', page_title=title)

