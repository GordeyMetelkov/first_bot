import telebot




TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['go', 'start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


bot.polling(none_stop=True)