import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the model
with open('forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the CSV data
cars_df = pd.read_csv('cars_df.csv')

# Display the title
st.title("Used Car Price Prediction" + " 🚗")

# User inputs
brand = st.selectbox('Select Car Brand', cars_df['brand'].unique())
filtered_models = cars_df[cars_df['brand'] == brand]['model'].unique()
model_input = st.selectbox('Select Car Model', filtered_models)
transmission = st.selectbox('Select Transmission', cars_df['transmission'].unique())
fuel_type = st.selectbox('Select Fuel Type', cars_df['fuel_type'].unique())
year = st.number_input('Enter Year', min_value=int(cars_df['year'].min()), max_value=int(cars_df['year'].max()), step=1)
mileage = st.number_input('Enter Mileage', min_value=0, step=1)


# Prepare the input data for prediction
input_data = pd.DataFrame({
    'brand': [brand],
    'model': [model_input],
    'transmission': [transmission],
    'fuel_type': [fuel_type],
    'year': [year],
    'mileage': [mileage],    
})

# Encoding model column
encoder = LabelEncoder()
cars_df['model_encoded'] = encoder.fit_transform(cars_df['model'])
input_data['model_encoded'] = encoder.transform(input_data['model'])

# Creating dummy variables for input data
transmission_dummies = pd.get_dummies(input_data['transmission'], prefix='transmission')
fuel_type_dummies = pd.get_dummies(input_data['fuel_type'], prefix='fuel_type')
brand_dummies = pd.get_dummies(input_data['brand'], prefix='brand')

input_data = pd.concat([input_data, transmission_dummies, fuel_type_dummies, brand_dummies], axis=1)
input_data = input_data.drop(columns=['transmission', 'fuel_type', 'brand', 'model'])

# Align the input data with the training data
input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

# Make prediction
if st.button('Predict Price'):
    prediction = model.predict(input_data)
    st.write(f'The predicted price is: {prediction[0]:,.2f}£'.replace(',', ' '))


