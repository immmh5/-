import pandas as pd
import time

def clean_chunk(df):
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['income'] = pd.to_numeric(df['income'], errors='coerce')
    return df.dropna(how='all')

def process_large_file(input_path, output_path, chunk_size=100):
    start_time = time.time()
    is_first_chunk = True

    for chunk in pd.read_csv(input_path, chunksize=chunk_size):
        cleaned_data = clean_chunk(chunk)
        
        write_mode = 'w' if is_first_chunk else 'a'
        cleaned_data.to_csv(output_path, mode=write_mode, index=False, header=is_first_chunk)
        
        is_first_chunk = False

    end_time = time.time()
    print(f"Processing finished. Execution time: {end_time - start_time:.2f} seconds.")

input_filename = 'day13_large_users.csv'
output_filename = 'done.csv'

process_large_file(input_filename, output_filename)