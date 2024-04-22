from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class FeelForm(FlaskForm):
    text_situation = StringField('Что сегодня с тобой произошло?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Опиши событие"})
    text_thoughts = StringField('Какие мысли и образы возникли при этом?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Перечисли мысли и образы"})
    text_emotions = StringField('Какие эмоции возникли?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Перечисли эмцоии"})
    text_bodily_sensations = StringField('Какие телесные ощущения наблюдались?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Опиши ощущения в теле"})
    text_result = StringField('Что думаешь об этом событии сейчас?', widget=TextArea(), render_kw={"class": "form-control", "placeholder": "Расскажи об этом"})
    submit = SubmitField('Сохранить',render_kw={"class":"btn btn-primary"})


class SmileForm(FlaskForm):
    smile_good = BooleanField('🙂', default = False,  render_kw={"class": "form-control smile_icon"})
    smile_crazy = BooleanField('🤪', default = False,  render_kw={"class": "form-control smile_icon"})
    smile_neutral = BooleanField('😑', default = False,  render_kw={"class": "form-control smile_icon"})
    smile_agry = BooleanField('😠', default = False,  render_kw={"class": "form-control smile_icon"})
    smile_sad = BooleanField('😔', default = False,  render_kw={"class": "form-control smile_icon"})
    submit = SubmitField('Сохранить смайлик', render_kw={"class":"btn btn-primary"})

# class MoodForm(FlaskForm):
#     username = StringField('Имя пользователя',validators=[DataRequired()],
#           render_kw={"class": "form-control"})
#     password = PasswordField('Пароль',validators=[DataRequired()],
#           render_kw={"class": "form-control"})
#     submit = SubmitField('Отправить',render_kw={"class":"btn btn-primary"})
