from flask_login import login_required, current_user, login_user, logout_user
from webapp.diary_of_emotions.models import Articles, TextRecord, SmileRecord, EmoRecord
from webapp.diary_of_emotions.forms import FeelForm
from webapp.diary_of_emotions.forms import SmileForm, EmotionForm
from flask import Blueprint, current_app, render_template, flash, redirect, url_for
from webapp.user.models import User
from webapp.db import db
from datetime import datetime


blueprint = Blueprint('diary_of_emotions', __name__, url_prefix='/diary_of_emotions')





@login_required
@blueprint.route('/')
def index():
    if current_user.is_authenticated:
        # title = "Дневник эмоций"
        smile_form = SmileForm()
        feel_form = FeelForm()
        emo_form = EmotionForm()
        # article_list = Articles.query.order_by(Articles.published.desc()).all()
        return render_template('diary_of_emotions/index.html', smile_form=smile_form, feel_form=feel_form, emo_form=emo_form)
    else:
        return redirect(url_for('user.register'))
    


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
                                     text_situation=form.text_situation.data,
                                     text_victory=form.text_victory.data,
                                     text_curiosity=form.text_curiosity.data
                                     )
        
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


@login_required
@blueprint.route('/save-emotions', methods=['POST'])
def save_emotions_form():
    form = EmotionForm()
    if form.validate_on_submit():
        new_emo_record = EmoRecord(user_id=current_user.id, 
                                     emotion_1=form.emotion_1.data,
                                     emotion_2=form.emotion_2.data,
                                     emotion_3=form.emotion_3.data,
                                     emotion_4=form.emotion_4.data,
                                     emotion_5=form.emotion_5.data,
                                     emotion_6=form.emotion_6.data,
                                     emotion_7=form.emotion_7.data,
                                     emotion_8=form.emotion_8.data,
                                     emotion_9=form.emotion_9.data,
                                     emotion_10=form.emotion_10.data,
                                     emotion_11=form.emotion_11.data,
                                     emotion_12=form.emotion_12.data,
                                     emotion_13=form.emotion_13.data,
                                     emotion_14=form.emotion_14.data,
                                     emotion_15=form.emotion_15.data,
                                     emotion_16=form.emotion_16.data,
                                     emotion_17=form.emotion_17.data,
                                     emotion_18=form.emotion_18.data,
                                     emotion_19=form.emotion_19.data,
                                     emotion_20=form.emotion_20.data,
                                     emotion_21=form.emotion_21.data,
                                     emotion_22=form.emotion_22.data,
                                     emotion_23=form.emotion_23.data,
                                     emotion_24=form.emotion_24.data,
                                     emotion_25=form.emotion_25.data,
                                     emotion_26=form.emotion_26.data,
                                     emotion_27=form.emotion_27.data,
                                     emotion_28=form.emotion_28.data,
                                     emotion_29=form.emotion_29.data,
                                     emotion_30=form.emotion_30.data,
                                     emotion_31=form.emotion_31.data,
                                     emotion_32=form.emotion_32.data,
                                     emotion_33=form.emotion_33.data,
                                     emotion_34=form.emotion_34.data,
                                     emotion_35=form.emotion_35.data,
                                     emotion_36=form.emotion_36.data,
                                     emotion_37=form.emotion_37.data,
                                     emotion_38=form.emotion_38.data,
                                     emotion_39=form.emotion_39.data,
                                     emotion_40=form.emotion_40.data,
                                     emotion_41=form.emotion_41.data,
                                     emotion_42=form.emotion_42.data,
                                     emotion_43=form.emotion_43.data,
                                     emotion_44=form.emotion_44.data,
                                     emotion_45=form.emotion_45.data
                                     )
        

        db.session.add(new_emo_record)
        db.session.commit()

        flash('Вы сохранили эмоции')
        return redirect(url_for('diary_of_emotions.index'))
    
    flash('Невалидные данные')
    return redirect(url_for('diary_of_emotions.index'))


