# Importando bibliotecas necessárias para o projeto.
from faker import Faker
import random
from datetime import datetime
import csv

# Variáveis globais para controle de IDs.
ULTIMO_ID_MODULO = 0
ULTIMO_ID_AULA = 0

ULTIMO_ID_MATRICULA = 0
ULTIMO_ID_PROGRESSO = 0

IDS_ALUNOS_REAIS = list(range(1, 31))
IDS_CURSOS_REAIS = list(range(4, 24))    
IDS_AULAS_REAIS = list(range(1, 1001))


# Configurando o gerador de dados para a língua portuguesa.
fake = Faker('pt_BR')

# Função para exportar os dados gerados para arquivos CSV.
def exportar_para_csv():
    colunas_alunos = ['nome', 'email', 'data_nascimento', 'data_cadastro']
    caminho_arquivo = 'data/alunos.csv'
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas_alunos)
        writer.writeheader()
        for aluno in dados_dos_alunos:
            writer.writerow(aluno)

    colunas_instrutores = ['nome', 'email', 'especialidade', 'biografia']
    caminho_arquivo = 'data/instrutores.csv'
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas_instrutores)
        writer.writeheader()
        for instrutor in dados_dos_instrutores:
            writer.writerow(instrutor)

    colunas_cursos = ['titulo', 'descricao', 'categoria_id', 'instrutor_id', 'preco', 'carga_horaria', 'nivel', 'data_criacao']
    caminho_arquivo = 'data/cursos.csv'
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas_cursos)
        writer.writeheader()
        for curso in dados_dos_cursos:
            writer.writerow(curso)

    colunas_modulos = ['id', 'curso_id', 'titulo', 'ordem', 'descricao']
    caminho_arquivo = 'data/modulos.csv'
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas_modulos)
        writer.writeheader()
        for modulo in dados_dos_modulos:
            writer.writerow(modulo)
    
    colunas_aulas = ['id', 'modulo_id', 'titulo', 'ordem', 'duracao_minutos', 'tipo']
    caminho_arquivo = 'data/aulas.csv'
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas_aulas)
        writer.writeheader()
        for aula in dados_das_aulas:
            writer.writerow(aula)
    
    colunas_matriculas = ['id', 'aluno_id', 'curso_id', 'data_matricula', 'data_conclusao', 'status', 'valor_pago']
    caminho_arquivo = 'data/matriculas.csv'
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas_matriculas)
        writer.writeheader()
        for matricula in dados_das_matriculas:
            writer.writerow(matricula)
    
    colunas_progresso = ['matricula_id', 'aula_id', 'concluida', 'data_conclusao', 'tempo_assistido_minutos']
    caminho_arquivo = 'data/progresso_aulas.csv'
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas_progresso)
        writer.writeheader()
        for progresso in dados_do_progresso:
            writer.writerow(progresso)

    colunas_avaliacoes = ['matricula_id', 'curso_id', 'nota', 'comentario', 'data_avaliacao']
    caminho_arquivo = 'data/avaliacoes.csv'
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=colunas_avaliacoes)
        writer.writeheader()
        for avaliacao in dados_das_avaliacoes:
            writer.writerow(avaliacao)

# Função para gerar os dados fictícios dos alunos.
def gerar_alunos(quantidade):
    alunos = []
    for _ in range(quantidade):
        nome = fake.name()
        email = fake.unique.email()
        data_nascimento = fake.date_of_birth(minimum_age=16, maximum_age=65)
        data_cadastro = fake.date_between(start_date='-2y', end_date='today')

        aluno = {
        'nome': nome,
        'email': email,
        'data_nascimento': data_nascimento,
        'data_cadastro': data_cadastro
    }
        alunos.append(aluno)
    return alunos

def gerar_instrutores(quantidade):
    instrutores = []
    for _ in range(quantidade):
        nome = fake.name()
        email = fake.unique.email()
        especialidade = random.choice ([
            'Desenvolvimento Web', 
            'Ciência de Dados', 
            'Design UX/UI', 
            'Marketing Digital', 
            'Gestão de Projetos', 
            'Cibersegurança', 
            'Cloud Computing', 
            'Inteligência Artificial'])
        
        anos_experiencia = random.randint(3, 20)
        empresa = fake.company()
        cidade = fake.city()

        tamplate_biografia = [
            f"{nome} é especialista em {especialidade} com {anos_experiencia} anos de experiência. Trabalhou em empresas como {empresa} e é apaixonado por ensinar.",
            f"Com {anos_experiencia} anos atuando em {especialidade}, {nome} tem sede em compartilhar seu conhecimento. Atualmente reside em {cidade}.",
            f"{nome} é um profissional experiente em {especialidade}, com passagens por empresas renomadas como {empresa}. Apaixonado por ensinar e pela sua cidade natal, {cidade}."
        ]
        biografia = random.choice(tamplate_biografia)

        instrutor = {
            'nome': nome,
            'email': email,
            'especialidade': especialidade,
            'biografia': biografia
        }
        instrutores.append(instrutor)
    return instrutores

def gerar_cursos(quantidade):

    id_categorias = [1, 2, 3, 4, 5]
    id_instrutores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    nomes_categorias_map = {
    1: 'Desenvolvimento Web', 
    2: 'Ciência de Dados e IA',
    3: 'Design UX/UI',
    4: 'Infraestrutura e Segurança',
    5: 'Gestão e Marketing',
}
    cursos_titulos_map = {
    'Desenvolvimento Web': ['Curso Completo de HTML, CSS e JavaScript', 'Desenvolvimento Back-end com Python e Django', 'React: Construindo Interfaces Dinâmicas'],
    'Ciência de Dados e IA': ['Machine Learning para Iniciantes', 'Análise de Dados com Python e Pandas', 'Visualização de Dados com Power BI', 'Introdução a Redes Neurais', 'Processamento de Linguagem Natural (NLP)'],
    'Design UX/UI': ['Figma para Designers', 'UX Design: da Pesquisa à Prototipagem', 'UI Design: Criando Interfaces Incríveis'],
    'Infraestrutura e Segurança': ['Fundamentos de Cibersegurança e Hacking Ético', 'Segurança em Redes e Sistemas Operacionais', 'AWS para Iniciantes', 'Fundamentos do Google Cloud (GCP)', 'Infraestrutura como Código com Terraform'],
    'Gestão e Marketing': ['Marketing nas Mídias Sociais', 'Análise de Campanhas e Google Analytics', 'Metodologias Ágeis (Scrum e Kanban)', 'Gestão de Projetos com Trello e Asana'],
}

    cursos = []
    for _ in range(quantidade):
       
        categorias_id_fk = random.choice(id_categorias)
        instrutores_id_fk = random.choice(id_instrutores)

        nome_categoria = nomes_categorias_map.get(categorias_id_fk)
        titulos_disponiveis = cursos_titulos_map.get(nome_categoria)
        titulo = random.choice(titulos_disponiveis)

        tamplate_descricao = [
            f"Domine {titulo}. Este curso é focado na aplicação prática do conhecimento, com exemplos do mundo real. Aprenda as ferramentas e conceitos essenciais que o mercado exige para iniciar sua jornada ou aprofundar suas habilidades.",
            f"Transforme sua carreira com o curso {titulo}. Com este treinamento, você construirá uma base sólida e estará apto a executar projetos complexos. Inclui exercícios práticos e acesso à comunidade de alunos.",
            f"Mergulhe na profundidade de {titulo}. Este é um curso ideal para quem busca uma qualificação aprofundada. Nossas aulas são projetadas para desafiar e elevar o seu conhecimento a um novo patamar de excelência."
        ]
        
        descricao = random.choice(tamplate_descricao)
        preco_bruto = random.uniform(49.90, 499.90)
        preco = round(preco_bruto, 2)

        carga_horaria = random.choice ([40, 80, 120, 200, 240, 320, 400])
        nivel = random.choice (['Iniciante', 'Intermediário', 'Avançado'])
        data_criacao = fake.date_between(start_date='-2y', end_date='today')

        curso = {
            'titulo': titulo,
            'descricao': descricao,
            'categoria_id': categorias_id_fk,
            'instrutor_id': instrutores_id_fk,
            'preco': preco,
            'carga_horaria': carga_horaria,
            'nivel': nivel,
            'data_criacao': data_criacao
        }
        cursos.append(curso)
    return cursos


def gerar_aulas(curso_id, quantidade):

    global ULTIMO_ID_AULA, ULTIMO_ID_MODULO
    
    if not isinstance(curso_id, int) or curso_id <= 0:
        raise ValueError("curso_id deve ser um inteiro positivo")
    if not isinstance(quantidade, int) or quantidade <= 0:
        raise ValueError("quantidade deve ser um inteiro positivo")
    
    if quantidade > 500:
        quantidade = 500
    
    modulos = []
    aulas = []

    temas_modulos = [
        "Fundamentos e Introdução",
        "Conceitos Básicos",
        "Técnicas Avançadas",
        "Prática e Exercícios",
        "Projetos Reais",
        "Otimização e Performance",
        "Boas Práticas",
        "Ferramentas e Recursos",
        "Casos de Uso",
        "Conclusão e Próximos Passos"
    ]

    descricao_modulos = [
        f"Neste módulo, você mergulhará em conhecimento. Vamos cobrir desde a instalação das ferramentas necessárias até as primeiras linhas de código. Essencial para criar sua base de conhecimento.",
        f"Chegou a hora de colocar a mão na massa! O módulo é focado em exercícios práticos e na construção de um mini-projeto. Ao final, você terá a confiança para aplicar o que aprendeu.",
        f"Com este módulo, você explorará técnicas avançadas de otimização e performance. Iremos além do básico para garantir que seus projetos sejam rápidos, robustos e sigam as melhores práticas do mercado.",
        f"Este módulo final, consolida todo o conhecimento adquirido. Revisaremos os pontos principais e faremos um projeto de conclusão. O próximo passo para a sua certificação começa aqui!"
    ]
    
    num_modulos = random.randint(3, 6)  
    aulas_por_modulo = quantidade // num_modulos
    aulas_restantes = quantidade % num_modulos
    
    for i in range(num_modulos):
       
        ULTIMO_ID_MODULO += 1

        tema_modulo = random.choice(temas_modulos)
        descricao = random.choice(descricao_modulos)
        
        modulo = {
            'id': ULTIMO_ID_MODULO,
            'curso_id': curso_id,
            'titulo': f"Módulo {i+1}: {tema_modulo}",
            'ordem': i + 1,
            'descricao': descricao 
        }
        modulos.append(modulo)
        
        if i == num_modulos - 1:  
            num_aulas_modulo = aulas_por_modulo + aulas_restantes
        else:
            num_aulas_modulo = aulas_por_modulo
        
        for j in range(num_aulas_modulo):

            ULTIMO_ID_AULA += 1
            
            tipo_aula = random.choices(
                ['Vídeo', 'Texto', 'Quiz'],
                weights=[60, 25, 15],  
                k=1
            )[0]
            
            titulo = f"{random.choice(['Introdução a', 'Como Funciona', 'Implementando'])} {fake.catch_phrase()}"
            
            if tipo_aula == 'Vídeo':
                duracao = random.randint(8, 45)  
            elif tipo_aula == 'Texto':
                duracao = random.randint(5, 20)
            else: 
                duracao = random.randint(5, 15)
            
            aula = {
                'id': ULTIMO_ID_AULA,
                'modulo_id': ULTIMO_ID_MODULO,
                'titulo': titulo,
                'ordem': j + 1, 
                'duracao_minutos': duracao,
                'tipo': tipo_aula
            }
            aulas.append(aula)
    
    return modulos, aulas

def gerar_matriculas(quantidade):
    
    global ULTIMO_ID_MATRICULA, ULTIMO_ID_PROGRESSO
    
    matriculas = []
    progresso_total = []
    avaliacoes = []
    
    for _ in range(quantidade):
        ULTIMO_ID_MATRICULA += 1
        
        
        aluno_id = random.choice(IDS_ALUNOS_REAIS)
        curso_id = random.choice(IDS_CURSOS_REAIS)
        
        
        status = random.choices(['ativa', 'concluída', 'cancelada'], weights=[60, 25, 15], k=1)[0]
        
        data_matricula = fake.date_time_between(start_date='-2y', end_date='-3m')
        
       
        data_conclusao_matricula = None
        if status == 'concluída':
            data_conclusao_matricula = fake.date_time_between(start_date=data_matricula, end_date='now')
        
        matricula_valor = round(random.uniform(49.90, 499.90), 2)
        
        
        matriculas.append({
            'id': ULTIMO_ID_MATRICULA, 
            'aluno_id': aluno_id, 
            'curso_id': curso_id,
            'data_matricula': data_matricula, 
            'data_conclusao': data_conclusao_matricula, 
            'status': status.capitalize(), 
            'valor_pago': matricula_valor
        })
        
       
        if status != 'cancelada':
            
            
            if status == 'concluída':
                percentual_concluido = random.uniform(0.9, 1.0) 
            else: 
                percentual_concluido = random.uniform(0.3, 0.7) 

            
            num_aulas_a_processar = int(len(IDS_AULAS_REAIS) * 0.5)
            aulas_processar = random.sample(IDS_AULAS_REAIS, k=num_aulas_a_processar) 
            
            for aula_id in aulas_processar:
                ULTIMO_ID_PROGRESSO += 1
                
                
                concluida = random.random() < percentual_concluido
                
                progresso_total.append({
                    'matricula_id': ULTIMO_ID_MATRICULA, 
                    'aula_id': aula_id, 
                    'concluida': concluida,
                    'data_conclusao': fake.date_time_between(start_date=data_matricula, end_date='now') if concluida else None,
                    'tempo_assistido_minutos': random.randint(1, 45) if concluida else 0
                })

        tamplate_comentario = [
           "Curso excelente! Aprendi muito e recomento a todos que estão começando na área.",
           "O conteúdo foi muito bem explicado e os exemplos práticos ajudaram bastante.",
           "Gostei do curso, mas senti falta de mais exercícios práticos.",
           "O instrutor foi muito claro e objetivo. A didática dele facilitou meu aprendizado.",
           "Curso muito bom, mas poderia ter mais material complementar para estudo.",
           "Gostei bastante! Indico muito!",
           "O curso superou minhas expectativas. Conteúdo de alta qualidade."
       ]
    
        comentario = random.choice(tamplate_comentario)

        if status == 'concluída':
            data_avaliacao_final = fake.date_time_between(start_date=data_conclusao_matricula, end_date='now')
            nota = random.randint(3, 5)
            avaliacoes.append({
                'matricula_id': ULTIMO_ID_MATRICULA, 
                'curso_id': curso_id, 
                'nota': nota,
                'comentario': comentario,
                'data_avaliacao': data_avaliacao_final
            })
            
    return matriculas, progresso_total, avaliacoes

# Chamando as funções para gerar dados fictícios.

dados_dos_alunos = gerar_alunos(30)

dados_dos_instrutores = gerar_instrutores(10)

dados_dos_cursos = gerar_cursos(20)

dados_dos_modulos = []
dados_das_aulas = []

for curso_id in range(4, 24): 
    modulos, aulas = gerar_aulas(curso_id, 50)
    dados_dos_modulos.extend(modulos)
    dados_das_aulas.extend(aulas)

    dados_das_matriculas, dados_do_progresso, dados_das_avaliacoes = gerar_matriculas(100)

exportar_para_csv()