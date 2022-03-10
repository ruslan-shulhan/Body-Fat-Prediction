from body_fat_prediction_model import BodyFatPrediction
from streamlit_web_app import StreamLit

# CMD command to run app locally: streamlit run main.py
if __name__ == '__main__':
    app_title = 'Body Fat Prediction - Web App'
    app_description = 'This web app can estimate your body fat based on some measurements. \n\n'
    problem_info = app_description + """The scientific term for body fat is "adipose tissue." Adipose tissue serves 
    a number of functions. Its primary purpose is to store lipids from which the body creates energy. In addition, 
    it secretes a number of important hormones, and provides the body with some cushioning as well as insulation.

Body fat includes essential body fat and storage body fat. Essential body fat is a base level of fat that is found in
 most parts of the body. It is necessary fat that maintains life and reproductive functions. The amount of essential
  fat differs between men and women, and is typically around 2-5% in men, and 10-13% in women. The healthy range of
   body fat for men is typically defined as 8-19%, while the healthy range for women is 21-33%. While having excess
    body fat can have many detrimental effects on a person's health, insufficient body fat can have negative health
     effects of its own, and maintaining a body fat percentage below, or even at the essential body fat percentage
      range is a topic that should be discussed with a medical professional."""

    obj_model_bfp = BodyFatPrediction()
    obj_web_app = StreamLit()

    obj_model_bfp.load_model('model/model_BodyFatPrediction_final.sav')

    obj_web_app.set_title(app_title)
    obj_web_app.set_write(problem_info)
    obj_web_app.set_slider()

    if obj_web_app.set_action_button(button_name='Predict'):
        prediction = obj_model_bfp.get_prediction(data_set=obj_web_app.features)
        obj_web_app.set_write(f"Body fat estimation: {round(prediction, 2)}%")
