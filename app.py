import streamlit as st


st.write("""
# Summation APP

This app sums up two numbers.
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
sum = number_1 + number_2
st.write(f'Summation of numbers is: {sum}')
