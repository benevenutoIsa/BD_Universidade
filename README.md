erDiagram

  DEPARTAMENTO {
    int id PK
    string nome
    int chefe_id FK
  }

  PROFESSOR {
    int id PK
    string nome
    string email
    string telefone
    date data_nascimento
    decimal salario
    int departamento_id FK
    int curso_id FK
  }

  CURSO {
    int id PK
    string nome
    int departamento_id FK
    int coordenador FK
    int disciplina_id FK
  }

  DISCIPLINA {
    int id PK
    string nome
    string codigo
    int carga_horaria
    int departamento_id FK
    int curso_id FK
    int professor_id FK
    int semestre
    boolean obrigatoria
  }

  ALUNO {
    int id PK
    string nome
    string matricula
    string email
    string telefone
    date data_nascimento
    char sexo
    int curso_id FK
    int disciplina_id FK
  }

  HIST_DISCIPLINAS {
    int professor_id PK, FK
    int disciplina_id PK, FK
    int curso_id
    int departamento_id
    int semestre
    int ano PK
  }

  HIST_ESCOLAR {
    int aluno_id PK, FK
    int disciplina_id PK, FK
    int professor_id
    string semestre PK
    decimal nota
    string situacao
  }

  TCC {
    int id PK
    string titulo
    int aluno_id FK
    int professor_id FK
    date data_inicio
    date data_fim
    decimal nota
    string status
    text projeto
  }

  %% RELACIONAMENTOS

  DEPARTAMENTO ||--o{ PROFESSOR : possui
  DEPARTAMENTO ||--o{ CURSO : oferece
  DEPARTAMENTO ||--o{ DISCIPLINA : organiza

  CURSO ||--o{ DISCIPLINA : contem
  CURSO ||--o{ ALUNO : possui
  CURSO ||--o{ PROFESSOR : pertence
  CURSO ||--o{ HIST_DISCIPLINAS : referencia

  DISCIPLINA ||--o{ HIST_DISCIPLINAS : esta_em
  DISCIPLINA ||--o{ HIST_ESCOLAR : registrada_em
  DISCIPLINA ||--o{ ALUNO : associada
  DISCIPLINA ||--|| PROFESSOR : ministrada_por

  PROFESSOR ||--o{ HIST_DISCIPLINAS : ministra
  PROFESSOR ||--o{ HIST_ESCOLAR : avalia
  PROFESSOR ||--o{ TCC : orienta

  ALUNO ||--o{ HIST_ESCOLAR : tem
  ALUNO ||--o{ TCC : apresenta
