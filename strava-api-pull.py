import requests
import json
import pandas as pd
from decouple import config

base_url = 'https://www.strava.com/api/v3//athlete/activities'
auth_token = ''
headers = {'Authorization': f'access_token {auth_token}'}
params = {'per_page':200}

def main():
    activity_list = call_api()
    # post_token()
    retrieve_insights(activity_list)


def retrieve_insights(activity_list):
    df = pd.DataFrame(activity_list, columns = ['id', 'name', 'distance', 'moving_time', 'elapsed_time', 'total_elevation_gain', 'type', 'sport_type', 
                                                'achievement_count', 'athlete_count', 'start_date', 'average_speed', 'max_speed', 'average_cadence', 
                                                'has_heartrate', 'average_heartrate', 'max_heartrate', 'elev_high', 'elev_low', 'pr_count'])
    df.to_csv('/data/strava-activities.csv')
    print('nothing')

def call_api():
    activity_list = []
    response = requests.get(base_url + '?scope=read_all', headers=headers, params=params)
    data = response.json()
    for activity in data:
        id = activity.get('id', {})
        name = activity.get('name', {})
        distance = activity.get('distance', {}) * 0.00062137
        moving_time = activity.get('moving_time', {}) / 3600
        elapsed_time = activity.get('elapsed_time', {}) / 3600
        total_elevation_gain = activity.get('total_elevation_gain', {})
        type = activity.get('type', {})
        sport_type = activity.get('sport_type', {})
        achievement_count = activity.get('achievement_count', {})
        athlete_count = activity.get('athlete_count', {})
        start_date = activity.get('start_date', {})
        average_speed = activity.get('average_speed', {})
        max_speed = activity.get('max_speed', {})
        average_cadence = activity.get('average_cadence', {})
        has_heartrate = activity.get('has_heartrate', {})
        average_heartrate = activity.get('average_heartrate', {})
        max_heartrate = activity.get('max_heartrate', {})
        elev_high = activity.get('elev_high', {})
        elev_low = activity.get('elev_low', {})
        pr_count = activity.get('pr_count', {})
        
        given_activity = [id, name, distance, moving_time, elapsed_time, total_elevation_gain, type, sport_type, achievement_count, athlete_count,
                            start_date, average_speed, max_speed, average_cadence, has_heartrate, average_heartrate, max_heartrate, elev_high,
                            elev_low, pr_count]
        activity_list.append(given_activity)

    return activity_list


def post_token():
    response = requests.post('https://www.strava.com/oauth/token?client_id=&client_secret=&code=&grant_type=authorization_code')
    print('nothing')


if __name__ == "__main__":
    main()