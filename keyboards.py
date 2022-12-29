from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Inline кнопки
inline_btn1 = InlineKeyboardButton('Добавить', callback_data='button_add')
inline_btn2 = InlineKeyboardButton('Нет', callback_data='button_cancel')
in_btn_confirm = InlineKeyboardButton('Да', callback_data='button_delete')
in_btn_del = InlineKeyboardButton('Удалить', callback_data='button_del')
# Inline клавиатуры
in_kb1 = InlineKeyboardMarkup().add(inline_btn1, inline_btn2)
in_kb_del = InlineKeyboardMarkup().add(in_btn_del)
in_kb_all_del = InlineKeyboardMarkup().add(in_btn_confirm, inline_btn2)

# Кнопки
btn1 = KeyboardButton('Показать заметки')
btn2 = KeyboardButton('Удалить заметки')
# Клавиатуры
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1).add(btn2)
