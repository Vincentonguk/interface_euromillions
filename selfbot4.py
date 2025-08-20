from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import os
from datetime import datetime

app = FastAPI()

PASTA = "interface_euromillions"
ARQUIVO = 'interface_euromillions (1).py'
LOGFILE = "selfbot.log"

TEMPLATE = '''import streamlit as st
import random
import pandas as pd

st.title("Smart EuroMillions Generator")
# Your Streamlit app here
'''

def log(msg):
    with open(LOGFILE, 'a') as logf:
        logf.write(f"[{datetime.now().isoformat()}] {msg}\n")

def ensure_setup():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)
        log(f"Pasta {PASTA} criada.")
    os.chdir(PASTA)
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w') as f:
            f.write(TEMPLATE)
        log(f"Arquivo {ARQUIVO} criado.")

def run_cmd(cmd):
    log(f"Rodando comando: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    output = result.stdout + (result.stderr or "")
    log(output)
    return output

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>🤖 SelfBot 4.0</h1>
    <button onclick="window.location.href='/deploy'">Deploy</button>
    <button onclick="window.location.href='/status'">Status</button>
    <button onclick="window.location.href='/log'">Ver Log</button>
    """

@app.get("/deploy", response_class=HTMLResponse)
def deploy():
    ensure_setup()
    output = ""
    output += run_cmd("git status")
    output += run_cmd("git add .")
    output += run_cmd(f'git commit -m "deploy by SelfBot 4.0"')
    output += run_cmd("git push")
    return f"<pre>{output}</pre><br><a href='/'>Voltar</a>"

@app.get("/status", response_class=HTMLResponse)
def status():
    ensure_setup()
    output = run_cmd("git status")
    return f"<pre>{output}</pre><br><a href='/'>Voltar</a>"

@app.get("/log", response_class=HTMLResponse)
def view_log():
    with open(LOGFILE) as f:
        content = f.read()
    return f"<pre>{content}</pre><br><a href='/'>Voltar</a>"
