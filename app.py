import streamlit as st

st.set_page_config(page_title="Calculadora del 16%", page_icon="🧮", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fb;
    }
    .titulo {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 10px;
    }
    .subtitulo {
        text-align: center;
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }
    .card {
        background: white;
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        max-width: 600px;
        margin: auto;
    }
    .resultado {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        color: #0f766e;
        margin-top: 25px;
    }
    .texto-resultado {
        text-align: center;
        font-size: 18px;
        color: #374151;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">Calculadora del 16%</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitulo">Ingresa una cantidad y mira el resultado al instante.</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

numero = st.number_input("Ingresa el monto", min_value=0.0, step=1.0)
resultado = numero * 0.16

st.markdown(
    f'<div class="texto-resultado">El 16% de <strong>${numero:,.2f}</strong> es:</div>',
    unsafe_allow_html=True
)
st.markdown(
    f'<div class="resultado">${resultado:,.2f}</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)