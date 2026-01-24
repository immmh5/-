import pandas as pd

df = pd.read_csv('day08_events.csv')

df['timestamp'] = pd.to_datetime(df['timestamp'])

event_counts = df['event'].value_counts()
print(event_counts)

daily_events = df.groupby(df['timestamp'].dt.date).size()
print(daily_events)

user_activity = df.groupby('user_id')['event'].count().sort_values(ascending=False)
print(user_activity.head())