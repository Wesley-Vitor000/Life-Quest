# Life Quests — Gamificação de Hábitos

**Status:** em desenvolvimento · **Tecnologia principal:** Python

O **Life Quests** é um projeto pessoal de estudos que transforma hábitos do dia a dia em missões, com metas, recompensas em pontos de experiência (XP) e evolução de nível, inspirado em jogos de RPG.

> **Estado atual:** este repositório contém uma versão funcional para **terminal**, escrita em Python. Uma interface web/mobile faz parte da evolução planejada do projeto e não está disponível neste repositório.

## Funcionalidades implementadas

- Menu de terminal para consultar o status do jogador e o quadro de missões.
- Missões com metas, progresso, recompensas e estados (não iniciada, em andamento e concluída).
- Atualização do progresso e conclusão automática ao atingir a meta.
- Sistema de XP, evolução de nível e títulos.
- Persistência local do progresso em arquivo JSON.

## Tecnologias e conceitos

- **Python 3:** funções, laços, condicionais, listas e dicionários.
- **JSON:** gravação e carregamento do estado do jogador e das missões.
- **Biblioteca padrão:** módulos `json`, `os` e `pathlib`.

## Como executar

1. Tenha o Python 3 instalado.
2. Baixe ou clone este repositório.
3. No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

O arquivo `save.json` armazena o progresso da versão de terminal e é atualizado ao salvar o jogo. O repositório contém um exemplo desse arquivo.

## Estrutura atual

```text
Life-Quest/
├── main.py       # Lógica, menus e missões
├── save.json     # Exemplo de dados e progresso persistido
└── README.md     # Documentação
```

## Próximas melhorias

- Evolução da interface responsiva para web/mobile.
- Separação entre dados de exemplo e progresso local do usuário.
- Melhorias na validação das entradas e testes automatizados.

---

Desenvolvido por [Wesley Vitor](https://github.com/Wesley-Vitor000) como projeto de aprendizado em desenvolvimento de software.
