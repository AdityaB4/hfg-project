from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
import authtoken
import backend


#insert valid token (have not verified with botfather yet)
TOKEN = authtoken.accessToken()
updater = Updater(TOKEN, use_context = True)
dispatcher = updater.dispatcher

def start(update, context):
    #create options
    options = [[InlineKeyboardButton("Volunteer", callback_data='Volunteer'), InlineKeyboardButton("User", callback_data='User')]]
    respond = InlineKeyboardMarkup(options)
    update.message.reply_text("Hi! Welcome to Bridge😊. Are you a volunteer or a specially-abled user?", reply_markup=respond)

    # to be handled at the backend
    typeUser = button_handler(update, context)
    

def userLogic(update, context):
    if update.message:
        update.message.reply_text("What is your name?")
    name = update.message.text
    
    update.message.reply_text("What is your age?")
    age = update.message.text
    
    options = [[InlineKeyboardButton("North", callback_data='North'), InlineKeyboardButton("South", callback_data='South'), InlineKeyboardButton('East', callback_data='East'), InlineKeyboardButton('West', callback_data='West')]]
    responds = InlineKeyboardMarkup(options)
    update.message.reply_text("Which part of Singapore are you from?", reply_markup=responds)
    location = button_handler(update, context)
    
    option = [[InlineKeyboardButton("Vision", callback_data='Vision'), InlineKeyboardButton("Physical Impairment", callback_data='Physical Impairment'), InlineKeyboardButton('Hearing', callback_data='Hearing'), InlineKeyboardButton('Speaking', callback_data='Speaking')]]
    respond = InlineKeyboardMarkup(option)
    update.message.reply_text("What disability do you have?", reply_markup=respond)
    disability = button_handler(update, context)
    endLogic(update, context)
    

def volunteerLogic(update, context):
    if update.message:
        update.message.reply_text("What is your name?")
    name = update.message.text

    update.message.reply_text("What is your age?")
    age = update.message.text
    
    options = [[InlineKeyboardButton("North", callback_data='North'), InlineKeyboardButton("South", callback_data='South'), InlineKeyboardButton('East', callback_data='East'), InlineKeyboardButton('West', callback_data='West')]]
    responds = InlineKeyboardMarkup(options)
    update.message.reply_text("Which part of Singapore are you from?", reply_markup=responds)
    location = button_handler(update, context)

    option = [[InlineKeyboardButton("Vision", callback_data='Vision'), InlineKeyboardButton("Physical Impairment", callback_data='Physical Impairment'), InlineKeyboardButton('Hearing', callback_data='Hearing'), InlineKeyboardButton('Speaking', callback_data='Speaking')]]
    respond = InlineKeyboardMarkup(option)
    update.message.reply_text("What disability would you like to service?", reply_markup=respond)
    disability = button_handler(update, context)
    endLogic(update, context)

def endLogic(update, context):
    update.message.reply_text("Thank you for waiting! Your match is <name> with the telegram id <tele_id>. Please contact them to continue Bridging! Thanks for using Bridge and we hope to see you again👋!")

def button_handler(update, context):
    if update.callback_query:
        query = update.callback_query
        return query.data
    return ""

def query_handler(update, context):
    query = update.callback_query
    if query:
        query.answer("")

def help(update, context):
    update.message.reply_text("""
    The following commands are available:

    /start -> Welcome Message
    /help -> This Message
    /contact -> Information about Contact
    """)


def contact(update, context):
    update.message.reply_text("u can contact me via : 99999999")
    reply = update.message.text

def info(update, context):
    update.message.reply_text("u can look at the devpost page for this project at https://devpost.com/software/bridge-03dxc1")

def main():
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('more_info', info))
    dispatcher.add_handler(CommandHandler('contact', contact))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CallbackQueryHandler(userLogic, pattern="User"))
    dispatcher.add_handler(CallbackQueryHandler(volunteerLogic, pattern="Volunteer"))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
