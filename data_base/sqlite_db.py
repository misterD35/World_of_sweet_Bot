import sqlite3 as sq
from create_bot import bot


class Dessert:
    photo: str
    name: str
    description: str
    price: str


def sql_start():
    global base, cur
    base = sq.connect('world_of_sweet_menu.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute(f'CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_position(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read_and_send(message):
    for menu_pos in cur.execute('SELECT * FROM menu').fetchall():
        # print(cur.execute('SELECT * FROM menu').fetchall())
        await bot.send_photo(message.from_user.id, menu_pos[0], f'{menu_pos[1]}\nОписание: {menu_pos[2]}\nЦена {menu_pos[-1]}')


async def sql_read_only():
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete_position(name_pos):
    cur.execute('DELETE FROM menu WHERE name = ?', (name_pos,))
    base.commit()
