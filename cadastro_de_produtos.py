import json
import os

ARQUIVO = "produtos.txt"



def salvar_dados(produtos):
    """Salva no arquivo (imutável: só escreve)"""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)


def carregar_dados():
    """Carrega do arquivo"""
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def criar_produto(id, nome, preco):
    return {"id": id, "nome": nome, "preco": preco}


def adicionar_produto(produtos, produto):
    return produtos + [produto]


def listar_produtos(produtos):
    return [f"{p['id']} - {p['nome']} - R${p['preco']}" for p in produtos]


def atualizar_produto(produtos, id, novo_nome, novo_preco):
    return [
        {"id": id, "nome": novo_nome, "preco": novo_preco} if p["id"] == id else p
        for p in produtos
    ]


def deletar_produto(produtos, id):
    return [p for p in produtos if p["id"] != id]


produtos = carregar_dados()  


def menu():
    print("\n=== CRUD PRODUTOS ===")
    print("1 - Criar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("5 - Sair")


while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        id = int(input("ID: "))
        nome = input("Nome: ")
        preco = float(input("Preço: "))

        novo = criar_produto(id, nome, preco)
        produtos = adicionar_produto(produtos, novo)
        salvar_dados(produtos)

        print("Produto criado e salvo!")

    elif opcao == "2":
        print("\nProdutos:")
        for item in listar_produtos(produtos):
            print(item)

    elif opcao == "3":
        id = int(input("ID do produto: "))
        nome = input("Novo nome: ")
        preco = float(input("Novo preço: "))

        produtos = atualizar_produto(produtos, id, nome, preco)
        salvar_dados(produtos)

        print("Produto atualizado e salvo!")

    elif opcao == "4":
        id = int(input("ID do produto: "))
        produtos = deletar_produto(produtos, id)
        salvar_dados(produtos)

        print("Produto deletado e salvo!")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")