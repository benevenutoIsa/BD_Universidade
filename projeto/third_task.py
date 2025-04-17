
import pandas as pd
import os
from supabase import create_client, Client
import re

SUPABASE_URL = "https://xjffixiirlmbqfbldnoz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhqZmZpeGlpcmxtYnFmYmxkbm96Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ2NzcxMTcsImV4cCI6MjA2MDI1MzExN30.yA-PjEK1UeVN6x91Suu6pwLQa4dA0wJhM5tFDh9nm5I"

# Função para gerar comandos INSERT SQL
def gerar_inserts_csv_para_sql():
    tabelas_csv = {
        "departamentos": "./data/departamentos.csv",
        "professores": "./data/professores.csv",
        "cursos": "./data/cursos.csv",
        "disciplinas": "./data/disciplinas.csv",
        "alunos": "./data/alunos.csv",
        "curso_disciplina": "./data/curso_disciplina.csv",
        "hist_escolar": "./data/hist_escolar.csv",
        "tccs": "./data/tccs.csv",
        "tcc_aluno": "./data/tcc_aluno.csv"
    }

    linhas_insert = []

    for tabela, arquivo in tabelas_csv.items():
        if not os.path.exists(arquivo):
            print(f"Arquivo nao encontrado: {arquivo}")
            continue

        df = pd.read_csv(arquivo)
        if tabela == "tccs" and "aluno_id" in df.columns:
            df = df.drop(columns=["aluno_id"])

        for _, row in df.iterrows():
            colunas = ', '.join(row.index)
            valores = []

            for val in row.values:
                if pd.isna(val):
                    valores.append("NULL")
                elif isinstance(val, str):
                    val = val.replace("'", "''")
                    valores.append(f"'{val}'")
                else:
                    valores.append(str(val))

            valores_sql = ', '.join(valores)
            sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores_sql});"
            linhas_insert.append(sql)

    # Salvar o SQL em um arquivo
    with open("insert_data.sql", "w", encoding="utf-8") as f:
        for linha in linhas_insert:
            f.write(linha + "\n")

        print("Arquivo insert_data.sql gerado com sucesso.")

# Função para executar o arquivo .sql no Supabase
def execute_sql_file(filepath):
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("Conectado ao Supabase")

        with open(filepath, 'r', encoding='utf-8') as file:
            sql_content = file.read()

        sql_commands = re.split(r';\s*\n', sql_content)
        sql_commands = [cmd.strip() for cmd in sql_commands if cmd.strip()]

        total = len(sql_commands)
        success = 0
        fail = 0

        for i, cmd in enumerate(sql_commands):
            print(f"Comando {i+1}/{total}: ", end="")
            try:
                supabase.rpc('exec_sql', {'sql': cmd}).execute()
                print("[OK]")
                success += 1
            except Exception as e:
                print(f"[ERRO] (erro: {str(e)[:200]})")
                fail += 1

        print(f"\nTotal: {success} sucesso, {fail} falha, taxa de sucesso: {success/total*100:.1f}%")

    except Exception as e:
        print(f"Erro geral: {str(e)}")

# Execução principal
if __name__ == "__main__":
    gerar_inserts_csv_para_sql()
    execute_sql_file("insert_data.sql")
