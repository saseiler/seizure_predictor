import pandas as pd

def load_patient_activity_data(patient_id):
    
    df_health_data = pd.read_csv(f"P{patient_id} sim.csv").dropna()
    df_processed = df_health_data.drop(columns=['seconds_since_hr_recording', 'index', 'date_time']).reset_index()
    return df_processed

def load_seizure_data(patient_id):

    df_seizure = pd.read_csv(f"P{patient_id}SimDiary.csv")
    return df_seizure