import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Hike',
    layout='wide',
    initial_sidebar_state='auto'
)

container = st.container()

with container:
    col1, col2 = st.columns([1, 17])
    with col1:
        st.image('./img/strava-logo-run.png')
    with col2:
        st.title('Hike')

st.divider()

cell_width = 300
cell_height = 300

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('### Hike Activities')
    df = pd.read_csv('./data/strava-activities.csv')
    hikes = df.loc[df['sport_type'] == 'Hike']
    st.dataframe(hikes)
    st.divider()

with col2:
    st.markdown('### Cumaltive Miles By Year/Month')
    hike_distances = hikes[['start_date','distance']]
    hike_distances['start_date'] = pd.to_datetime(hike_distances['start_date'])
    hike_distances = hike_distances.sort_values(by=['start_date'])
    hike_distances['start_date'] = hike_distances['start_date'].astype(str)
    hike_distances['start_date'] = hike_distances['start_date'].str[:7]
    st.line_chart(hike_distances, x='start_date', y='distance')
    st.divider()

with col3:
    st.markdown('### Year To Date Metrics')
    col1, col2, col3 = st.columns(3)
    total_hikes_ytd = hikes.shape[0]
    col1.metric("Total Hikes", str(total_hikes_ytd))
    total_distance = int(round(hikes['distance'].sum(), 0))
    col2.metric("Distance", str(total_distance) + ' mi')
    longest_hike = hikes.loc[hikes['distance'].idxmax()]
    longest_hike_distance = int(round(longest_hike['distance'], 0))
    col3.metric("Longest Hike", str(longest_hike_distance) + ' mi')
    st.divider()