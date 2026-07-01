import asyncio
import logging
import yookassa
from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery, InputMediaPhoto, FSInputFile, \
    InputMediaDocument

from keyboard import Pay
from lexicon import lexicon


logger = logging.getLogger(__name__)
router = Router()


@router.callback_query(Pay.filter()) #Pay.filter()
async def successful_payment_handler(callback: CallbackQuery, bot: Bot, callback_data: Pay): #, callback_data: Pay
    loop = asyncio.get_event_loop()
    payment = await loop.run_in_executor(None, yookassa.Payment.find_one, callback_data.pay_id)
    if payment.status == 'succeeded':
        if payment.description == 'Покупка игры':
            await callback.message.answer_document(document=FSInputFile('game.pdf', filename='Игра.pdf'),
                                                   caption=lexicon['succeeded'])
        elif payment.description == "Рождество":
            await callback.message.answer_document(document=FSInputFile('christmas.pdf', filename='Рождество.pdf'),
                                                   caption=lexicon['succeeded'])
        elif payment.description == 'Трекер чтения Библии':
            await bot.send_media_group(chat_id=callback.from_user.id, media=[InputMediaDocument(media=FSInputFile('Treker_chtenia_Biblii_-_pechat/Закладки А4 для принтера по порядку.pdf', filename='Закладки А4 Для принтера по порядку')),
                                                              InputMediaDocument(media=FSInputFile('Treker_chtenia_Biblii_-_pechat/Закладки А4 поворот по вертикали.pdf', filename='Закладки А4 Поворот по вертикали')),
                                                              InputMediaDocument(media=FSInputFile('Treker_chtenia_Biblii_-_pechat/Закладки А4 поворот по горизонтали.pdf',filename='Закладки А4 Поворот по горизонтали')),
                                                              InputMediaDocument(media=FSInputFile('Treker_chtenia_Biblii_-_pechat/Как правильно распечатать закладки.docx',filename='Как_правильно_распечатать_закладки'))])
            await callback.message.answer(text=lexicon['succeeded'])
        elif payment.description == "Пасха":
            await callback.message.answer_document(document=FSInputFile('easter.pdf', filename='Пасха.pdf'),
                                                   caption=lexicon['succeeded'])
        elif payment.description == 'Помощь моя от Господа':
            await bot.send_media_group(chat_id=callback.from_user.id, media=[InputMediaDocument(
                media=FSInputFile('Posters/Постеры строгие бот.pdf',
                                  filename='Помощь моя от Господа'))])
        elif payment.description == 'Бог есть любовь':
            await bot.send_media_group(chat_id=callback.from_user.id, media=[InputMediaDocument(
                media=FSInputFile('Posters/Постеры дофамин бот.pdf',
                                  filename='Бог есть любовь'))])
    else:
        await callback.message.answer(text=lexicon['failed'])