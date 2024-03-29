import aiosqlite


class User:
    @staticmethod
    async def get_user_by_id(user_id: int):
        async with aiosqlite.connect('users.db') as db:
            cursor = await db.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user_data = await cursor.fetchone()

            if user_data is None:
                raise ValueError(f"User {user_id} not found")

            return user_data

    @staticmethod
    async def update_balance(user_id: int, new_balance: float):
        async with aiosqlite.connect('users.db') as db:
            await db.execute('UPDATE users SET balance = ? WHERE id = ?', (new_balance, user_id))
            await db.commit()
