# Api de pdfs

## Dependências

Para instalar as dependências, utilize o pip com o arquivo requirements-dev.txt

```
pip install -r requirements-dev.txt
```

ou instale as dependencias com o comando abaixo:

```
fastapi uvicorn python-multipart requests fonttools pymupdf pytest pytest-cov
```

## Testes

Para rodar os teste, utilize o comando:

```
pytest --cov=api tests/
```