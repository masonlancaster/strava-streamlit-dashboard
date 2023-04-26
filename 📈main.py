import streamlit as st
import pandas as pd


# Set page configuration using Streamlit's set_page_config()
st.set_page_config(
    page_title='Strava Performance Analysis Dashboard',
    layout='wide',
    initial_sidebar_state='auto'
)

# Create a container to hold the streamlit layout
container = st.container()

# Add a title to the container
with container:
    col1, col2 = st.columns([1, 17])
    with col1:
        st.image('./img/strava-logo.png')
    with col2:
        st.title('Strava Performance Analysis Dashboard')

st.markdown('---')

st.markdown('### All Activites')
df = pd.read_csv('./data/strava-activities.csv')
rides = df.loc[df['sport_type'] == 'Ride']
st.dataframe(rides)
st.divider()