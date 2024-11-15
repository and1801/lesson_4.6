import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '7560819978:AAHbEZGYrW1BckKVoVWTMxDRGQJpeD7khLg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Этот бот лежит на локальном сервере")

if __name__ == "__main__":
    bot.polling(none_stop=True)