# 🏆 Plataforma de Avaliação de Projetos – InovaES

Plataforma web para seleção e avaliação colaborativa de projetos, feita em Streamlit.

## 🚀 Funcionalidades

- Upload da lista de projetos via arquivo Excel (.xlsx)
- Seleção de 10 projetos por avaliador (sem duplicidade)
- Pontuação dos projetos em 5 critérios (pesos Alto, Médio, Baixo)
- Ranking automático dos 5 projetos mais bem avaliados
- Exportação dos resultados e avaliações em .csv

## 🖥️ Como rodar localmente

```bash
git clone https://github.com/tecgabo/inovaes.git
cd inovaes
pip install -r requirements.txt
streamlit run app.py
