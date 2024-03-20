
from flask import Flask, request, render_template,  redirect, flash, url_for, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Cupcake



app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_ECHO'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

if __name__ == "__main__":
    app.run(debug=True)


connect_db(app)
app_context = app.app_context()
app_context.push()
"""Flask app for Cupcakes"""
