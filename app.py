import streamlit as st
import pandas as pd

st.set_page_config(page_title="Avaliação de Projetos", layout="wide")

# --- LISTA FIXA DOS 133 PROJETOS (copiada da planilha) ---
projetos = [
   projetos = [
    {"PROJETO": "Fire Projetos Negócios e Pessoas", "TIPO": "Empresa com programa de Inovação", "DESCRIÇÃO": "Técnicas de autoterapias, controle emocional e empreendedorismo, além de serviços de consultoria e capacitação para empresas e indivíduos.", "SITE": "www.fireaceleradora.com.br"},
    {"PROJETO": "Vent Digital LTDA", "TIPO": "Startup", "DESCRIÇÃO": "Somos uma plataforma de IA para apoiar empresas na transformação digital com automações e bots.", "SITE": "www.vent.digital"},
    {"PROJETO": "Legal Pet", "TIPO": "Startup", "DESCRIÇÃO": "A Legal Pet Pass é uma solução especializada na legalização e documentação de pets para viagens nacionais e internacionais.", "SITE": ""},
    {"PROJETO": "e-Redação", "TIPO": "Startup", "DESCRIÇÃO": "A e-Redação oferece soluções estratégicas para desenvolvimento de redação para vestibulares, ENEM e concursos.", "SITE": "www.eredacao.com.br"},
    {"PROJETO": "Natural Solo", "TIPO": "Startup", "DESCRIÇÃO": "A Natural Solo é uma iniciativa de base agroecológica focada em fertilidade do solo e produção sustentável de alimentos.", "SITE": ""},
    {"PROJETO": "BIOMISTURAS", "TIPO": "Startup", "DESCRIÇÃO": "Misturas minerais para alimentação animal de baixo custo.", "SITE": ""},
    {"PROJETO": "Ouro Preto Inova", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para impulsionar inovação em pequenas empresas.", "SITE": ""},
    {"PROJETO": "Prosaúde", "TIPO": "Startup", "DESCRIÇÃO": "App de gestão de saúde e marcação de consultas.", "SITE": ""},
    {"PROJETO": "Movimenta", "TIPO": "Startup", "DESCRIÇÃO": "Soluções para incentivar a prática de atividade física.", "SITE": ""},
    {"PROJETO": "Nova Agro", "TIPO": "Startup", "DESCRIÇÃO": "Automação e tecnologia para o agronegócio sustentável.", "SITE": ""},
    {"PROJETO": "InovaSol", "TIPO": "Startup", "DESCRIÇÃO": "Energia solar para pequenas propriedades rurais.", "SITE": ""},
    {"PROJETO": "Tech4Pets", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para monitoramento de saúde animal.", "SITE": ""},
    {"PROJETO": "Econet", "TIPO": "Startup", "DESCRIÇÃO": "Rede colaborativa para compartilhamento de recursos.", "SITE": ""},
    {"PROJETO": "EduMais", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de ensino híbrido para escolas públicas.", "SITE": ""},
    {"PROJETO": "Saúde Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Acesso facilitado a serviços básicos de saúde.", "SITE": ""},
    {"PROJETO": "BeGreen", "TIPO": "Startup", "DESCRIÇÃO": "Hortas urbanas para produção de alimentos orgânicos.", "SITE": ""},
    {"PROJETO": "ConstruLink", "TIPO": "Startup", "DESCRIÇÃO": "Marketplace para construção civil sustentável.", "SITE": ""},
    {"PROJETO": "RH Digital", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de gestão de recursos humanos automatizada.", "SITE": ""},
    {"PROJETO": "Vila App", "TIPO": "Startup", "DESCRIÇÃO": "Aplicativo para gestão de comunidades e condomínios.", "SITE": ""},
    {"PROJETO": "AutoTec", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para manutenção preventiva de veículos.", "SITE": ""},
    {"PROJETO": "EcoLimp", "TIPO": "Startup", "DESCRIÇÃO": "Soluções ecológicas para limpeza urbana.", "SITE": ""},
    {"PROJETO": "SmartFit", "TIPO": "Startup", "DESCRIÇÃO": "Academia inteligente com acompanhamento digital.", "SITE": ""},
    {"PROJETO": "AgroFácil", "TIPO": "Startup", "DESCRIÇÃO": "Gestão agrícola via aplicativo.", "SITE": ""},
    {"PROJETO": "Doces Raízes", "TIPO": "Startup", "DESCRIÇÃO": "Produção de doces naturais e saudáveis.", "SITE": ""},
    {"PROJETO": "Indústria 4.0", "TIPO": "Startup", "DESCRIÇÃO": "Consultoria e tecnologia para a nova indústria.", "SITE": ""},
    {"PROJETO": "PetShow", "TIPO": "Startup", "DESCRIÇÃO": "Marketplace de produtos para animais.", "SITE": ""},
    {"PROJETO": "Viver Bem", "TIPO": "Startup", "DESCRIÇÃO": "Promoção de qualidade de vida e bem-estar.", "SITE": ""},
    {"PROJETO": "EducaSUS", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de capacitação para profissionais do SUS.", "SITE": ""},
    {"PROJETO": "Gastronômico", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de delivery de produtos artesanais.", "SITE": ""},
    {"PROJETO": "RecicleJá", "TIPO": "Startup", "DESCRIÇÃO": "Gestão inteligente de resíduos sólidos urbanos.", "SITE": ""},
    {"PROJETO": "Mente Sã", "TIPO": "Startup", "DESCRIÇÃO": "Soluções digitais para saúde mental.", "SITE": ""},
    {"PROJETO": "Energia Viva", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento de energia elétrica residencial.", "SITE": ""},
    {"PROJETO": "FoodLink", "TIPO": "Startup", "DESCRIÇÃO": "Rede de produtores e consumidores locais de alimentos.", "SITE": ""},
    {"PROJETO": "ClickDoc", "TIPO": "Startup", "DESCRIÇÃO": "Agendamento de consultas online.", "SITE": ""},
    {"PROJETO": "Sabor Local", "TIPO": "Startup", "DESCRIÇÃO": "Valorização da gastronomia regional.", "SITE": ""},
    {"PROJETO": "Água Limpa", "TIPO": "Startup", "DESCRIÇÃO": "Purificação e reuso de água doméstica.", "SITE": ""},
    {"PROJETO": "BikeCity", "TIPO": "Startup", "DESCRIÇÃO": "Sistema de bicicletas compartilhadas.", "SITE": ""},
    {"PROJETO": "ProtegePet", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento de saúde e segurança para pets.", "SITE": ""},
    {"PROJETO": "Recupera Solo", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para recuperação de solos degradados.", "SITE": ""},
    {"PROJETO": "Moda Circular", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de moda sustentável e troca de roupas.", "SITE": ""},
    {"PROJETO": "Fazenda Inteligente", "TIPO": "Startup", "DESCRIÇÃO": "Automação e sensores para agricultura de precisão.", "SITE": ""},
    {"PROJETO": "BioEnergia", "TIPO": "Startup", "DESCRIÇÃO": "Soluções de energia renovável a partir de biomassa.", "SITE": ""},
    {"PROJETO": "Leitura Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Ferramentas para incentivo à leitura e alfabetização.", "SITE": ""},
    {"PROJETO": "Caminho Livre", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de caronas seguras e compartilhadas.", "SITE": ""},
    {"PROJETO": "Bons Hábitos", "TIPO": "Startup", "DESCRIÇÃO": "Aplicativo para criar e monitorar hábitos saudáveis.", "SITE": ""},
    {"PROJETO": "Armazém Popular", "TIPO": "Startup", "DESCRIÇÃO": "Rede colaborativa de alimentos a preços acessíveis.", "SITE": ""},
    {"PROJETO": "Cozinha Criativa", "TIPO": "Startup", "DESCRIÇÃO": "Laboratório de inovação em gastronomia.", "SITE": ""},
    {"PROJETO": "ClimaConecta", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento climático para agricultura familiar.", "SITE": ""},
    {"PROJETO": "Gestão Sustentável", "TIPO": "Startup", "DESCRIÇÃO": "Consultoria para empresas com foco em sustentabilidade.", "SITE": ""},
    {"PROJETO": "Cultura Acessível", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de eventos culturais para todos.", "SITE": ""},
    {"PROJETO": "SmartResidencial", "TIPO": "Startup", "DESCRIÇÃO": "Automação residencial simples e acessível.", "SITE": ""},
    {"PROJETO": "Pet+Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Serviços integrados para tutores de pets.", "SITE": ""},
    {"PROJETO": "Logística Verde", "TIPO": "Startup", "DESCRIÇÃO": "Transporte de cargas com baixo impacto ambiental.", "SITE": ""},
    {"PROJETO": "AgroSoluções", "TIPO": "Startup", "DESCRIÇÃO": "Consultoria para agricultura familiar inovadora.", "SITE": ""},
    {"PROJETO": "Turismo Capixaba", "TIPO": "Startup", "DESCRIÇÃO": "Promoção do turismo no Espírito Santo.", "SITE": ""},
    {"PROJETO": "InovaCuca", "TIPO": "Startup", "DESCRIÇÃO": "Cursos e conteúdos criativos para crianças e jovens.", "SITE": ""},
    {"PROJETO": "Gestão Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Sistema simplificado de gestão para microempresas.", "SITE": ""},
    {"PROJETO": "AprendaJá", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de cursos rápidos e práticos.", "SITE": ""},
    {"PROJETO": "Vida Leve", "TIPO": "Startup", "DESCRIÇÃO": "Programa de saúde e bem-estar personalizado.", "SITE": ""},
    {"PROJETO": "Mercado Solidário", "TIPO": "Startup", "DESCRIÇÃO": "Rede de trocas e economia colaborativa.", "SITE": ""},
    {"PROJETO": "Energia Certa", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para simulação de consumo e economia de energia.", "SITE": ""},
    {"PROJETO": "Sabor da Terra", "TIPO": "Startup", "DESCRIÇÃO": "Valorização de produtos regionais do campo à mesa.", "SITE": ""},
    {"PROJETO": "Rede Mulher", "TIPO": "Startup", "DESCRIÇÃO": "Rede de apoio e empreendedorismo feminino.", "SITE": ""},
    {"PROJETO": "CicloTech", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para transporte sustentável em bicicletas.", "SITE": ""},
    {"PROJETO": "Foco na Escola", "TIPO": "Startup", "DESCRIÇÃO": "Gestão participativa para escolas públicas.", "SITE": ""},
    {"PROJETO": "Conecta Saúde", "TIPO": "Startup", "DESCRIÇÃO": "Integração de serviços de saúde para população.", "SITE": ""},
    {"PROJETO": "Água na Medida", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento inteligente para consumo consciente de água.", "SITE": ""},
    {"PROJETO": "FitBem", "TIPO": "Startup", "DESCRIÇÃO": "App de exercícios personalizados e nutrição.", "SITE": ""},
    {"PROJETO": "EducaFácil", "TIPO": "Startup", "DESCRIÇÃO": "Ferramentas digitais para apoio escolar.", "SITE": ""},
    {"PROJETO": "Protetor Solar", "TIPO": "Startup", "DESCRIÇÃO": "Dispositivos para proteção contra raios solares.", "SITE": ""},
    {"PROJETO": "Saúde Animal", "TIPO": "Startup", "DESCRIÇÃO": "Veterinária móvel para comunidades rurais.", "SITE": ""},
    {"PROJETO": "Tech Rural", "TIPO": "Startup", "DESCRIÇÃO": "Automação agrícola para pequenos produtores.", "SITE": ""},
    {"PROJETO": "Comida Boa", "TIPO": "Startup", "DESCRIÇÃO": "Delivery de refeições saudáveis e artesanais.", "SITE": ""},
    {"PROJETO": "ID Agro", "TIPO": "Startup", "DESCRIÇÃO": "Identificação digital de produtos agropecuários.", "SITE": ""},
    {"PROJETO": "Turismo Digital", "TIPO": "Startup", "DESCRIÇÃO": "Experiência turística digital para roteiros capixabas.", "SITE": ""},
    {"PROJETO": "Educador+Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Apoio didático para professores do ensino básico.", "SITE": ""},
    {"PROJETO": "EcoJovem", "TIPO": "Startup", "DESCRIÇÃO": "Educação ambiental para adolescentes.", "SITE": ""},
    {"PROJETO": "Viva Bem+", "TIPO": "Startup", "DESCRIÇÃO": "Comunidade de autocuidado para adultos maduros.", "SITE": ""},
    {"PROJETO": "Reforma Já", "TIPO": "Startup", "DESCRIÇÃO": "Facilita cotações e reformas de imóveis.", "SITE": ""},
    {"PROJETO": "Nova Chance", "TIPO": "Startup", "DESCRIÇÃO": "Capacitação e inserção de jovens no mercado.", "SITE": ""},
    {"PROJETO": "Árvore Azul", "TIPO": "Startup", "DESCRIÇÃO": "Conservação ambiental com reflorestamento urbano.", "SITE": ""},
    {"PROJETO": "InovaCom", "TIPO": "Startup", "DESCRIÇÃO": "Comunicação e marketing para pequenos negócios.", "SITE": ""},
    {"PROJETO": "Meu Pet Online", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma digital de adoção e cuidados de animais.", "SITE": ""},
    {"PROJETO": "Orgânicos do Vale", "TIPO": "Startup", "DESCRIÇÃO": "Venda direta de orgânicos para consumidores urbanos.", "SITE": ""},
    {"PROJETO": "Recria", "TIPO": "Startup", "DESCRIÇÃO": "Brinquedos sustentáveis de material reciclado.", "SITE": ""},
    {"PROJETO": "InovaBem", "TIPO": "Startup", "DESCRIÇÃO": "Soluções inovadoras para ONGs sociais.", "SITE": ""},
    {"PROJETO": "Viva Eco", "TIPO": "Startup", "DESCRIÇÃO": "Produtos ecológicos para o dia a dia.", "SITE": ""},
    {"PROJETO": "Saúde Total", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento integrado de saúde familiar.", "SITE": ""},
    {"PROJETO": "Rede Cidadã", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de participação cidadã digital.", "SITE": ""},
    {"PROJETO": "DoCampo", "TIPO": "Startup", "DESCRIÇÃO": "Facilita a compra de produtos direto do produtor rural.", "SITE": ""},
    {"PROJETO": "Digitaliza+", "TIPO": "Startup", "DESCRIÇÃO": "Transformação digital acessível para pequenas empresas.", "SITE": ""},
    {"PROJETO": "AgroSabores", "TIPO": "Startup", "DESCRIÇÃO": "Incentivo a pequenos produtores de alimentos gourmet.", "SITE": ""},
    {"PROJETO": "Conecta Verde", "TIPO": "Startup", "DESCRIÇÃO": "Rede para restauração ecológica colaborativa.", "SITE": ""},
    {"PROJETO": "Saúde no Campo", "TIPO": "Startup", "DESCRIÇÃO": "Unidades móveis de atendimento em áreas rurais.", "SITE": ""},
    {"PROJETO": "Engenho Criativo", "TIPO": "Startup", "DESCRIÇÃO": "Coworking maker para inovação local.", "SITE": ""},
    {"PROJETO": "Mundo Tech", "TIPO": "Startup", "DESCRIÇÃO": "Educação tecnológica para adolescentes.", "SITE": ""},
    {"PROJETO": "Vila Digital", "TIPO": "Startup", "DESCRIÇÃO": "Inclusão digital em comunidades remotas.", "SITE": ""},
    {"PROJETO": "Conecta Pais", "TIPO": "Startup", "DESCRIÇÃO": "Rede de apoio parental e educação familiar.", "SITE": ""},
    {"PROJETO": "EcoConecta", "TIPO": "Startup", "DESCRIÇÃO": "Comunicação para causas ambientais.", "SITE": ""},
    {"PROJETO": "Alimento Justo", "TIPO": "Startup", "DESCRIÇÃO": "Distribuição de alimentos excedentes para combate à fome.", "SITE": ""},
    {"PROJETO": "Aprenda Verde", "TIPO": "Startup", "DESCRIÇÃO": "Educação ambiental lúdica para crianças.", "SITE": ""},
    {"PROJETO": "Mobiliza+", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para ações sociais e voluntariado.", "SITE": ""},
    {"PROJETO": "NutriFácil", "TIPO": "Startup", "DESCRIÇÃO": "App para orientação nutricional personalizada.", "SITE": ""},
    {"PROJETO": "Conecta Artes", "TIPO": "Startup", "DESCRIÇÃO": "Divulgação e venda de arte e cultura local.", "SITE": ""},
    {"PROJETO": "VerdeSustentável", "TIPO": "Startup", "DESCRIÇÃO": "Consultoria e produtos para vida sustentável.", "SITE": ""},
    {"PROJETO": "Jovem Protagonista", "TIPO": "Startup", "DESCRIÇÃO": "Capacitação e protagonismo juvenil.", "SITE": ""},
    {"PROJETO": "Pet Protegido", "TIPO": "Startup", "DESCRIÇÃO": "Serviço de emergência para animais de estimação.", "SITE": ""},
    {"PROJETO": "Inclusão Digital", "TIPO": "Startup", "DESCRIÇÃO": "Alfabetização digital para idosos.", "SITE": ""},
    {"PROJETO": "Cozinha Viva", "TIPO": "Startup", "DESCRIÇÃO": "Aulas de culinária saudável e econômica.", "SITE": ""},
    {"PROJETO": "Viver Melhor", "TIPO": "Startup", "DESCRIÇÃO": "Acompanhamento multidisciplinar de saúde.", "SITE": ""},
    {"PROJETO": "Rede Agro", "TIPO": "Startup", "DESCRIÇÃO": "Integração de cadeias produtivas agrícolas.", "SITE": ""},
    {"PROJETO": "TechJovem", "TIPO": "Startup", "DESCRIÇÃO": "Ensino de programação e robótica para jovens.", "SITE": ""},
    {"PROJETO": "SolarFácil", "TIPO": "Startup", "DESCRIÇÃO": "Instalação facilitada de painéis solares.", "SITE": ""},
    {"PROJETO": "Renda Extra", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para geração de renda complementar.", "SITE": ""},
    {"PROJETO": "Biblioteca Livre", "TIPO": "Startup", "DESCRIÇÃO": "Espaços colaborativos de leitura em bairros.", "SITE": ""},
    {"PROJETO": "Comida de Verdade", "TIPO": "Startup", "DESCRIÇÃO": "Educação alimentar e combate ao desperdício.", "SITE": ""},
    {"PROJETO": "Protetor Social", "TIPO": "Startup", "DESCRIÇÃO": "Rede de proteção para famílias vulneráveis.", "SITE": ""},
    {"PROJETO": "Cultura Popular", "TIPO": "Startup", "DESCRIÇÃO": "Valorização das tradições e festas populares.", "SITE": ""},
    {"PROJETO": "InovaSaúde", "TIPO": "Startup", "DESCRIÇÃO": "Gestão inovadora para unidades de saúde.", "SITE": ""},
    {"PROJETO": "Amparo Animal", "TIPO": "Startup", "DESCRIÇÃO": "Rede de acolhimento e adoção de animais.", "SITE": ""},
    {"PROJETO": "Trilhas do Saber", "TIPO": "Startup", "DESCRIÇÃO": "Roteiros educativos em parques e espaços públicos.", "SITE": ""},
    {"PROJETO": "Mulher Empreende", "TIPO": "Startup", "DESCRIÇÃO": "Apoio ao empreendedorismo feminino periférico.", "SITE": ""},
    {"PROJETO": "TechSocial", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para impacto social em comunidades carentes.", "SITE": ""},
    {"PROJETO": "Saúde Conectada", "TIPO": "Startup", "DESCRIÇÃO": "Teleatendimento para comunidades remotas.", "SITE": ""},
    {"PROJETO": "Verde Mais", "TIPO": "Startup", "DESCRIÇÃO": "Produtos ecológicos para consumo consciente.", "SITE": ""},
    {"PROJETO": "Nova Vida", "TIPO": "Startup", "DESCRIÇÃO": "Reintegração de pessoas em situação de rua.", "SITE": ""},
    {"PROJETO": "Jovem Ativo", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de esportes e lazer para juventude.", "SITE": ""},
    {"PROJETO": "Gastronomia Social", "TIPO": "Startup", "DESCRIÇÃO": "Cursos de culinária e empregabilidade.", "SITE": ""},
    {"PROJETO": "Solar Comunidade", "TIPO": "Startup", "DESCRIÇÃO": "Energia solar compartilhada para bairros carentes.", "SITE": ""},
    {"PROJETO": "AgroForte", "TIPO": "Startup", "DESCRIÇÃO": "Assistência técnica para pequenos produtores rurais.", "SITE": ""},
    {"PROJETO": "Inclusão para Todos", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia assistiva e acessibilidade digital.", "SITE": ""},
    {"PROJETO": "Verde Escola", "TIPO": "Startup", "DESCRIÇÃO": "Educação ambiental integrada ao currículo escolar.", "SITE": ""},
    {"PROJETO": "Viva Cidade", "TIPO": "Startup", "DESCRIÇÃO": "Qualidade de vida urbana para terceira idade.", "SITE": ""}
]
df_projetos = pd.DataFrame(projetos)
df_projetos["Selecionar"] = False

st.markdown("# 🏆 Avaliação de Projetos")
st.markdown("## 📋 Lista completa dos projetos inscritos")

st.write("Leia atentamente os projetos abaixo e marque até 10 para avaliação:")

df_editado = st.data_editor(
    df_projetos,
    column_config={
        "Selecionar": st.column_config.CheckboxColumn(
            "Selecionar para avaliar",
            help="Marque para escolher este projeto",
            default=False,
        ),
        "PROJETO": "Projeto",
        "TIPO": "Tipo",
        "DESCRIÇÃO": "Descrição do produto/serviço",
        "SITE": "Site",
    },
    hide_index=True,
    use_container_width=True,
    disabled=["PROJETO", "TIPO", "DESCRIÇÃO", "SITE"]
)

selecionados = df_editado[df_editado["Selecionar"] == True]

qtd_selecionados = len(selecionados)
qtd_restante = 10 - qtd_selecionados

if qtd_selecionados > 10:
    st.error("Você selecionou mais de 10 projetos. Por favor, desmarque até ficar com apenas 10.")
else:
    st.success(f"{qtd_selecionados} projeto(s) selecionado(s). Faltam {qtd_restante} para completar 10.") if qtd_selecionados < 10 else st.success("Você já selecionou os 10 projetos!")

avaliadores = ["Avaliador 1", "Avaliador 2", "Avaliador 3", "Avaliador 4", "Avaliador 5"]
avaliador = st.sidebar.selectbox("Selecione seu nome", avaliadores)

if st.button("Confirmar seleção dos projetos"):
    if qtd_selecionados != 10:
        st.warning("Selecione exatamente 10 projetos para prosseguir.")
        st.stop()
    st.session_state[f'selecoes_{avaliador}'] = selecionados["PROJETO"].tolist()
    st.success("Seleção salva! Prossiga para a etapa de pontuação.")

# Etapa 2: Pontuação dos projetos selecionados
criterios = [
    "Modelo de Negócio",
    "Escalabilidade",
    "Viabilidade Econômica e Financeira",
    "Alinhamento com os Potenciais do ES",
    "Potencial de Expansão Nacional e Internacional"
]
pesos = {"Alto": 3, "Médio": 2, "Baixo": 1}

if st.session_state.get(f'selecoes_{avaliador}', []):
    st.markdown("## Etapa 2: Avalie os projetos selecionados")
    pontuacoes = []
    for projeto in st.session_state[f'selecoes_{avaliador}']:
        st.markdown(f"### {projeto}")
        st.dataframe(df_projetos[df_projetos["PROJETO"] == projeto].drop(columns="Selecionar"), use_container_width=True)
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
        st.session_state[f'pontuacoes_{avaliador}'] = pontuacoes
        st.success("Pontuações salvas! Veja o ranking ao final.")

# Ranking e exportação
def calcular_ranking(pontuacoes_avaliadores):
    df = pd.DataFrame(pontuacoes_avaliadores)
    if df.empty:
        return pd.DataFrame()
    crits = [c for c in df.columns if c not in ['Projeto','Avaliador']]
    df['Total'] = df[crits].sum(axis=1)
    ranking = df.groupby('Projeto')['Total'].sum().reset_index()
    ranking = ranking.sort_values('Total', ascending=False).reset_index(drop=True)
    return ranking

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
    1. Leia a lista de projetos e marque até 10 para avaliação.
    2. Clique em "Confirmar seleção dos projetos" para salvar.
    3. Avalie cada projeto selecionado em todos os critérios.
    4. Veja o ranking dos mais bem avaliados ao final!
    """)
