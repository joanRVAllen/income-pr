# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Imports from this application
from app import app
from joblib import load
pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

column1 = dbc.Col(
    [ #start of column 1
        dcc.Markdown('## Information:', className='nb-5'),
        dcc.Markdown('#### Age'),
        dcc.Slider(
            id='age',
            min=0,
            max=80,
            step=1, #each step of the slider
            value=40, #default value
            marks={n: str(n) for n in range(0,80,10)},
            className='nb-5'
        ), # end of feature

        dcc.Markdown('#### Gender'),
        dcc.Dropdown(
        id='gender',
        options=[
            {'label': 'Male', 'value':1},
            {'label': 'Female', 'value':0}
        ],
        value=1,
        className='nb-5',
        ), #end of feature


        dcc.Markdown('#### Race'),
        dcc.Dropdown(
        id='race',
        options=[
            {'label': 'White', 'value':'White'},
            {'label': 'Black', 'value':'Black'},
            {'label': 'Asian/Pacific Islander', 'value':'Asian-Pac-Islander'},
            {'label': 'American Indian', 'value':'Amer-Indian-Eskimo'},
            {'label': 'Other', 'value':'Other'}
        ],
        value='White',
        className='nb-5'
        ), #end of feature

        dcc.Markdown('#### Highest Education'),
        dcc.Dropdown(
        id='education',
        options=[
            {'label': 'Preschool', 'value':1},
            {'label': '1st-4th Grade', 'value':2},
            {'label': '5th-6th Grade', 'value':3},
            {'label': '7th-8th Grade', 'value':4},
            {'label': '9th Grade', 'value':5},
            {'label': '10th Grade', 'value':6},
            {'label': '11th Grade', 'value':7},
            {'label': '12th Grade', 'value':8},            
            {'label': 'High Shool Graduate', 'value':9},
            {'label': 'Some College', 'value':10},
            {'label': 'Associate-Vocational', 'value':11},
            {'label': 'Associate-Academic', 'value':12},
            {'label': 'Bachelors', 'value':13},
            {'label': 'Masters', 'value':14},
            {'label': 'Professional School', 'value':15},
            {'label': 'Doctorate', 'value':16}
        ],
        value=1,
        className='nb-5'
        ), #end of feature

        dcc.Markdown('#### Marital Status'),
        dcc.Dropdown(
        id='marital',
        options=[
            {'label': 'Married-Spouse Present', 'value':'Married-civ-spouse'},
            {'label': 'Married-Spouse Absent', 'value':'Married-spouse-absent'},
            {'label': 'Married-Spouse in Armed Forces', 'value':'Married-AF-spouse'},
            {'label': 'Never Married', 'value':'Never-married'},
            {'label': 'Divorced', 'value':'Divorced'},
            {'label': 'Widowed', 'value':'Widowed'},
            {'label': 'Saparated', 'value':'Separated'}
        ],
        value='Married-civ-spouse',
        className='nb-5'
        ), #end of feature

        dcc.Markdown('#### Relationship'),
        dcc.Dropdown(
        id='relationship',
        options=[
            {'label': 'Husband', 'value':'Husband'},
            {'label': 'Wife', 'value':'Wife'},
            {'label': 'Unmarried', 'value':'Unmarried'},
            {'label': 'Own Child', 'value':'Own-child'},
            {'label': 'Other relative', 'value':'Other-relative'},
            {'label': 'Not in Family', 'value':'Not-in-family'},
        ],
        value='Husband',
        className='nb-5'
        ), #end of feature

        dcc.Markdown('#### Occupation'),
        dcc.Dropdown(
        id='occupation',
        options=[
            {'label': 'Prof Specialty', 'value':'Prof-specialty'},
            {'label': 'Exec Managerial', 'value':'Exec-managerial'},
            {'label': 'Admin Clerical', 'value':'Adm-clerical'},
            {'label': 'Tech Support', 'value':'Tech-support'},
            {'label': 'Sales', 'value':'Sales'},
            {'label': 'Protective Services', 'value':'Protective-serv'},
            {'label': 'Private House Services', 'value':'Priv-house-serv'},
            {'label': 'Other Services', 'value':'Other-service'},
            {'label': 'Machine Operation', 'value':'Machine-op-inspct'},
            {'label': 'Transportation', 'value':'Transport-moving'},
            {'label': 'Handlers/Cleaners', 'value':'Handlers-cleaners'},
            {'label': 'Farming/Fishing', 'value':'Farming-fishing'},
            {'label': 'Craft/Repair', 'value':'Craft-repair'},
            {'label': 'Armed Forces', 'value':'Armed-Forces'}
        ],
        value='Prof-specialty',
        className='nb-5'
        ), #end of feature

       dcc.Markdown('#### Hours Woked per Week'),
        dcc.Slider(
            id='hours',
            min=0,
            max=100,
            step=1, #each step of the slider
            value=40, #default value
            marks={n: str(n) for n in range(0,100,20)},
            className='nb-5'
        ), # end of feature 


        dcc.Markdown('#### Capital Gain'),
        dcc.Slider(
            id='gain',
            min=0,
            max=100000,
            step=1, #each step of the slider
            value=50000, #default value
            marks={n: str(n) for n in range(0,100000,10000)},
            className='nb-5'
        ), # end of feature

        dcc.Markdown('#### Capital Loss'),
        dcc.Slider(
            id='loss',
            min=0,
            max=100000,
            step=1, #each step of the slider
            value=50000, #default value
            marks={n: str(n) for n in range(0,100000,10000)},
            className='nb-5'
        ), # end of feature

    ] #end of column 1
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
        

        html.H2('Predicted Income', className='nb-5'),
        html.Div(id='prediction', className='lead')
    ],
    md=4,
)# end of column 2

layout = dbc.Row([column1, column2])

@app.callback(
    Output('trial','children'),
    [
        Input('marital','value'),
        Input('loss','value')
    ],
)

def sum(marital,loss):
    su=marital + str(loss)
    return su,

@app.callback(
    Output('prediction', 'children'),
    [
        Input('age', 'value'),
        Input('education', 'value'),
        Input('marital', 'value'),
        Input('occupation', 'value'),
        Input('relationship', 'value'),
        Input('race', 'value'),
        Input('gender', 'value'),
        Input('gain', 'value'),
        Input('loss', 'value'),
        Input('hours', 'value')
    ],
)

def predict(age, education, marital, occupation, relationship, race, gender, gain, loss, hours):
    
    data = [[age, education, marital, occupation, relationship, race, gender, gain, loss, hours]]
    cols = ['age', 'education', 'marital', 'occupation', 'relationship', 'race', 'gender', 'gain',
            'loss', 'hours']
    df = pd.DataFrame(data=data, columns=cols)
    y_pred = pipeline.predict(df)[0]
    if y_pred == 0:
        return 'Predicted income is below $50,000'
    if y_pred == 1:
        return 'Predicted income is above $50,000'
