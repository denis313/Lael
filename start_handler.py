from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message, InputMediaPhoto, CallbackQuery
import asyncio
from bot import bot
from keyboard import kb_buy, kb_posters
from lexicon import lexicon
from service import get_photo, create_payment, get_photo2, get_photo3, get_photo4, get_photo5, get_photo6, get_photo7, get_photo8

router = Router()
router.message.filter(F.chat.type == 'private')


@router.message(CommandStart(), StateFilter(default_state))
async def start_command(message: Message):
    await bot.send_photo(chat_id=message.from_user.id, photo=get_photo3(), caption=lexicon["about"])
    loop = asyncio.get_running_loop()
    products = [
        (300, "Покупка игры", get_photo(), lexicon["start"]),
        (100, "Рождество", get_photo2(), lexicon["christmas"]),
        (200, "Трекер чтения Библии", get_photo4(), lexicon["bookmarks"]),
        (100, "Пасха", get_photo5(), lexicon["easter"]),
    ]



    for price, description, photo, caption in products:
        url, payment_id = await loop.run_in_executor(
            None,
            create_payment,
            price,
            description,
            message.from_user.id,
            message.from_user.username or None,
        )

        await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=caption,reply_markup=kb_buy(id_payment=payment_id, url=url),)
    await bot.send_photo(chat_id=message.from_user.id, photo=get_photo8(), caption=lexicon["posters"], reply_markup=kb_posters())


@router.callback_query(F.data.in_({"white", "yellow"}))
async def check_posters(callback: CallbackQuery):
    loop = asyncio.get_event_loop()
    description = 'Бог есть любовь'
    photo = get_photo7()
    if callback.data == 'white':
        description = 'Помощь моя от Господа'
        photo = get_photo6()
    url, id_prepayment = await loop.run_in_executor(None,
                                                    create_payment,
                                                    300,
                                                    description,
                                                    callback.message.from_user.id,
                                                    callback.message.from_user.username or None)
    kb = kb_buy(id_payment=id_prepayment, url=url)
    await bot.send_photo(chat_id=callback.from_user.id, photo=photo, reply_markup=kb)