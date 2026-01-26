#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def run():
 
    df = pd.read_parquet('./data/green_tripdata_2025-11.parquet')
    zones = pd.read_csv('./data/taxi_zone_lookup.csv')

    df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
    df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])
    
    # ---------------------------------------------------------
    # Question 3: Counting short trips
    # ---------------------------------------------------------
    nov_trips = df[
        (df['lpep_pickup_datetime'] >= '2025-11-01') & 
        (df['lpep_pickup_datetime'] < '2025-12-01')
    ]
    
    short_trips_count = len(nov_trips[nov_trips['trip_distance'] <= 1.0])
    print(f"Question 3: {short_trips_count}")

    # ---------------------------------------------------------
    # Question 4: Longest trip for each day
    # ---------------------------------------------------------
    valid_trips = df[df['trip_distance'] < 100]
    
    # Find the row with the max trip_distance
    max_distance_idx = valid_trips['trip_distance'].idxmax()
    max_trip_row = valid_trips.loc[max_distance_idx]
    
    # Get the day formatted as YYYY-MM-DD
    longest_trip_day = max_trip_row['lpep_pickup_datetime'].strftime('%Y-%m-%d')
    print(f"Question 4: {longest_trip_day}")

    # ---------------------------------------------------------
    # Question 5: Biggest pickup zone
    # ---------------------------------------------------------
    
    target_date = '2025-11-18'
    
    # Filter for that specific day
    daily_trips = df[df['lpep_pickup_datetime'].dt.strftime('%Y-%m-%d') == target_date]
    
    # Group by PULocationID and sum total_amount
    revenue_by_zone = daily_trips.groupby('PULocationID')['total_amount'].sum()
    best_zone_id = revenue_by_zone.idxmax()
    best_zone_name = zones.loc[zones['LocationID'] == best_zone_id, 'Zone'].values[0]
    print(f"Question 5: {best_zone_name}")

    # ---------------------------------------------------------
    # Question 6: Largest tip
    # ---------------------------------------------------------
    
    ehn_id = zones.loc[zones['Zone'] == "East Harlem North", 'LocationID'].values[0]
    ehn_trips = nov_trips[nov_trips['PULocationID'] == ehn_id]
    max_tip_idx = ehn_trips['tip_amount'].idxmax()
    max_tip_row = ehn_trips.loc[max_tip_idx]
    
    do_id = max_tip_row['DOLocationID']
    do_zone_name = zones.loc[zones['LocationID'] == do_id, 'Zone'].values[0]
    print(f"Question 6: {do_zone_name}")

if __name__ == "__main__":
    run()