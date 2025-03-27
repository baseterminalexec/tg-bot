from aiogram import types
from bot.payments import process_payment
from database.database import check_subscription

async def start(message: types.Message):
    await message.answer(f"👋 Welcome, {message.from_user.first_name}!\n\n"
                         "This bot allows you to subscribe for premium access.\n"
                         "💰 Subscription Fee: 10 USDT (TRC20)\n"
                         "To subscribe, use /subscribe.")

async def subscribe(message: types.Message):
    await message.answer(f"📌 Send 10 USDT to the following wallet:\n\n"
                         "💳 Wallet: `your_usdt_trc20_wallet_address`\n\n"
                         "After payment, send your transaction ID using:\n"
                         "`/confirm <TXID>`")

async def confirm_payment(message: types.Message):
    await process_payment(message)

async def check_subscription_status(message: types.Message):
    if check_subscription(message.from_user.id):
        await message.reply("✅ You have an active subscription! 🎉")
    else:
        await message.reply("❌ You don't have an active subscription. Use /subscribe to get started.")
