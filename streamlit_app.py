
import streamlit as st
import pickle

st.write('Hello, world!')

def load ():
    with open("c:/project-new/model.pcl", "rb") as fid:
      return pickle.load(fid)
    
year = st.slider('Возраст', 39, 64, key='year ')
height = st.slider('Рост', 143, 186, key='height ')
weight = st.slider('Вес', 40, 107, key='weight ')
ap_hi = st.slider('Давление верх', 93, 169, key='ap_hi ')
ap_lo = st.slider('Давление низ', 66, 104, key='ap_lo ')

model = load()

#y_pr = model.predict_proba([[year, height, weight, ap_hi, ap_lo]])[:, 1]
y_pr = model.predict_proba([[year, height, weight, ap_hi, ap_lo]])[:, 1]

st.write(y_pr)
