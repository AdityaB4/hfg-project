import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./hfg-project-fe558-firebase-adminsdk-6m0wo-b22b5aa40a.json")
firebase_admin.initialize_app(cred)


#insert valid token
Token = ""
updater = Updater(Token, use_context = True)
dispatcher = updater.dispatcher
def start(update, context):
    update.message.reply_text("Hello, this is InsertName bot, here to connect
    u with helpful volunteers.")



