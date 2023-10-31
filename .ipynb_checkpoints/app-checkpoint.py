"""
@author: Keshinro Mus'ab
"""
import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color: lightblue; padding: 16px">
    <h2 style="color:black";text-align:center> Health Insurance Cost Prediction Using ML</h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    model =  joblib.load('model_joblib_gr')
    
    p1 = st.slider('Enter Your Age', 18, 100)


if __name__ == '__main__':
    main()