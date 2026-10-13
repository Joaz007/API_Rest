# API Loja Gamer (FastAPI)

API REST didática para gerenciamento de produtos de uma loja de videogames. O tema é diferente do exemplo de sorveteria do professor, mas mantém a estrutura simples de uma API CRUD.

## Requisitos

- Python 3.10 ou superior
- pip

## Executar no Ubuntu/Linux

Abra o terminal nesta pasta e rode:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Depois, abra:

- API: http://127.0.0.1:8000/
- Lista de produtos: http://127.0.0.1:8000/produtos/
- Documentação interativa: http://127.0.0.1:8000/docs

## Operações disponíveis

| Método | Endpoint | Operação |
|---|---|---|
| GET | `/` | Verifica se a API está ativa |
| GET | `/produtos/` | Lista os produtos |
| GET | `/produtos/{produto_id}/` | Consulta um produto |
| POST | `/produtos/` | Cadastra produto |
| PUT | `/produtos/{produto_id}/` | Atualiza produto |
| DELETE | `/produtos/{produto_id}/` | Exclui produto |

## Teste do cadastro (POST)

Na documentação `/docs`, abra `POST /produtos/`, clique em **Try it out** e use um ID ainda não cadastrado:

```json
{
  "id": 5,
  "nome": "Headset gamer",
  "categoria": "Acessório",
  "preco": 199.90,
  "estoque": 6
}
```

O resultado esperado é `201 Created`. Para atualizar, use `PUT /produtos/5/` com o corpo:

```json
{
  "nome": "Headset gamer USB",
  "categoria": "Acessório",
  "preco": 219.90,
  "estoque": 4
}
```

Os preços são dados fictícios para demonstrar a API.

## Publicar no Render

1. Envie os arquivos `main.py`, `requirements.txt` e `README.md` para um repositório GitHub.
2. No painel Render, selecione **New > Web Service** e conecte o repositório.
3. Use o comando de build `pip install -r requirements.txt`.
4. Use o comando de inicialização `uvicorn main:app --host 0.0.0.0 --port $PORT`.
5. Selecione o plano disponível adequado para o exercício e conclua a implantação.
6. Quando o serviço estiver ativo, teste a URL atribuída pelo Render, acrescentando `/`, `/produtos/` e `/docs`.

Guia oficial: https://render.com/docs/deploy-fastapi

## Limitações

Os produtos ficam em uma lista na memória e não em um banco de dados. Os dados adicionados, alterados ou removidos são perdidos quando o processo reinicia ou é reimplantado. A API é apenas didática e não implementa autenticação.