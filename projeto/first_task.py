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

    