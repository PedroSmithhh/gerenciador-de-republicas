"""Interface gráfica com Streamlit"""
import streamlit as st
import requests
import os

# Título da aplicação
st.title("Gerenciador de República")

# Campos de entrada para despesas fixas
st.header("Despesas Fixas")
aluguel = st.number_input("Aluguel (R$)", min_value=0.0, value=1800.0)
agua = st.number_input("Água (R$)", min_value=0.0, value=33.70)
energia = st.number_input("Energia (R$)", min_value=0.0, value=165.85)
tv_internet = st.number_input("TV/Internet (R$)", min_value=0.0, value=120.0)
iptu = st.number_input("IPTU (R$)", min_value=0.0, value=198.00)

# Campo para extras
st.header("Gastos Extras")
extras_input = st.text_area("Digite os extras (ex.: Gás: 50, Mercado: 20)", "Gás: 68.55")

# Botão para calcular e gerar relatórios
if st.button("Calcular e Gerar Relatórios"):
    # Converte o texto de extras em um dicionário
    try:
        extras_dict = {k.strip(): float(v.strip()) for k, v in [x.split(":") for x in extras_input.split(",")]}
    except ValueError:
        st.error("Formato inválido nos extras. Use: 'Item: valor, Item: valor'")
        st.stop()
    
    # Dados a serem enviados para o backend
    data = {
        "aluguel": aluguel,
        "agua": agua,
        "energia": energia,
        "tv_internet": tv_internet,
        "iptu": iptu,
        "extras": extras_dict
    }
    
    # Faz a requisição ao backend
    response = requests.post("http://localhost:8000/despesas", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Total: R$ {result['total']:.2f}")
        st.success(f"Valor por morador: R$ {result['valor_por_morador']:.2f}")
        
        # Botões para download dos arquivos gerados
        with open("static/relatorio.csv", "rb") as f:
            st.download_button("Baixar CSV", f, file_name="relatorio.csv")
        with open("static/relatorio.pdf", "rb") as f:
            st.download_button("Baixar PDF", f, file_name="relatorio.pdf")
    else:
        st.error("Erro ao processar os dados. Verifique o backend.")

# Rodapé
st.write("Desenvolvido por [Seu Nome] - 2025")