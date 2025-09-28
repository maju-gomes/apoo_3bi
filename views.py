import streamlit as st
from controller.itemController import ItemController

controller = ItemController()

st.title("Cadastro de Itens")

menu = ["Cadastrar", "Listar"]
escolha = st.sidebar.selectbox("Menu", menu)

if escolha == "Cadastrar":
    st.subheader("Cadastrar novo item")
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)

    if st.button("Salvar"):
        controller.criarItem(descricao, quantidade)
        st.success("Item cadastrado com sucesso!")

elif escolha == "Listar":
    st.subheader("Lista de Itens")
    itens = controller.obterTodosOsItens()

    if itens:
        for item in itens:
            st.write(f"ID: {item.get_id()} | {item.get_descricao()} ({item.get_quantidade()})")
    else:
        st.info("Nenhum item cadastrado ainda.")
