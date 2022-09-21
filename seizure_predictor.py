import pandas as pd
import sys
import pickle

from Utils.data_loader import load_patient_activity_data, load_seizure_data
from Utils.data_processor import process_data
from model import classifier, oversampler


if __name__ == '__main__':

    mode = sys.argv[1]

    if mode == 'train':
        train_files_count = int(sys.argv[2])
        
        patient_data_merged = pd.DataFrame()

        for patient_id in range(1, train_files_count+1):
            health_data = load_patient_activity_data(patient_id)
            seizure_data = load_seizure_data(patient_id)

            print("Processing Patient", patient_id, "data.....")
            df = process_data(health_data, seizure_data)
            patient_data_merged = pd.concat([patient_data_merged, df], axis=0)

        print("Training Model....")
        #Oversample data
        x_train, y_train = oversampler(patient_data_merged)
        model = classifier(X=x_train, Y=y_train)
        filename = 'finalized_model.sav'
        pickle.dump(model, open(filename, 'wb'))

    if mode == 'predict':

        filename = sys.argv[2]
        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))

        # load data from the disk
        print("Loading Test data.....")

        health_data = load_patient_activity_data(patient_id)

        prediction_result = loaded_model.predict(patient_data_merged)
        print(prediction_result)
        ##TODO - if prediction result has true values send alert.