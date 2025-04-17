
import pandas as pd
import os

def validate_data():
    data_files = [
        "departamentos.csv", "professores.csv", "cursos.csv", "disciplinas.csv",
        "alunos.csv", "curso_disciplina.csv", "hist_escolar.csv", "tccs.csv"
    ]
    
    missing_files = [f for f in data_files if not os.path.exists(f)]
    if missing_files:
        print(f"Erro: Os seguintes arquivos não foram encontrados: {missing_files}")
        return False

    df_departamentos = pd.read_csv("departamentos.csv")
    df_professores = pd.read_csv("professores.csv")
    df_cursos = pd.read_csv("cursos.csv")
    df_disciplinas = pd.read_csv("disciplinas.csv")
    df_alunos = pd.read_csv("alunos.csv")
    df_curso_disciplina = pd.read_csv("curso_disciplina.csv")
    df_hist_escolar = pd.read_csv("hist_escolar.csv")
    df_tccs = pd.read_csv("tccs.csv")
    df_tcc_aluno = pd.read_csv("tcc_aluno.csv")

    validations = []

    # Validações anteriores (resumidas para foco nos novos pontos)
    validations.append(("IDs duplicados em alunos", df_alunos['id'].is_unique))
    validations.append(("Emails duplicados em professores", df_professores['email'].is_unique))
    validations.append(("Curso-disciplina duplicado", df_curso_disciplina.duplicated(subset=['curso_id', 'disciplina_id']).sum() == 0))
    validations.append(("Histórico escolar duplicado", df_hist_escolar.duplicated(subset=['aluno_id', 'disciplina_id', 'semestre', 'ano']).sum() == 0))
    validations.append(("Duplicidade em tcc_aluno (tcc_id, aluno_id)", df_tcc_aluno.duplicated(subset=["tcc_id", "aluno_id"]).sum() == 0))

    # NOVAS VALIDAÇÕES:

    # 1. Notas fora da faixa (deve estar entre 0 e 10)
    notas_validas = df_hist_escolar['nota'].dropna().between(0, 10).all()
    validations.append(("Notas fora da faixa permitida (0-10)", notas_validas))

    # 2. Reprovação seguida de aprovação na mesma disciplina
    alunos_reaprovados = []
    for aluno_id in df_alunos['id']:
        aluno_hist = df_hist_escolar[df_hist_escolar['aluno_id'] == aluno_id]
        agrupado = aluno_hist.groupby('disciplina_id')['situacao'].apply(list)
        for disciplina_id, situacoes in agrupado.items():
            if "Reprovado" in situacoes and "Aprovado" in situacoes:
                alunos_reaprovados.append((aluno_id, disciplina_id))
    validations.append(("Alunos com reprovação seguida de aprovação", len(alunos_reaprovados) > 0))

    # 3. TCC: datas inconsistentes (data_conclusao antes da data_inicio)
    df_tccs_filtrado = df_tccs.dropna(subset=["data_inicio", "data_conclusao"])
    df_tccs_filtrado["data_inicio"] = pd.to_datetime(df_tccs_filtrado["data_inicio"])
    df_tccs_filtrado["data_conclusao"] = pd.to_datetime(df_tccs_filtrado["data_conclusao"])
    datas_validas = (df_tccs_filtrado["data_conclusao"] >= df_tccs_filtrado["data_inicio"]).all()
    validations.append(("TCCs com data de conclusão anterior à data de início", datas_validas))

    #Valida a tabela de tcc_alunos, numero de alunos por tcc
    validations.append((
    "TCCs inválidos em tcc_aluno", df_tcc_aluno['tcc_id'].isin(df_tccs['id']).all()))
    validations.append(("Alunos inválidos em tcc_aluno", df_tcc_aluno['aluno_id'].isin(df_alunos['id']).all()))


    # Mostrar resultados
    all_ok = True
    for message, passed in validations:
        if not passed:
            print(f"ERRO: {message}")
            all_ok = False

    if all_ok:
        print("Todos os dados foram validados com sucesso.")
    else:
        print("Foram encontrados erros nos dados.")

    return all_ok
