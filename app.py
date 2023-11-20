import numpy as np
import pandas as pd
import pickle 
import streamlit as st

pickle_a=open("random_forest_model_weights.pkl","rb")
regressor=pickle.load(pickle_a) # our model

def predict_range(time travelled,Speed,battery degraded):
    prediction=regressor.predict([[time travelled,Speed,battery degraded]]) #predictions using our model
    return prediction 


def main():
    st.title("Range prediction for B1001BlackRedv5 ") #simple title for the app
    html_temp="""
        <div>
        <h2>Range prediction for B1001BlackRedv5</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    time travelled=st.text_input("time travelled")
    Speed=st.text_input("Speed")
    battery degraded=st.text_input("battery degraded") #giving inputs as used in building the model
    result=""
    if st.button("Predict"):
        result=predict_chance(time travelled,Speed,battery degraded) #result will be displayed if button is pressed
    st.success("Predicted range{}".format(result))
        
if __name__=='__main__':
    main()