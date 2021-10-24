from flask_login import LoginManager


def configurate(app):

    app.config['SECRET_KEY'] = 'Some-my-very-secret-key'



    return app
