import streamlit as st
import pandas as pd

st.set_page_config(page_title="Avaliação de Projetos", layout="wide")

# --- Funções auxiliares ---
def carregar_projetos(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df.iloc[:, 0].tolist()  # Primeira coluna da planilha

def get_projetos_disponiveis(lista, ja_escolhidos):
    return [p for p in lista if p not in ja_escolhidos]

def salvar_selecoes(nome, selecoes):
    st.session_state[f'selecoes_{nome}'] = selecoes

def salvar_pontuacoes(nome, pontuacoes):
    st.session_state[f'pontuacoes_{nome}'] = pontuacoes

def calcular_ranking(pontuacoes_avaliadores):
    df = pd.DataFrame(pontuacoes_avaliadores)
    if df.empty:
        return pd.DataFrame()
    crits = [c for c in df.columns if c not i]()
