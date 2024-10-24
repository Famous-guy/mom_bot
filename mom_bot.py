
import nest_asyncio
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Now you can access the environment variable
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Send the cover image
    cover_image_url = "https://moneymingle.app/icons/mom.png"  # Replace with your image URL
    

    # Create buttons
    keyboard = [
        [InlineKeyboardButton("Join mingle now", url='https://t.me/money_mingle_bot/mom')],
        [InlineKeyboardButton("Join now", url='https://moneymingle.app')],
        [InlineKeyboardButton("Get Login ID", callback_data='login_id')],
        [InlineKeyboardButton("Subscribe to the channel", url="https://t.me/joinmoneymingle")],
        [InlineKeyboardButton("Join our community", url="https://t.me/money_mingle_community")],
        [InlineKeyboardButton("How to earn from the game", callback_data='earn')]
    ]

    # Create an InlineKeyboardMarkup with the buttons
    reply_markup = InlineKeyboardMarkup(keyboard)


    await update.message.reply_photo(
        photo=cover_image_url,
        caption=(
            "<b>Money Mingle helps businesses grow by posting tasks, while freelancers earn money completing them—featuring instant payouts and a vibrant social community.</b>\n\n"
            "Businesses benefit symbiotically. Whether you’re looking to earn extra cash or seeking strategic business insights, this app bridges the gap by creating a win-win scenario for all.\n\n"
            "For hustlers, it's a seamless way to earn real cash on the go, completing fun and engaging tasks that fit into your lifestyle. For businesses, it's a growth engine that provides valuable feedback, deeper user engagement, and marketing insights—all while building your brand presence across digital platforms."
        ),
        parse_mode='HTML',
        reply_markup=reply_markup
    )

# Function to handle button clicks
# Function to handle button clicks
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the callback query

    # Handle button clicks based on callback_data
    if query.data == 'login_id':
        # Send a new message with the login ID
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text=f"Here is your login ID: {update.effective_user.id}"
        )
    elif query.data == 'earn':
        # Send a new message with the earning information
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text="You can earn by playing contests and referring others."
        )


# Main function to set up the bot
async def main() -> None:
    app = ApplicationBuilder().token(bot_token).build()  # Replace with your bot token

    # Register the /start command
    app.add_handler(CommandHandler("start", start))

    # Register button handler
    app.add_handler(CallbackQueryHandler(button))

    # Start the bot
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())