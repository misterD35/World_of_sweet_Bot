from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в МИР СЛАДОСТЕЙ', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом происходит через личные сообщения. Писать сюда: \nhttps://t.me/World_of_sweets_Bot')


# @dp.message_handler(commands=['Режим_работы'])
async def get_opening_hours(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПН-ПТ с 9:00 до 21:00, СБ-ВС с 10:00 до 22:00')


# @dp.message_handler(commands=['Расположение'])
async def get_cafe_address(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Сладкая, д.1')


async def exit_from_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Всего вам сладкого! :) \n\nЧтобы снова меня запустить, кликни => "/start"', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(lambda message: 'сладкое' in message.text)
async def sweet(message: types.Message):
    await message.answer('Ты всегда можешь заказать что-нибудь сладкое у нас!')


async def promo_code(message: types.Message):
    await message.answer(f'Твой промокод "{message.text[9:]}" принят! Скидка применена')
    ...


async def read_db_menu(message: types.Message):
    await sqlite_db.sql_read_and_send(message)


async def delete_from_db(message: types.Message):
    await sqlite_db.sql_delete_position(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(get_opening_hours, commands=['Режим_работы'])
    dp.register_message_handler(get_cafe_address, commands=['Расположение'])
    dp.register_message_handler(exit_from_menu, commands=['Выход'])
    dp.register_message_handler(sweet, lambda message: 'сладкое' in message.text.lower())
    dp.register_message_handler(promo_code, lambda message: message.text.lower().startswith('промокод'))
    dp.register_message_handler(read_db_menu, commands=['Меню'])
