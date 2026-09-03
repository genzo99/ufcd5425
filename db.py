import sqlite3

DB_NAME = "task_manager.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            data_criacao TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_projeto INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            estado TEXT NOT NULL,
            data_criacao TEXT NOT NULL,
            FOREIGN KEY (id_projeto) REFERENCES projetos (id)
        );
    """)

    conn.commit()
    conn.close()


# ---------------------------
# PROJETOS
# ---------------------------

def criar_projeto(nome, descricao, data_criacao):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO projetos (nome, descricao, data_criacao)
        VALUES (?, ?, ?)
    """, (nome, descricao, data_criacao))

    conn.commit()
    conn.close()


def listar_projetos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, descricao, data_criacao FROM projetos")
    projetos = cursor.fetchall()

    conn.close()
    return projetos


# ---------------------------
# TAREFAS
# ---------------------------

def criar_tarefa(id_projeto, titulo, prioridade, estado, data_criacao):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tarefas (id_projeto, titulo, prioridade, estado, data_criacao)
        VALUES (?, ?, ?, ?, ?)
    """, (id_projeto, titulo, prioridade, estado, data_criacao))

    conn.commit()
    conn.close()


def listar_tarefas(id_projeto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, prioridade, estado, data_criacao
        FROM tarefas
        WHERE id_projeto = ?
    """, (id_projeto,))

    tarefas = cursor.fetchall()
    conn.close()
    return tarefas


def editar_tarefa(id_tarefa, novo_titulo, nova_prioridade, novo_estado):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET titulo = ?, prioridade = ?, estado = ?
        WHERE id = ?
    """, (novo_titulo, nova_prioridade, novo_estado, id_tarefa))

    conn.commit()
    conn.close()


def remover_tarefa(id_tarefa):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()


# ---------------------------
# FILTROS
# ---------------------------

def filtrar_tarefas_por_estado(id_projeto, estado):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, prioridade, estado, data_criacao
        FROM tarefas
        WHERE id_projeto = ? AND estado = ?
    """, (id_projeto, estado))

    tarefas = cursor.fetchall()
    conn.close()
    return tarefas


def filtrar_tarefas_por_prioridade(id_projeto, prioridade):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, prioridade, estado, data_criacao
        FROM tarefas
        WHERE id_projeto = ? AND prioridade = ?
    """, (id_projeto, prioridade))

    tarefas = cursor.fetchall()
    conn.close()
    return tarefas
