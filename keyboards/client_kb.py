from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('/Выход')
b5 = KeyboardButton('Свяжитесь со мной', request_contact=True)
b6 = KeyboardButton('Мой город', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

# kb_client.add(b1).add(b2).insert(b3)
kb_client.row(b1, b2, b3).row(b5, b6).add(b4)
