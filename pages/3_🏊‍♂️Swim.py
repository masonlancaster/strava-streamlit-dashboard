import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Swim',
    layout='wide',
    initial_sidebar_state='auto'
)

container = st.container()

with container:
    col1, col2 = st.columns([1, 17])
    with col1:
        st.image('./img/strava-logo.png')
    with col2:
        st.title('Swim')

st.divider()

cell_width = 300
cell_height = 300

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('### Swim Activities')
    df = pd.read_csv('./data/strava-activities.csv')
    swims = df.loc[df['sport_type'] == 'Swim']
    st.dataframe(swims)
    st.divider()

with col2:
    st.markdown('### Cumaltive Miles By Year/Month')
    swim_distances = swims[['start_date','distance']]
    swim_distances['start_date'] = pd.to_datetime(swim_distances['start_date'])
    swim_distances = swim_distances.sort_values(by=['start_date'])
    swim_distances['start_date'] = swim_distances['start_date'].astype(str)
    swim_distances['start_date'] = swim_distances['start_date'].str[:7]
    st.line_chart(swim_distances, x='start_date', y='distance')
    st.divider()

with col3:
    st.markdown('### Year To Date Metrics')
    col1, col2, col3 = st.columns(3)
    total_rides_ytd = swims.shape[0]
    col1.metric("Total Swims", str(total_rides_ytd))
    total_distance = int(round(swims['distance'].sum(), 0))
    col2.metric("Distance", str(total_distance) + ' mi')
    longest_swim = swims.loc[swims['distance'].idxmax()]
    longest_swim_distance = round(longest_swim['distance'], 2)
    col3.metric("Longest Swim", str(longest_swim_distance) + ' mi')
    st.divider()