# Importação das bibliotecas necessárias
import streamlit as st
import sqlite3
import pandas as pd

# Conexão com o banco de dados SQLite
conn = sqlite3.connect("pedidos.db")
cursor = conn.cursor()

# Criar tabela para os pedidos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        cliente TEXT,
        pedido TEXT,
        valor REAL
    )
""")

# Interface do Streamlit
st.title("Aplicativo de Delivery")

# Formulário para registrar um novo pedido
cliente = st.text_input("Nome do cliente:")
pedido = st.text_area("Pedido:")
valor = st.number_input("Valor do pedido:", min_value=0.0)

if st.button("Registrar Pedido"):
    cursor.execute("INSERT INTO pedidos (cliente, pedido, valor) VALUES (?, ?, ?)", (cliente, pedido, valor))
    conn.commit()
    st.success("Pedido registrado com sucesso!")

# Exibir pedidos registrados
st.subheader("Pedidos Registrados")
#pedidos = cursor.execute("SELECT * FROM pedidos").fetchall()

df_pedidos = pd.read_sql_query("SELECT * FROM pedidos", conn)
st.dataframe(df_pedidos, hide_index=True, width=1000)

# Fechar conexão com o banco de dados
conn.close()