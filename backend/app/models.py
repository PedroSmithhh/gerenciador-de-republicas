"""Definições de modelos de dados usando Pydantic"""
from pydantic import BaseModel
from typing import Dict

# Modelo para as despesas
class Despesa(BaseModel):
    aluguel: float = 0.0
    agua: float = 0.0
    energia: float = 0.0
    tv_internet: float = 0.0
    iptu: float = 0.0
    internet: float = 0.0
    extras: Dict[str, float] = {}  # {"manutenção": 50.0, "piso": 20.0}