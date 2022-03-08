from body_fat_prediction_model import BodyFatPrediction
from streamlit_web_app import StreamLit

# import sklearn
# import numpy as np
# import pandas as pd

def get_input():
    user_input = [[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]]

    return user_input


if __name__ == '__main__':
    app_title = 'Body Fat Prediction - Web App'
    app_description = 'This web app can estimate your body fat based on some measurements'

    obj_model_bfp = BodyFatPrediction()
    obj_web_app = StreamLit()

    model_bfp = obj_model_bfp.load_model('model/model_BodyFatPrediction_final.sav')
    user_input = get_input()

    obj_web_app.set_title(app_title)
    obj_web_app.set_write(app_description)
    obj_web_app.set_slider()


    # print(model_bfp.predict(user_input))
