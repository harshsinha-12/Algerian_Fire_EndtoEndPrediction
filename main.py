import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the Ridge regression model and the standard scaler
ridge_model = pickle.load(open('Models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('Models/scaler.pkl', 'rb'))

# Set the page configuration
st.set_page_config(page_title='FWI Prediction', layout='centered')

# Define custom CSS to mimic the provided HTML styles
css = """
<style>
body {
    background-color: #f2f2f2;
    font-family: Arial, sans-serif;
}
.container, .login {
    width: 100%;
    max-width: 800px;
    margin: auto;
    padding: 50px;
    text-align: center;
}
.login {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 0px #0000001a;
}
h1 {
    color: #333333;
    margin-bottom: 20px;
}
h2 {
    margin-top: 30px;
    color: #333333;
}
p {
    color: #666666;
    font-size: 18px;
    line-height: 1.6;
}
.btn {
    padding: 15px 30px;
    background-color: #4285f4;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 18px;
    cursor: pointer;
    margin-top: 30px;
    text-decoration: none;
}
.btn:hover {
    background-color: #357ae8;
}
.social-icons {
    margin-top: 30px;
    display: flex;
    justify-content: center;
    gap: 20px;
}
.social-icons a {
    color: #666666;
    text-decoration: none;
    transition: color 0.3s ease;
}
.social-icons a:hover {
    color: #333333;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def show_home():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<h1>Fire Weather Index (FWI) Prediction</h1>', unsafe_allow_html=True)
    st.markdown('''
        <p>
            Welcome to the FWI Prediction Tool. This project utilizes machine learning to predict the Fire Weather Index (FWI), a key indicator used by forest fire management agencies to assess fire danger levels.
        </p>
        <p>
            By analyzing environmental factors such as temperature, relative humidity, wind speed, rainfall, and more, our model provides accurate predictions to help in proactive planning and resource allocation for wildfire prevention and control.
        </p>
    ''', unsafe_allow_html=True)
    if st.button('Get Started', key='get_started', help='Click to enter prediction page'):
        st.session_state.page = 'predict'
    st.markdown('''
        <div class="social-icons">
            <a href="https://github.com/harshsinha-12" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
                <!-- GitHub SVG Icon -->
                <!-- (Insert your full GitHub SVG path data here) -->
            </a>
            <a href="https://linkedin.com/in/harshsinha12" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                <!-- LinkedIn SVG Icon -->
                <!-- (Insert your full LinkedIn SVG path data here) -->
            </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

def show_predict():
    # st.markdown('<div class="login">', unsafe_allow_html=True)
    st.markdown('<h1>FWI Prediction</h1>', unsafe_allow_html=True)
    with st.form(key='prediction_form'):
        Temperature = st.text_input('Temperature', value='', help='Enter the temperature')
        RH = st.text_input('Relative Humidity (RH)', value='', help='Enter the relative humidity')
        Ws = st.text_input('Wind Speed (Ws)', value='', help='Enter the wind speed')
        Rain = st.text_input('Rainfall', value='', help='Enter the rainfall amount')
        FFMC = st.text_input('Fine Fuel Moisture Code (FFMC)', value='', help='Enter the FFMC value')
        DMC = st.text_input('Duff Moisture Code (DMC)', value='', help='Enter the DMC value')
        ISI = st.text_input('Initial Spread Index (ISI)', value='', help='Enter the ISI value')
        Classes = st.text_input('Classes (0 or 1)', value='', help='Enter the class (0 or 1)')
        Region = st.text_input('Region (0 or 1)', value='', help='Enter the region (0 or 1)')

        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        try:
            # Convert inputs to floats and create an array
            input_data = np.array([[float(Temperature), float(RH), float(Ws), float(Rain),
                                    float(FFMC), float(DMC), float(ISI), float(Classes), float(Region)]])
            # Scale the input data
            new_data_scaled = standard_scaler.transform(input_data)
            # Make prediction
            result = ridge_model.predict(new_data_scaled)
            st.markdown(f'<h2>THE FWI Prediction is {result[0]:.2f}</h2>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f'Error: {e}')
    st.markdown('''
        <div class="social-icons">
            <a href="https://github.com/harshsinha-12" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
                <!-- GitHub SVG Icon -->
                <!-- (Insert your full GitHub SVG path data here) -->
            </a>
            <a href="https://linkedin.com/in/harshsinha12" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                <!-- LinkedIn SVG Icon -->
                <!-- (Insert your full LinkedIn SVG path data here) -->
            </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# Main logic to display pages
if st.session_state.page == 'home':
    show_home()
elif st.session_state.page == 'predict':
    show_predict()