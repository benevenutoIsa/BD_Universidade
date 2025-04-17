
-- Tabela DEPARTAMENTOS
CREATE TABLE departamentos (
    id INT PRIMARY KEY,
    nome VARCHAR(100)
);

-- Tabela PROFESSORES
CREATE TABLE professores (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20),
    area_conhecimento VARCHAR(100),
    salario DECIMAL(10,2),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- Tabela CURSOS
CREATE TABLE cursos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- Tabela DISCIPLINAS
CREATE TABLE disciplinas (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    carga_horaria INT,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- Tabela ALUNOS
CREATE TABLE alunos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20),
    nascimento DATE,
    cpf VARCHAR(14),
    curso_id INT,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Tabela CURSO_DISCIPLINA
CREATE TABLE curso_disciplina (
    curso_id INT,
    disciplina_id INT,
    PRIMARY KEY (curso_id, disciplina_id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
);

-- Tabela HIST_ESCOLAR
CREATE TABLE hist_escolar (
    id SERIAL PRIMARY KEY,
    aluno_id INT,
    disciplina_id INT,
    professor_id INT,
    semestre VARCHAR(10),
    ano INT,
    nota DECIMAL(3,1),
    situacao VARCHAR(50),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id),
    FOREIGN KEY (professor_id) REFERENCES professores(id)
);

-- Tabela TCCS
CREATE TABLE tccs (
    id INT PRIMARY KEY,
    titulo VARCHAR(255),
    professor_id INT,
    data_inicio DATE,
    data_conclusao DATE,
    nota DECIMAL(3,1),
    status VARCHAR(50),
    FOREIGN KEY (professor_id) REFERENCES professores(id)
);

-- Tabela TCC_ALUNO (relacionamento n:n entre tccs e alunos)
CREATE TABLE tcc_aluno (
    tcc_id INT,
    aluno_id INT,
    PRIMARY KEY (tcc_id, aluno_id),
    FOREIGN KEY (tcc_id) REFERENCES tccs(id),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);
