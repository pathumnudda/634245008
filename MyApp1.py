import streamlit as st
import pandas as pd 
st.title("🌷🌷Website Developing using Python🌷🌷")
st.header("🎈🎈Website Developing using Python🎈🎈")
st.subheader("🐬Pathumnudda🐬")
st.image('aa.jpg')

dt=pd.read_csv('./data/iris.csv')
st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))
#Index(['sepal.length', 'sepal.width', 'petal.length', 'petal.width',
#       'variety'],

st.subheader("สถิติข้อมูลดอกไม้ Iris")


 