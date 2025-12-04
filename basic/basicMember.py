import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# This sets our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///members.db"

# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'members.db')



db = SQLAlchemy(app)


class Member(db.Model):                                                 # Defines members that inherits from db.Model - in SQL Alchemy, it turns the class into a databse model 
    __tablename__ = "members"                       # specifiees the name of the table in the database as members

    id = db.Column(db.Integer, primary_key=True)                        # defines column name; the primary key is a uniquie identifier 
    name = db.Column(db.String(80), unique=False, nullable=False)       # define column name; multiple members can have the same name; member name must have a name, can't be null in the databse
    email = db.Column(db.String(120), unique=False, nullable=False)     # emails don't have to be unique and field can't be null; something is required

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):                     # special method that defines how the object is printed or represented as a string
        return f"<Member {self.name}>"      # returns  member name


with app.app_context():             # Creates a temporary Flask application context
    db.create_all()               # checks if the database for all defined models(like members) and creates the corresponding table if they don't exists



# import os

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# # This grabs our directory
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# # Connects our Flask App to our Database
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
#     basedir, "data.sqlite"
# )
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)


# class Member(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def __repr__(self):
#         return f"<Member {self.name}>"