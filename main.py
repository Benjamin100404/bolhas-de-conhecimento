import json
import os

ALUNOS_USUARIOS = 'usuarios.json'

def main():
    print("Bem-vindo à Bolha de Conhecimento")


if __name__ == "__main__":
    main()

def carregar_dados():
    if os.path.exists(ALUNOS_USUARIOS):  
        with open(ALUNOS_USUARIOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo) 
    else:
        return {"alunos": []} 
    
def salvar_dados(dados):
    with open(ALUNOS_USUARIOS, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4)  

def cadastrar_aluno():
    print("\n--- CADASTRO DE NOVO ALUNO ---")
    
    nome = input("Nome completo: ").strip()
    matricula = input("Matrícula (somente números): ").strip()
    senha = input("Senha: ").strip()
    
    dados = carregar_dados()
    
    for aluno in dados["alunos"]:
        if aluno["matricula"] == matricula:
            print("\nErro: Matrícula já cadastrada!")
            return
    
    
    novo_aluno = {
        "nome": nome,
        "matricula": matricula,
        "senha": senha  
    }
    
    dados["alunos"].append(novo_aluno)
    salvar_dados(dados)
    print("\nAluno cadastrado com sucesso!")

cadastrar_aluno()gi