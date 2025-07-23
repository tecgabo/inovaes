import streamlit as st
import pandas as pd

st.set_page_config(page_title="Avaliação de Projetos", layout="wide")

projetos = [
    {"PROJETO": "Fire Projetos Negócios e Pessoas", "TIPO": "Empresa com programa de Inovação", "DESCRIÇÃO": "Trabalhamos com técnicas de autoterapias, controle emocional e empreendedorismo, além de serviços de consultoria e capacitação para empresas e indivíduos.", "SITE": "www.fireaceleradora.com.br"},
    {"PROJETO": "Vent Digital LTDA", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de IA para apoiar empresas na transformação digital com automações e bots personalizados para WhatsApp, Instagram e Facebook.", "SITE": "www.vent.digital"},
    {"PROJETO": "Legal Pet", "TIPO": "Startup", "DESCRIÇÃO": "A Legal Pet Pass é uma solução especializada na legalização e documentação de pets para viagens nacionais e internacionais, desburocratizando o processo e proporcionando segurança.", "SITE": ""},
    {"PROJETO": "e-Redação", "TIPO": "Startup", "DESCRIÇÃO": "Soluções estratégicas para desenvolvimento de redação para vestibulares, ENEM e concursos, com correção personalizada e feedback detalhado.", "SITE": "www.eredacao.com.br"},
    {"PROJETO": "Natural Solo", "TIPO": "Startup", "DESCRIÇÃO": "Iniciativa de base agroecológica com foco em fertilidade do solo, compostagem e produção sustentável de alimentos orgânicos, consultorias e cursos.", "SITE": ""},
    {"PROJETO": "BIOMISTURAS", "TIPO": "Startup", "DESCRIÇÃO": "Misturas minerais para alimentação animal de baixo custo, produzidas a partir de resíduos da indústria local.", "SITE": ""},
    {"PROJETO": "Ouro Preto Inova", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para impulsionar inovação em pequenas empresas, com mentoria, capacitação e rede de contatos estratégicos.", "SITE": ""},
    {"PROJETO": "Prosaúde", "TIPO": "Startup", "DESCRIÇÃO": "Aplicativo de gestão de saúde com agendamento de consultas, controle de exames e lembretes de medicamentos, integrado ao SUS.", "SITE": ""},
    {"PROJETO": "Movimenta", "TIPO": "Startup", "DESCRIÇÃO": "Soluções tecnológicas para incentivar a prática de atividade física e bem-estar em empresas, escolas e comunidades.", "SITE": ""},
    {"PROJETO": "Nova Agro", "TIPO": "Startup", "DESCRIÇÃO": "Automação e tecnologia acessível para o agronegócio sustentável, com monitoramento de lavouras e gestão de produção.", "SITE": ""},
    {"PROJETO": "InovaSol", "TIPO": "Startup", "DESCRIÇÃO": "Energia solar para pequenas propriedades rurais, com instalação, financiamento facilitado e acompanhamento técnico.", "SITE": ""},
    {"PROJETO": "Tech4Pets", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia de monitoramento de saúde animal por sensores e plataforma web para clínicas veterinárias.", "SITE": ""},
    {"PROJETO": "Econet", "TIPO": "Startup", "DESCRIÇÃO": "Rede colaborativa para compartilhamento de recursos, ferramentas e máquinas entre microempreendedores.", "SITE": ""},
    {"PROJETO": "EduMais", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de ensino híbrido para escolas públicas com conteúdos interativos, videoaulas e relatórios de desempenho.", "SITE": ""},
    {"PROJETO": "Saúde Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Acesso facilitado a serviços básicos de saúde, com agendamento online, consulta remota e encaminhamentos.", "SITE": ""},
    {"PROJETO": "BeGreen", "TIPO": "Startup", "DESCRIÇÃO": "Hortas urbanas para produção de alimentos orgânicos, cursos e venda de kits de cultivo doméstico.", "SITE": ""},
    {"PROJETO": "ConstruLink", "TIPO": "Startup", "DESCRIÇÃO": "Marketplace para conectar construtores, fornecedores e clientes no setor da construção civil sustentável.", "SITE": ""},
    {"PROJETO": "RH Digital", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de gestão de recursos humanos automatizada, com seleção, treinamento e acompanhamento de colaboradores.", "SITE": ""},
    {"PROJETO": "Vila App", "TIPO": "Startup", "DESCRIÇÃO": "Aplicativo para gestão de comunidades, condomínios e associações, com comunicação, finanças e serviços integrados.", "SITE": ""},
    {"PROJETO": "AutoTec", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para manutenção preventiva de veículos, controle de revisões, peças e agendamento em oficinas.", "SITE": ""},
    {"PROJETO": "EcoLimp", "TIPO": "Startup", "DESCRIÇÃO": "Soluções ecológicas para limpeza urbana, coleta seletiva, reciclagem e compostagem em bairros.", "SITE": ""},
    {"PROJETO": "SmartFit", "TIPO": "Startup", "DESCRIÇÃO": "Academia inteligente com acompanhamento digital de desempenho, treinos personalizados e integração com smartwatches.", "SITE": ""},
    {"PROJETO": "AgroFácil", "TIPO": "Startup", "DESCRIÇÃO": "Gestão agrícola via aplicativo, para controle de produção, custos e vendas no campo.", "SITE": ""},
    {"PROJETO": "Doces Raízes", "TIPO": "Startup", "DESCRIÇÃO": "Produção de doces naturais e saudáveis, sem adição de açúcar ou conservantes, direto do produtor.", "SITE": ""},
    {"PROJETO": "Indústria 4.0", "TIPO": "Startup", "DESCRIÇÃO": "Consultoria e tecnologia para a nova indústria, com automação, robótica e IoT.", "SITE": ""},
    {"PROJETO": "PetShow", "TIPO": "Startup", "DESCRIÇÃO": "Marketplace de produtos e serviços para animais, com agendamento, compras e delivery.", "SITE": ""},
    {"PROJETO": "Viver Bem", "TIPO": "Startup", "DESCRIÇÃO": "Promoção de qualidade de vida e bem-estar com acompanhamento multidisciplinar e programas personalizados.", "SITE": ""},
    {"PROJETO": "EducaSUS", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de capacitação e atualização para profissionais do SUS, com conteúdos certificados.", "SITE": ""},
    {"PROJETO": "Gastronômico", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de delivery e eventos de gastronomia artesanal, conectando chefs locais e consumidores.", "SITE": ""},
    {"PROJETO": "RecicleJá", "TIPO": "Startup", "DESCRIÇÃO": "Gestão inteligente de resíduos sólidos urbanos, integração com catadores e recompensas para recicladores.", "SITE": ""},
    {"PROJETO": "Mente Sã", "TIPO": "Startup", "DESCRIÇÃO": "Aplicativo e programa de acompanhamento para saúde mental, com sessões online e grupos de apoio monitorados.", "SITE": ""},
    {"PROJETO": "Energia Viva", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento de energia elétrica residencial, consumo em tempo real, dicas de economia e gestão remota.", "SITE": ""},
    {"PROJETO": "FoodLink", "TIPO": "Startup", "DESCRIÇÃO": "Rede que conecta produtores rurais e consumidores locais, otimizando logística e promovendo o consumo regional.", "SITE": ""},
    {"PROJETO": "ClickDoc", "TIPO": "Startup", "DESCRIÇÃO": "Agendamento de consultas online, integração com clínicas e planos de saúde, lembretes automáticos e histórico do paciente.", "SITE": ""},
    {"PROJETO": "Sabor Local", "TIPO": "Startup", "DESCRIÇÃO": "Valorização da gastronomia regional por meio de eventos, feiras, cursos e divulgação de receitas típicas.", "SITE": ""},
    {"PROJETO": "Água Limpa", "TIPO": "Startup", "DESCRIÇÃO": "Purificação, reuso e gestão de água doméstica, sistemas de captação de chuva e tecnologia para economia.", "SITE": ""},
    {"PROJETO": "BikeCity", "TIPO": "Startup", "DESCRIÇÃO": "Sistema inteligente de bicicletas compartilhadas para cidades, integração com transporte público e incentivo à mobilidade.", "SITE": ""},
    {"PROJETO": "ProtegePet", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento remoto da saúde, segurança e localização de animais de estimação, com alertas em tempo real.", "SITE": ""},
    {"PROJETO": "Recupera Solo", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para recuperação de solos degradados, consultoria para produtores e fornecimento de insumos ecológicos.", "SITE": ""},
    {"PROJETO": "Moda Circular", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para troca, venda e upcycling de roupas e acessórios, promovendo economia circular na moda.", "SITE": ""},
    {"PROJETO": "Fazenda Inteligente", "TIPO": "Startup", "DESCRIÇÃO": "Automação e sensores para agricultura de precisão, acompanhamento remoto da produção e análise de dados.", "SITE": ""},
    {"PROJETO": "BioEnergia", "TIPO": "Startup", "DESCRIÇÃO": "Soluções de energia renovável gerada a partir de biomassa agrícola e resíduos orgânicos.", "SITE": ""},
    {"PROJETO": "Leitura Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Ferramentas digitais e físicas para incentivo à leitura e alfabetização em todas as idades.", "SITE": ""},
    {"PROJETO": "Caminho Livre", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de caronas seguras e compartilhadas para trajetos urbanos e intermunicipais, com avaliação dos usuários.", "SITE": ""},
    {"PROJETO": "Bons Hábitos", "TIPO": "Startup", "DESCRIÇÃO": "Aplicativo para criação, monitoramento e recompensa de hábitos saudáveis, com gamificação e desafios semanais.", "SITE": ""},
    {"PROJETO": "Armazém Popular", "TIPO": "Startup", "DESCRIÇÃO": "Rede colaborativa de alimentos a preços acessíveis, com foco em segurança alimentar e fortalecimento comunitário.", "SITE": ""},
    {"PROJETO": "Cozinha Criativa", "TIPO": "Startup", "DESCRIÇÃO": "Laboratório de inovação em gastronomia para chefs, pequenos produtores e startups do ramo alimentício.", "SITE": ""},
    {"PROJETO": "ClimaConecta", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento climático com sensores e previsão para agricultura familiar e urbana, alertas e recomendações.", "SITE": ""},
    {"PROJETO": "Gestão Sustentável", "TIPO": "Startup", "DESCRIÇÃO": "Consultoria e plataforma para empresas implementarem práticas ESG e projetos de sustentabilidade corporativa.", "SITE": ""},
    {"PROJETO": "Cultura Acessível", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma digital para divulgação e acesso facilitado a eventos culturais inclusivos e acessíveis.", "SITE": ""},
    {"PROJETO": "SmartResidencial", "TIPO": "Startup", "DESCRIÇÃO": "Automação residencial, controle de iluminação, segurança e eletrodomésticos com tecnologia acessível.", "SITE": ""},
    {"PROJETO": "Pet+Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Serviços integrados para tutores de pets, incluindo agendamento, dicas, vacinas e petshops próximos.", "SITE": ""},
    {"PROJETO": "Logística Verde", "TIPO": "Startup", "DESCRIÇÃO": "Transporte de cargas com baixo impacto ambiental, rotas inteligentes e uso de veículos sustentáveis.", "SITE": ""},
    {"PROJETO": "AgroSoluções", "TIPO": "Startup", "DESCRIÇÃO": "Consultoria para agricultura familiar inovadora, tecnologia, crédito e capacitação.", "SITE": ""},
    {"PROJETO": "Turismo Capixaba", "TIPO": "Startup", "DESCRIÇÃO": "Promoção do turismo regional com roteiros personalizados, experiências culturais e divulgação digital.", "SITE": ""},
    {"PROJETO": "InovaCuca", "TIPO": "Startup", "DESCRIÇÃO": "Cursos criativos para crianças e jovens, programação, robótica, artes e conteúdos de inovação.", "SITE": ""},
    {"PROJETO": "Gestão Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Sistema simplificado de gestão financeira, estoque e vendas para micro e pequenas empresas.", "SITE": ""},
    {"PROJETO": "AprendaJá", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de cursos rápidos, práticos e certificados para formação profissional.", "SITE": ""},
    {"PROJETO": "Vida Leve", "TIPO": "Startup", "DESCRIÇÃO": "Programa personalizado de saúde e bem-estar, acompanhamento nutricional e atividades físicas.", "SITE": ""},
    {"PROJETO": "Mercado Solidário", "TIPO": "Startup", "DESCRIÇÃO": "Rede de trocas, doações e economia colaborativa, conectando pessoas para consumo consciente.", "SITE": ""},
    {"PROJETO": "Energia Certa", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para simulação de consumo, economia de energia, cálculo de retorno de investimento e sugestões para residências e empresas.", "SITE": ""},
    {"PROJETO": "Sabor da Terra", "TIPO": "Startup", "DESCRIÇÃO": "Valorização dos produtos regionais do campo à mesa, fortalecendo o pequeno produtor com logística e marketplace.", "SITE": ""},
    {"PROJETO": "Rede Mulher", "TIPO": "Startup", "DESCRIÇÃO": "Rede de apoio ao empreendedorismo feminino, mentorias, formação e canal para venda de produtos/serviços feitos por mulheres.", "SITE": ""},
    {"PROJETO": "CicloTech", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para transporte sustentável em bicicletas, monitoramento de trajetos e incentivo à mobilidade ativa.", "SITE": ""},
    {"PROJETO": "Foco na Escola", "TIPO": "Startup", "DESCRIÇÃO": "Gestão participativa para escolas públicas, integração entre pais, alunos e educadores, eventos e resultados escolares.", "SITE": ""},
    {"PROJETO": "Conecta Saúde", "TIPO": "Startup", "DESCRIÇÃO": "Integração de serviços de saúde para a população, telemedicina, prontuário digital e agendamento centralizado.", "SITE": ""},
    {"PROJETO": "Água na Medida", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento inteligente para consumo consciente de água, alertas de vazamento e economia doméstica.", "SITE": ""},
    {"PROJETO": "FitBem", "TIPO": "Startup", "DESCRIÇÃO": "Aplicativo de exercícios personalizados, rotina de atividades, nutrição e acompanhamento remoto de treinos.", "SITE": ""},
    {"PROJETO": "EducaFácil", "TIPO": "Startup", "DESCRIÇÃO": "Ferramentas digitais para apoio escolar, avaliação diagnóstica e reforço para estudantes com dificuldades.", "SITE": ""},
    {"PROJETO": "Protetor Solar", "TIPO": "Startup", "DESCRIÇÃO": "Dispositivos para proteção contra raios solares, orientação personalizada para evitar câncer de pele.", "SITE": ""},
    {"PROJETO": "Saúde Animal", "TIPO": "Startup", "DESCRIÇÃO": "Veterinária móvel para comunidades rurais e urbanas, vacinação, consultas e adoção responsável.", "SITE": ""},
    {"PROJETO": "Tech Rural", "TIPO": "Startup", "DESCRIÇÃO": "Automação agrícola acessível, sensores de umidade e solo, controle de irrigação e produtividade para pequenos produtores.", "SITE": ""},
    {"PROJETO": "Comida Boa", "TIPO": "Startup", "DESCRIÇÃO": "Delivery de refeições saudáveis, naturais e artesanais, feitas por chefs e cozinheiros da região.", "SITE": ""},
    {"PROJETO": "ID Agro", "TIPO": "Startup", "DESCRIÇÃO": "Identificação digital de produtos agropecuários, rastreabilidade e selo de procedência para consumidores.", "SITE": ""},
    {"PROJETO": "Turismo Digital", "TIPO": "Startup", "DESCRIÇÃO": "Experiência turística digital, roteiros personalizados, informações e vendas de pacotes pelo app.", "SITE": ""},
    {"PROJETO": "Educador+Fácil", "TIPO": "Startup", "DESCRIÇÃO": "Apoio didático para professores do ensino básico, banco de planos de aula e compartilhamento de experiências.", "SITE": ""},
    {"PROJETO": "EcoJovem", "TIPO": "Startup", "DESCRIÇÃO": "Educação ambiental para adolescentes em escolas públicas, oficinas práticas e monitoramento de resultados.", "SITE": ""},
    {"PROJETO": "Viva Bem+", "TIPO": "Startup", "DESCRIÇÃO": "Comunidade de autocuidado para adultos maduros, eventos, rodas de conversa e acompanhamento multidisciplinar.", "SITE": ""},
    {"PROJETO": "Reforma Já", "TIPO": "Startup", "DESCRIÇÃO": "Facilita cotações e reformas de imóveis, rede de profissionais avaliados e garantia de entrega.", "SITE": ""},
    {"PROJETO": "Nova Chance", "TIPO": "Startup", "DESCRIÇÃO": "Capacitação e inserção de jovens no mercado de trabalho, com acompanhamento e vagas inclusivas.", "SITE": ""},
    {"PROJETO": "Árvore Azul", "TIPO": "Startup", "DESCRIÇÃO": "Conservação ambiental com reflorestamento urbano, educação ambiental em escolas e comunidades.", "SITE": ""},
    {"PROJETO": "InovaCom", "TIPO": "Startup", "DESCRIÇÃO": "Comunicação e marketing digital para pequenos negócios, com foco em fortalecimento de marca local.", "SITE": ""},
    {"PROJETO": "Meu Pet Online", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma digital para adoção, cuidados, informações veterinárias e venda de produtos para pets.", "SITE": ""},
    {"PROJETO": "Orgânicos do Vale", "TIPO": "Startup", "DESCRIÇÃO": "Venda direta de produtos orgânicos, assinaturas semanais e pontos de entrega em toda a região.", "SITE": ""},
    {"PROJETO": "Recria", "TIPO": "Startup", "DESCRIÇÃO": "Brinquedos sustentáveis de material reciclado, oficinas de educação ambiental e vendas online.", "SITE": ""},
    {"PROJETO": "InovaBem", "TIPO": "Startup", "DESCRIÇÃO": "Soluções inovadoras para ONGs sociais, captação de recursos, gestão e avaliação de impacto.", "SITE": ""},
    {"PROJETO": "Viva Eco", "TIPO": "Startup", "DESCRIÇÃO": "Produtos ecológicos e sustentáveis para o dia a dia, consultoria e eventos de educação ambiental.", "SITE": ""},
    {"PROJETO": "Saúde Total", "TIPO": "Startup", "DESCRIÇÃO": "Monitoramento integrado de saúde familiar, plataforma para registros, vacinas, consultas e exames.", "SITE": ""},
    {"PROJETO": "Rede Cidadã", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de participação cidadã digital, consulta pública, votação e acompanhamento de políticas públicas.", "SITE": ""},
    {"PROJETO": "DoCampo", "TIPO": "Startup", "DESCRIÇÃO": "Facilita a compra de produtos diretamente do produtor rural para consumidores urbanos, sem intermediários.", "SITE": ""},
    {"PROJETO": "Digitaliza+", "TIPO": "Startup", "DESCRIÇÃO": "Transformação digital acessível para pequenas empresas, com consultoria, treinamento e implantação de sistemas online.", "SITE": ""},
    {"PROJETO": "AgroSabores", "TIPO": "Startup", "DESCRIÇÃO": "Incentivo a pequenos produtores de alimentos gourmet, assessoria em marketing, embalagem e acesso a mercados especiais.", "SITE": ""},
    {"PROJETO": "Conecta Verde", "TIPO": "Startup", "DESCRIÇÃO": "Rede colaborativa para restauração ecológica, plantio de mudas e mapeamento de áreas degradadas.", "SITE": ""},
    {"PROJETO": "Saúde no Campo", "TIPO": "Startup", "DESCRIÇÃO": "Unidades móveis de atendimento em áreas rurais, exames, consultas, prevenção e vacinação itinerante.", "SITE": ""},
    {"PROJETO": "Engenho Criativo", "TIPO": "Startup", "DESCRIÇÃO": "Coworking maker para inovação local, prototipagem rápida, cursos de robótica e fabricação digital.", "SITE": ""},
    {"PROJETO": "Mundo Tech", "TIPO": "Startup", "DESCRIÇÃO": "Educação tecnológica para adolescentes, robótica, programação, impressão 3D e iniciação científica.", "SITE": ""},
    {"PROJETO": "Vila Digital", "TIPO": "Startup", "DESCRIÇÃO": "Inclusão digital em comunidades remotas, cursos de informática, acesso à internet e cidadania digital.", "SITE": ""},
    {"PROJETO": "Conecta Pais", "TIPO": "Startup", "DESCRIÇÃO": "Rede de apoio parental, educação familiar, grupos de pais, trocas de experiências e dicas práticas.", "SITE": ""},
    {"PROJETO": "EcoConecta", "TIPO": "Startup", "DESCRIÇÃO": "Comunicação estratégica para causas ambientais, campanhas, eventos e sensibilização nas mídias sociais.", "SITE": ""},
    {"PROJETO": "Alimento Justo", "TIPO": "Startup", "DESCRIÇÃO": "Distribuição de alimentos excedentes para combate à fome, parcerias com supermercados e bancos de alimentos.", "SITE": ""},
    {"PROJETO": "Aprenda Verde", "TIPO": "Startup", "DESCRIÇÃO": "Educação ambiental lúdica para crianças, oficinas, jogos, atividades práticas e conteúdo online.", "SITE": ""},
    {"PROJETO": "Mobiliza+", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para ações sociais, mobilização de voluntários e doações em causas comunitárias.", "SITE": ""},
    {"PROJETO": "NutriFácil", "TIPO": "Startup", "DESCRIÇÃO": "App para orientação nutricional personalizada, receitas saudáveis e acompanhamento com profissionais.", "SITE": ""},
    {"PROJETO": "Conecta Artes", "TIPO": "Startup", "DESCRIÇÃO": "Divulgação, venda e conexão de artistas locais, eventos culturais e oficinas de arte.", "SITE": ""},
    {"PROJETO": "VerdeSustentável", "TIPO": "Startup", "DESCRIÇÃO": "Consultoria e produtos para vida sustentável, construção ecológica, hortas e energia renovável.", "SITE": ""},
    {"PROJETO": "Jovem Protagonista", "TIPO": "Startup", "DESCRIÇÃO": "Capacitação, protagonismo juvenil, participação cidadã, oficinas e apoio a projetos liderados por jovens.", "SITE": ""},
    {"PROJETO": "Pet Protegido", "TIPO": "Startup", "DESCRIÇÃO": "Serviço de emergência 24h para animais de estimação, resgate, socorro veterinário e teleorientação.", "SITE": ""},
    {"PROJETO": "Inclusão Digital", "TIPO": "Startup", "DESCRIÇÃO": "Alfabetização digital para idosos, acesso à tecnologia, inclusão social e comunicação com familiares.", "SITE": ""},
    {"PROJETO": "Cozinha Viva", "TIPO": "Startup", "DESCRIÇÃO": "Aulas de culinária saudável, receitas acessíveis, aproveitamento integral dos alimentos e economia doméstica.", "SITE": ""},
    {"PROJETO": "Viver Melhor", "TIPO": "Startup", "DESCRIÇÃO": "Acompanhamento multidisciplinar de saúde para idosos, fisioterapia, nutrição e lazer.", "SITE": ""},
    {"PROJETO": "Rede Agro", "TIPO": "Startup", "DESCRIÇÃO": "Integração de cadeias produtivas agrícolas, logística, comercialização e compartilhamento de máquinas.", "SITE": ""},
    {"PROJETO": "TechJovem", "TIPO": "Startup", "DESCRIÇÃO": "Ensino de programação, robótica e iniciação tecnológica para jovens em situação de vulnerabilidade.", "SITE": ""},
    {"PROJETO": "SolarFácil", "TIPO": "Startup", "DESCRIÇÃO": "Instalação facilitada de painéis solares, simulação de economia e financiamento acessível.", "SITE": ""},
    {"PROJETO": "Renda Extra", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma para geração de renda complementar, microtrabalho e capacitação profissional.", "SITE": ""},
    {"PROJETO": "Biblioteca Livre", "TIPO": "Startup", "DESCRIÇÃO": "Espaços colaborativos de leitura em bairros, acervos compartilhados e incentivo à cultura local.", "SITE": ""},
    {"PROJETO": "Comida de Verdade", "TIPO": "Startup", "DESCRIÇÃO": "Educação alimentar, combate ao desperdício, incentivo ao consumo consciente e alimentação saudável.", "SITE": ""},
    {"PROJETO": "Protetor Social", "TIPO": "Startup", "DESCRIÇÃO": "Rede de proteção para famílias vulneráveis, apoio jurídico, psicológico e acesso a benefícios sociais.", "SITE": ""},
    {"PROJETO": "Cultura Popular", "TIPO": "Startup", "DESCRIÇÃO": "Valorização das tradições, festas populares, grupos folclóricos e cultura afro-brasileira.", "SITE": ""},
    {"PROJETO": "InovaSaúde", "TIPO": "Startup", "DESCRIÇÃO": "Gestão inovadora para unidades de saúde, digitalização de prontuários, telemedicina e redução de filas.", "SITE": ""},
    {"PROJETO": "Amparo Animal", "TIPO": "Startup", "DESCRIÇÃO": "Rede de acolhimento, adoção responsável, resgate e reabilitação de animais em situação de abandono.", "SITE": ""},
    {"PROJETO": "Trilhas do Saber", "TIPO": "Startup", "DESCRIÇÃO": "Roteiros educativos em parques e espaços públicos, oficinas de meio ambiente, educação patrimonial e cidadania.", "SITE": ""},
    {"PROJETO": "Mulher Empreende", "TIPO": "Startup", "DESCRIÇÃO": "Apoio ao empreendedorismo feminino em regiões periféricas, microcrédito, formação e rede de negócios solidários.", "SITE": ""},
    {"PROJETO": "TechSocial", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia para impacto social em comunidades carentes, coleta de dados, inclusão digital e participação cidadã.", "SITE": ""},
    {"PROJETO": "Saúde Conectada", "TIPO": "Startup", "DESCRIÇÃO": "Teleatendimento para comunidades remotas, encaminhamento de exames e acompanhamento por equipe multiprofissional.", "SITE": ""},
    {"PROJETO": "Verde Mais", "TIPO": "Startup", "DESCRIÇÃO": "Produtos ecológicos para consumo consciente, consultoria ambiental e campanhas de educação sustentável.", "SITE": ""},
    {"PROJETO": "Nova Vida", "TIPO": "Startup", "DESCRIÇÃO": "Reintegração social de pessoas em situação de rua, capacitação, geração de renda e apoio psicológico.", "SITE": ""},
    {"PROJETO": "Jovem Ativo", "TIPO": "Startup", "DESCRIÇÃO": "Plataforma de esportes, lazer, saúde e formação cidadã para juventude periférica.", "SITE": ""},
    {"PROJETO": "Gastronomia Social", "TIPO": "Startup", "DESCRIÇÃO": "Cursos de culinária, empregabilidade, alimentação saudável e inserção no mercado gastronômico.", "SITE": ""},
    {"PROJETO": "Solar Comunidade", "TIPO": "Startup", "DESCRIÇÃO": "Energia solar compartilhada para bairros carentes, redução de custos e geração de renda.", "SITE": ""},
    {"PROJETO": "AgroForte", "TIPO": "Startup", "DESCRIÇÃO": "Assistência técnica para pequenos produtores rurais, inovação no campo, novas culturas e gestão de produção.", "SITE": ""},
    {"PROJETO": "Inclusão para Todos", "TIPO": "Startup", "DESCRIÇÃO": "Tecnologia assistiva, acessibilidade digital, adaptação de conteúdos e formação em inclusão para educadores.", "SITE": ""},
    {"PROJETO": "Verde Escola", "TIPO": "Startup", "DESCRIÇÃO": "Educação ambiental integrada ao currículo escolar, projetos ecológicos, hortas, reciclagem e participação estudantil.", "SITE": ""},
    {"PROJETO": "Viva Cidade", "TIPO": "Startup", "DESCRIÇÃO": "Qualidade de vida urbana para a terceira idade, lazer, mobilidade, saúde e integração social.", "SITE": ""}
]
df_projetos = pd.DataFrame(projetos)
df_projetos["Selecionar"] = False
)
st.markdown("# 🏆 Avaliação de Projetos")
st.markdown("## 📋 Lista completa dos projetos inscritos")

st.write(
    "Leia atentamente os projetos abaixo. "
    "Use a tabela para selecionar até 10 projetos para avaliação. "
    "A descrição completa de cada projeto pode ser lida logo abaixo da tabela:"
)

# Tabela resumida apenas para seleção rápida (projeto, tipo, selecionar)
df_selecao = df_projetos[["PROJETO", "TIPO"]].copy()
df_selecao["Selecionar"] = False

df_editado = st.data_editor(
    df_selecao,
    column_config={
        "Selecionar": st.column_config.CheckboxColumn(
            "Selecionar para avaliar",
            help="Marque para escolher este projeto",
            default=False,
        ),
        "PROJETO": "Projeto",
        "TIPO": "Tipo",
    },
    hide_index=True,
    use_container_width=True,
)

selecionados = df_editado[df_editado["Selecionar"] == True]
qtd_selecionados = len(selecionados)
qtd_restante = 10 - qtd_selecionados

if qtd_selecionados > 10:
    st.error("Você selecionou mais de 10 projetos. Por favor, desmarque até ficar com apenas 10.")
else:
    if qtd_selecionados < 10:
        st.success(f"{qtd_selecionados} projeto(s) selecionado(s). Faltam {qtd_restante} para completar 10.")
    else:
        st.success("Você já selecionou os 10 projetos!")

avaliadores = ["Avaliador 1", "Avaliador 2", "Avaliador 3", "Avaliador 4", "Avaliador 5"]
avaliador = st.sidebar.selectbox("Selecione seu nome", avaliadores)

if st.button("Confirmar seleção dos projetos"):
    if qtd_selecionados != 10:
        st.warning("Selecione exatamente 10 projetos para prosseguir.")
        st.stop()
    st.session_state[f'selecoes_{avaliador}'] = selecionados["PROJETO"].tolist()
    st.success("Seleção salva! Prossiga para a etapa de pontuação.")

# --- Descrição expandida dos projetos (sempre visível para leitura fácil) ---
st.markdown("### 📝 Descrição completa dos projetos")
for idx, row in df_projetos.iterrows():
    with st.expander(f"{row['PROJETO']} [{row['TIPO']}]"):
        st.markdown(f"**Descrição:** {row['DESCRIÇÃO']}")
        if row['SITE']:
            st.markdown(f"🌐 [Site oficial]({row['SITE']})")

# ETAPA 2: Avaliação individual do avaliador
if st.session_state.get(f'selecoes_{avaliador}', []):
    projetos_selecionados = st.session_state[f'selecoes_{avaliador}']
    if len(projetos_selecionados) < 10:
        st.warning("Você precisa selecionar exatamente 10 projetos na etapa anterior para avaliá-los.")
        st.stop()
    st.markdown("## Etapa 2: Avalie os 10 projetos que você escolheu")
    st.info("Para cada projeto, preencha todos os critérios abaixo. Só será possível salvar ao avaliar todos.")

    criterios = [
        "Modelo de Negócio",
        "Escalabilidade",
        "Viabilidade Econômica e Financeira",
        "Alinhamento com os Potenciais de Desenvolvimento do Espírito Santo",
        "Potencial de Expansão Nacional e Internacional"
    ]
    pesos = {"Alto": 3, "Médio": 2, "Baixo": 1}

    pontuacoes = st.session_state.get(f'pontuacoes_{avaliador}_tmp', [])
    if not pontuacoes or len(pontuacoes) != len(projetos_selecionados):
        pontuacoes = []
        for projeto in projetos_selecionados:
            p = {"Projeto": projeto}
            for c in criterios:
                p[c] = 2  # Médio como padrão
            pontuacoes.append(p)

    todos_avaliados = True
    for idx, projeto in enumerate(projetos_selecionados):
        st.markdown(f"### {projeto}")
        st.dataframe(df_projetos[df_projetos["PROJETO"] == projeto][["PROJETO", "TIPO", "DESCRIÇÃO", "SITE"]], use_container_width=True)
        for c in criterios:
            key_radio = f"{avaliador}_{projeto}_{c}"
            valor_atual = pontuacoes[idx][c] if c in pontuacoes[idx] else 2
            index = {3: 0, 2: 1, 1: 2}.get(valor_atual, 1)
            val = st.radio(
                f"{c} ({projeto})",
                options=["Alto", "Médio", "Baixo"],
                index=index,
                key=key_radio,
                horizontal=True
            )
            pontuacoes[idx][c] = pesos[val]
        if any(pontuacoes[idx][c] not in [1,2,3] for c in criterios):
            todos_avaliados = False

    st.session_state[f'pontuacoes_{avaliador}_tmp'] = pontuacoes

    if st.button("Salvar pontuações"):
        if not todos_avaliados:
            st.warning("Avalie todos os critérios de todos os projetos antes de salvar!")
        else:
            st.session_state[f'pontuacoes_{avaliador}'] = pontuacoes
            st.success("Pontuações salvas! Seu ranking já aparece abaixo.")

# ETAPA 3: Ranking geral consolidado
st.markdown("## Ranking Final dos Projetos")
avaliadores_lista = ["Avaliador 1", "Avaliador 2", "Avaliador 3", "Avaliador 4", "Avaliador 5"]
todas_pontuacoes = []
for a in avaliadores_lista:
    resp = st.session_state.get(f'pontuacoes_{a}', [])
    for r in resp:
        r_copia = r.copy()
        r_copia["Avaliador"] = a
        todas_pontuacoes.append(r_copia)

def calcular_ranking(pontuacoes_avaliadores):
    df = pd.DataFrame(pontuacoes_avaliadores)
    if df.empty:
        return pd.DataFrame()
    crits = [c for c in df.columns if c not in ['Projeto','Avaliador']]
    df['Total'] = df[crits].sum(axis=1)
    ranking = df.groupby('Projeto')['Total'].sum().reset_index()
    ranking = ranking.sort_values('Total', ascending=False).reset_index(drop=True)
    return ranking

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
    st.info("O ranking será exibido após as primeiras avaliações serem concluídas.")

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
    st.info("As respostas aparecerão aqui após as avaliações.")

with st.expander("Como funciona?"):
    st.write("""
    1. Escolha 10 projetos na lista geral.
    2. Leia a descrição de cada projeto clicando no nome na lista expandida.
    3. Avalie apenas os 10 escolhidos nos 5 critérios.
    4. Salve suas avaliações.
    5. O sistema mostra o ranking geral dos projetos mais bem avaliados (TOP 5).
    """)
