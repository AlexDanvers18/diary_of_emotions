
from io import BytesIO
from flask import Blueprint, current_app, render_template, flash, redirect, url_for, request, send_file
from flask_login import login_required, current_user, login_user, logout_user
from webapp.diary_of_emotions.models import SmileRecord
from webapp.my_records.models import Upload
from webapp.diary_of_emotions.forms import FeelForm, SmileForm
from webapp.diary_of_emotions.forms import EmotionForm
from webapp.db import db
from sqlalchemy import update, delete
from webapp.my_stat.crud_record import stat
import os


blueprint = Blueprint('my_stat', __name__, url_prefix='/my_stat')



@blueprint.route('/')
def my_stat():
    title = "Статистика моего настроения и эмоций"
    smile_record = SmileRecord.query.order_by(SmileRecord.published.desc()).all()
    emo_form = EmotionForm()
    complete = stat.complete_smile_record(current_user.id)
    emo_dict = stat.complete_emo_record(current_user.id)
    return render_template('my_stat/my_stat.html', page_title=title, smile_record=smile_record, complete=complete, emo_dict=emo_dict, emo_form=emo_form)


# @blueprint.route('/', methods=['POST'])
# def smile():

#     complete = stat.complete_smile_record(current_user.id)

#     print(complete)

    # download_file = stat.complete_smile_record(1)

    # try:
    #     if download_file != None:

    #         return send_file(download_file, download_name = "my_stats.txt")
    
    # except(ValueError, TypeError) as e:
    #     print(e)

    #     flash('Ошибка')
    #     return redirect(url_for('my_stat.my_stat'))