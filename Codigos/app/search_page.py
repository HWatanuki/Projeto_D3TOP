# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

import os

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

# Class to render search form
class SearchForm(FlaskForm):
    search = StringField('Termos de busca:', validators=[DataRequired(), Length(min=4)], id='search', render_kw={"placeholder": "Busca livre"})
    submit = SubmitField('Pesquisar')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    message = "Preecha todos os campos obrigatórios."
    if form.validate_on_submit():
        return # replace with the response of ml algoritm
    return render_template('index.html', form=form, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)