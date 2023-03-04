import streamlit as st
import pickle

st.title('Heart diseases prediction - Прогнозирование сердечных заболеваний')
st.write('Изменение шкал признаков для получения прогноза')

def load ():
    with open("c:/project-new/model.pcl", "rb") as fid:
      return pickle.load(fid)
    
year = st.slider('Возраст', 39, 64, key='year ')
height = st.slider('Рост', 143, 186, key='height ')
weight = st.slider('Вес', 40, 107, key='weight ')
ap_hi = st.slider('Давление верх', 93, 169, key='ap_hi ')
ap_lo = st.slider('Давление низ', 66, 104, key='ap_lo ')

st.sidebar.subheader(' Признаки: ')
st.sidebar.write('- id — индекс пациента')
st.sidebar.write('- age — возраст пациента')
st.sidebar.write('- gender — пол пациента')
st.sidebar.write('- height — рост пациента, см')
st.sidebar.write('- weight — вес пациента, кг')
st.sidebar.write('- ap_hi — систолическое давление(верхнее)')
st.sidebar.write('- ap_lo — диастолическое давление(нижнее)')
st.sidebar.write('- cholesterol — уровень холестерина')
st.sidebar.write('- gluc — уровень глюкозы')
st.sidebar.write('- smoke — курящий пациент')
st.sidebar.write('- alco — отношение к алкоголю у пациента')
st.sidebar.write('- active — физическая активность пациента')

st.sidebar.subheader(' Целевой признак ')
st.sidebar.write('- Cardio — risk of heart diseases')


model = load()

#y_pr = model.predict_proba([[year, height, weight, ap_hi, ap_lo]])[:, 1]
y_pr = model.predict_proba([[year, height, weight, ap_hi, ap_lo]])[:, 1]

st.write(y_pr)
