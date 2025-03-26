"""Funções auxiliares para gerar CSV e PDF"""
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_csv(dados: dict, caminho: str):
    # Cria um DataFrame com os moradores e seus valores
    df = pd.DataFrame({
        "Morador": dados["moradores"],
        "Valor do Mês": [dados["total"]]
    })
    # Salva o CSV
    df.to_csv(caminho, index=False)

def gerar_pdf(dados: dict, caminho: str):
    # Inicializa o canvas do PDF
    c = canvas.Canvas(caminho, pagesize=A4)
    y = 800  # Posição inicial no eixo Y
    
    # Título
    c.drawString(100, y, "Planiha Casinha JSB")
    y -= 30
    
    # Tabela de moradores
    c.drawString(100, y, "Moradores | Valor do Mês")
    y -= 20
    for morador in dados["moradores"]:
        c.drawString(100, y, f"{morador} | R$ {dados['valor_por_morador']:.2f}")
        y -= 20
    
    # Tabela de gastos
    y -= 20
    c.drawString(100, y, "Gastos")
    y -= 20
    despesas = dados["despesas"]
    c.drawString(100, y, f"Aluguel: R$ {despesas['aluguel']:.2f}")
    y -= 20
    c.drawString(100, y, f"Água: R$ {despesas['agua']:.2f}")
    y -= 20
    c.drawString(100, y, f"Energia: R$ {despesas['energia']:.2f}")
    y -= 20
    c.drawString(100, y, f"TV/Internet: R$ {despesas['tv_internet']:.2f}")
    y -= 20
    c.drawString(100, y, f"IPTU: R$ {despesas['iptu']:.2f}")
    
    # Extras
    y -= 20
    c.drawString(100, y, "Extras")
    y -= 20
    for item, valor in despesas["extras"].items():
        c.drawString(100, y, f"{item}: R$ {valor:.2f}")
        y -= 20
    
    # Total
    y -= 20
    c.drawString(100, y, f"Total: R$ {dados['total']:.2f}")
    
    # Finaliza o PDF
    c.save()