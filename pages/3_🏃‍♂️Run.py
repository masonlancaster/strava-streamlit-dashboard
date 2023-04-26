import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Run',
    layout='wide',
    initial_sidebar_state='auto'
)

container = st.container()

with container:
    col1, col2 = st.columns([1, 17])
    with col1:
        st.image('./img/strava-logo-run.png')
    with col2:
        st.title('Run')

st.divider()

cell_width = 300
cell_height = 300

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('### Run Activities')
    df = pd.read_csv('./data/strava-activities.csv')
    runs = df.loc[df['sport_type'] == 'Run']
    st.dataframe(runs)
    st.divider()

with col2:
    st.markdown('### Cumaltive Miles YTD By Month')
    runs_ytd = runs.loc[runs['start_date'] >= '2023-01-01']
    runs_ytd_distances = runs_ytd[['start_date','distance']]
    runs_ytd_distances['start_date'] = pd.to_datetime(runs_ytd_distances['start_date'])
    runs_ytd_distances = runs_ytd_distances.sort_values(by=['start_date'])
    runs_testing = runs_ytd_distances.cumsum()
    runs_ytd_distances['cumsum'] = runs_testing['distance']
    runs_ytd_distances['start_date'] = runs_ytd_distances['start_date'].astype(str)
    runs_ytd_distances['start_date'] = runs_ytd_distances['start_date'].str[:7]
    rides_ytd_distances = runs_ytd_distances[['start_date', 'cumsum']]
    st.line_chart(rides_ytd_distances, x='start_date', y='cumsum')
    st.divider()

with col3:
    st.markdown('### Year To Date Metrics')
    col1, col2, col3 = st.columns(3)
    total_rides_ytd = runs_ytd.shape[0]
    col1.metric("Runs YTD", str(total_rides_ytd) + ' runs')
    total_distance_ytd = int(round(runs_ytd['distance'].sum(), 0))
    col2.metric("Distance YTD", str(total_distance_ytd) + ' mi')
    longest_run_ytd = runs_ytd.loc[runs_ytd['distance'].idxmax()]
    longest_run_distance = int(round(longest_run_ytd['distance'], 0))
    col3.metric("Longest Run YTD", str(longest_run_distance) + ' mi')
    st.divider()