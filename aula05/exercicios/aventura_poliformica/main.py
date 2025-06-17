from personagem import Personagem
from inimigo import Inimigo


def jogo_de_turno():
    print("Bem-vindo ao Jogo de Turnos!")
    print("Você controlará Arthur contra um Goblin!")

    # Instancia os objetos do jogador e do inimigo
    heroi = Personagem("Arthur", 50, 10)
    monstro = Inimigo("Goblin", 40, 8)

    # Loop do jogo
    while heroi.vida > 0 and monstro.vida > 0:
        print("\n--- Turno do Jogador ---")
        print("Escolha uma ação:")
        print("1. Atacar")
        print("2. Defender")
        print("3. Usar Habilidade Especial")
        escolha = input("Digite o número da sua ação: ")

        if escolha == "1":
            dano = heroi.atacar()
            monstro.receber_dano(dano)
        elif escolha == "2":
            heroi.defender()
        elif escolha == "3":
            dano = heroi.usar_habilidade_especial()
            monstro.receber_dano(dano)
        else:
            print("Escolha inválida! Você perdeu o turno.")

        # Verifica se o inimigo foi derrotado
        if monstro.vida <= 0:
            break

        print("\n--- Turno do Inimigo ---")
        acao_inimigo = monstro.agir()
        if acao_inimigo == "atacar":
            dano = monstro.atacar()
            heroi.receber_dano(dano)
        elif acao_inimigo == "defender":
            monstro.defender()

    print("\n--- Fim do Jogo ---")
    if heroi.vida > 0:
        print(f"Parabéns, {heroi.nome} venceu a batalha!")
    else:
        print(f"{monstro.nome} venceu a batalha! Tente novamente.")


if __name__ == "__main__":
    jogo_de_turno()
