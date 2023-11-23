import streamlit as st

def main():
    st.set_page_config(page_title="Proyecto Apprende", layout="wide")
    with st.container():
        st.subheader("Proyecto Apprende Grupo 8")
        st.write("Néstor Guajardo")
        st.write("Pablo Guzmán")
        st.write("Eva Wang")

    with st.container():
        left_column, right_column = st.columns([3, 1])
    with left_column:
        prompt = st.text_input("Describe el taller")

    with right_column:
        if st.button("Enviar"):
            # Aqui se agrega lo que se hara con el prompt
            print("Hola")
            
    with st.container():
        st.markdown("[Búsquedas](http://localhost:8000/Búsquedas)")
if __name__ == "__main__":
    main()