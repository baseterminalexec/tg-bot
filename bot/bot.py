import logging
from aiogram import Bot, Dispatcher, executor, types
from bot.handlers import start, subscribe, confirm_payment, check_subscription_status
from bot.payments import approve_subscription
from database.database import init_db
from config.config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

init_db()

dp.register_message_handler(start, commands=['start'])
dp.register_message_handler(subscribe, commands=['subscribe'])
dp.register_message_handler(confirm_payment, commands=['confirm'])
dp.register_message_handler(check_subscription_status, commands=['check'])
dp.register_message_handler(approve_subscription, commands=['approve'])

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
