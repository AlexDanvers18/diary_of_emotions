from flask_login import login_required, current_user, login_user, logout_user
from webapp.diary_of_emotions.models import Articles, TextRecord, SmileRecord
from webapp.diary_of_emotions.forms import FeelForm
from webapp.diary_of_emotions.forms import SmileForm
from flask import Blueprint, current_app, render_template, flash, redirect, url_for
from webapp.user.models import User
from webapp.db import db
from datetime import datetime


blueprint = Blueprint('diary_of_emotions', __name__, url_prefix='/diary_of_emotions')


@login_required
@blueprint.route('/')
def index():
    title = "Добро пожаловать в безопасное пространство!"
    smile_form = SmileForm()
    feel_form = FeelForm()
    
    # article_list = Articles.query.order_by(Articles.published.desc()).all()
    return render_template('diary_of_emotions/index.html', page_title=title, smile_form=smile_form, feel_form=feel_form)


@login_required
@blueprint.route('/save-text-from-diary', methods=['POST'])
def save_feel_form():
    form = FeelForm()
    # published=datetime.now().strftime(f"%d/%B/%Y %H:%M")
    if form.validate_on_submit():
        new_text_record = TextRecord(user_id=current_user.id, 
                                
                                     text_emotions=form.text_emotions.data, 
                                     text_bodily_sensations=form.text_bodily_sensations.data, 
                                     text_thoughts=form.text_thoughts.data, 
                                     text_result=form.text_result.data,
                                     text_situation=form.text_situation.data)
        
        db.session.add(new_text_record)
        db.session.commit()

        flash('Вы сохранили текстовую запись')
        return redirect(url_for('diary_of_emotions.index'))
    
    flash('Невалидные данные')
    return redirect(url_for('diary_of_emotions.index'))



@login_required
@blueprint.route('/save-smile', methods=['POST'])
def save_smile_form():
    form = SmileForm()
    if form.validate_on_submit():
        new_smile_record = SmileRecord(user_id=current_user.id, 
                                     smile_good=form.smile_good.data,
                                     smile_crazy=form.smile_crazy.data,
                                     smile_neutral=form.smile_neutral.data,
                                     smile_agry=form.smile_agry.data,
                                     smile_sad=form.smile_sad.data)
        

        db.session.add(new_smile_record)
        db.session.commit()

        flash('Вы сохранили смайлик')
        return redirect(url_for('diary_of_emotions.index'))
    
    flash('Невалидные данные')
    return redirect(url_for('diary_of_emotions.index'))


