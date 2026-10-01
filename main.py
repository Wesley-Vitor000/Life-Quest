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
    print("Digite 0 para voltar ao menu.")




# Exibir quadro de missões
def exibir_missoes(missoes):
    print("\n===== QUADRO DE MISSÕES =====")
    for i, missao in enumerate(missoes):
        print(f"{i + 1}. {missao['nome']}\nDescrição: {missao['descricao']}\nMeta: {missao['meta']}\nProgresso: {missao['progresso']}\nUnidade: {missao['unidade']}\nRecompensa: {missao['recompensa']}\nStatus: {missao['status']}\n")
    print("Digite 0 para voltar ao menu.")




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
    
    
    # Exibir status do jogador
    if opcao == "1":
        exibir_status(jogador)
        voltar_status = int(input(">>> "))
        
        if voltar_status == 0:
            continue
    
    # Exibir quadro de missões    
    elif opcao == "2":
        exibir_missoes(missoes)
        voltar_quadro_missoes = int(input(">>> "))
        
        if voltar_quadro_missoes == 0:
            continue
    
    # Iniciar missão    
    elif opcao == "3":
        print("Digite o número conrrespondente a missão desejada")
        exibir_missoes(missoes)
        escolha_missao = input(">>> ")
        
        if escolha_missao.isdigit():
            escolha_missao_int = int(escolha_missao)
            
            if escolha_missao_int == 0:
                continue
            
            elif escolha_missao_int >= 1 and escolha_missao_int <= len(missoes):
                indice = escolha_missao_int - 1
                missao_escolhida = missoes[indice]           
                iniciar_missao(missao_escolhida)
        else:
            print("Opção inválida. Por favor, escolha uma missão válida.")
    
    # Atualizar progresso da missão    
    elif opcao == "4":
        exibir_missoes(missoes)
        opcao_progresso = input("Qual missão você deseja atualizar o seu progresso? ")
        
        if opcao_progresso.isdigit():
            opcao_progresso_int = int(opcao_progresso)
            
            if opcao_progresso_int == 0:
                continue 
            elif opcao_progresso_int >= 1 and opcao_progresso_int <= len(missoes):
                opcao_progresso = opcao_progresso_int - 1
                missao_selecionada = missoes[opcao_progresso]
                
                if missao_selecionada['status'] == 'concluida':
                    print(f"A missão '{missao_selecionada['nome']}' já foi concluída. Escolha outra missão.")
                    continue
                elif missao_selecionada['status'] == 'nao iniciada':
                    print(f"A missão '{missao_selecionada['nome']}' ainda não foi iniciada. Por favor, inicie a missão antes de atualizar o progresso.")
                    continue
                elif missao_selecionada['status'] == 'em andamento':
                    print(f"Você escolheu a missão: {missao_selecionada['nome']}.")
                    progresso_incremento = input(f"Digite a quantidade de {missao_selecionada['unidade']} que você deseja adicionar ao progresso da missão: ")
            else:
                print("Opção inválida. Por favor, escolha uma missão válida.")
                continue
        
        
        if progresso_incremento.isdigit():
            progresso_incremento_int = int(progresso_incremento)
            atualizar_progresso(missao_selecionada, progresso_incremento_int)
        else:
            print("Opção inválida. Por favor, insira um número válido.")
        
    
    # Sair do programa
    elif opcao == "0":
        print("Saindo do programa.. até a próxima!")
        break