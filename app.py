import streamlit as st
import pandas as pd


st.write("""
# Multiplication APP

This app multiply two numbers.
""")
#Get Input

st.header('Please Enter Your Numbers.')

def user_input_features():
    number_1 = st.number_input('Insert first number')
    number_2 = st.number_input('Insert Second number')

    data = {'First_Number' : number_1,
            'Second_Number' : number_2,

            }
    features = pd.DataFrame(data, index=[0])
    return features , number_1 , number_2

df , number_1 , number_2 = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

st.subheader('Result')
p = number_1 * number_2
st.write(f'Product of numbers is: {p}')
