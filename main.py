from scripts.titanic import Titanic
import streamlit as st


st.title('Titanic Web App')
st.image('src/img/titanic.jpg')
st.header('Количество пассажиров каждого пола по указанному классу обслуживания')

titanic = Titanic(path_name='src/data/data.csv')

class_dict = titanic.get_class()

st.header('Количество пассажиров каждого пола по указанному классу обслуживания')

option = st.selectbox(
    "Выберите класс",
    ("1", "2", "3"))

passengers = class_dict[option]

data = {'Пол': ['Мужчины', 'Женщины'],
        'Количество': [passengers['male'], passengers['female']]}

st.bar_chart(data=data, x='Пол', y='Количество')