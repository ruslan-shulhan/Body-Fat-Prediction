import pickle

class BodyFatPrediction(object):
    """
    This class represents the Linear Regression model
    """
    def __init__(self, built_model=None):
        self.model_obj = built_model

    def load_model(self, path_to_model=""):
        """
        Loading the model.
        :param path_to_model: str - relative path to the existing model
        :return: obj - Linear Regression Object
        """
        loaded_model = pickle.load(open(path_to_model, 'rb'))
        self.model_obj = loaded_model

        return loaded_model