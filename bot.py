import config
import telebot
from random import randint

bot = telebot.TeleBot(config.TOKEN)
secretnum=0
attemps=0
inGame=False

@bot.message_handler(commands=["start"])
def start(message):
	text='Привет,'+str(message.from_user.first_name)+"!\n Чтобы начать игру, нажми /game \n Чтобы увидеть количество неудачных попыток нажми /Try "
	bot.send_message(message.chat.id,text)

@bot.message_handler(commands=["game"])
def game (message):
	global secretnum,inGame
	secretnum=randint(1,100)
	inGame=True
	bot.send_message(message.chat.id,'Я загадал число от 1 до 100')

@bot.message_handler(func = lambda message: message.text.isdigit()==True and inGame==True)
def game (message):
	global secretnum
	usernum = int(message.text)
	if usernum < secretnum:
		bot.send_message(message.chat.id,'Мое число больше.')
		attemps=attemps+1
	elif usernum > secretnum:
		bot.send_message(message.chat.id,'Мое число меньше.')
		attemps=attemps+1
	elif usernum == secretnum:
		bot.send_message(message.chat.id,'Ты угадал')
		attemps=0
		inGame=False
@bot.message_handler(commands=["Try"])
def Try(message):
	ot.send_message(message.chat.id,'Количество попыток '+str(attemps))

if __name__ == '__main__':
	bot.infinity_polling()