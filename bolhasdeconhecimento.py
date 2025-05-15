import json
import os
from datetime import datetime

ALUNOS_USUARIOS = 'usuarios.json'
URL_VIDEO = "https://youtu.be/dPX9vb3e-d8"

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
        "senha": senha,
        "notas": []
    }
    dados["alunos"].append(novo_aluno)
    salvar_dados(dados)
    print("\nAluno cadastrado com sucesso!")

def menu_ensino():
    print("\n--- Bolhas: ---")
    print("1. Bolha 1: Lógica Computacional")
    print("2. Bolha 2: Python")
    print("3. Bolha 3: Cibersegurança")
    print("4. Bolha 4: Estoure a bolha!")
    print("5. Ver histórico de pontuação")
    print("6. Sair da bolha")
    escolha = input("\nEscolha uma opção (1-6): ")
    return escolha

def bolha_1():
    print("\nLógica de programação é como ensinar um passo a passo para o computador.\nImagine que você está explicando como fazer um sanduíche para um robô:\ntem que dizer cada ação na ordem certa, como \"pegue o pão\", \"coloque o queijo\".\nSe faltar um passo, o robô fica perdido e não faz direito!")
    input("\n\nPressione ENTER para avançar...\n")
    print("Os programas usam regras simples como \"SE isso acontecer, ENTÃO faça aquilo\". Por exemplo: \"SE o botão for apertado, ENTÃO acenda a luz\". Isso se chama condicional, e ajuda o programa a tomar decisões. Também existem loops, que repetem ações até dar o resultado certo.")
    input("\n\nPressione ENTER para avançar...\n")
    print("Python usa comandos fáceis que parecem inglês simples, como \"print()\".Dá para fazer jogos, cálculos e até robôs que respondem perguntas! A comunidade ajuda com códigos prontos que você pode usar.É gratuito e funciona em qualquer computador ou celular.")
    input("\n\nPressione ENTER para avançar à próxima bolha...\n")

def bolha_2():
    print("Python é uma linguagem de programação muito famosa e fácil de aprender. Ela é usada para criar jogos, sites, aplicativos e até inteligência artificial!")
    input("\n\nPressione ENTER para avançar...\n")
    print("Python foi criado em 1991 por um programador chamado Guido van Rossum. Ele quis fazer uma linguagem simples e poderosa, inspirada em desenhos de comédia (por isso o nome \"Python\", como a cobra!). Desde então, Python cresceu e ficou uma das linguagens mais usadas no mundo. E o legal é que ela é de graça e roda em qualquer computador")
    input("\n\nPressione ENTER para avançar...\n")
    print("Ela é usada por grandes empresas como Google e YouTube, então saber Python pode ajudar no futuro. Além disso, a comunidade Python é muito grande, então sempre tem gente pronta para ajudar.")
    input("\n\nPressione ENTER para avançar...\n")
    print("Agora vamos sair dessa bolha e ir programar o seu primeiro código! Então abra o Visual Studio, mas continue aqui para ter as intruções!")
    print("Digite EXATAMENTE isso: \"print(\"Hello World!\")\". Depois aperte ENTER e... MÁGICA!")
    input("\n\nPressione ENTER para avançar à próxima bolha...\n")

def bolha_3():
    print("Cibersegurança é como proteger seu computador e seus códigos do mesmo jeito que você protege seu quarto. Você não deixa qualquer pessoa entrar, certo? Na programação, fazemos o mesmo: protegemos nossos programas para que ninguém bagunce ou roube nada. Isso é cibersegurança!")
    input("\n\nPressione ENTER para avançar...\n")
    print("Quando você cria algo com Python, como um joguinho ou uma calculadora, pode ter informações importantes ali. Se alguém malvado invadir seu código, pode apagar tudo ou pegar dados secretos. A cibersegurança ajuda a evitar que isso aconteça. É como colocar senha no seu programa.")
    input("\n\nPressione ENTER para avançar...\n")
    print("Usar senhas fortes, tomar cuidado com links estranhos e não mostrar seu código para qualquer um são jeitos de se proteger. Também existem comandos em Python que ajudam a deixar o programa mais seguro. Com o tempo, você vai aprender a usar essas ferramentas para ser um programador esperto!")
    input("\n\nPressione ENTER para avançar à próxima bolha FINAL...\n")

def bolha_4(matricula_atual):
    
    pontuacao = 0
    print("O que é um \"algoritmo\" na programação? ")
    print("a) Um tipo de computador")
    print("b) Uma sequência de passos para resolver um problema")
    print("c) Um programa de edição de fotos")
    resposta_correta = "b"
    resposta_aluno = input("\nEscolha a alternativa correta (a, b ou c): ").strip().lower()
    if resposta_aluno == resposta_correta:
        pontuacao += 25
        print("\nParabéns! Você acertou!")
    else:
        print("\nOps! Não foi dessa vez.")
    input("\nPressione ENTER para continuar...")

    print("Para que serve um fluxograma?")
    print("a) Mostrar o caminho que o programa segue, com ações e decisões")
    print("b) Desenhar personagens de jogos")
    print("c) Fazer contas matemáticas")
    resposta_correta = "a"
    resposta_aluno = input("\nEscolha a alternativa correta (a, b ou c): ").strip().lower()
    while resposta_aluno not in ['a', 'b', 'c']:
        print("Opção inválida! Por favor, escolha a, b ou c.")
        resposta_aluno = input("Escolha a alternativa correta (a, b ou c): ").strip().lower()
    if resposta_aluno == resposta_correta:
        pontuacao += 25
        print("\nParabéns! Você acertou!")
    else:
        print("\nOps! Não foi dessa vez.")
    input("\nPressione ENTER para continuar...")

    print("Por que não devemos clicar em links estranhos que aparecem em jogos online?")
    print("a) Porque podem ser golpes para roubar sua conta ou infectar o computador com vírus!")
    print("b) Porque o link pode ser de um jogo novo e muito legal.")
    print("c) Porque o link pode fazer seu computador ficar mais rápido.")
    resposta_correta = "a"
    resposta_aluno = input("\nEscolha a alternativa correta (a, b ou c): ").strip().lower()
    if resposta_aluno == resposta_correta:
        pontuacao += 25
        print("\nParabéns! Você acertou!")
    else:
        print("\nOps! Não foi dessa vez.")
    input("\nPressione ENTER para continuar...")

    print("O que um 'antivírus' faz no computador?")
    print("a) Toca música")
    print("b) Protege contra vírus e hackers")
    print("c) Aumenta o brilho da tela")
    resposta_correta = "b"
    resposta_aluno = input("\nEscolha a alternativa correta (a, b ou c): ").strip().lower()
    if resposta_aluno == resposta_correta:
        pontuacao += 25
        print("\nParabéns! Você acertou!")
    else:
        print("\nOps! Não foi dessa vez.")
    print(f"\nSua pontuação final: {pontuacao}/100")

    dados = carregar_dados()
    for aluno in dados["alunos"]:
        if aluno["matricula"] == matricula_atual:
            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            registro_nota = {
                "pontuacao": pontuacao,
                "data": data_atual
            }
            if "notas" not in aluno:
                aluno["notas"] = []
            aluno["notas"].append(registro_nota)
            salvar_dados(dados)
            break
    input("\nPressione ENTER para finalizar...")

def ver_historico(matricula_atual):
    dados = carregar_dados()
    for aluno in dados["alunos"]:
        if aluno["matricula"] == matricula_atual:
            if "notas" in aluno and aluno["notas"]:
                print("\n=== SEU HISTÓRICO DE NOTAS ===")
                for i, registro in enumerate(aluno["notas"], 1):
                    print(f"Tentativa {i}: {registro['pontuacao']}/100 - Data: {registro['data']}")
                total_notas = sum(registro['pontuacao'] for registro in aluno["notas"])
                media = total_notas / len(aluno["notas"])
                print(f"\nSua média atual: {media:.1f}/100")
            else:
                print("\nVocê ainda não realizou nenhum teste.")
            break
    input("\n\nPressione ENTER para finalizar...\n")

def login():
    print("=============== LOGIN ================")
    matricula = input("Insira sua matrícula: ")
    senha = input("Insira sua senha: ")
    cadastros = carregar_dados()
    for aluno in cadastros["alunos"]:
        if aluno["matricula"] == matricula and aluno["senha"] == senha:
            print("Login com sucesso!")
            print(f"\nOlá {aluno['nome']}")
            print("Bem-vindo à Bolhas de conhecimento!")
            print("\nNossa plataforma é bem fácil de usar. Em cada etapa, você encontrará materiais de aprendizado e atividades para praticar. O nosso ponto de partida é preparar o seu computador para essa jornada. Para isso, preparamos um vídeo tutorial bem curtinho que vai te mostrar como instalar dois programas importantes: o Python, que é a linguagem de programação que vamos aprender, e o VS Code, que é onde vamos escrever os nossos códigos. Depois de assistir ao vídeo e instalar os programas, você estará pronto para seguir para a próxima bolha de conhecimento! Lá, você encontrará explicações e exercícios práticos para começar a programar, entender sobre segurança na internet e aprender a pensar como um programador.")

            input("\n\nPressione ENTER para avançar...")

            print(f"""\nAssista ao vídeo de instalação aqui: {URL_VIDEO}
Depois de assistir ao vídeo e instalar os programas, você estará pronto para seguir para a próxima bolha de conhecimento!""")
                
            input("\n\nPressione ENTER para avançar...")
            while True:
                escolha = menu_ensino()
                if escolha == '1':
                    bolha_1()
                elif escolha == '2':
                    bolha_2()
                elif escolha == '3':
                    bolha_3()
                elif escolha == '4':
                    bolha_4(matricula)
                elif escolha == '5':
                    ver_historico(matricula)
                elif escolha == '6':
                    print("\nAté a próxima!")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            return
    print("Matrícula ou senha incorretas.")


def main():
    print("Bem-vindo à Bolha de Conhecimento")
    while True:
        print("\n======== MENU PRINCIPAL ========")
        option = input("1 - Fazer Login\n2 - Fazer Cadastro\n3 - Sair\nEscolha uma opção: ")
        
        if option == "1":
            login() 
        elif option == "2":
            cadastrar_aluno()
        elif option == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()