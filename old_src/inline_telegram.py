import os
from telepot import Bot, glance, flavor
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from musher import mush

token = os.environ.get('SECRET')

bot = Bot(token)

users = []

def handle(msg):
    # {'message_id': 19, 'from': {'id': 391834810, 'is_bot': False, 'first_name': 'Sergey', 'last_name': 'Bobkov', 'username': 'WillDrug', 'language_code': 'en'}, 'chat': {'id': 391834810, 'first_name': 'Sergey', 'last_name': 'Bobkov', 'username': 'WillDrug', 'type': 'private'}, 'date': 1543236398, 'text': 'f'}
    flavour = flavor(msg)
    if flavour == 'inline_query':

        return do_business(msg)
    content_type, chat_type, chat_id = glance(msg)
    if content_type == 'text' and chat_type == 'private':
        if chat_id not in users:
            bot.sendMessage(chat_id, "I don't answer to commoners!", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Go somewhere else", switch_inline_query="")]]))
            users.append(chat_id)

def do_business(msg):
    # {'id': '1682917695207139721', 'from': {'id': 391834810, 'is_bot': False, 'first_name': 'Sergey', 'last_name': 'Bobkov', 'username': 'WillDrug', 'language_code': 'en'}, 'query': '', 'offset': ''}"
    sid = msg['id']
    to_mush = msg['query'] if msg['query'] != '' else '_'
    articles = [InlineQueryResultArticle(
        id='30',
        title='30% mush',
        input_message_content=InputTextMessageContent(
            message_text=mush(to_mush, threshold=0.7)
        )),
        InlineQueryResultArticle(
            id='50',
            title='50% mush',
            input_message_content=InputTextMessageContent(
                message_text=mush(to_mush, threshold=0.5)
            )),
        InlineQueryResultArticle(
            id='100',
            title='100% mush',
            input_message_content=InputTextMessageContent(
                message_text=mush(to_mush, threshold=-1)
            ))
        ]
    bot.answerInlineQuery(sid, articles, cache_time=0)


if __name__ == '__main__':
    MessageLoop(bot, handle).run_as_thread()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            break