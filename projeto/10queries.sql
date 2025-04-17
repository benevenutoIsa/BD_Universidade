--24. Liste os professores que ministraram cursos com mais de 50 alunos matriculados.
SELECT p.id, p.nome
FROM professores p
JOIN hist_escolar h ON h.professor_id = p.id
GROUP BY p.id, p.nome
HAVING COUNT(h.aluno_id) > 50;

--25. Encontre os departamentos que oferecem cursos ministrados por um professor específico (ex: professor_id = 1).
SELECT DISTINCT d.id, d.nome AS nome_departamento
FROM departamentos d
JOIN cursos c ON c.departamento_id = d.id
JOIN alunos a ON a.curso_id = c.id
JOIN hist_escolar h ON h.aluno_id = a.id
WHERE h.professor_id = 1;

--34. Cursos (disciplinas) ministradas por mais de um professor em semestres diferentes.
SELECT disciplina_id
FROM hist_escolar
GROUP BY disciplina_id
HAVING COUNT(DISTINCT professor_id) > 1;

--35. Estudantes que cursaram disciplinas de mais de 3 departamentos.
SELECT a.id, a.nome
FROM alunos a
JOIN hist_escolar h ON a.id = h.aluno_id
JOIN disciplinas d ON h.disciplina_id = d.id
GROUP BY a.id, a.nome
HAVING COUNT(DISTINCT d.departamento_id) > 3;

--50. Estudantes que não cursaram nenhuma disciplina do departamento de "Engenharia".
SELECT a.id, a.nome
FROM alunos a
WHERE a.id NOT IN (
    SELECT h.aluno_id
    FROM hist_escolar h
    JOIN disciplinas d ON h.disciplina_id = d.id
    JOIN departamentos dept ON d.departamento_id = dept.id
    WHERE dept.nome ILIKE '%Engenharia%'
);

-- 19. Encontre os professores que ensinam "Sistemas de Banco de Dados" no 1º semestre de 2024.
SELECT DISTINCT p.id, p.nome
FROM professores p
JOIN hist_escolar h ON p.id = h.professor_id
JOIN disciplinas d ON d.id = h.disciplina_id
WHERE d.nome ILIKE '%Sistemas de Banco de Dados%'
  AND h.ano = 2024
  AND h.semestre = '1/2024';

--28. Professores que ensinam cursos com mais de 40 alunos.
SELECT p.id, p.nome
FROM professores p
JOIN hist_escolar h ON h.professor_id = p.id
GROUP BY p.id, p.nome
HAVING COUNT(DISTINCT h.aluno_id) > 40;

--39. Professores que ministraram disciplinas onde todos os alunos tiraram nota >= 9 (simulando "A")
SELECT p.nome
FROM professores p
JOIN hist_escolar h ON h.professor_id = p.id
GROUP BY p.id, p.nome, h.disciplina_id
HAVING MIN(h.nota) >= 9;

--8. Liste os IDs dos professores que ensinam mais de uma disciplina.
SELECT professor_id
FROM hist_escolar
GROUP BY professor_id
HAVING COUNT(DISTINCT disciplina_id) > 1;


--31. Estudantes que cursaram disciplinas de todos os departamentos
SELECT a.nome
FROM alunos a
JOIN hist_escolar h ON h.aluno_id = a.id
JOIN disciplinas d ON d.id = h.disciplina_id
GROUP BY a.id, a.nome
HAVING COUNT(DISTINCT d.departamento_id) = (
    SELECT COUNT(*) FROM departamentos
);

--10. Alunos que são orientados por um professor específico (ex: professor_id = 1)
SELECT a.id, a.nome AS nome_aluno
FROM tccs t
JOIN tcc_aluno ta ON ta.tcc_id = t.id
JOIN alunos a ON a.id = ta.aluno_id
WHERE t.professor_id = 1;