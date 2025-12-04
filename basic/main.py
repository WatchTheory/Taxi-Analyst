from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import pickle
import numpy as np

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

# Load the pickle file with error handling
try:
    upload_model = pickle.load(open('EDA_taxi_pkl_file', 'rb'))
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: Pickle file not found!")
    upload_model = None
except Exception as e:
    print(f"Error loading model: {e}")
    upload_model = None

class PredictionForm(FlaskForm):
    # Replace with your actual features
    distance = IntegerField('Distance', validators=[DataRequired()])
    tolls = FloatField('Number of tolls', validators=[DataRequired()])
    fare = FloatField('fare', validators=[DataRequired()])
    submit = SubmitField('Predict Price')

# Route to pages 
@app.route("/")
def index():
    return render_template("home.html")


# Works -- about the author page
@app.route("/about")
def about():
    return render_template("about.html")

# Works -- view profile 
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = PredictionForm()
    prediction = None
    if form.validate_on_submit():
        input_data = np.array([[
            form.distance.data,                    # Change the fields here
            form.tolls.data,                #
            form.fare.data,   #
        ]])
        
        try:
            price_prediction = float(upload_model.predict(input_data)[0])
            prediction = f"You will pay ${price_prediction:,.2f}"
        except Exception as e:
            prediction = f"Error: {str(e)}"
    
    return render_template("predict.html", form=form, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

#-----------------------------------------------
# Uncomment 
# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# import pickle
# import numpy


# app = Flask(__name__)

# # load your picke file here 
# app.config["SECRET_KEY"] = "your_secret_key"
# upload_model = pickle.load(open('EDA_churn_pkl_file','rb'))


# # Route to pages 
# @app.route("/")
# def index():
#     return render_template("home.html")

##---------------------------------------------





# @app.route("/member", methods=["GET", "POST"])
# def member():
#     name = False
#     email = False
#     form = MemberInfo()
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         form.name.data = ""
#     return render_template("member.html", name=name, email=email, form=form)


# @app.route("/member/<name>")
# def member(name):
#     return render_template("member.html", name=name)

## Uncomment 
## -----------------------------------------------
# # Works -- about the auther page
# @app.route("/about")
# def about():
#     return render_template("about.html")


# # Works -- view profile 
# @app.route("/profile")
# def profile():
#     return render_template("profile.html")

## --------------------------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)

# def main():
#     print("Hello from basic!")


# if __name__ == "__main__":
#     main(debug=True)



