import streamlit as st
import pandas as pd

class StreamLit(object):
    """
    Class provides the option to deploy the ML object locally or on cloud service. Some permission for cloud service
    is required
    """
    def __init__(self):
        """
        Initializer of class related attributes
        """
        self.features = {}

    def set_title(self, app_title=""):
        """
        Sets the tile
        :param app_title: str - the title of the web application
        :return: bool - true if everything went right otherwise false
        """
        try:
            st.title(app_title)

            return True
        except:
            return False

    def set_write(self, app_description=""):
        """
        Sets the description of the web application
        :param app_description: str - description of the web application
        :return: bool - true if everything went right otherwise false
        """
        try:
            st.write(app_description)

            return True
        except:
            return False

    def set_slider(self):
        """
        Sets the slider widget with all applicable actions including the range, type, and default values
        :return: bool - true if everything went right otherwise false
        """
        try:
            self.features['density'] = [st.slider(label='density', min_value=0.1, max_value=2.0, value=1.0, step=0.1)]
            self.features['age'] = [st.slider(label='age', min_value=1, max_value=150, value=42, step=1)]
            self.features['weight_kg'] = [st.slider(label='weight_kg', min_value=10, max_value=350, value=82, step=1)]
            self.features['height_cm'] = [st.slider(label='height_cm', min_value=1, max_value=250, value=179, step=1)]
            self.features['neck_cm'] = [st.slider(label='neck_cm', min_value=1, max_value=100, value=34, step=1)]
            self.features['chest_cm'] = [st.slider(label='chest_cm', min_value=1, max_value=200, value=100, step=1)]
            self.features['abdomen_cm'] = [st.slider(label='abdomen_cm', min_value=1, max_value=200, value=92, step=1)]
            self.features['hip_cm'] = [st.slider(label='hip_cm', min_value=1, max_value=200, value=89, step=1)]
            self.features['thigh_cm'] = [st.slider(label='thigh_cm', min_value=1, max_value=100, value=50, step=1)]
            self.features['knee_cm'] = [st.slider(label='knee_cm', min_value=1, max_value=80, value=38, step=1)]
            self.features['ankle_cm'] = [st.slider(label='ankle_cm', min_value=1, max_value=70, value=23, step=1)]
            self.features['biceps_cm'] = [st.slider(label='biceps_cm', min_value=1, max_value=90, value=33, step=1)]
            self.features['forearm_cm'] = [st.slider(label='forearm_cm', min_value=1, max_value=70, value=33, step=1)]
            self.features['wrist_cm'] = [st.slider(label='wrist_cm', min_value=1, max_value=70, value=18, step=1)]

            self.convert_feature_to_df(self.features)

            return True
        except:
            return False



    def convert_feature_to_df(self, feature_dict):
        """
        Converts dictionary into DataFrame for further analysis
        :param feature_dict: dict - dictionary obejct to be converted into DF
        :return: bool - true if everything went right otherwise false
        """
        try:
            features_df = pd.DataFrame(feature_dict)
            st.table(features_df)

            return True
        except:
            return False

    def set_action_button(self, button_name=""):
        """
        Activates the action button on web page to send the form to backend for further analysis
        :param button_name: str - the name of activation button
        :return: obj/None - the object of activation button otherwise the None value
        """
        try:

            return st.button(label=button_name)
        except:
            return None

