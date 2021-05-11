import asyncio

from aiogram import Bot, Dispather, executor 

from config import Bot_TOKEN

loop = asyncio.get_event_loop
bot  = Bot(BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher(bot, loop=loop)

if __name__== "__main__":
  from handlers import dp, send_to_admin
  executor.start_polling(dp, on_startup=sent_to_admin)