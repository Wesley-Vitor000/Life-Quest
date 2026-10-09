# Life Quest

# Funções do APP


# Função para exibir o menu principal
def exibir_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Exibir status do jogador")
    print("2. Exibir quadro de missões")
    print("3. Atualizar progresso da missão")
    print("0. Sair do jogo")


# Função para exibir status do jogador
def exibir_status(jogador):
    print("\n===== STATUS DO JOGADOR =====")
    print(f"Nome: {jogador['nome']}")
    print(f"Nível: {jogador['nivel']}")
    
    # Porcentagem de XP para o próximo nível
    porcentagem_xp = (jogador['xp'] / jogador['proximo_nivel']) * 100
    blocos_preenchidos = int(porcentagem_xp / 10)
    blocos_vazios = 10 - blocos_preenchidos
    barra_preenchida = "█" * blocos_preenchidos
    barra_vazia = "░" * blocos_vazios
        
    
    
    print(f"XP: {jogador['xp']} / {jogador['proximo_nivel']} {barra_preenchida}{barra_vazia} ({porcentagem_xp:.0f}%)")
    print(f"Título: {jogador['titulo']}")
    print("Digite 0 para voltar ao menu.")



# Função para iniciar a missão
def iniciar_missao(missao):
    if missao["status"] == "concluida":
        print(f"A missão '{missao['nome']}' já foi concluída. Escolha outra missão.")
        return
    elif missao["status"] == "nao iniciada":
        missao["status"] = "em andamento"
        print(f"Você iniciou a missão: {missao['nome']}")
        print(f"Descrição: {missao['descricao']}")
        print(f"Meta: {missao['meta']} {missao['unidade']}")
        print(f"Progresso: {missao['progresso']} {missao['unidade']}")
        print(f"Recompensa: {missao['recompensa']} XP")
        print(f"Status: {missao['status']}")


# Função para atualizar o progresso da missão
def atualizar_progresso(missao, incremento):
    
    if missao["status"] != "em andamento":
        print(f"A missão '{missao['nome']}' não está em andamento. Por favor, inicie a missão antes de atualizar o progresso.")
        return
    
    missao["progresso"] += incremento
    if missao["progresso"] >= missao["meta"]:
        missao["status"] = "concluida"
        missao["progresso"] = missao["meta"]  # Garante que o progresso não ultrapasse a meta
        print(f"Parabéns! Você concluiu a missão: {missao['nome']}")
        print(f"Você ganhou +{missao['recompensa']} XP!")
        jogador["xp"] += missao["recompensa"]
        verificar_nivel(jogador)
        print(f"XP atual: {jogador['xp']}")
    else:
        print(f"Progresso atualizado: {missao['progresso']} {missao['unidade']}")


# Função para verificar se o jogador subiu de nível
def verificar_nivel(jogador):
    xp_atual = jogador["xp"]

    while xp_atual >= jogador["proximo_nivel"]:
        jogador["nivel"] += 1
        print(f"Parabéns! Você subiu para o nível {jogador['nivel']}!")
        
        if jogador["nivel"] in titulos:
            jogador["titulo"] = titulos[jogador["nivel"]]        
            print(f"🏆 Novo título conquistado!\n⚔️ {jogador['titulo']}")
            
        xp_restante = xp_atual - jogador["proximo_nivel"]
        xp_atual = xp_restante
        jogador["xp"] = xp_atual
        jogador["proximo_nivel"] = int(
        jogador["proximo_nivel"] * 1.5)  # Aumenta a meta para o próximo nível
        print(f"Requisito para o próximo nível: {jogador['proximo_nivel']} XP")


# Função exibir quadro de missões e iniciar missão
def exibir_quadro_missoes_e_iniciar(missoes):
    print("\n===== QUADRO DE MISSÕES =====")
    
    indice = 0
    
    while True:
        missao = missoes[indice]
        soma_de_indice = 1
        print(f"\nMissão {indice + soma_de_indice} de {len(missoes)}")
        print(f"{indice + soma_de_indice}. {missao['nome']}\nDescrição: {missao['descricao']}\nMeta: {missao['meta']}\nProgresso: {missao['progresso']}\nUnidade: {missao['unidade']}\nRecompensa: {missao['recompensa']}Xp\nStatus: {missao['status']}\n")
        print("[A] Anterior | [P] Próximo | [I] Iniciar Missão | [0] Voltar ao Menu")
        escolha = input(">>> ").lower()
        
        if escolha == "a":
            if indice > 0:
                indice -= 1
            else:
                print("Você já está na primeira missão.")
        
        elif escolha == "p":
            if indice < len(missoes) -1:
                indice += 1
            else:
                print("Você já está na última missão.")
        elif escolha == "i":
            if missao["status"] == "concluida":
                print(f"A missão '{missao['nome']}' já foi concluída. Escolha outra missão.")
            elif missao["status"] == "em andamento":
                print(f"A missão '{missao['nome']}' já está em andamento. Você pode atualizar o progresso no menu de atualização de missões.")
            elif missao["status"] == "nao iniciada":
                iniciar_missao(missao)
        elif escolha == "0":
            return escolha
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


# Função para exibir missões e permitir ao jogador escolher uma para atualizar o progresso
def selecionar_missao_para_atualizar(missoes):
    print("\n===== ATUALIZAR PROGRESSO DA MISSÃO =====")
    
    while True:
        for i, missao in enumerate(missoes):
            print(f"{i + 1}. {missao['nome']} - Status: {missao['status']} - Progresso: {missao['progresso']}/{missao['meta']} {missao['unidade']}")
        print("Digite o número da missão que deseja atualizar ou 0 para voltar ao menu.")
        missao_selecionada = input(">>> ")
        if missao_selecionada.isdigit() and 1 <= int(missao_selecionada) <= len(missoes):
            indice = int(missao_selecionada) - 1
            if missoes[indice]["status"] == "concluida":
                print(f"A missão '{missoes[indice]['nome']}' já foi concluída. Por favor, escolha outra missão.")
                continue
            elif missoes[indice]["status"] == "nao iniciada":
                print(f"A missão '{missoes[indice]['nome']}' ainda não foi iniciada. Por favor, inicie a missão antes de atualizar o progresso.")
                continue
            elif missoes[indice]["status"] == "em andamento":
                print(f"Você selecionou a missão '{missoes[indice]['nome']}' para atualizar o progresso.")
                return missoes[indice]
        elif missao_selecionada == "0":
            break
        else:
            print("Opção inválida. Por favor, escolha uma missão válida ou 0 para voltar ao menu.")
    

# Dados do Jogador
jogador = {
    "nome": "Wesley",
    "nivel": 1,
    "proximo_nivel": 100,
    "xp": 0,
    "titulo": "Plebeu da Primeira Jornada",
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
        "status": "nao iniciada",
    },
    {
        "nome": "Caminhada do Herói",
        "descricao": "Caminhe 10.000 passos",
        "meta": 10000,
        "progresso": 0,
        "unidade": "passos",
        "recompensa": 50,
        "status": "nao iniciada",
    },
    {
        "nome": "Sono do Guardião",
        "descricao": "Durma 8 horas por noite",
        "meta": 8,
        "progresso": 0,
        "unidade": "horas",
        "recompensa": 30,
        "status": "nao iniciada",
    },
]


# Titulos Life Quest
titulos = {
    1: "Plebeu da Primeira Jornada",
    10: "Aventureiro dos Caminhos Selvagens",
    20: "Guerreiro de Sangue e Aço",
    30: "Cavaleiro do Juramento Antigo",
    40: "Guardião das Terras Sagradas",
    50: "Herói das Grandes Batalhas",
    60: "Campeão da Coroa Dourada",
    70: "Mestre das Mil Jornadas",
    80: "Lorde das Terras Conquistadas",
    90: "Soberano do Último Reino",
    100: "Lenda Além do Tempo"
}


nome = input("Digite o seu nome aventureiro: ")
jogador["nome"] = nome


while True:
    exibir_menu()
    opcao = input(">>> ")

    # Exibir status do jogador
    if opcao == "1":
        while True:
            exibir_status(jogador)
            voltar_status = input(">>> ")
            
            if voltar_status.isdigit() and int(voltar_status) == 0:
                break
            else:
                print("Opção inválida. Por favor, digite 0 para voltar ao menu.")
                

    # Exibir quadro de missões
    elif opcao == "2":

        exibir_quadro_missoes_e_iniciar(missoes)

    
    # Atualizar progresso da missão
    elif opcao == "3":
        while True:
            missao_selecionada = selecionar_missao_para_atualizar(missoes)
            if missao_selecionada is None:
                break
            
            # While do incremento de progresso
            while True:
                progresso_incremento = input(f"Quanto de progresso você deseja adicionar à missão '{missao_selecionada['nome']}'? ")
                
                if progresso_incremento.isdigit() and int(progresso_incremento) > 0:
                    progresso_incremento = int(progresso_incremento)
                    atualizar_progresso(missao_selecionada, progresso_incremento)
                    break  # Sai do loop após atualizar o progresso
                else:
                    print("Opção inválida. Por favor, insira um número válido maior que 0.")
                    continue
                
            # While da pergunta
            while True:
                continuar_atualizacao = input("Deseja atualizar outra missão? (s/n): ")
                
                if continuar_atualizacao.lower() == "s":
                    break
                elif continuar_atualizacao.lower() == "n":
                    break
                else:
                    print("Opção inválida. Por favor, insira 's' para sim ou 'n' para não.")
                
            # Sai do loop principal se o usuário não quiser continuar atualizando
            if continuar_atualizacao.lower() == "n":
                break
            
            else:
                print("Opção inválida. Por favor, insira um número válido.")
        
    elif opcao == "0":
        print("Saindo do jogo. Até a próxima aventura!")
        break