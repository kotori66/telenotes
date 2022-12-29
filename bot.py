from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import BOT_TOKEN, DATABASE
from keyboards import in_kb1, in_kb_del, kb_menu, in_kb_all_del

from db_connect import SqlCrud

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

sql = SqlCrud(DATABASE)

text_note = ''


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    if not sql.user_exists(message.from_user.id):
        sql.add_user(message.from_user.id)
    await message.answer("Напишите мне что-нибудь\nили выберите действие",
                         reply_markup=kb_menu)


@dp.message_handler(Text('Показать заметки'))
async def show_notes(message: types.Message):
    notes = sql.get_all_notes(message.from_user.id)
    if bool(len(notes)):
        for i in notes:
            await message.answer(f'{i[0]}\n{i[1]}\n{i[2][:-3]}',
                                 reply_markup=in_kb_del)
    else:
        await message.answer('Заметки отсутствуют')


@dp.message_handler(Text('Удалить заметки'))
async def delete_notes(message: types.Message):
    await message.answer('Вы действительно хотите удалить все заметки?',
                         reply_markup=in_kb_all_del)


@dp.message_handler()
async def add_notes(message: types.Message):
    global text_note
    await message.reply('Добавить в заметки?', reply_markup=in_kb1)
    text_note = message.text


@dp.callback_query_handler(lambda c: c.data == 'button_del')
async def del_note(call: types.CallbackQuery):
    sql.delete_note(call.from_user.id, call.message.text.split()[0])
    await call.answer(f'Заметка удалена')
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'button_add')
async def add_message(call: types.CallbackQuery):
    sql.set_note(text_note, call.from_user.id)
    await call.answer('Заметка добавлена')
    await call.message.delete()


@dp.callback_query_handler(lambda c: c.data == 'button_cancel')
async def return_message(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id,
                           text='Выберите действие',
                           reply_markup=kb_menu)


@dp.callback_query_handler(lambda c: c.data == 'button_delete')
async def delete_all_message(call: types.CallbackQuery):
    sql.delete_all_notes(call.from_user.id)
    await call.answer('Все заметки удалены')
    await call.message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
