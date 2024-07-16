import os
import requests
import json
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import pandas as pd
import vis as vis
import streamlit as st
from datetime import datetime


oura_token = st.secrets["OURA_API_TOKEN"]

def get_oura_data(oura_token, d_type="workout", start_date="2024-06-01", end_date="2024-07-01"):
    url = f'https://api.ouraring.com/v2/usercollection/{d_type}' 
    
    params={ 
        'start_date': start_date, 
        'end_date': end_date
    }
    headers = { 
    'Authorization': f'Bearer {oura_token}' 
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    df = pd.DataFrame(response.json()["data"])
    
    return df


def get_govee_data(file_path="yw_govee.csv"):
    return pd.read_csv(file_path)


# Streamlit App
st.title('User Data Dashboard')

# User selection
users = ['YW', 'User2']
user = st.selectbox('Select User', users)


# Date input
start_date = st.date_input('Start Date', datetime(2024, 6, 11))
end_date = st.date_input('End Date', datetime(2024, 7, 9))

# Data type selection
select_data = st.selectbox('Select Data', ['Oura Sleeping Data', 'Govee Temperature Data'])

api_token = oura_token

# Fetch and display data based on user selection
if select_data == 'Oura Sleeping Data':
    # if st.checkbox('Show all Oura plots'):
        activity = get_oura_data(api_token, "daily_activity", start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        sleep = get_oura_data(api_token, "sleep", start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        d_readiness = get_oura_data(api_token, "daily_readiness", start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

        merged_oura_data = sleep[["day", "average_hrv", "lowest_heart_rate", "total_sleep_duration", "average_breath"]] \
            .merge(d_readiness[["day", "temperature_deviation"]], "left", on="day") \
            .merge(activity[["day", "steps"]], "left", on="day")

        st.plotly_chart(vis.visualize_daily_sleep_time(merged_oura_data))
        st.plotly_chart(vis.visualize_daily_lowest_hr(merged_oura_data))
        st.plotly_chart(vis.visualize_respiratory(merged_oura_data))
        st.plotly_chart(vis.visualize_temperature(merged_oura_data))
        st.plotly_chart(vis.visualize_daily_hrv(merged_oura_data))
        st.plotly_chart(vis.visualize_daily_steps(merged_oura_data))

elif select_data == 'Govee Temperature Data':
    # if st.checkbox('Show all Govee plots'):
        govee_data = get_govee_data()
        st.plotly_chart(vis.visualize_daily_average_temp_humidity(govee_data))
        st.plotly_chart(vis.visualize_govee_temperature(govee_data))
        st.plotly_chart(vis.visualize_govee_humidity(govee_data))