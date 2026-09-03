"""Cadastro de Produto - aplicacao de linha de comando."""

from produto import Produto

produtos = []


def menu():
    print()
    print("=== Cadastro de Produto ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("0 - Sair")


def cadastrar():
    nome = input("Nome do produto: ")
    preco = float(input("Preco: "))
    quantidade = int(input("Quantidade: "))
    produtos.append(Produto(nome, preco, quantidade))
    print("Produto cadastrado com sucesso.")


def listar():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. {produto}")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
