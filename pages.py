import yookassa
from aiogram import Bot
from aiogram.types import InputMediaPhoto, CallbackQuery, FSInputFile, InputMediaDocument
import asyncio
from bot import bot
from keyboard import kb_buy
from lexicon import lexicon
import keyboard as kb
import service as s


async def show_start(chat_id: int):
    await bot.send_photo(
        chat_id=chat_id,
        photo=s.get_photo3(),
        caption=lexicon["about"],
        reply_markup=kb.kb_all()
    )

async def show_about(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=s.get_photo3(),
            caption=lexicon["about"]
        ),
        reply_markup=kb.kb_all()
    )


async def edit_cards(callback: CallbackQuery):
    loop = asyncio.get_event_loop()
    url, id_prepayment = await loop.run_in_executor(None,
                                                    s.create_payment,
                                                    s.PRODUCTS['cards']['price'],
                                                    s.PRODUCTS['cards']['description'],
                                                    callback.message.from_user.id,
                                                    callback.message.from_user.username or None)
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=s.get_photo(),
            caption=lexicon["cards"]
        ),
        reply_markup=kb.kb_buy(url=url, id_payment=id_prepayment)
    )


async def show_christmas(callback: CallbackQuery):
    loop = asyncio.get_event_loop()
    url, id_prepayment = await loop.run_in_executor(None,
                                                    s.create_payment,
                                                    s.PRODUCTS['christmas']['price'],
                                                    s.PRODUCTS['christmas']['description'],
                                                    callback.message.from_user.id,
                                                    callback.message.from_user.username or None)
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=s.get_photo2(),
            caption=lexicon['christmas']
        ),
        reply_markup=kb.kb_buy(url=url, id_payment=id_prepayment)
    )


async def show_bookmarks(callback: CallbackQuery):
    loop = asyncio.get_event_loop()
    url, id_prepayment = await loop.run_in_executor(None,
                                                    s.create_payment,
                                                    s.PRODUCTS['bookmarks']['price'],
                                                    s.PRODUCTS['bookmarks']['description'],
                                                    callback.message.from_user.id,
                                                    callback.message.from_user.username or None)
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=s.get_photo4(),
            caption=lexicon['bookmarks']
        ),
        reply_markup=kb.kb_buy(url=url, id_payment=id_prepayment)
    )


async def show_easter(callback: CallbackQuery):
    loop = asyncio.get_event_loop()
    url, id_prepayment = await loop.run_in_executor(None,
                                                    s.create_payment,
                                                    s.PRODUCTS['easter']['price'],
                                                    s.PRODUCTS['easter']['description'],
                                                    callback.message.from_user.id,
                                                    callback.message.from_user.username or None)

    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=s.get_photo5(),
            caption=lexicon['easter']
        ),
        reply_markup=kb.kb_buy(url=url, id_payment=id_prepayment)
    )


async def show_posters(callback: CallbackQuery):
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=s.get_photo8(),
            caption=lexicon['posters']
        ),
        reply_markup=kb.kb_posters()
    )


async def show_poster(callback: CallbackQuery):
    loop = asyncio.get_event_loop()
    description = 'Бог есть любовь'
    photo = s.get_photo7()
    if callback.data == 'white':
        description = 'Помощь моя от Господа'
        photo = s.get_photo6()
    url, id_prepayment = await loop.run_in_executor(None,
                                                    s.create_payment,
                                                    s.PRODUCTS['posters']['price'],
                                                    description,
                                                    callback.message.from_user.id,
                                                    callback.message.from_user.username or None)
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=photo,
            caption=description
        ),
        reply_markup=kb_buy(id_payment=id_prepayment, url=url)
    )


async def show_purchase(callback: CallbackQuery, bot: Bot, callback_data: kb.Pay):
    loop = asyncio.get_event_loop()
    payment = await loop.run_in_executor(None, yookassa.Payment.find_one, callback_data.pay_id)
    if payment.status == 'succeeded':
        if payment.description == 'Покупка игры':
            await callback.message.answer_document(document=FSInputFile('game.pdf', filename='game.pdf'),
                                                   caption=lexicon['succeeded'])
        elif payment.description == "Рождество":
            await callback.message.answer_document(document=FSInputFile('christmas.pdf', filename='christmas.pdf'),
                                                   caption=lexicon['succeeded'])
        elif payment.description == 'Трекер чтения Библии':
            await bot.send_media_group(chat_id=callback.from_user.id, media=[InputMediaDocument(media=FSInputFile('Treker/Закладки А4 для принтера по порядку.pdf', filename='Закладки А4 Для принтера по порядку')),
                                                              InputMediaDocument(media=FSInputFile('Treker/Закладки А4 поворот по вертикали.pdf', filename='Закладки А4 Поворот по вертикали')),
                                                              InputMediaDocument(media=FSInputFile('Treker/Закладки А4 поворот по горизонтали.pdf',filename='Закладки А4 Поворот по горизонтали')),
                                                              InputMediaDocument(media=FSInputFile('Treker/Как правильно распечатать закладки.docx',filename='Как_правильно_распечатать_закладки'))])
            await callback.message.answer(text=lexicon['succeeded'])
        elif payment.description == "Пасха":
            await callback.message.answer_document(document=FSInputFile('easter.pdf', filename='easter.pdf'),
                                                   caption=lexicon['succeeded'])
        elif payment.description == 'Помощь моя от Господа':
            await callback.message.answer_document(document=FSInputFile('Posters/Постеры строгие.pdf',
                                  filename='Помощь моя от Господа.pdf'))
        elif payment.description == 'Бог есть любовь':
            await callback.message.answer_document(document=FSInputFile('Posters/Постеры дофамин.pdf',
                                  filename='Бог есть любовь.pdf'))
    else:
        await callback.message.answer(text=lexicon['failed'])