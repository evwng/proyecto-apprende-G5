INSTRUCCIONES DE COMPILACIÓN Y EJECUCIÓN:
- En el archivo crear_link.py se debe asignar la key de OpenAi a la variable openai.api_key
- Instalar requerimientos con el comando: pip install -r .\requirements.txt

API:
(0) Instalar requerimientos (fastapi, uvicorn, sqlalchemy)
(1) python -m venv env (?)
(2) python -m uvicorn api.main:app --reload
(3) http://127.0.0.1:8000/docs

STREAMLIT:
(0) Instalar requerimientos (streamlit)
(1) python -m streamlit run app.py