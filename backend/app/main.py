"""Arquivo principal do backend com FastAPI"""
from fastapi import FastAPI
from models import Despesa  # Importa o modelo de dados
from utils import gerar_csv, gerar_pdf  # Importa funções auxiliares

# Inicializa a aplicação FastAPI
app = FastAPI(title="Gerenciador de República API")

# Rota POST para adicionar despesas e calcular os valores
@app.post("/despesas")
def adicionar_despesa(despesa: Despesa): # Recebe e calcula as despesas por morador
    # Calcula o total dos gastos fixos
    total_fixo = despesa.aluguel + despesa.agua + despesa.energia + despesa.tv_internet + despesa.iptu + despesa.internet
    # Calcula o total dos extras (soma os valores do dicionário)
    total_extras = sum(despesa.extras.values())
    # Total geral
    total = total_fixo + total_extras
    
    # Número fixo de moradores (pode ser dinâmico no futuro)
    moradores = 4
    valor_por_morador = total / moradores
    
    # Dados para o relatório
    dados_relatorio = {
        "moradores": ["Fiu", "Mococa", "Tchola", "Tes"],
        "valor_por_morador": valor_por_morador,
        "total": total,
        "despesas": despesa.model_dump()
    }
    
    # Gera os arquivos CSV e PDF
    gerar_csv(dados_relatorio, "static/relatorio.csv")
    gerar_pdf(dados_relatorio, "static/relatorio.pdf")
    
    # Retorna o resultado como JSON
    return {"total": total, "valor_por_morador": valor_por_morador}

# Rota GET para testar se a API está funcionando
@app.get("/")
def root():
    """Rota inicial para verificar se a API está ativa."""
    return {"message": "API do Gerenciador de República funcionando!"}