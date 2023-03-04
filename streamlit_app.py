import streamlit as st
import pickle

st.title('Heart diseases prediction - Прогнозирование сердечных заболеваний')
st.write('Изменение шкал признаков для получения прогноза')

st.sidebar.subheader(' Признаки: ')
st.sidebar.write('- gender — пол пациента')
st.sidebar.write('- age — возраст пациента')
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

gender = st.selectbox('Пол пациента:', [' 1 ', ' 2 '], key='gender')
year = st.slider('Возраст', 39, 64, key='year')
height = st.slider('Рост', 143, 186, key='height')
weight = st.slider('Вес', 40, 107, key='weight')
ap_hi = st.slider('Cистолическое давление (верхнее)', 93, 169, key='ap_hi')
ap_lo = st.slider('Диастолическое давление (нижнее)', 66, 104, key='ap_lo')
cholesterol = st.selectbox('Уровень холестерина:', [' 1 ', ' 2 ', ' 3 '], key='cholesterol')
gluc = st.selectbox('Уровень глюкозы:', [' 1 ', ' 2 ', ' 3 '], key='gluc')
smoke = st.selectbox('Отношение к курению: ', [' 0 ', ' 1 '], key='smoke')
alco = st.selectbox('Отношение к алкоголю: ', [' 0 ', ' 1 '], key='alco')
active = st.selectbox('Отношение к спорту: ', [' 0 ', ' 1 '], key='active')

def load ():
    with open("\model.pcl", "rb") as fid:
      return pickle.load(fid)
   
model = load()
y_pr = model.predict_proba([[gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, year]])[:, 1]

st.write(y_pr)
