from collections import OrderedDict

import numpy as np
from joblib import load


class MlModel:
    def __init__(self, path, feature_set):
        self.model = load(path)
        self.feature_set = feature_set

    def predict(self, data):
        self.validate_input(data)
        preprocessed_data = self.pre_process(data)
        pred = self.model.predict(preprocessed_data)
        return self.humanize(pred)

    def pre_process(self, data):
        return data

    @staticmethod
    def validate_input(data):
        pass

    def humanize(self, prediction):
        return prediction


class CovidModel(MlModel):
    @staticmethod
    def validate_input(data):
        if not isinstance(data, dict):
            raise TypeError('Expected a dictionary')

    def pre_process(self, data):
        data = OrderedDict([(key, data[key]) for key in self.feature_set])
        return np.array(list(data.values())).reshape(1, -1)

    def humanize(self, prediction):
        mask_pos_neg = {1: 'Positive', 0: 'Negative'}
        return mask_pos_neg.get(prediction[0])
