#### Isabella Benevenuto RA: 22.123.007-1
#### Mateus Marana       RA: 22.123.026-1
---

# 🏛️ Projeto: Banco de Dados Universitário

Este projeto simula o ambiente acadêmico de uma universidade por meio de um banco de dados relacional completo. Ele foi desenvolvido com o objetivo de apoiar atividades de ensino e prática em:

- 📐 Modelagem de dados (MER e DDL)
- 🧬 Geração de dados fictícios com Python
- ✅ Validação de integridade e consistência dos dados
- 🔍 Execução e testes de queries SQL com Supabase (PostgreSQL)

A base contempla os principais elementos de um sistema acadêmico:

- *Departamentos*
- *Professores*
- *Cursos*
- *Disciplinas*
- *Alunos*
- *Histórico escolar*
- *Trabalhos de Conclusão de Curso (TCCs)* com grupos de alunos

Todos os relacionamentos foram modelados de forma a refletir situações reais de uma universidade.

---

## 🛠️ Como Executar o Projeto

### 1. 📦 Pré-requisitos

- Python 3.10 ou superior
- Conta no [Supabase](https://supabase.io)
- Instalar as bibliotecas Python:

```bash
pip install pandas numpy supabase
---
```

### 2. 🧬 Gerar os dados fictícios
- Execute o gerador de dados para criar os arquivos .csv:
python first_task.py
- Os arquivos serão salvos automaticamente na pasta /data.

### 3. ✅ Validar os dados (opcional)
- Você pode rodar um validador automático para verificar:
Duplicidade de chaves
Integridade referencial
Campos nulos ou inconsistentes
python second_task.py

### 4. 📄 Gerar comandos SQL e inserir no Supabase
- Use o script abaixo para transformar os .csv em comandos INSERT INTO e executá-los no Supabase:
python third_task.py
Esse comando:
Gera o arquivo insert_data.sql
Executa os comandos via exec_sql (RPC) na instância do Supabase

⚠️ Certifique-se de já ter criado as tabelas (via DDL) no Supabase antes de executar este passo.

## 🧠 Consultas SQL
O projeto foi desenhado para responder a diversos exercícios e desafios SQL, incluindo:
- Mostrar o histórico escolar de um aluno
- Listar TCCs e seus orientadores
- Consultar disciplinas cursadas e os professores que lecionaram
- Identificar coordenadores e departamentos
- Consultas com JOIN, GROUP BY, HAVING, COALESCE, entre outros


## 🗂️ Estrutura do Projeto
```
├── data/                      # Arquivos CSV com os dados gerados
│   ├── alunos.csv
│   ├── cursos.csv
│   ├── disciplinas.csv
│   ├── professores.csv
│   ├── departamentos.csv
│   ├── tccs.csv
│   ├── tcc_aluno.csv
│   └── hist_escolar.csv
├── first_task.py             # Gerador de dados fictícios
├── second_task.py            # Validador de dados e integridade
├── third_task.py             # Gerador de INSERTS e integrador com Supabase
├── insert_data.sql           # Comandos SQL gerados automaticamente
├── estrutura_ddl.sql         # Script para criação das tabelas (DDL)
├── mermaid.md                # Diagrama MER em sintaxe Mermaid.js
└── diagramas/                # Imagens PNG com o modelo relacional
```
### 📌 Observações
Todos os dados são fictícios e gerados aleatoriamente.

O projeto pode ser adaptado facilmente para outras entidades ou domínios.

Ideal para estudos, apresentações acadêmicas ou testes de sistemas acadêmicos.

Você pode ajustar a quantidade de registros gerados modificando os parâmetros nos scripts Python.

```mermaid
erDiagram
    DEPARTAMENTOS ||--o{ PROFESSORES : "possui"
    DEPARTAMENTOS ||--o{ CURSOS : "possui"
    DEPARTAMENTOS ||--o{ DISCIPLINAS : "oferece"
    CURSOS ||--o{ ALUNOS : "matricula"
    CURSOS }|--|{ DISCIPLINAS : "composto por"
    ALUNOS }|--|{ TCCS : "desenvolve"
    PROFESSORES ||--o{ TCCS : "orienta"
    ALUNOS }|--o{ HIST_ESCOLAR : "possui"
    DISCIPLINAS ||--o{ HIST_ESCOLAR : "registra"
    PROFESSORES ||--o{ HIST_ESCOLAR : "leciona"
    
    DEPARTAMENTOS {
        int id PK
        varchar nome
    }
    
    PROFESSORES {
        int id PK
        varchar nome
        varchar email
        varchar telefone
        varchar area_conhecimento
        decimal salario
        int departamento_id FK
    }
    
    CURSOS {
        int id PK
        varchar nome
        int departamento_id FK
    }
    
    DISCIPLINAS {
        int id PK
        varchar nome
        int carga_horaria
        int departamento_id FK
    }
    
    ALUNOS {
        int id PK
        varchar nome
        varchar email
        varchar telefone
        date nascimento
        varchar cpf
        int curso_id FK
    }
    
    CURSO_DISCIPLINA {
        int curso_id PK,FK
        int disciplina_id PK,FK
    }
    
    HIST_ESCOLAR {
        serial id PK
        int aluno_id FK
        int disciplina_id FK
        int professor_id FK
        varchar semestre
        int ano
        decimal nota
        varchar situacao
    }
    
    TCCS {
        int id PK
        varchar titulo
        int professor_id FK
        date data_inicio
        date data_conclusao
        decimal nota
        varchar status
    }
    
    TCC_ALUNO {
        int tcc_id PK,FK
        int aluno_id PK,FK
    }
```
![ERDiagram](https://github.com/benevenutoIsa/BD_Universidade/blob/main/ERdiagram_EDPlus.png)
