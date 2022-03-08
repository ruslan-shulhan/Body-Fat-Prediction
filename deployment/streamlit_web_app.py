import streamlit as st

class StreamLit(object):
    """
    This class provides the option to deploy the ML object locally/cloud service
    """
    def __init__(self):
        pass

    def set_title(self, app_title=""):
        """
        Sets the tile of web application
        :param app_title: str - the name of the web application
        :return: None
        """
        st.title(app_title)

        return None

    def set_write(self, app_description=""):
        """
        Sets the description of the web application
        :param app_description: str - description of the web application
        :return: None
        """
        st.write(app_description)

        return None

    def set_slider(self):
        """
        Sets the slider widget
        :return: None
        """
        density = st.slider(label='density', min_value=0.1, max_value=2.0, value=1.0, step=0.1)
        age = st.slider(label='age', min_value=1, max_value=150, value=42, step=1)
        weight_kg = st.slider(label='weight_kg', min_value=10, max_value=350, value=82, step=1)
        height_cm = st.slider(label='height_cm', min_value=1, max_value=250, value=179, step=1)
        neck_cm = st.slider(label='neck_cm', min_value=1, max_value=100, value=34, step=1)
        chest_cm = st.slider(label='chest_cm', min_value=1, max_value=200, value=100, step=1)
        abdomen_cm = st.slider(label='abdomen_cm', min_value=1, max_value=200, value=92, step=1)
        hip_cm = st.slider(label='hip_cm', min_value=1, max_value=200, value=89, step=1)
        thigh_cm = st.slider(label='thigh_cm', min_value=1, max_value=100, value=50, step=1)
        knee_cm = st.slider(label='knee_cm', min_value=1, max_value=80, value=38, step=1)
        ankle_cm = st.slider(label='ankle_cm', min_value=1, max_value=70, value=23, step=1)
        biceps_cm = st.slider(label='biceps_cm', min_value=1, max_value=90, value=33, step=1)
        forearm_cm = st.slider(label='forearm_cm', min_value=1, max_value=70, value=33, step=1)
        wrist_cm = st.slider(label='wrist_cm', min_value=1, max_value=70, value=18, step=1)

        return None

