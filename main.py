import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#insert valid token (have not verified with botfather yet)
Token = ""
updater = Updater(Token, use_context = True)
dispatcher = updater.dispatcher
def start(update, context):
    update.message.reply_text("Hello, this is InsertName bot, here to connect
    u with helpful volunteers.")
    update.message.reply_text("Please state ur disabilities:")
    disability = update.message.text
    update.message.reply_text("Please wait while we get in contact with one of
    our volunteers")

def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome Message
    /help -> This Message
    /content -> Information About Volunteer Content
    /contact -> Information about Contact
    """)

def content(update, context):
    pass

def contact(update, context):
    update.message.reply_text("u can contact me via : 99999999")

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('content', content))
dispatcher.add_handler(CommandHandler('contact', contact))
dispatcher.add_handler(CommandHandler('help', help))
updater.start_polling()
updater.idle()


=======
// firebase 
>>>>>>> befe15dfe622f5d4b299b2be701b1158fd232d68
