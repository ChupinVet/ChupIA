from chupia import SessaoChupIA

sessao = SessaoChupIA(id_pet=1)

print("=== ChupIA - Assistente Inteligente do ChupinVet ===")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Responsável: ")

    if pergunta.lower() in ["sair", "exit"]:
        print("\nChupIA: Até mais!")
        break

    resposta = sessao.enviar(
        pergunta,
        mostrar_log=False
    )

    print("\nChupIA:", resposta)
    print()