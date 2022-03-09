import pickle
import pandas as pd

class BodyFatPrediction(object):
    """
    This class represents the instance of Linear Regression model
    """
    def __init__(self, built_model=None):
        self.model_obj = built_model

    def load_model(self, path_to_model=""):
        """
        Loading the model from the provided path and saving as instance of this class
        :param path_to_model: str - relative path to the existing model from the root folder
        :return: bool - true if there were no issues of loading the model otherwise false
        """
        loaded_model = pickle.load(open(path_to_model, 'rb'))
        self.model_obj = loaded_model

        return True

    def get_prediction(self, data_set):
        """
        Estimates the value based on the provided values
        :param data_set: dict - set of features to be used for model prediction
        :return: float - the predicted value based on the provided information
        """
        data_set_df = pd.DataFrame(data_set)
        predictions = self.model_obj.predict(data_set_df.values)

        return predictions[0]