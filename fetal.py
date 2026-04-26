import pandas as pd
import numpy as np
import joblib
import streamlit as st
from streamlit_option_menu import option_menu
import base64
from PIL import Image

#LOAD MODELS


#GUI Creation - PAGE SETUP

st.set_page_config(page_title='Maternal & Fetal Risk Predictor', layout='wide', page_icon='')
st.title('Maternal and Fetal Risk Prediction System')
image_banner = Image.open('dataset_cover.png')
st.image(image_banner)

st.markdown("<p style='font-weight:bold;'>About</p>", unsafe_allow_html=True)
st.write('This app predict likelyhood of maternal risk level during pregnacy and fetal health assessment based on the clinical data'
         'A Maternal and Fetal Risk Prediction System structured around maternal, fetal, and newborn assessment provides a continuous framework for identifying health risks across pregnancy and early life.')

col1, col2 = st.columns([1, 18])  # adjust ratio as needed

with col1:
    st.image("elisha.png", width=50)  # replace with your image file
with col2:
    st.caption('®Developed by Dr. Elisha Magobo | @2026 | Machine Learning Project | University of Warwick')
    st.markdown("<p style='font-weight:bold;'>®Developed by Dr. Elisha Magobo | @2026 | Machine Learning Project | University of Warwick</p>", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    selected = option_menu('Maternal and Fetal Health Prediction', 
                           ['Maternal Health Assessment', 'Fetal Health Assessment', 'Neonatal Health Assessment'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)


# ====================
#MATERNAL MODEL
# ====================
if selected == 'Maternal Health Assessment':
    st.header('Maternal Risk Prediction')
  
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.number_input('Age of the Pregnant mother', 18, 70, 30)
        SystolicBP = st.number_input('Systolic Blood Pressure(mmHg)', 90, 160, 120)
        DiastolicBP = st.number_input('Diastolic Blood Pressure(mmHg)', 60, 100, 90)

    
    with col2:
        BS = st.number_input('Blood Sugar Level(mg/dL)',5.0, 28.0, 15.6 )
        BodyTemp = st.number_input('Body Temperature (˚C))',25, 41, 38)
        HeartRate = st.number_input('Maximum Heart Rate', 60, 220, 135) 

    if st.button('Predict Maternal Risk Level'):
        maternal_features = np.array([[Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate]])
    prediction = maternal_model.predict(maternal_features)[0]
    if prediction == 0:
        st.success('Low Risk: Continue routine antenatla care')
    
    elif prediction == 1:
        st.warning('Moderate Risk: Monitor closely and consult a healthcare provider/Medical Doctor')
    
    elif prediction == 2:
        st.error('High Risk: Refer the mother to a Medical doctor Immediately')

    else:
        st.write('Unexpected prediction result.')

#=======================
#FETAL MODEL
# ======================

elif selected == 'Fetal Health Assessment':
    st.header('Fetal Health Classification')
    col1, col2, col3 = st.columns(3)
    with col1:
        baseline_value = st.number_input('Baseline Values', 0, 10, 2)
        accelerations = st.number_input('Fetal Acceleration', 2, 15, 10)
        fetal_movement = st.number_input('Fetal Movement', 20, 40, 20)
        uterine_contractions = st.number_input('Periodic Uterine Contractions', 0.0, 0.09, 0.05)
        light_decelerations = st.number_input('Light Decelerations', 0.0, 0.09, 0.01)
        abnormal_short_term_variability = st.number_input('Abnormal Short Term Variability', 0.0, 1.9, 1.2)

    with col2:
        mean_value_of_short_term_variability = st.number_input('Mean Value of Short Term Variability', 0, 10, 2)
        percentage_of_time_with_abnormal_long_term_variability = st.number_input('Time Percentage with Abnormal Term Variability', 2, 15, 10)
        mean_value_of_long_term_variability = st.number_input('Mean Value of Long Term Variability', 0, 10, 2)
        histogram_width = st.number_input('Histogram Width (mm)', 0.0, 0.09, 0.02)
        histogram_min = st.number_input('Histogram Minimum Value', 0.0, 0.09, 0.03)
        histogram_max = st.number_input('Histogram Maximu Value', 0.0, 0.09, 0.07)

    with col3:
        histogram_number_of_peaks = st.number_input('Histogram Peaks Number', 60, 190, 150)
        histogram_mode = st.number_input('Histogram Mode', 70, 180, 89)
        histogram_mean = st.number_input('Histogram Average', 90, 180, 100)
        histogram_median = st.number_input('Histogram Median', 70, 170, 77)
        histogram_variance = st.number_input('Histogram Variance', 0, 80, 50)
        histogram_tendency = st.number_input('Histogram Tendency', 70, 180, 89)


    if st.button('Predict Fetal Health'):
        fetal_features = np.array([[
        'baseline value', 'accelerations', 'fetal_movement',
       'uterine_contractions', 'light_decelerations',
       'abnormal_short_term_variability',
       'mean_value_of_short_term_variability',
       'percentage_of_time_with_abnormal_long_term_variability',
       'mean_value_of_long_term_variability', 'histogram_width',
       'histogram_min', 'histogram_max', 'histogram_number_of_peaks',
       'histogram_mode', 'histogram_mean', 'histogram_median',
       'histogram_variance', 'histogram_tendency']])
    

    prediction = fetal_model.predict(fetal_features)[0]
    if prediction == 0:
        st.success('Normal: Continue routine antenatal care')
    
    elif prediction == 1:
        st.warning('Suspect: Monitor closely and consult a Medical Doctor')
    
    elif prediction == 2:
        st.error('Pathological: Refer the mother to a Gynaecologist Immediately')

    else:
        st.write('Unexpected prediction result.')

# ===============
# NEONATAL MODEL
# ===============

if selected == 'Neonatal Health Assessment':
    st.header('Neonatal Risk Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox('Gender of the Baby:', ['Male', 'Female'])
        gestational_age_weeks  = st.number_input('Gestational age at birth in Weeks', 20, 42, 35)
        birth_weight_kg = st.number_input('Birth Weight in Kg:', 0.5, 5.0, 3.2)
        birth_length_cm = st.number_input('Length at Birth in cm:', 30.0, 60.0, 35.9)
        birth_head_circumference_cm = st.number_input('Head circumference at birth in cm:', 20, 40, 33)
        age_days = st.number_input('Age of Baby in days since Birth:', 0, 60, 12)
        weight_kg = st.number_input('Daily Updated weight (gram/day): 20, 35, 22')

    
    with col2:
        lenght_cm = st.number_input('Daily Updated body lenght in cm:', 40, 60, 45)
        head_circumference_cm  = st.number_input('Daily updated head circumference:', 30, 45, 30)
        temperature_c  = st.number_input('Body temperature in °C', 30.0, 41.0, 36.8)
        heart_rate_bpm = st.number_input('Heart Rate:', 90, 160, 120)
        respiratory_rate_bpm = st.number_input('Breathing Rate (breaths/min):', 30, 70, 55)
        oxygen_saturation = st.number_input('SpO₂ level (%):', 50, 100, 95)
        feeding_type = st.selectbox('Feeding Type:', ['Breastfeeding', 'Formula', 'Mixed'])
       

    with col3:
        feeding_frequency_per_day  = st.number_input('Number of feeds per day:', 7, 12, 8)
        urine_output_count = st.number_input('Wet Diapers/day:', 5, 15, 10)
        stool_count = st.number_input('Bowel Movements per day:', 0, 8, 4)
        jaundice_level_mg_dl = st.number_input('Bilirubin Level (mg/dL):', 1, 25, 15)
        apgar_score = ('APGAR Score at Birth:', 0, 10, 8)
        immunizations_done = st.selectbox('Immunizaition done (BCG, HepB, OPV on Day 1 & 30):', ['Yes', 'No'])
        reflexes_normal = st.selectbox('Newborn Reflex:', ['Yes', 'No'])
        


    if st.button('Predict Neonate Risk'):
        neonatal_features = np.array([[
            'gender', 'gestational_age_weeks', 'birth_weight_kg', 'birth_length_cm',
            'birth_head_circumference_cm', 'age_days', 'weight_kg', 'length_cm',
            'head_circumference_cm', 'temperature_c', 'heart_rate_bpm',
            'respiratory_rate_bpm', 'oxygen_saturation', 'feeding_type',
            'feeding_frequency_per_day', 'urine_output_count', 'stool_count',
            'jaundice_level_mg_dl', 'apgar_score', 'immunizations_done',
            'reflexes_normal',]])
    

    prediction = neonatal_model.predict(neonatal_features)[0]
    if prediction == 0:
        st.success('✅ Heathy: All Newborn vitals normal')
    
    else:
        st.error('⚠️ Newborn at Risk: Mild Jaundice, Slight fever, SpO₂ 92–95%, Refer the mother & Neonate to a Pediatrician Immediately')