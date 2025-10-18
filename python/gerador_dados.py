# Importando bibliotecas necessárias para o projeto.
from faker import Faker
import random
from datetime import datetime
import csv

# Configurando o gerador de dados para a língua portuguesa.
fake = Faker('pt_BR')

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
    



    


   
dados_dos_alunos = gerar_alunos(30)
for aluno in dados_dos_alunos:
   print(aluno)
   

dados_dos_instrutores = gerar_instrutores(10)
for instrutor in dados_dos_instrutores:
    print(instrutor)
    

dados_dos_cursos = gerar_cursos(20)
for curso in dados_dos_cursos:
    print(curso)

    exportar_para_csv()
