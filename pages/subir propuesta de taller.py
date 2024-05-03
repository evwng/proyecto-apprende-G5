import streamlit as st
import requests
import json

st.set_page_config(page_title = "Subir propuesta de taller",
                   layout = "wide",
                   initial_sidebar_state = "collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title = "Subir propuesta de taller"

with st.container():
    
    st.header("SUBIR PROPUESTA DE TALLER")

with st.container():

    id_tallerista = st.text_input("Ingrese identificador enviado:")

    descripcion = st.text_input("Ingrese descripción del taller:")

    modalidad = st.selectbox("Ingrese una modalidad:",
                             ["Presencial", "Híbrido", "Online"])

    numero_vacantes = st.slider("Ingrese número de vacantes", 1, 50, 1)

    numero_sesiones = st.slider("Ingrese número de sesiones", 1, 10, 1)

    propuesta_atributos = {"descripcion": descripcion,
                           "modalidad": modalidad,
                           "numero_vacantes": numero_vacantes,
                           "numero_sesiones": numero_sesiones,
                           "id_tallerista": id_tallerista}

    if st.button("Enviar propuesta"):

        request = requests.post("http://127.0.0.1:8000/propuesta", data = json.dumps(propuesta_atributos))

        if request:
            st.text("¡Propuesta de taller enviada con éxito!")
        else:
            st.text("Ha ocurrido un error")