import subprocess
import sys
import time
from threading import Thread
import webbrowser

def run_api():
    subprocess.run([sys.executable, "-m", "uvicorn", "api:app", "--reload", "--port", "8000"])
def run_dashboard():
    time.sleep(3)
    subprocess.run([sys.executable, "-m", "streamlit", "run", "dashboard.py", "--server.port", "8501"])
def open_browser():
    time.sleep(5)
    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    Thread(target=run_api, daemon=True).start()
    Thread(target=open_browser, daemon=True).start()
    run_dashboard()
