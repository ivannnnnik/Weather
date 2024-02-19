import asyncio
from random import randint

import aiosqlite
from flask import Flask

app = Flask(__name__)


async def create_tables():
    async with aiosqlite.connect('users.db') as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(255),
                balance INTEGER
            )
        ''')
        for _ in range(5):
            username = f"User{_ + 1}"
            balance = randint(5000, 15000)
            print(username, balance)
            await db.execute('INSERT INTO users (username, balance) VALUES (?, ?)', (username, balance))

        await db.commit()


def create_db():
    asyncio.run(create_tables())
    print('Database complete!')


from app import routes
