
from io import BytesIO
from flask import Blueprint, current_app, render_template, flash, redirect, url_for, request, send_file
from flask_login import login_required, current_user, login_user, logout_user
from webapp.diary_of_emotions.models import TextRecord
from webapp.my_records.models import Upload
from webapp.diary_of_emotions.forms import FeelForm
from webapp.db import db
from sqlalchemy import update, delete
from webapp.my_records.crud_record import crud
import os


blueprint = Blueprint('my_records', __name__, url_prefix='/my_records')



@blueprint.route('/')
def my_records():
    title = "Мои записи"
    text_list = TextRecord.query.order_by(TextRecord.published.desc()).all()
    # delete_feel_form = DeleteFeelForm()
    return render_template('my_records/my_records.html', page_title=title, text_list=text_list)



@login_required
@blueprint.route('<int:id>/update_text_record', methods=['POST', 'GET'])
def update_text_record(id):
    feel_form = FeelForm()
    update_text_record = TextRecord.query.get(id)
    if request.method == 'POST':
        update_text_record.id = id
        update_text_record.text_emotions = request.form.get('text_emotions')
        update_text_record.text_bodily_sensations = request.form.get('text_bodily_sensations')
        update_text_record.text_thoughts = request.form.get('text_thoughts')
        update_text_record.text_situation = request.form.get('text_situation')
        update_text_record.text_result = request.form.get('text_result')


        try:
            db.session.commit()

            flash('Вы отредактировали текстовую запись')
            return redirect(url_for('my_records.my_records'))
        
        except:
            flash('Невалидные данные')

    else:
        return render_template('my_records/update_record.html', update_text_record=update_text_record, form=feel_form) 
    

@login_required
@blueprint.route('<int:id>/delete_text_record', methods=['GET'])
def delete_text_record(id):
    delete_text_record = TextRecord.query.get_or_404(id)

    try:
        db.session.delete(delete_text_record)
        db.session.commit()

        flash('Вы удалили текстовую запись')
        return redirect(url_for('my_records.my_records'))
    
    except:
        flash('Невалидные данные')
        return redirect(url_for('my_records.my_records'))
    




@blueprint.route('/download/', methods=['GET'])
def download():

    download_file = crud.complete_text_record(1)

    try:
        if download_file != None:

            return send_file(download_file, download_name = "my_records.txt")
    
    except(ValueError, TypeError) as e:
        print(e)

        flash('Ошибка')
        return redirect(url_for('my_records.my_records'))





