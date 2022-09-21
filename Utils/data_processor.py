import pandas as pd
import math

def generate_timestamp(integer):
        integer = math.floor(integer)
        return list(range(integer-1, integer+3))
    
def process_data(df_health_data, df_seziure):
    
    df_seziure = df_seziure['0'].values.tolist()
    seizure_time = []
    for data in df_seziure:
        seizure_time = seizure_time+ generate_timestamp(data)
    
    bool_seizure = df_health_data['index'].isin(seizure_time)
    assert(len(bool_seizure)==len(df_health_data))
    processed_df = pd.merge(df_health_data, bool_seizure, left_index=True, right_index=True)
    return processed_df