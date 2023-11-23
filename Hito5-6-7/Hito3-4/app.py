import streamlit as st

def main():
    st.set_page_config(page_title="Proyecto Apprende", layout="wide")
    with st.container():
        st.subheader("Proyecto Apprende Grupo 8")
        st.write("Néstor Guajardo")
        st.write("Pablo Guzmán")
        st.write("Eva Wang")
    texto = st.text_input("Describa el taller deseado", "texto ejemplo")
    
    ## Podemos usar markdown para poner hypervínculos
    st.markdown("Text[o](https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUTbmV2ZXIgZ29ubmEgZ2l2ZSB1cA%3D%3D&ab_channel=RickAstley)")
    st.markdown("[Búsquedas]](http://localhost:8000/Búsquedas)")
    
    # .\app.py

if __name__ == "__main__":
    main()