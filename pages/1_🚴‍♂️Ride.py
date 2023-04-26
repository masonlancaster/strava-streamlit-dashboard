import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Ride',
    layout='wide',
    initial_sidebar_state='auto'
)

container = st.container()

with container:
    col1, col2 = st.columns([1, 17])
    with col1:
        st.image('./img/strava-logo-ride.jpg')
    with col2:
        st.title('Ride')

st.divider()

cell_width = 300
cell_height = 300

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('### Ride Activities')
    df = pd.read_csv('./data/strava-activities.csv')
    rides = df.loc[df['sport_type'] == 'Ride']
    st.dataframe(rides)
    st.divider()

with col2:
    st.markdown('### Cumaltive Miles YTD By Month')
    rides_ytd = rides.loc[rides['start_date'] >= '2023-01-01']
    rides_ytd_distances = rides_ytd[['start_date','distance']]
    rides_ytd_distances['start_date'] = pd.to_datetime(rides_ytd_distances['start_date'])
    rides_ytd_distances = rides_ytd_distances.sort_values(by=['start_date'])
    rides_testing = rides_ytd_distances.cumsum()
    rides_ytd_distances['cumsum'] = rides_testing['distance']
    rides_ytd_distances['start_date'] = rides_ytd_distances['start_date'].astype(str)
    rides_ytd_distances['start_date'] = rides_ytd_distances['start_date'].str[:7]
    rides_ytd_distances = rides_ytd_distances[['start_date', 'cumsum']]
    st.line_chart(rides_ytd_distances, x='start_date', y='cumsum')
    st.divider()

with col3:
    st.markdown('### Year To Date Metrics')
    col1, col2, col3 = st.columns(3)
    total_rides_ytd = rides_ytd.shape[0]
    col1.metric("Rides YTD", str(total_rides_ytd))
    total_distance_ytd = int(round(rides_ytd['distance'].sum(), 0))
    col2.metric("Distance YTD", str(total_distance_ytd) + ' mi')
    longest_ride_ytd = rides_ytd.loc[rides_ytd['distance'].idxmax()]
    longest_ride_distance = int(round(longest_ride_ytd['distance'], 0))
    col3.metric("Longest Ride YTD", str(longest_ride_distance) + ' mi')
    st.divider()