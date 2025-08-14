# Importamos las librerías
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leemos nuestro archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Ponemos nuestro encabezado
st.header('Gráficas sobre las ventas de coches')

# Creamos las casillas de verificación y el botón para crear el histograma
build_histogram = st.checkbox('Construir un histograma')
hist_button = st.button('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna "Odómetro"')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig_hist, use_container_width=True)


# Creamos las casillas de verificación y el botón para crear la gráfica de dispersión
build_scatter = st.checkbox('Construir una gráfica de dispersión')
scat_button = st.button('Construir una gráfica de dispersión')

if build_scatter:
    st.write('Relación entre las columnas "Odómetro" y "Precio"')

if scat_button:
    st.write(
        'Creación de gráfica de dispersión sobre la relación entre kilometraje y precio')
    fig_scat = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig_scat.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig_scat, use_container_width=True)
