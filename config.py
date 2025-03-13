import os

# Токены Telegram-ботов
TELEGRAM_CLIENT_TOKEN = os.environ.get("TELEGRAM_CLIENT_TOKEN")
TELEGRAM_ADMIN_TOKEN = os.environ.get("TELEGRAM_ADMIN_TOKEN")

# Ключ OpenAI API
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Параметры подключения к базе данных PostgreSQL
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
