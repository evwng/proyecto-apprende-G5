import subprocess
import sys

windows: bool = sys.platform == "win32"
 
slash: str =  "/" if not windows else "\\"

comando_fastapi = ["python", "-m", "uvicorn", "api.main:app", "--reload"]
comando_streamlit = ["python", "-m", "streamlit", "run", "app.py"]
comando_req = ["pip", "install", "-r", f".{slash}requirements.txt"]

proceso_req = subprocess.Popen(comando_req)
proceso_req.wait()
proceso_fastapi = subprocess.Popen(comando_fastapi)
proceso_streamlit = subprocess.Popen(comando_streamlit)

try:
    proceso_fastapi.wait()
    proceso_streamlit.wait()
except KeyboardInterrupt:
    proceso_fastapi.terminate()
    proceso_streamlit.terminate()
