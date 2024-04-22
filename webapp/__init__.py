from flask import Flask

from flask_login import LoginManager
from flask_migrate import Migrate
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.models import User
from webapp.db import db
from webapp.user.views import blueprint as user_blueprint
from webapp.diary_of_emotions.views import blueprint as diary_of_emotions_blueprint
from webapp.my_records.views import blueprint as my_records_blueprint
from webapp.dict_of_emotions.views import blueprint as dict_of_emotions_blueprint
from webapp.my_stat.views import blueprint as stat_blueprint

# from jinja2 import Template, FileSystemLoader, Environment

# # Configure the template directory
# env = Environment(loader=FileSystemLoader('template'))

# # Render a template that doesn't exist
# template = env.get_template('login.html')




def create_app():
    # app = Flask(__name__)
    app = Flask(__name__, template_folder='template')
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(my_records_blueprint)
    app.register_blueprint(diary_of_emotions_blueprint)
    app.register_blueprint(stat_blueprint)
    app.register_blueprint(dict_of_emotions_blueprint)
    app.register_blueprint(user_blueprint)
    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    return app

# if __name__=="__main__":
#     app.run(debug=True)