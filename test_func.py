from webapp import create_app
from webapp.my_stat.crud_record import stat
from webapp.my_records.crud_record import crud

app = create_app()
with app.app_context():
    # psycho_b17.get_articles_snippets()
    # psycho_b17.get_articles_content()
    # psycho_b17.get_one_article_text()

    # crud.complete_text_record(1)
    # stat.complete_smile_record(1)
    stat.complete_emo_record(2)
    # crud.get_text_record_id()
    # crud.get_my_records()


