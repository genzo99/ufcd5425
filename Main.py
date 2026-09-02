from db import init_db


def mostrar_menu():
    print("\n=== SISTEMA DE GESTÃO DE TAREFAS E PROJETOS ===")
    print("1 - Listar projetos")
    print("2 - Criar projeto")
    print("3 - Gerir tarefas de um projeto")
    print("0 - Sair")


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
            print("TODO: listar projetos")
        elif opcao == "2":
            print("TODO: criar projeto")
        elif opcao == "3":
            print("TODO: gerir tarefas")
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
