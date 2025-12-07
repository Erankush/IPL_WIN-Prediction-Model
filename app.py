import streamlit as st
import pickle
import pandas as pd
import numpy as np

teams =['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Delhi Capitals',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals']
cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah']

st.title("IPL Win Predictor")
col1,col2 = st.columns(2)

pipe=pickle.load(open('pipe.pkl', 'rb'))

with col1:
    batting_team=st.selectbox("Select Batting Team",sorted(teams))
with col2:
    bowling_team=st.selectbox("Select Bowling Team",sorted(teams))
selected_city=st.selectbox("Select host City",sorted(cities))

target=st.number_input("Select Target")
col3,col4,col5=st.columns(3)
with col3:
    score=st.number_input("Score")
with col4:
    overs=st.number_input("Overs")
with col5:
    wickets= st.number_input("Wickets")
if st.button("Win Probability"):
    runs_left=target-score
    balls_left=120-overs*6
    wickets_left=10-wickets
    crr=(score/overs)*100
    rrr=(runs_left*6)/balls_left



    input_df = pd.DataFrame([{
        "batting_team": batting_team,
        "bowling_team": bowling_team,
        "city": selected_city,
        "runs_left": runs_left,
        "balls_left": balls_left,
        "wickets_left": wickets_left,
        "total_runs_x": target,
        "CRR": crr,
        "RRR": rrr
    }])

    result= pipe.predict_proba(input_df)
    st.text(f"Win Probability of {batting_team}______{np.round((result[0][1])*100,2)}%")
    st.text(f"Win Probability of {bowling_team}______{np.round((result[0][0]) * 100, 2)}%")