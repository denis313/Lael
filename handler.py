from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from bot import bot
from keyboard import Pay
from pages import show_about, edit_cards, show_christmas, show_start, show_bookmarks, show_easter, show_posters, \
    show_poster, show_purchase

router = Router()
router.message.filter(F.chat.type == 'private')


@router.message(CommandStart())
async def start(message: Message):
    await show_start(message.chat.id)


@router.callback_query(F.data == "about")
async def start(call: CallbackQuery):
    await show_about(call)


@router.callback_query(F.data == "cards")
async def cards(callback: CallbackQuery):
    await edit_cards(callback)


@router.callback_query(F.data == 'christmas')
async def christmas(callback: CallbackQuery):
    await show_christmas(callback)


@router.callback_query(F.data == 'bookmarks')
async def bookmarks(callback: CallbackQuery):
    await show_bookmarks(callback)


@router.callback_query(F.data == 'easter')
async def easter(callback: CallbackQuery):
    await show_easter(callback)


@router.callback_query(F.data == 'posters')
async def posters(callback: CallbackQuery):
    await show_posters(callback)


@router.callback_query(F.data.in_({"white", "yellow"}))
async def poster(callback: CallbackQuery):
    await show_poster(callback)


@router.callback_query(Pay.filter())
async def purchase(callback: CallbackQuery, callback_data: Pay):
    await show_purchase(callback, bot, callback_data)

