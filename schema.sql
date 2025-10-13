CREATE TABLE alunos (
    id_aluno SERIAL PRIMARY KEY,
    nome_aluno VARCHAR(100) NOT NULL,
    email_aluno VARCHAR(100) UNIQUE NOT NULL,
    data_nascimento_aluno DATE  NOT NULL,
    data_cadastro_aluno TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE instrutores (
    id_instrutor SERIAL PRIMARY KEY,
    nome_instrutor VARCHAR(100) NOT NULL,
    email_instrutor VARCHAR(100) UNIQUE NOT NULL,
    especialidade_instrutor VARCHAR(100) NOT NULL,
    biografia_instrutor TEXT
);

CREATE TABLE categorias (
    id_categoria SERIAL PRIMARY KEY,
    nome_categoria VARCHAR(100) NOT NULL,
    descricao_categoria TEXT
);

CREATE TABLE cursos (
    id_curso SERIAL PRIMARY KEY,
    titulo_curso VARCHAR(200) NOT NULL,
    descricao_curso TEXT,
    categoria_id INTEGER NOT NULL,
    instrutor_id INTEGER NOT NULL,
    preco_curso DECIMAL(10, 2) NOT NULL,
    carga_horaria_curso INTEGER NOT NULL,
    nivel_curso VARCHAR(50) CHECK (nivel_curso IN ('Iniciante', 'Intermediário', 'Avançado')) NOT NULL,
    data_criacao_curso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id_categoria),
    FOREIGN KEY (instrutor_id) REFERENCES instrutores(id_instrutor)
);

CREATE TABLE modulos (
    id_modulo SERIAL PRIMARY KEY,
    curso_id INTEGER NOT NULL,
    titulo_modulo VARCHAR(200) NOT NULL,
    ordem_modulo INTEGER NOT NULL,
    descricao_modulo TEXT,
    FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
);

CREATE TABLE aulas (
    id_aula SERIAL PRIMARY KEY,
    modulo_id INTEGER NOT NULL,
    titulo_aula VARCHAR(200) NOT NULL,
    ordem_aula INTEGER NOT NULL,
    duracao_minutos_aula INTEGER NOT NULL,
    tipo_aula VARCHAR(50) CHECK (tipo_aula IN ('Vídeo', 'Texto', 'Quiz')) NOT NULL,
    FOREIGN KEY (modulo_id) REFERENCES modulos(id_modulo)
);

CREATE TABLE matriculas (
    id_matricula SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    data_matricula TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_conclusao_matricula TIMESTAMP,
    status_matricula VARCHAR(50) CHECK (status_matricula IN ('Ativa', 'Concluída', 'Cancelada')) NOT NULL,
    valor_pago_matricula DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id_aluno),
    FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
);

CREATE TABLE progresso_aulas(
    id_progresso SERIAL PRIMARY KEY,
    matricula_id INTEGER NOT NULL,
    aula_id INTEGER NOT NULL,
    concluida_progresso BOOLEAN DEFAULT FALSE,
    data_conclusao_progresso TIMESTAMP,
    tempo_assistido_minutos INTEGER DEFAULT 0,
    FOREIGN KEY (matricula_id) REFERENCES matriculas(id_matricula),
    FOREIGN KEY (aula_id) REFERENCES aulas(id_aula)
);

CREATE TABLE avaliacoes (
    id_avaliacao SERIAL PRIMARY KEY,
    matricula_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    nota_avaliacao INTEGER CHECK (nota_avaliacao BETWEEN 1 AND 5) NOT NULL,
    comentario_avaliacao TEXT, 
    data_avalicao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (matricula_id) REFERENCES matriculas(id_matricula),
    FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
);