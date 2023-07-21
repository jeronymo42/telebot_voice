import telebot, settings

token = settings.token

# В этой строчке мы заводим бота и даем ему запомнить токен
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name)


bot.polling()