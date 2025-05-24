from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog'), KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Отправить локацию', request_location=True),
     KeyboardButton(text='Отправить контакт', request_contact=True)]
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт ниже')

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Catalog', url='https://youtube.com'), 
    InlineKeyboardButton(text='Checkout', url='https://youtube.com')],
    [InlineKeyboardButton(text='Contacts', url='https://youtube.com')]
])