from flask import Flask, request, redirect, render_template, url_for
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
