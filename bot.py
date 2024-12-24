import asyncio
from aiogram import Bot, Dispatcher
from handlers import router

token='7585776111:AAHwz-FOu9kZ96piHD0ZlU8QrUBxqNgS8Bc'
async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    
bot = Bot(token=token)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
