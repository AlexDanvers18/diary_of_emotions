
from io import BytesIO
from flask import Blueprint, current_app, render_template, flash, redirect, url_for, request, send_file
from flask_login import login_required, current_user, login_user, logout_user
from webapp.diary_of_emotions.models import SmileRecord
from webapp.my_records.models import Upload
from webapp.diary_of_emotions.forms import FeelForm, SmileForm
from webapp.db import db
from sqlalchemy import update, delete
from webapp.my_stat.crud_record import stat
import os


blueprint = Blueprint('my_stat', __name__, url_prefix='/my_stat')



@blueprint.route('/')
def my_stat():
    title = "Статистика моего настроения и эмоций"
    smile_record = SmileRecord.query.order_by(SmileRecord.published.desc()).all()
    # delete_feel_form = DeleteFeelForm()
    return render_template('my_stat/my_stat.html', page_title=title, smile_record=smile_record)




@blueprint.route('/download/', methods=['GET'])
def download():

    download_file = stat.complete_smile_record(1)

    try:
        if download_file != None:

            return send_file(download_file, download_name = "my_stats.txt")
    
    except(ValueError, TypeError) as e:
        print(e)

        flash('Ошибка')
        return redirect(url_for('my_stat.my_stat'))





