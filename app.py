import json
from pathlib import Path
from datetime import datetime

import streamlit as st

ARQUIVO_MENSAGENS = Path("mensagens.json")

def carregar_mensagens():
    if not ARQUIVO_MENSAGENS.exists():
        return []


    try:
        with open(ARQUIVO_MENSAGENS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_mensagens(mensagens):
    print()

def adicionar_mensagens(username,mensagem):
    print()

st.title(" chat entre usúarios")

username = st.sidebar.text.input("Nome de usúario", key="username", value="Antônio")

@st.fragment(run_every=3)
def renderizar_chat():
    mensagens = carregar_mensagens()
    with st.container(border = True, height=500):
        for msg in mensagens:
            st.write(f"{msg["time"]} - {msg["username"]}: {msg["mensagem"]}")
renderizar_chat()
