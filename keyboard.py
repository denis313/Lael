from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pay(CallbackData, prefix='pay', sep=':'):
    pay_id: str


def about():
    kb = InlineKeyboardBuilder()
    kb.row(*[InlineKeyboardButton(text='Дальше ➡️', callback_data='cards')], width=1)
    return kb.as_markup()


def main_menu(buy: str, next_page: str, previous_page: str):
    kb = InlineKeyboardBuilder()
    kb.row(*[InlineKeyboardButton(text='Купить 🛒', callback_data=buy),
             InlineKeyboardButton(text='Дальше ➡️', callback_data=next_page),
             InlineKeyboardButton(text='Назад ⬅️', callback_data=previous_page)],
           width=1)
    return kb.as_markup()


def kb_buy(url:str, id_payment):
    kb = InlineKeyboardBuilder()
    kb.row(*[InlineKeyboardButton(text='Оплата 💳', url=url),
             InlineKeyboardButton(text='Проверка оплаты ✅',
                                  callback_data=Pay(pay_id=id_payment).pack()),
             InlineKeyboardButton(text='Меню ⬅️', callback_data='about')],
           width=1)
    return kb.as_markup()


def kb_posters():
    kb = InlineKeyboardBuilder()
    kb.row(*[InlineKeyboardButton(text='Помощь моя от Господа', callback_data='white'),
             InlineKeyboardButton(text='Бог есть любовь', callback_data='yellow'),
             InlineKeyboardButton(text='Меню ⬅️', callback_data='about')
             ], width=1)
    return kb.as_markup()


def kb_all():
    kb = InlineKeyboardBuilder()
    kb.row(*[InlineKeyboardButton(text='Закладки 📖', callback_data='bookmarks'),
             InlineKeyboardButton(text='Игра 🧩', callback_data='cards'),
             InlineKeyboardButton(text='Рождество ✨️', callback_data='christmas'),
             InlineKeyboardButton(text='Пасха ✝️', callback_data='easter'),
             InlineKeyboardButton(text='Постеры 🖼️ ', callback_data='posters')],
           width=1)
    return kb.as_markup()
