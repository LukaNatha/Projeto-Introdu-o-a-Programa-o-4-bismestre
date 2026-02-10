import json

with open("cardapio.json", "r") as f:
    cardapio = json.load(f)

with open("pedidos.json", "r") as f:
    pedidos = json.load(f)

def salvar_pedidos():
    with open("pedidos.json", "w") as f:
        json.dump(pedidos, f, indent = 4)

def mostrar_cardapio():
    print("\nCARDÁPIO")
    for pizza, preco in cardapio.items():
        print(f"{pizza} - R$ {preco}")

def adicionar_pedido():
    nome_cliente = input("Digite seu nome: ").lower()
    pizza = input("Nome da pizza: ").lower()

    if pizza in cardapio:
        quantidade = int(input("Quantidade: "))
        tamanho = input("Tamanho (P/M/G): ").upper()

        pedido = {
            "cliente": nome_cliente,
            "pizza": pizza,
            "quantidade": quantidade,
            "tamanho": tamanho,
            "preco": cardapio[pizza]
        }

        pedidos.append(pedido)
        salvar_pedidos()
        print("Pizza adicionada com sucesso!")
    else:
        print("Pizza não encontrada")

def ver_pedidos():
    if len(pedidos) == 0:
        print("Nenhum pedido registrado")
    else:
        print("\nPEDIDOS")
        for i, p in enumerate(pedidos):
            print(f"{i} - {p['cliente']} | {p['pizza']} | {p['quantidade']}x | R$ {p['preco']}")
            

def calcular_total():
    total = 0
    for p in pedidos:
        total += p["quantidade"] * p["preco"]
    return total

def remover_pedido():
    ver_pedidos()
    if len(pedidos) > 0:
        indice = int(input("Digite o número do pedido para remover: "))
        if 0 <= indice < len(pedidos):
            pedidos.pop(indice)
            salvar_pedidos()
            print("Pedido removido")
        else:
            print("Índice inválido")


while True:
    print("\nPIZZARIA")
    print("1 - Ver cardápio")
    print("2 - Adicionar pizza")
    print("3 - Remover pedido")
    print("4 - Ver pedidos")
    print("5 - Finalizar pedido")
    print("6 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        mostrar_cardapio()
    elif opcao == "2":
        adicionar_pedido()
    elif opcao == "3":
        remover_pedido()
    elif opcao == "4":
        ver_pedidos()
    elif opcao == "5":
        total = calcular_total()
        print("Total a pagar: R$", total)
        break
    elif opcao == "6":
        print("Saindo...")
        break
    else:

        print("Opção inválida")
