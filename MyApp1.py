import streamlit as st
import pandas as pd

st.title("🌷🌷Website Developing using Python🌷🌷")
st.header("🎈🎈Website Developing using Python🎈🎈")
st.subheader("🐬Pathumnudda🐬")
st.image('aa.jpg')

#Index(['sepal.length', 'sepal.width', 'petal.length', 'petal.width','variety'], dtype='object')

dt=pd.read_csv('./data/iris.csv')
st.subheader("ข้อมูลดอกไม้")
st.write(dt.head(10))

st.subheader("ข้อมูลดอกไม้")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].sum())
cl2.write(dt['sepal.width'].sum())
cl3.write(dt['petal.length'].sum())
cl4.write(dt['petal.width'].sum())

dx=pd.DataFrame(
    {
        "cl1":dt['sepal.length'].sum()
        "cl2":dt['sepal.width'].sum()
        "cl3":dt['petal.length'].sum()
    }
)
st.bar_chart(dx,x='col1',y='col2',color='col3')

st.write('ค่าเฉลี่ย')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].mean())
cl2.write(dt['sepal.width'].mean())
cl3.write(dt['petal.length'].mean())
cl4.write(dt['petal.width'].mean())


st.write('ค่ามากสุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['sepal.length'].max())
cl22.write(dt['sepal.width'].max())
cl23.write(dt['petal.length'].max())
cl24.write(dt['petal.width'].max())

st.write('ค่าน้อยสุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['sepal.length'].min())
cl32.write(dt['sepal.width'].min())
cl33.write(dt['petal.length'].min())
cl34.write(dt['petal.width'].min())