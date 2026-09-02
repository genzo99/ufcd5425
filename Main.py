from datetime import datetime
from db import init_db, criar_projeto, listar_projetos


def mostrar_menu():
    print("\n=== SISTEMA DE GESTÃO DE TAREFAS E PROJETOS ===")
    print("1 - Listar projetos")
    print("2 - Criar projeto")
    print("3 - Gerir tarefas de um projeto")
    print("0 - Sair")


def opcao_listar_projetos():
    projetos = listar_projetos()

    if not projetos:
        print("\nNão existem projetos criados.")
        return

    print("\n=== LISTA DE PROJETOS ===")
    for p in projetos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Descrição: {p[2]} | Criado em: {p[3]}")


def opcao_criar_projeto():
    print("\n=== CRIAR NOVO PROJETO ===")
    nome = input("Nome do projeto: ").strip()
    descricao = input("Descrição do projeto: ").strip()
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not nome:
        print("O nome do projeto não pode ser vazio.")
        return

    criar_projeto(nome, descricao, data_criacao)
    print("Projeto criado com sucesso!")


def main():
    # Inicializar base de dados
    init_db()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("A sair da aplicação...")
            break
        elif opcao == "1":
            opcao_listar_projetos()
        elif opcao == "2":
            opcao_criar_projeto()
        elif opcao == "3":
            print("TODO: gerir tarefas de um projeto")
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
