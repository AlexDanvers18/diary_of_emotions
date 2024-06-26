from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.widgets import TextArea
from wtforms.fields import Label
from wtforms.validators import DataRequired

class FeelForm(FlaskForm):
    text_situation = StringField('Что сегодня с тобой произошло?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Опиши событие"})
    text_thoughts = StringField('Какие мысли и образы возникли при этом?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Перечисли мысли и образы"})
    text_emotions = StringField('Какие эмоции возникли?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Перечисли эмцоии"})
    text_bodily_sensations = StringField('Какие телесные ощущения наблюдались?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Опиши ощущения в теле"})
    text_result = StringField('Что думаешь об этом событии сейчас?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Расскажи об этом"})
    text_victory = StringField('Твои победы дня', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Расскажи о своих достижениях в дне"})
    text_curiosity = StringField('Курьёзы дня', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Что забавного случилось сегодня?"})
    submit = SubmitField('Сохранить',render_kw={"class":"btn btn-primary"})


class SmileForm(FlaskForm):
    smile_good = BooleanField('🙂', default = False,  render_kw={"class": "form-control smile_icon"})
    smile_crazy = BooleanField('🤪', default = False,  render_kw={"class": "form-control smile_icon"})
    smile_neutral = BooleanField('😑', default = False,  render_kw={"class": "form-control smile_icon"})
    smile_agry = BooleanField('😠', default = False,  render_kw={"class": "form-control smile_icon"})
    smile_sad = BooleanField('😔', default = False,  render_kw={"class": "form-control smile_icon"})
    submit = SubmitField('Сохранить смайлик', render_kw={"class":"btn btn-primary"})

class EmotionForm(FlaskForm):
    emotion_1 = BooleanField(label='Радость', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_2 = BooleanField(label='Грусть', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_3 = BooleanField(label='Тревога', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_4 = BooleanField(label='Любопытство', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_5 = BooleanField(label='Злость', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_6 = BooleanField(label='Умиротворение', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_7 = BooleanField(label='Интерес', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_8 = BooleanField(label='Сомнение', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_9 = BooleanField(label='Вина', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_10 = BooleanField(label='Стыд', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_11 = BooleanField(label='Доверие', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_12 = BooleanField(label='Спокойствие', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_13 = BooleanField(label='Благодарность', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_14 = BooleanField(label='Лень', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_15 = BooleanField(label='Жалость', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_16 = BooleanField(label='Отчаяние', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_17 = BooleanField(label='Печаль', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_18 = BooleanField(label='Восторг', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_19 = BooleanField(label='Освобождение', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_20 = BooleanField(label='Ревность', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_21 = BooleanField(label='Зависть', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_22 = BooleanField(label='Обида', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_23 = BooleanField(label='Возмущение', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_24 = BooleanField(label='Досада', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_25 = BooleanField(label='Принятие', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_26 = BooleanField(label='Ненависть', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_27 = BooleanField(label='Ожидание', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_28 = BooleanField(label='Ярость', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_29 = BooleanField(label='Негодование', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_30 = BooleanField(label='Недовольство', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_31 = BooleanField(label='Изумление', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_32 = BooleanField(label='Забота', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_33 = BooleanField(label='Нежность', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_34 = BooleanField(label='Загнанность', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_35 = BooleanField(label='Скука', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_36 = BooleanField(label='Тоска', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_37 = BooleanField(label='Безысходность', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_38 = BooleanField(label='Скорбь', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_39 = BooleanField(label='Оцепенение', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_40 = BooleanField(label='Ужас', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_41 = BooleanField(label='Сочувствие', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_42 = BooleanField(label='Гордость', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_43 = BooleanField(label='Влюбленность', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_44 = BooleanField(label='Безопасность', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    emotion_45 = BooleanField(label='Блаженство', default = False,  render_kw={"class": "form-control emotion_class checkbox-input"})
    submit = SubmitField('Сохранить эмоции', render_kw={"class":"btn btn-primary"})

