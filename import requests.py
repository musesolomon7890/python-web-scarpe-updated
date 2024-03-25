import requests
from bs4 import BeautifulSoup
import telebot
import telegram
import asyncio

bot_token = ''
bot_chat_id = '@'
bot = telebot.TeleBot(bot_token)
bot2 = telegram.Bot(token=bot_token)

@bot.message_handler(commands=['news'])
def handle_scrape_command(message):
    asyncio.run(send_message_to_telegram_channel())
@bot.message_handler(commands=['tech'])
def handle_scrape_command(message):
    asyncio.run(send_message_to_telegram_channel2())   
@bot.message_handler(commands=['sports'])
def handle_scrape_command(message):
    asyncio.run(send_message_to_telegram_channel3())
@bot.message_handler(commands=['business'])
def handle_scrape_command(message):
    asyncio.run(send_message_to_telegram_channel3())
             
async def send_message_to_telegram_channel():
    url = 'https://www.fanabc.com/%e1%8b%9c%e1%8a%93'
    response = requests.get(url)
    s = BeautifulSoup(response.text, 'html.parser')
    post_url = s.find_all(class_='post-url')

    for i, post_link in enumerate(post_url):
        message = post_link['href']

        try:
            await bot2.send_message(chat_id=bot_chat_id, text=message)
        except telegram.error.TelegramError as e:
            print(f"Failed to send message: {e}")
            
async def send_message_to_telegram_channel2():
    url = 'https://www.fanabc.com/archives/category/tech'
    response = requests.get(url)
    s = BeautifulSoup(response.text, 'html.parser')
    post_url = s.find_all(class_='post-url')

    for i, post_link in enumerate(post_url):
        message = post_link['href']

        try:
            await bot2.send_message(chat_id=bot_chat_id, text=message)
        except telegram.error.TelegramError as e:
            print(f"Failed to send message: {e}")

async def send_message_to_telegram_channel3():
    url = 'https://www.fanabc.com/%e1%88%b5%e1%8d%93%e1%88%ad%e1%89%b5'
    response = requests.get(url)
    s = BeautifulSoup(response.text, 'html.parser')
    post_url = s.find_all(class_='post-url')

    for i, post_link in enumerate(post_url):
        message = post_link['href']

        try:
            await bot2.send_message(chat_id=bot_chat_id, text=message)
        except telegram.error.TelegramError as e:
            print(f"Failed to send message: {e}")
            
async def send_message_to_telegram_channel3():
    url = 'https://www.fanabc.com/archives/category/business'
    response = requests.get(url)
    s = BeautifulSoup(response.text, 'html.parser')
    post_url = s.find_all(class_='post-url')

    for i, post_link in enumerate(post_url):
        message = post_link['href']

        try:
            await bot2.send_message(chat_id=bot_chat_id, text=message)
        except telegram.error.TelegramError as e:
            print(f"Failed to send message: {e}")
bot.polling()
