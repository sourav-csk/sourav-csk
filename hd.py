import pickle
import pandas as pd   
import numpy as np   
import matplotlib.pyplot as plt   
      
import plotly_express as px    
from PIL import Image
import seaborn as sns 
import streamlit as st 
import altair as alt
import random
from streamlit_option_menu import option_menu 

#loading the saved model 

heart_disease_model = pickle.load(open('D:/python program project/Heart disease predictions/saved model/heart_disease_model.sav','rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu(
               menu_title="Disease Prediction System",
                           
                          
                          options=['Heart Disease Prediction'],
                          icons=['heart'],
                          orientation='horizontal',
                          default_index=0)
    


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
# creating a button for graphical Prediction
if st.button('Heart Test Graphical Result'):
    st.title('Visualization plots using Facts & DataSet')
    heart_data = pd.read_csv('D:\MCA PROJECT\MDPS\Dataset\heart.csv')
    st.dataframe(heart_data)
    
    
    st.title('Visualization plots using Age DataSet')
    fig1 = plt.figure()
    heart_data['age'].value_counts().plot(kind= 'bar')
    st.pyplot(fig1)
    
    st.title('Visualization plots using Age,Sex,Target DataSet')
    st.line_chart(heart_data[['age','sex','target']])
    
    st.title('Visualization plots using age & sex dataset')
    st.area_chart(heart_data[['age','sex']])
    
    st.dataframe(heart_data.head())




