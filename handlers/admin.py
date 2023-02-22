from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from config import user_ID
from data_base import sqlite_db
from keyboards import admin_kb
from create_bot import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def make_changes_command(message: types.Message):
    if message.from_user.id in user_ID:
        await bot.send_message(message.from_user.id, 'Что будем делать?', reply_markup=admin_kb.button_case_admin)
        await message.delete()


# @dp.message_handler(commands='Загрузить', State=None)
async def start_load_position_menu(message: types.Message):
    await FSMAdmin.photo.set()   # установить состояние "Машина состояния" (ожидание фото)
    await message.reply('Загрузи фото')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Введите название новой позиции')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи описание')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь укажи цену')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
        name_new_pos = data['name']
    # async with state.proxy() as data:
    #     await message.reply(str(data))
    await sqlite_db.sql_add_position(state)
    await message.reply(f'Добавил позицию "{name_new_pos}" в базу данных')
    await state.finish()


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def delete_from_db_by_callback(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_position(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)


async def delete_position_menu(message: types.Message):
    all_menu_positions = await sqlite_db.sql_read_only()
    for pos in all_menu_positions:
        await bot.send_photo(message.from_user.id, pos[0], f'{pos[1]}\nОписание: {pos[2]}\nЦена {pos[-1]}')
        await bot.send_message(message.from_user.id, text='<<< >>>', reply_markup=InlineKeyboardMarkup().
                               add(InlineKeyboardButton(f'Удалить {pos[1]}', callback_data=f'del {pos[1]}')))


# @dp.message_handler(state="*", commands='Отмена')
# @dp.message_handler(Text(equals='Отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отменил добавление новой позиции')


async def unknown_handler(message: types.Message):
    await message.answer('Вижу, что ты пишешь что-то интересное :)\nПопробуй написать команду или воспользоваться кнопками')
    await message.delete()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(make_changes_command, commands='admin')
    dp.register_message_handler(start_load_position_menu, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='Отмена')
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_callback_query_handler(delete_from_db_by_callback, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_position_menu, commands=['Удалить'])
    dp.register_message_handler(unknown_handler)
