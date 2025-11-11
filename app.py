import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis de data de carros')

car_data = pd.read_csv('notebooks/vehicles_us.csv', sep=';')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón
model_button = st.button('Construir gráfico de dispersión')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if model_button:
    # crear un gráfico de dispersión
    st.write(
        'Creacion de una gráfica de dispersión que grafique el año del modelo vs el precio')
    st.write('Datos totales:', len(car_data))
    st.write('Valores nulos en model_year: ',
             car_data['model_year'].isnull().sum())
    st.write('Valores nulos en price: ', car_data['price'].isnull().sum())
    fig = px.scatter(car_data, x="model_year", y="price")
    # crear gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
