# Life Quest

# Funções do APP


# Função para exibir o menu principal
def exibir_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Exibir status do jogador")
    print("2. Exibir quadro de missões")
    print("3. Iniciar missão")
    print("4. Atualizar progresso da missão")
    print("0. Sair do jogo")



# Função para exibir status do jogador
def exibir_status(jogador):
    print("\n===== STATUS DO JOGADOR =====")
    print(f"Nome: {jogador['nome']}")
    print(f"Nível: {jogador['nivel']}")
    print(f"XP: {jogador['xp']}")
    print(f"Título: {jogador['titulo']}")




# Exibir quadro de missões
def exibir_missoes(missoes):
    print("\n===== QUADRO DE MISSÕES =====")
    for i, missao in enumerate(missoes):
        print(f"{i + 1}. {missao['nome']}\nDescrição: {missao['descricao']}\nMeta: {missao['meta']}\nProgresso: {missao['progresso']}\nUnidade: {missao['unidade']}\nRecompensa: {missao['recompensa']}\nStatus: {missao['status']}\n")




# Função para iniciar a missão
def iniciar_missao(missao):
    if missao['status'] == 'concluida':
        print(f"A missão '{missao['nome']}' já foi concluída. Escolha outra missão.")
        return
    elif missao['status'] == 'nao iniciada':
        missao['status'] = 'em andamento'
        print(f"Você iniciou a missão: {missao['nome']}")
        print(f"Descrição: {missao['descricao']}")
        print(f"Meta: {missao['meta']} {missao['unidade']}")
        print(f"Progresso: {missao['progresso']} {missao['unidade']}")
        print(f"Recompensa: {missao['recompensa']} XP")
        print(f"Status: {missao['status']}")




# Função para atualizar o progresso da missão
def atualizar_progresso(missao, incremento):
    missao['progresso'] += incremento
    if missao['progresso'] >= missao['meta']:
        missao['status'] = 'concluida'
        print(f"Parabéns! Você concluiu a missão: {missao['nome']}")
        print(f"Você ganhou +{missao['recompensa']} XP!")
        jogador['xp'] += missao['recompensa']
        print(f"XP atual: {jogador['xp']}")
    else:
        print(f"Progresso atualizado: {missao['progresso']} {missao['unidade']}")
        



# Dados do Jogador
jogador = {
    "nome": "Wesley",
    "nivel": 1,
    "xp": 0,
    "titulo": "Plebeu da Primeira Jornada"
}

# Missões Life Quest
missoes = [
    
    {  
        "nome": "Poção do Vigor",
        "descricao": "Beba água ao longo do dia",
        "meta": 3000,
        "progresso": 0,
        "unidade": "ml",
        "recompensa": 20,
        "status": "nao iniciada"
    },
    {
        "nome": "Caminhada do Herói",
        "descricao": "Caminhe 10.000 passos",
        "meta": 10000,
        "progresso": 0,
        "unidade": "passos",
        "recompensa": 50,
        "status": "nao iniciada"
    },
    {
        "nome": "Sono do Guardião",
        "descricao": "Durma 8 horas por noite",
        "meta": 8,
        "progresso": 0,
        "unidade": "horas",
        "recompensa": 30,
        "status": "nao iniciada"
    }
]

nome = input("Digite o seu nome aventureiro: ")
jogador["nome"] = nome


while True:
    exibir_menu()
    opcao = input(">>> ")
    
    if opcao == "1":
        exibir_status(jogador)
    elif opcao == "2":
        exibir_missoes(missoes)
    elif opcao == "3":
        exibir_missoes(missoes)
        escolha_missao = input("Digite o número conrrespondente a missão desejada: ")
        
        if escolha_missao.isdigit() >= 0 and escolha_missao <= len(missoes):
            iniciar_missao()
    elif opcao == "4":
        exibir_missoes(missoes)
        opcao_progresso = int(input("Qual missão você deseja atualizar o seu progresso? ")) - 1
        missao_selecionada = missoes[opcao_progresso]
        print(f"Você escolheu a missão: {missao_selecionada['nome']}.")
        
        
    elif opcao == "0":
        print("Saindo do programa.. até a próxima!")
        break