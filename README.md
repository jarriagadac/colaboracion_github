# colaboracion_github

## Ambiente de Desarrollo

### Configurar un ambiente virtual de python

```ps
PS > python -m venv venv
PS > .\venv\Scripts\Activate.ps1
(venv) PS > python -m pip install --upgrade pip
(venv) PS > pip install -r requirements.txt
```

### Consideraciones

- Copiar archivo src/telegram_bot/.env-example a src/telegram_bot/.env e incluir credenciales bot Telegram

## Documentación

- https://core.telegram.org/bots
- https://python-telegram-bot.readthedocs.io/en/stable/
- https://pypi.org/project/python-dotenv/
