import streamlit as st
import numpy as np
from neuron import Neuron

st.set_page_config(layout="wide")
st.image('img/neurona.jpg', width=250)
st.title('Simulador de neurona')
numeroNeuronas = st.slider('Elige el número de entradas/pesos que tendrá la neurona', 1, 10, key="numeroNeuronas")

entradas = []
pesos = []

st.header('Pesos', divider='rainbow')

col_pesos = st.columns(numeroNeuronas)
for i in range(0, numeroNeuronas):
    with col_pesos[i]:
        pesos.append(st.number_input(f'w{i}', key=f'w{i}'))

st.text(f'w = {pesos}')

st.header('Entradas', divider='rainbow')

col_entradas = st.columns(numeroNeuronas)
for i in range(0, numeroNeuronas):
    with col_entradas[i]:
        entradas.append(st.number_input(f'x{i}', key=f'x{i}'))

st.text(f'x = {entradas}')

col1, col2 = st.columns(2)
with col1:
    st.header('Sesgo', divider='rainbow')
    b = st.number_input("Introduce el valor del sesgo", key='sesgo')

with col2:
    st.header('Función de activación', divider='rainbow')
    func = st.selectbox(
    'Elige la función de activación',
    ('sigmoid', 'relu', 'tanh'))

if st.button('Calcular la salida'):
    n1 = Neuron(weights=pesos, bias=b, func=func)
    output = n1.run(input_data=entradas)
    st.text(f'La salida de la neurona es: {output}')
