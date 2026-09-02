from datetime import datetime
from db import (
    init_db,
    criar_projeto,
    listar_projetos,
    criar_tarefa,
    listar_tarefas
)


def mostrar_menu():
    print("\n=== SISTEMA DE GESTÃO DE TAREFAS E PROJETOS ===")
    print("1 - Listar projetos")
    print("2 - Criar projeto")
    print("3 - Gerir tarefas de um projeto")
    print("0 - Sair")


# ---------------------------
# PROJETOS
# ---------------------------

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


# ---------------------------
# TAREFAS
# ---------------------------

def menu_tarefas(id_projeto):
    while True:
        print("\n=== GESTÃO DE TAREFAS ===")
        print("1 - Listar tarefas")
        print("2 - Criar tarefa")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break
        elif opcao == "1":
            opcao_listar_tarefas(id_projeto)
        elif opcao == "2":
            opcao_criar_tarefa(id_projeto)
        else:
            print("Opção inválida.")


def opcao_listar_tarefas(id_projeto):
    tarefas = listar_tarefas(id_projeto)

    if not tarefas:
        print("\nNão existem tarefas neste projeto.")
        return

    print("\n=== LISTA DE TAREFAS ===")
    for t in tarefas:
        print(f"ID: {t[0]} | Título: {t[1]} | Prioridade: {t[2]} | Estado: {t[3]} | Criada em: {t[4]}")


def opcao_criar_tarefa(id_projeto):
    print("\n=== CRIAR NOVA TAREFA ===")
    titulo = input("Título da tarefa: ").strip()
    prioridade = input("Prioridade (baixa/média/alta): ").strip().lower()
    estado = "a fazer"
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not titulo:
        print("O título não pode ser vazio.")
        return

    criar_tarefa(id_projeto, titulo, prioridade, estado, data_criacao)
    print("Tarefa criada com sucesso!")


def opcao_gerir_tarefas():
    projetos = listar_projetos()

    if not projetos:
        print("\nNão existem projetos. Crie um primeiro.")
        return

    print("\n=== SELECIONE UM PROJETO ===")
    for p in projetos:
        print(f"{p[0]} - {p[1]}")

    try:
        id_projeto = int(input("ID do projeto: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    ids_validos = [p[0] for p in projetos]

    if id_projeto not in ids_validos:
        print("Projeto não encontrado.")
        return

    menu_tarefas(id_projeto)


# ---------------------------
# MAIN
# ---------------------------

def main():
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
            opcao_gerir_tarefas()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
