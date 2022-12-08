from mdblog.factory import create_create_flask_app
from mdblog.models import db
from mdblog.models import User

flask_app, celery_app = create_create_flask_app()

## CLI DOMMAND
def init_db(app):
    with app.app_context():
        db.create_all()
        print("database initialized")

        default_user = User(username="admin")
        default_user.set_password("admin")

        db.session.add(default_user)
        db.session.commit()
        print("default user was created")