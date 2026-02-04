import pandas as pd


df = pd.read_csv('day12_users.csv')

def standardize_city(city_name):
    if pd.isna(city_name):
        return "Unknown"
    
    c = str(city_name)
    c = c.strip()
    c = c.lower()
    import re
    c = re.sub(r'[!,-]', ' ', c)
    c = " ".join(c.split())
    
    if c in ['nyc', 'new york']:
        return 'new york'
    if c in ['san francisco', 'sf']:
        return 'san francisco'
        
    return c


df['city_cleaned'] = df['city'].apply(standardize_city)


def parse_and_localize(df):
    df['signup_time_clean'] = pd.to_datetime(df['signup_time'], errors='coerce')

    df['signup_time_clean'] = df['signup_time_clean'].dt.tz_localize(None).dt.tz_localize('UTC')
    
    return df



df = parse_and_localize(df)


print("done")
print(df[['city', 'city_cleaned', 'signup_time', 'signup_time_clean']])

print("\n datatayp")
print(df.dtypes)