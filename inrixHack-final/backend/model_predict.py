import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def model_predict(y, model):
    model = pickle.load(open(model, 'rb'))
    pred = model.predict(y)
    return pred
