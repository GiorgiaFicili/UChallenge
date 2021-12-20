from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a3da75de0ca80a0ad68f146489ce029f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

