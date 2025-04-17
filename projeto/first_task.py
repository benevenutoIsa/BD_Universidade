import random
import string
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

random.seed(42)
np.random.seed(42)

def generate_fake_data():
    def generate_name():
        nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Juliana", "Lucas", "Beatriz", 
                "Marcos", "Fernanda", "Rafael", "Gabriela", "Luiz", "Camila", "André", 
                "Patrícia", "Ricardo", "Daniela", "Gustavo", "Mariana"]
        sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Lima", "Pereira", "Costa", "Rodrigues", 
                    "Almeida", "Nascimento", "Carvalho", "Gomes", "Martins", "Araújo", "Moreira", 
                    "Ribeiro", "Ferreira", "Barbosa", "Cardoso", "Mendes"]
        return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

    def generate_email(nome):
        nomes = nome.lower().split()
        base = f"{nomes[0]}.{nomes[-1]}"
        dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
        return f"{base}@{random.choice(dominios)}"

    def generate_phone():
        ddd = random.choice(["11", "21", "31", "41", "51", "61", "71", "81", "91"])
        num = ''.join(random.choice(string.digits) for _ in range(9))
        return f"({ddd}) {num[:5]}-{num[5:]}"

    def generate_birth_date(min_age=18, max_age=65):
        hoje = datetime.now()
        anos = random.randint(min_age, max_age)
        dias = random.randint(0, 365)
        nascimento = hoje - timedelta(days=(anos * 365 + dias))
        return nascimento.strftime('%Y-%m-%d')

    def generate_departamentos(n=5):
        nomes_base = ["Ciências", "Engenharia", "Humanidades", "Saúde", "Tecnologia"]
        return [{"id": i+1, "nome": f"Departamento de {random.choice(nomes_base)}"} for i in range(n)]

    def generate_cursos(n=6, departamentos=None):
        nomes_base = ["Ciência da Computação", "Engenharia Civil", "Medicina", "Direito", "Administração", "Matemática", "Ciência de Dados"]
        cursos = []
        for i in range(n):
            dept_id = random.choice(departamentos)["id"]
            cursos.append({"id": i+1, "nome": nomes_base[i], "departamento_id": dept_id})
        return cursos

    def generate_professores(n=10, departamentos=None):
        professores = []
        emails_usados = set()
        for i in range(n):
            nome = generate_name()
            email = generate_email(nome)
            while email in emails_usados:
                nome = generate_name()
                email = generate_email(nome)
            emails_usados.add(email)
            prof = {
                "id": i+1,
                "nome": nome,
                "email": email,
                "telefone": generate_phone(),
                "area_conhecimento": random.choice(["Algoritmos", "Cálculo", "História", "Redes", "Bioética"]),
                "salario": round(random.uniform(4000, 12000), 2),
                "departamento_id": random.choice(departamentos)["id"]
            }
            professores.append(prof)
        return professores

    def generate_disciplinas(n=20, departamentos=None):
        nomes = ["Matemática", "Física", "Programação", "Química", "Literatura", "Geografia"]
        disciplinas = []
        for i in range(n):
            dept_id = random.choice(departamentos)["id"]
            disciplinas.append({
                "id": i+1,
                "nome": f"Disciplina de {random.choice(nomes)} {random.choice(['I', 'II'])}",
                "carga_horaria": random.choice([30, 60, 90]),
                "departamento_id": dept_id
            })
        return disciplinas

    def generate_curso_disciplina(cursos, disciplinas):
        curso_disc = []
        for curso in cursos:
            selecionadas = random.sample(disciplinas, k=random.randint(5, 10))
            for d in selecionadas:
                curso_disc.append({
                    "curso_id": curso["id"],
                    "disciplina_id": d["id"]
                })
        return curso_disc

    def generate_alunos(n=50, cursos=None):
        alunos = []
        emails_usados = set()
        for i in range(n):
            nome = generate_name()
            email = generate_email(nome)
            while email in emails_usados:
                nome = generate_name()
                email = generate_email(nome)
            emails_usados.add(email)
            aluno = {
                "id": i+1,
                "nome": nome,
                "email": email,
                "telefone": generate_phone(),
                "nascimento": generate_birth_date(18, 30),
                "cpf": ''.join(random.choices(string.digits, k=11)),
                "curso_id": random.choice(cursos)["id"]
            }
            alunos.append(aluno)
        return alunos

    def generate_hist_escolar(alunos, disciplinas, professores):
        hist = []
        semestres = ["1/2022", "2/2022", "1/2023", "2/2023", "1/2024", "2/2024"]

        for aluno in alunos:
            qtd_disciplinas = random.randint(3, 8)
            for i in range(qtd_disciplinas):
                disciplina = random.choice(disciplinas)
                professores_validos = [p for p in professores if p["departamento_id"] == disciplina["departamento_id"]]
                if not professores_validos:
                    continue
                professor = random.choice(professores_validos)
                semestre_idx = min(i, len(semestres)-1)
                nota = round(random.uniform(0, 10), 1)
                situacao = "Aprovado" if nota >= 6 else "Reprovado"
                hist.append({
                    "aluno_id": aluno["id"],
                    "disciplina_id": disciplina["id"],
                    "professor_id": professor["id"],
                    "semestre": semestres[semestre_idx],
                    "ano": int(semestres[semestre_idx].split("/")[1]),
                    "nota": nota,
                    "situacao": situacao
                })
        return hist

    def generate_tcc(alunos, professores, cursos):
        tccs = []
        titulos_usados = set()
        for i in range(1, 21):
            aluno = random.choice(alunos)
            curso = next(c for c in cursos if c["id"] == aluno["curso_id"])
            professores_curso = [p for p in professores if p["departamento_id"] == curso["departamento_id"]]
            if not professores_curso:
                continue
            professor = random.choice(professores_curso)
            while True:
                titulo = f"Análise sobre {random.choice(['IA', 'Redes', 'Banco de Dados', 'Sistemas', 'Algoritmos'])} em {random.choice(['Ambientes Web', 'Sistemas Distribuídos', 'Educação', 'Saúde'])}"
                if titulo not in titulos_usados:
                    titulos_usados.add(titulo)
                    break
            data_inicio = datetime.now() - timedelta(days=random.randint(180, 365))
            if random.random() < 0.5:
                data_conclusao = data_inicio + timedelta(days=random.randint(60, 120))
                nota = round(random.uniform(6, 10), 1)
                status = "Concluído"
            else:
                data_conclusao = None
                nota = None
                status = "Em Andamento"
            tccs.append({
                "id": i,
                "titulo": titulo,
                "professor_id": professor["id"],
                "data_inicio": data_inicio.strftime('%Y-%m-%d'),
                "data_conclusao": data_conclusao.strftime('%Y-%m-%d') if data_conclusao else None,
                "nota": nota,
                "status": status
            })
        return tccs

    def generate_tcc_aluno(tccs, alunos, grupo=5):
        random.shuffle(alunos)
        grupos = [alunos[i:i+grupo] for i in range(0, len(alunos), grupo)]
        tcc_aluno = []
        for i, tcc in enumerate(tccs):
            if i >= len(grupos): break
            for aluno in grupos[i]:
                tcc_aluno.append({"tcc_id": tcc["id"], "aluno_id": aluno["id"]})
        return tcc_aluno

    departamentos = generate_departamentos()
    cursos = generate_cursos(departamentos=departamentos)
    professores = generate_professores(departamentos=departamentos)
    disciplinas = generate_disciplinas(departamentos=departamentos)
    curso_disciplina = generate_curso_disciplina(cursos, disciplinas)
    alunos = generate_alunos(cursos=cursos)
    hist_escolar = generate_hist_escolar(alunos, disciplinas, professores)
    tccs = generate_tcc(alunos, professores, cursos)
    tcc_aluno = generate_tcc_aluno(tccs, alunos)
    
    return {
        "departamentos": departamentos,
        "professores": professores,
        "cursos": cursos,
        "disciplinas": disciplinas,
        "alunos": alunos,
        "curso_disciplina": curso_disciplina,
        "hist_escolar": hist_escolar,
        "tccs": tccs,
        "tcc_aluno": tcc_aluno
    }

if __name__ == "__main__":
    data = generate_fake_data()
    
    df_departamentos = pd.DataFrame(data["departamentos"])
    df_professores = pd.DataFrame(data["professores"])
    df_cursos = pd.DataFrame(data["cursos"])
    df_disciplinas = pd.DataFrame(data["disciplinas"])
    df_alunos = pd.DataFrame(data["alunos"])
    df_curso_disciplina = pd.DataFrame(data["curso_disciplina"])
    df_hist_escolar = pd.DataFrame(data["hist_escolar"])
    df_tccs = pd.DataFrame(data["tccs"])
    df_tcc_aluno = pd.DataFrame(data["tcc_aluno"])

    import os
    if not os.path.exists("data"):
        os.makedirs("data")
    
    df_departamentos.to_csv("data/departamentos.csv", index=False)
    df_professores.to_csv("data/professores.csv", index=False)
    df_cursos.to_csv("data/cursos.csv", index=False)
    df_disciplinas.to_csv("data/disciplinas.csv", index=False)
    df_alunos.to_csv("data/alunos.csv", index=False)
    df_curso_disciplina.to_csv("data/curso_disciplina.csv", index=False)
    df_hist_escolar.to_csv("data/hist_escolar.csv", index=False)
    df_tccs.to_csv("data/tccs.csv", index=False)
    df_tcc_aluno.to_csv("data/tcc_aluno.csv", index=False)
    
    print("Dados gerados e salvos com sucesso!")
