import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("API_TOKEN")  # Render’da token Environment’dan olinadi

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Baza
conn = sqlite3.connect("hisobchi.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    type TEXT,
    amount REAL,
    category TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")
conn.commit()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Salom! Men buxgalteriya hisobchi botman 📊")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
