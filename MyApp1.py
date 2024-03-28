import streamlit as st
import pandas as pd 

st.title("🌷🌷Website Developing using Python🌷🌷")
st.header("🎈🎈Website Developing using Python🎈🎈")
st.subheader("🐬Pathumnudda🐬")
st.image('aa.jpg')

dt=pd.read_csv('./Data.iris.csv')
st.write(dt.head(10))