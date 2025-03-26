# Gerenciador de República

Aplicação para gerenciar despesas de uma república, calcular valores por morador e gerar relatórios em CSV e PDF.

## Estrutura
- `backend/`: API com FastAPI.
- `frontend/`: Interface com Streamlit.
- `static/`: Arquivos gerados (CSV e PDF).

## Instruções para Executar o Código

Para executar o sistema, siga os passos abaixo:

1. **Pré-requisitos**:
   - Instale o Python 3.8 ou superior.
   - Crie um ambiente virtual:
     ```bash
     python -m venv venv
     source venv/bin/activate  # No Windows: venv\Scripts\activate
     ```  
    - Instale as dependências listadas no requirements.txt:
      ```bash
      pip install -r requirements.txt
      ```
2. **Execução**:
    - Dentro de backend/app inicie o backend:
      ```bash
      uvicorn app.main:app
      ```
    - Abra a interface streamlit através desse link: https://gerenciador-de-republicas.streamlit.app
