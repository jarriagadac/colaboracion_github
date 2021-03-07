from include.telegram import bot_start

# busca archivo .env en el directorio actual
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if __name__ == "__main__":
    bot_start()
