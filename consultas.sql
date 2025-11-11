-- Lista todos os cursos com nome da categoria e do instrutor
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

-- Lista todos os alunos matriculados em um curso específico
SELECT
    a.nome_aluno AS "Nome do Aluno",
    a.email_aluno AS "Email do Aluno",
    c.titulo_curso AS "Curso Matriculado",
    m.data_matricula AS "Data da Matrícula"
FROM
    alunos a
JOIN
    matriculas m ON a.id_aluno = m.aluno_id
JOIN
    cursos c ON m.curso_id = c.id_curso
WHERE
    c.titulo_curso = 'React: Construindo Interfaces Dinâmicas';

-- Exibe todas as aulas de um curso ordenadas por módulo e ordem
SELECT
    c.titulo_curso AS "Curso",
    m.titulo_modulo AS "Módulo",
    a.titulo_aula AS "Título da Aula",
    a.duracao_minutos_aula AS "Duração (min)"
FROM
    aulas a
JOIN
    modulos m ON a.modulo_id = m.id_modulo
JOIN
    cursos c ON m.curso_id = c.id_curso
WHERE
    c.titulo_curso = 'AWS para Iniciantes' 
ORDER BY
    m.ordem_modulo,
    a.ordem_aula; 

-- Calcula a média de avaliações de cada curso 
SELECT
    c.titulo_curso AS "Curso",
    ROUND(AVG(a.nota_avaliacao), 2) AS "Média de Avaliações",
    COUNT(a.nota_avaliacao) AS "Total de Avaliações"
FROM
    cursos c
LEFT JOIN  
    avaliacoes a ON c.id_curso = a.curso_id
GROUP BY
    c.titulo_curso
ORDER BY
    "Média de Avaliações" DESC;

-- Conta quantos alunos estão matriculados por curso 
SELECT
    c.titulo_curso AS "Curso",
    
    COUNT(m.id_matricula) AS "Número de Alunos Matriculados"
FROM
    cursos c
LEFT JOIN 
    matriculas m ON c.id_curso = m.curso_id 
GROUP BY
    c.titulo_curso 
ORDER BY
    "Número de Alunos Matriculados" DESC;

-- Calcula o faturamento total por categoria
SELECT
    cat.nome_categoria AS "Categoria",
    
    ROUND(SUM(m.valor_pago), 2) AS "Faturamento Total (R$)"
FROM
    categorias cat
LEFT JOIN
    cursos c ON cat.id_categoria = c.categoria_id 
LEFT JOIN
    matriculas m ON c.id_curso = m.curso_id       
GROUP BY
    cat.nome_categoria                        
ORDER BY
    "Faturamento Total (R$)" DESC;

-- Calcula o faturamento total por categoria
SELECT
    cat.nome_categoria AS "Categoria",
    
    ROUND(SUM(m.valor_pago_matricula), 2) AS "Faturamento Total (R$)"
FROM
    categorias cat
LEFT JOIN
    cursos c ON cat.id_categoria = c.categoria_id 
LEFT JOIN
    matriculas m ON c.id_curso = m.curso_id       
GROUP BY
    cat.nome_categoria                        
ORDER BY
    "Faturamento Total (R$)" DESC;

-- Identifica o curso com maior número de matrículas ativas
SELECT
    c.titulo_curso AS "Curso Mais Popular (Ativas)",
    COUNT(m.id_matricula) AS "Matrículas Ativas"
FROM
    cursos c
JOIN
    matriculas m ON c.id_curso = m.curso_id 
WHERE
    m.status_matricula = 'Ativa' 
GROUP BY
    c.titulo_curso 
ORDER BY
    "Matrículas Ativas" DESC 
LIMIT 1;

 -- Lista alunos, cursos matriculados e porcentagem de conclusão
SELECT
    a.nome_aluno AS "Aluno",
    c.titulo_curso AS "Curso Matriculado",
    
    ROUND(
        (CAST(PA_CONCLUIDAS.aulas_concluidas AS NUMERIC) / NULLIF(PA_TOTAL.total_aulas, 0)) * 100, 
        2
    ) AS "Porcentagem de Conclusão (%)",
    
    PA_CONCLUIDAS.aulas_concluidas AS "Aulas Concluídas",
    PA_TOTAL.total_aulas AS "Total de Aulas do Curso"
FROM
    alunos a
JOIN
    matriculas m ON a.id_aluno = m.aluno_id
JOIN
    cursos c ON m.curso_id = c.id_curso

LEFT JOIN (
    SELECT
        m.curso_id,
        COUNT(au.id_aula) AS total_aulas 
    FROM
        modulos m
    JOIN
        aulas au ON au.modulo_id = m.id_modulo
    GROUP BY
        m.curso_id
) AS PA_TOTAL ON c.id_curso = PA_TOTAL.curso_id

LEFT JOIN (
    SELECT
        matricula_id,
        COUNT(aula_id) AS aulas_concluidas 
    FROM
        progresso_aulas
    WHERE
        concluida_progresso = TRUE
    GROUP BY
        matricula_id
) AS PA_CONCLUIDAS ON m.id_matricula = PA_CONCLUIDAS.matricula_id 

WHERE
    PA_TOTAL.total_aulas IS NOT NULL 
ORDER BY
    a.nome_aluno, "Porcentagem de Conclusão (%)" DESC;