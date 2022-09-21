from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier

def oversampler(df_train):

    ros = RandomOverSampler(random_state=42)
    print(df_train.columns)
    # fit predictor and target variable
    x_ros, y_ros = ros.fit_resample(df_train.drop(columns=['index_x', 'index_y']), df_train['index_y'])
    return x_ros, y_ros

def classifier(X, Y):
    clf = RandomForestClassifier()
    clf.fit(X, Y)
    return clf
