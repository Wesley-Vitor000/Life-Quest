
from InquirerPy import inquirer

opcao = inquirer.select(
    message="⚔️ LIFE QUEST — Escolha uma ação:",
    choices=[
        "Exibir status do jogador",
        "Exibir quadro de missões",
        "Atualizar progresso",
        "Sair do jogo"
    ],
    pointer="❯",
    cycle=True
).execute()

print(f"\nVocê selecionou: {opcao}")
