import json
import os

ALUNOS_USUARIOS = 'usuarios.json'

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

def login():
    print("=============== LOGIN ================")
    matricula = input("Insira sua matrícula: ")
    senha = input("Insira sua senha: ")
    cadastros = carregar_dados()
    
    for aluno in cadastros["alunos"]:
        if aluno["matricula"] == matricula:
            if aluno["senha"] == senha:
                print("Login com sucesso!")
                return True  # Retorna True para indicar login bem-sucedido
            else:
                print("Senha incorreta")
                return False  # Retorna False para indicar falha no login
    
    # Se chegou aqui, a matrícula não foi encontrada
    print("Matrícula não cadastrada")
    return False
           
def main():
    print("Bem-vindo à Bolha de Conhecimento")
    while True:
        print("\n======== MENU PRINCIPAL ========")
        option = input("1 - Fazer Login\n2 - Fazer Cadastro\n3 - Sair\nEscolha uma opção: ")
        
        if option == "1":
            if login():  # Se o login for bem-sucedido
                menu_aluno()  # Chama o menu do aluno (você precisa implementar esta função)
        elif option == "2":
            cadastrar_aluno()
        elif option == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()