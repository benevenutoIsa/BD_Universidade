--1 Mostre todo o histórico escolar de um aluno que teve reprovação em uma disciplina, retornando inclusive a reprovação em um semestre e a aprovação no semestre seguinte;

SELECT 
    a.nome AS alunos,
    d.nome AS disciplinas,
    h.semestre,
    h.ano,
    h.situacao
FROM hist_escolar h
JOIN alunos a ON h.aluno_id = a.id
JOIN disciplinas d ON h.disciplina_id = d.id
WHERE h.aluno_id = 5
  AND h.situacao IN ('Reprovado', 'Aprovado')
ORDER BY d.nome, h.ano, h.semestre;

--2 Mostre todos os TCCs orientados por um professor junto com os nomes dos alunos que fizeram o projeto;
SELECT 
    p.nome AS professor,
    t.titulo AS tcc,
    STRING_AGG(a.nome, ', ') AS alunos
FROM tccs t
JOIN professores p ON t.professor_id = p.id
JOIN tcc_aluno ta ON ta.tcc_id = t.id
JOIN alunos a ON a.id = ta.aluno_id
GROUP BY p.nome, t.titulo
ORDER BY p.nome, t.titulo;


--3 Mostre a matriz curricular de pelo menos 2 cursos diferentes que possuem disciplinas em comum (e.g., Ciência da Computação e Ciência de Dados). Este exercício deve ser dividido em 2 queries sendo uma para cada curso;
SELECT 
    c.nome AS curso,
    d.id AS cod_disciplina,
    d.nome AS nome_disciplina
FROM cursos c
JOIN curso_disciplina cd ON c.id = cd.curso_id
JOIN disciplinas d ON cd.disciplina_id = d.id
WHERE c.nome = 'Ciência da Computação';

SELECT 
    c.nome AS curso,
    d.id AS cod_disciplina,
    d.nome AS nome_disciplina
FROM cursos c
JOIN curso_disciplina cd ON c.id = cd.curso_id
JOIN disciplinas d ON cd.disciplina_id = d.id
WHERE c.nome = 'Ciência de Dados';

--4 Para um determinado aluno, mostre os códigos e nomes das disciplinas já cursadas junto com os nomes dos professores que lecionaram a disciplina para o aluno;
SELECT 
    d.id AS codigo_disciplina,
    d.nome AS nome_disciplina,
    p.nome AS nome_professor
FROM hist_escolar h
JOIN disciplinas d ON h.disciplina_id = d.id
JOIN professores p ON h.professor_id = p.id
WHERE h.aluno_id = 42
  AND h.situacao = 'Aprovado';


--5 Liste todos os chefes de departamento e coordenadores de curso em apenas uma query de forma que a primeira coluna seja o nome do professor, a segunda o nome do departamento coordena e a terceira o nome do curso que coordena. Substitua os campos em branco do resultado da query pelo texto "nenhum".
SELECT 
    p.nome AS professor,
    COALESCE(d.nome, 'nenhum') AS departamento_coordena,
    COALESCE(c.nome, 'nenhum') AS curso_coordena
FROM professores p
LEFT JOIN departamentos d ON p.id = d.chefe_id
LEFT JOIN cursos c ON p.id = c.coordenador_id
WHERE d.id IS NOT NULL OR c.id IS NOT NULL;