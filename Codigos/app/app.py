from flask import Flask, render_template, session, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import NumberRange

#import numpy as np  
#from tensorflow.keras.models import load_model
#import joblib
import pandas as pd



def return_prediction(dataframe_full,guest_criteria,price_max_criteria,price_min_criteria,room_criteria):
    #unused_columns = ['isAvailable','isHostedBySuperhost','location/lat','location/lng','photos/0/caption','photos/0/pictureUrl',]
    #dataframe = dataframe.drop(unused_columns, axis=1)
    dataframe_full['thumbnail'] = dataframe_full['photos/0/thumbnailUrl'].apply(lambda x: '<img src="{}"/>'.format(x) if x else '')
    dataframe_full['url'] = '<a href="' + dataframe_full['url'] + '">' + dataframe_full['url'] + '</a>'
    dataframe = dataframe_full[['address','stars','numberOfGuests','roomType','pricing/rate/amount','thumbnail','url']]
    numeric_cols = ['numberOfGuests','pricing/rate/amount']
    #numeric_cols = ['numberOfGuests']
    dataframe[numeric_cols] = dataframe[numeric_cols].apply(pd.to_numeric, errors='coerce', axis=1)
    filtered_df = dataframe[(dataframe['numberOfGuests'] == guest_criteria) & (dataframe['pricing/rate/amount'] <= price_max_criteria) & (dataframe['pricing/rate/amount'] >= price_min_criteria) & (dataframe['roomType'].str.contains(room_criteria, case=False))]
    #filtered_df = dataframe[dataframe['numberOfGuests'] == criteria]
    #return criteria
    return filtered_df
    
 


app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'someRandomKey'


# REMEMBER TO LOAD THE MODEL AND THE SCALER!
#flower_model = load_model('final_iris_model.h5')
#flower_scaler = joblib.load('iris_scaler.pkl')
#df = pd.read_csv('D:\GitHub\Projeto_D3TOP\Datasets\processed\dataset_airbnb-processed-relevant_words_2023-04-13_03-28-09-439.csv')
#df = pd.read_csv('D:\GitHub\Projeto_D3TOP\Datasets\processed\dataset_airbnb-processed-spacy_2023-04-13_03-28-09-439.csv')
df = pd.read_csv('D:\GitHub\Projeto_D3TOP\Datasets\processed\dataset_airbnb-processed-summary_2023-04-13_03-28-09-439.csv')

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class PropertyForm(FlaskForm):
    guest_no = IntegerField('Max Number of Guests:')
    price_max = IntegerField('Max Price (per night in US$):')
    price_min = IntegerField('Min Price (per night in US$):')
    room_type = StringField('Property Type:')
    core_attr = StringField('Type One or More Core Attributes of the Property (separated by comma):')

    submit = SubmitField('Analyze')



@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = PropertyForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['guest_no'] = form.guest_no.data
        session['price_max'] = form.price_max.data
        session['price_min'] = form.price_min.data
        session['room_type'] = request.form['options']
        #session['pet_wid'] = form.pet_wid.data

        return redirect(url_for("prediction"))


    return render_template('home.html', form=form)


@app.route('/prediction')
def prediction():
    #category = request.args.get('category')
    #filter_criteria = str(session['guest_no'])
    #filter_criteria = session['guest_no']
    filter_guest_no = session['guest_no']
    filter_price_max = session['price_max']
    filter_price_min = session['price_min']
    filter_room_type = session['room_type']
    filtered_results = return_prediction(dataframe_full=df,guest_criteria=filter_guest_no,price_max_criteria=filter_price_max,price_min_criteria=filter_price_min,room_criteria=filter_room_type)
    #filtered_results = return_prediction(dataframe=df,criteria=filter_guest_no)
    # Rest of the code to filter the DataFrame based on the category
    #return render_template('prediction.html',tables=[filtered_results.to_html()], titles=[''])
    return render_template('prediction.html',tables=[filtered_results.to_html(escape=False)], titles=[''])
    #return render_template('prediction.html', results=filtered_results)
    return render_template('prediction.html')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)