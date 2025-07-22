import streamlit as st
import pandas as pd

st.set_page_config(page_title="Avaliação de Projetos", layout="wide")

def carregar_projetos(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df

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
    crits = [c for c in df.columns if c not in ['Projeto','Avaliador']]
    df['Total'] = df[crits].sum(axis=1)
    ranking = df.groupby('Projeto')['Total'].sum().reset_index()
    ranking = ranking.sort_values('Total', ascending=False).reset_index(drop=True)
    return ranking

st.markdown("# 🏆 Avaliação de Projetos")

uploaded_file = st.sidebar.file_uploader("1️⃣ Faça upload da lista (Excel)", type=["xlsx"])
if not uploaded_file:
    st.info("Envie o arquivo Excel da lista de projetos.")
    st.stop()

df_projetos = carregar_projetos(uploaded_file)
st.markdown("## 📋 Lista completa dos projetos inscritos")
st.dataframe(df_projetos, use_container_width=True)

# Para seleção, usaremos a primeira coluna (pode mudar se quiser outra)
coluna_projeto = df_projetos.columns[0]
lista_projetos = df_projetos[coluna_projeto].tolist()
avaliadores = ["Avaliador 1", "Avaliador 2", "Avaliador 3", "Avaliador 4", "Avaliador 5"]
avaliador = st.sidebar.selectbox("2️⃣ Selecione seu nome", avaliadores)

# Controle: projetos já escolhidos pelos outros avaliadores
ja_escolhidos = []
for a in avaliadores:
    if a != avaliador:
        ja_escolhidos += st.session_state.get(f'selecoes_{a}', [])

projetos_disponiveis = get_projetos_disponiveis(lista_projetos, ja_escolhidos)

st.markdown("## Etapa 1: Selecione até 10 projetos (sem duplicidade)")
selecionados = st.multiselect(
    "Escolha seus 10 projetos para avaliar:",
    options=projetos_disponiveis,
    default=st.session_state.get(f'selecoes_{avaliador}', []),
    max_selections=10
)

if st.button("Confirmar seleção"):
    if len(selecionados) != 10:
        st.warning("Selecione exatamente 10 projetos.")
        st.stop()
    salvar_selecoes(avaliador, selecionados)
    st.success("Seleção salva! Prossiga para pontuar os projetos.")

# --- Etapa 2: Pontuação ---
criterios = [
    "Modelo de Negócio",
    "Escalabilidade",
    "Viabilidade Econômica e Financeira",
    "Alinhamento com os Potenciais do ES",
    "Potencial de Expansão Nacional e Internacional"
]
pesos = {"Alto": 3, "Médio": 2, "Baixo": 1}

if st.session_state.get(f'selecoes_{avaliador}', []):
    st.markdown("## Etapa 2: Pontue os projetos selecionados")
    pontuacoes = []
    for projeto in st.session_state[f'selecoes_{avaliador}']:
        st.markdown(f"### {projeto}")
        # Exibe as informações do projeto na tabela para consulta fácil
        st.dataframe(df_projetos[df_projetos[coluna_projeto] == projeto], use_container_width=True)
        p = {"Projeto": projeto}
        for c in criterios:
            val = st.radio(
                c,
                options=["Alto", "Médio", "Baixo"],
                key=f"{avaliador}_{projeto}_{c}"
            )
            p[c] = pesos[val]
        pontuacoes.append(p)

    if st.button("Salvar pontuações"):
        salvar_pontuacoes(avaliador, pontuacoes)
        st.success("Pontuações salvas. Ranking final será atualizado.")

# --- Etapa 3: Ranking ---
st.markdown("## Ranking Final")
avaliadores_lista = avaliadores
todas_pontuacoes = []
for a in avaliadores_lista:
    resp = st.session_state.get(f'pontuacoes_{a}', [])
    for r in resp:
        r_copia = r.copy()
        r_copia["Avaliador"] = a
        todas_pontuacoes.append(r_copia)

ranking = calcular_ranking(todas_pontuacoes)
if not ranking.empty:
    st.dataframe(ranking.head(5), use_container_width=True)
    st.download_button(
        "Baixar ranking completo",
        ranking.to_csv(index=False),
        file_name="ranking.csv",
        mime="text/csv"
    )
else:
    st.info("O ranking será exibido após todas as avaliações serem concluídas.")

# --- Exportação das respostas completas ---
st.markdown("### Exportar todas as respostas completas")
if todas_pontuacoes:
    df_respostas = pd.DataFrame(todas_pontuacoes)
    st.dataframe(df_respostas, use_container_width=True)
    st.download_button(
        "Baixar respostas completas (.csv)",
        df_respostas.to_csv(index=False),
        file_name="respostas_completas.csv",
        mime="text/csv"
    )
else:
    st.info("As respostas aparecerão aqui após os avaliadores preencherem as pontuações.")

with st.expander("Como funciona?"):
    st.write("""
    1. Veja a lista completa dos projetos para consulta e panorama geral.
    2. Selecione 10 projetos (sem duplicidade entre avaliadores).
    3. Após selecionar, avalie cada um nos critérios definidos.
    4. O ranking será mostrado ao final!
    """)
