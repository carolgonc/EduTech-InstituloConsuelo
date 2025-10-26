# 📚 Sistema de Gerenciamento de Cursos Online (EduTech)

## 📌 Descrição do Projeto
Este projeto consiste na criação de um robusto Sistema de Gerenciamento de Cursos Online (EduTech), focado principalmente no desenvolvimento Back-end e na modelagem e consulta de banco de dados. O sistema simula a estrutura de dados de uma plataforma de e-learning, demonstrando o domínio em SQL para APIs REST futuras.
O foco principal (70%) está na modelagem relacional de dados normalizados e em consultas SQL avançadas. O restante (30%) é dedicado a scripts auxiliares em Python para processamento, geração e validação de dados

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Justificativa / Uso no Projeto |
| :--- | :--- | :--- |
| **Banco de Dados** | **PostgreSQL** | SGBD robusto utilizado para o schema, consultas avançadas e armazenamento dos dados. |
| **Linguagem (Auxiliar)** | **Python 3.x** | Utilizado para scripts de Geração de Dados Fictícios e processamento de relatórios, simulando a camada de API. |
| **Geração de Dados** | **Faker** | Biblioteca essencial para gerar dados fictícios, realistas e em volume (e-mails, nomes, datas). |
| **Manipulação de Dados** | **Módulo CSV (Python)** | Utilizado para importar e exportar os dados do Python para o PostgreSQL. |


## 🚀 Como Executar o Projeto
Siga os passos abaixo para configurar o ambiente e popular o banco de dados.

### 1. Configuração do PostgreSQL
- Instale o PostgreSQL e um cliente SQL (pgAdmin ou DBeaver).

- Crie um novo banco de dados vazio (ex: edutech_db).

- Execute o arquivo schema.sql para criar todas as 9 tabelas do sistema.

### 2. População de Dados Manuais (SQL)
Execute o arquivo dados.sql para inserir as categorias e outros dados de referência diretamente no PostgreSQL. Isto é crucial para as chaves estrangeiras.

### 3. Configuração do Ambiente Python
Crie e ative um ambiente virtual (venv).

Instale as dependências exigidas:

```bash 
pip install Faker
```
### 1. Geração e Importação Automática de Dados

- **Geração:** Rode o script principal para criar todos os CSVs na pasta data/:

```bash 
python python/gerador_dados.py
```

- **Importação:** Importe os arquivos CSV para as tabelas correspondentes no PostgreSQL. Lembre-se da ordem correta (Pai antes do Filho):

```alunos.csv``` -> ```alunos```

```instrutores.csv``` -> ```instrutores```

```cursos.csv``` -> ```cursos```

```modulos.csv``` -> ```modulos```

```aulas.csv``` -> ```aulas```

```matriculas.csv```, ```progresso_aulas.csv```, ```avaliacoes.csv```

### 5. Execução das Consultas
Execute o arquivo consultas.sql no seu cliente SQL para verificar os resultados de todas as consultas e relatórios.

## 📊 Exemplos de Consultas

```sql
SELECT
    c.titulo_curso AS "Título do Curso",
    cat.nome_categoria AS "Nome da Categoria",
    i.nome_instrutor AS "Nome do Instrutor"
FROM
    cursos c
JOIN
    categorias cat ON c.categoria_id = cat.id_categoria
JOIN
    instrutores i ON c.instrutor_id = i.id_instrutor
ORDER BY
    c.titulo_curso; 
```



