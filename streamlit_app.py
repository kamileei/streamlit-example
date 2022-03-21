
import streamlit as st
import pandas as pd
import numpy as np

st.title("My first app")
st.header("DS4 > DS3 == True")
st.header("eyo")


my_str = st.text_input("What's your name?")
st.text(f'Hello {my_str}')
