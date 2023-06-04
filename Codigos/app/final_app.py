from flask import Flask, render_template, session, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired, Length

#import numpy as np  
#from tensorflow.keras.models import load_model
#import joblib
import pandas as pd
import torch
from transformers import BertTokenizer, BertModel
from sklearn.preprocessing import StandardScaler


# REMEMBER TO LOAD THE MODEL AND THE SCALER!
#flower_model = load_model('final_iris_model.h5')
#flower_scaler = joblib.load('iris_scaler.pkl')
#df = pd.read_csv('D:\GitHub\Projeto_D3TOP\Datasets\processed\dataset_airbnb-processed-relevant_words_2023-04-13_03-28-09-439.csv')
#df = pd.read_csv('D:\GitHub\Projeto_D3TOP\Datasets\processed\dataset_airbnb-processed-spacy_2023-04-13_03-28-09-439.csv')
#df = pd.read_csv('D:\GitHub\Projeto_D3TOP\Datasets\processed\dataset_airbnb-processed-summary_2023-04-13_03-28-09-439.csv')

file_path = 'https://media.githubusercontent.com/media/HWatanuki/Projeto_D3TOP/main/Datasets/processed/'
file_name = 'dataset_airbnb-processed-summary_2023-04-13_03-28-09-439.csv'
df = pd.read_csv(file_path + file_name)

# Loading pre-trained bert
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)



## Function to use BERT and calcule cosine similarity for each text variable
def fn_encode_covs_txt(cov, df, dic):
    #print(cov)
    
    # Creating the corpus
    vocabulary =list(df[cov].fillna('').values)
    #print(vocabulary[:3])
    #print(dicionario[cov])
    vocabulary.append(dic[cov])
    #print(vocabulary)
    #print(type(vocabulary))

    # Coding the query and recommended items
    encoded_inputs = tokenizer(vocabulary, padding=True, truncation=True, return_tensors='pt')
    #print(encoded_inputs)
    # Getting the text representations
    with torch.no_grad():
        outputs = model(**encoded_inputs)
        query_embeddings = outputs.last_hidden_state[0, 0, :]  # Query representation
        item_embeddings = outputs.last_hidden_state[1:, 0, :]  # Representations of recommended items
    #print('hello')
    # Calculating the cosine similarity
    cosine_similarity = torch.nn.functional.cosine_similarity(query_embeddings.unsqueeze(0), item_embeddings, dim=1)

    return(cosine_similarity)


def return_prediction(dataframe_full,guest_criteria,price_max_criteria,price_min_criteria,room_criteria,sim_criteria):
    #unused_columns = ['isAvailable','isHostedBySuperhost','location/lat','location/lng','photos/0/caption','photos/0/pictureUrl',]
    #dataframe = dataframe.drop(unused_columns, axis=1)
    dataframe_full['thumbnail'] = dataframe_full['photos/0/thumbnailUrl'].apply(lambda x: '<img src="{}"/>'.format(x) if x else '')
    #dataframe_full['url'] = '<a href="' + dataframe_full['url'] + '">' + dataframe_full['url'] + '</a>'
    dataframe_full['url'] = '<a href="' + dataframe_full['url'] + '"> Click here </a>'
    #dataframe = dataframe_full[['address','name','stars','numberOfGuests','roomType','pricing/rate/amount','thumbnail','url','comments_list','summary']]
    dataframe = dataframe_full[['address','name','stars','numberOfGuests','roomType','pricing/rate/amount','thumbnail','url','summary']]
    #numeric_cols = ['numberOfGuests','pricing/rate/amount']
    #numeric_cols = ['numberOfGuests']
    #dataframe[numeric_cols] = dataframe[numeric_cols].apply(pd.to_numeric, errors='coerce', axis=1)
    filtered_df = dataframe[(dataframe['numberOfGuests'] <= guest_criteria) & (dataframe['pricing/rate/amount'] <= price_max_criteria) & (dataframe['pricing/rate/amount'] >= price_min_criteria) & (dataframe['roomType'].str.contains(room_criteria, case=False))]
    #filtered_df = dataframe
    #print(type(guest_criteria))
    #print(type(price_max_criteria))
    #print(type(price_min_criteria))
    #print(type(room_criteria))
    #print(type(sim_criteria))
    #filtered_df = dataframe[dataframe['numberOfGuests'] == criteria]
    #return criteria
    
    # Covariates to be used in the model
    #covs = ['address', 'numberOfGuests', 'name', 'pricing/rate/amount', 'roomType', 'stars', 'summary']
    covs = ['numberOfGuests', 'pricing/rate/amount', 'roomType', 'stars', 'summary']
    #covs = ['stars', 'summary']
    #covs = ['summary']
    covs_num = ['numberOfGuests', 'pricing/rate/amount', 'stars']
    covs_txt =  [c for c in covs if c not in covs_num]
    
    
    #chamar fn_encode for all covs_txt
    #user_input = [5, 'comfortable']
    #user_input = ['near']
    #user_input = ['Jersey', 6, 'near', 300, 'Entire', 4.5, sim_criteria]
    user_input = [guest_criteria, round((price_max_criteria + price_min_criteria)/2), room_criteria, 5, sim_criteria]
    input_dict = dict(zip(covs, user_input))
    print(input_dict)

    cosine_similarity = list(map(lambda x: fn_encode_covs_txt(x, filtered_df, input_dict), covs_txt))

    # Normalizing the numeric covariates
    scaler = StandardScaler()
    covs_scaled = scaler.fit_transform(filtered_df[covs_num])
    normalized_covariates = torch.tensor(covs_scaled)

    # Incorporating all cosines into the similarity
    prd = cosine_similarity[0]
    for c in cosine_similarity[1:]:
        prd = prd * c 

    # Incorporating the covariates into the similarity
    weighted_similarity = prd * normalized_covariates.prod(dim=1)

    # Ranking recommended items based on weighted similarity
    #df_result = filtered_df.copy()
    #df_result['similarity'] = weighted_similarity
    df_sim = filtered_df.copy()
    df_sim['similarity'] = weighted_similarity
    df_result = df_sim[['address','name','stars','numberOfGuests','roomType','pricing/rate/amount','thumbnail','url','similarity']]

    return df_result.sort_values('similarity', ascending=False)
    
 


app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'someRandomKey'

# Flask-Bootstrap requires this line
Bootstrap(app)

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class PropertyForm(FlaskForm):
    guest_no = IntegerField('Max Number of Guests:')
    price_max = IntegerField('Max Price:', render_kw={"placeholder": "per night in US$"})
    price_min = IntegerField('Min Price:', render_kw={"placeholder": "per night in US$"})
    room_type = StringField('Property Type:')
    core_attr = StringField('Core Attributes of the Property:', render_kw={"placeholder": "Type One or More separated by comma"})

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
        session['core_attr'] = form.core_attr.data

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
    filter_core_attr = session['core_attr']
    #user_input = [filter_core_attr, 5, filter_core_attr]
    #user_similarity = ['near', 5, 'comfortable']
    #user_similarity = 'comfortable'
    
    filtered_results = return_prediction(dataframe_full=df,guest_criteria=filter_guest_no,price_max_criteria=filter_price_max,price_min_criteria=filter_price_min,room_criteria=filter_room_type,sim_criteria=filter_core_attr)
    #filtered_results = return_prediction(dataframe_full=df,guest_criteria=filter_guest_no,price_max_criteria=filter_price_max,price_min_criteria=filter_price_min,room_criteria=filter_room_type,sim_criteria='comfortable')
    #filtered_results = return_prediction(dataframe=df,criteria=filter_guest_no)
    # Rest of the code to filter the DataFrame based on the category
    #return render_template('prediction.html',tables=[filtered_results.to_html()], titles=[''])
    return render_template('prediction.html',tables=[filtered_results.to_html(escape=False)], titles=[''])
    #return render_template('prediction.html', results=filtered_results)
    #return render_template('prediction.html')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)