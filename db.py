import sqlite3

DB_NAME = "task_manager.db"


def get_connection():
    """Cria e devolve uma ligação à base de dados SQLite."""
    conn = sqlite3.connect(DB_NAME)
    return conn


def init_db():
    """Cria as tabelas do projeto, caso ainda não existam."""
    conn = get_connection()
    cursor = conn.cursor()

    # Tabela de projetos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            data_criacao TEXT NOT NULL
        );
    """)

    # Tabela de tarefas
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


def criar_projeto(nome, descricao, data_criacao):
    """Insere um novo projeto na base de dados."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO projetos (nome, descricao, data_criacao)
        VALUES (?, ?, ?)
    """, (nome, descricao, data_criacao))

    conn.commit()
    conn.close()


def listar_projetos():
    """Devolve a lista de projetos existentes."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, descricao, data_criacao FROM projetos")
    projetos = cursor.fetchall()

    conn.close()
    return projetos
