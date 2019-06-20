import telebot
from flask import Flask, request
import os

from config_bot import *
from markups import *
from db_st import *
from inlines import *

bot = telebot.TeleBot(TOKEN)

def save_new_message(messages):
	for m in messages:
		if m.content_type == 'text':
			pass
			# TODO save to DB

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    if is_usr_present(uid) and get_psw_mode(uid):
        psw_input_error(message)
    else:
        bot.send_message(uid, 'Hello, fellow human being', reply_markup=start_markup())

# === Authorization ===
@bot.message_handler(func=lambda mess: "Authorize" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Authorize" == mess.text, content_types=['text'])
def auth(message):
    uid = message.from_user.id
    if is_usr_present(uid) and get_usr_state(uid):
        if get_psw_mode(uid):
            psw_input_error(message)
        else:
            authorized_handler(message)
    else:
        bot.send_message(message.chat.id, "Choose the way to authorize:", reply_markup=auth_markup())
    
# === Info ===
@bot.message_handler(func=lambda mess: "Info" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Info" == mess.text, content_types=['text'])
def info(message):
    uid = message.from_user.id
    if is_usr_present(uid) and get_psw_mode(uid):
        psw_input_error(message)
    else:
        bot.send_message(message.chat.id, "In time there would be a proper information about this bot, but now we  apologize for the inconveniences caused to you.\nHave a good day.")

# === Logouts ===
@bot.message_handler(func=lambda mess: "Logout" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Logout" == mess.text, content_types=['text'])
def logout(message):
    uid = message.from_user.id
    set_usr_state(uid, False)
    bot.send_message(message.chat.id, "Done")
    bot.send_message(message.chat.id, "Authorize, please:", reply_markup=start_markup())

@bot.message_handler(func=lambda mess: "Forget me" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Forget me" == mess.text, content_types=['text'])
def forget(message):
    uid = message.from_user.id
    delete_trader(uid)
    bot.send_message(message.chat.id, "Done")
    bot.send_message(message.chat.id, "Authorize, please:", reply_markup=start_markup())

# ===== TRADING =====
# === Reboot ===
@bot.message_handler(func=lambda mess: "Reboot" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Reboot" == mess.text, content_types=['text'])
def reboot(message):
	pass
	#get_last_updates(4)

# === Trading ===
@bot.message_handler(func=lambda mess: "Trading" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Trading" == mess.text, content_types=['text'])
def trading(message):
    bot.send_message(message.chat.id, 'Trading:', reply_markup=trade_markup())
    set_step(message.chat.id, 'trade')

# === Profit/Loss ===
@bot.message_handler(func=lambda mess: "Profit/Loss" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Profit/Loss" == mess.text, content_types=['text'])
def pl(message):
    bot.send_message(message.chat.id, 'Choose a period:', reply_markup=period_markup())
    set_step(message.chat.id, 'period')

# === P/L period ===
@bot.message_handler(func=lambda mess: "Year" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Year" == mess.text, content_types=['text'])
def pl_period(message):
    period_handler(message, 'year')

@bot.message_handler(func=lambda mess: "Month" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Month" == mess.text, content_types=['text'])
def pl_period(message):
    period_handler(message, 'month')

@bot.message_handler(func=lambda mess: "Week" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Week" == mess.text, content_types=['text'])
def pl_period(message):
    period_handler(message, 'week')

@bot.message_handler(func=lambda mess: "Day" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Day" == mess.text, content_types=['text'])
def pl_period(message):
    period_handler(message, 'day')

@bot.message_handler(func=lambda mess: "All" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "All" == mess.text, content_types=['text'])
def pl_period(message):
    period_handler(message, 'all')

@bot.message_handler(func=lambda mess: "Hour" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Hour" == mess.text, content_types=['text'])
def pl_period(message):
    period_handler(message, 'hour')

# === Get course ===
@bot.message_handler(func=lambda mess: "Get course" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Get course" == mess.text, content_types=['text'])
def course(message):
    bot.send_message(message.chat.id, 'Choose an instrument:', reply_markup=instrument_markup())
    set_step(message.chat.id, 'instr_get')

# === Check balance ===
@bot.message_handler(func=lambda mess: "Check balance" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Check balance" == mess.text, content_types=['text'])
def balance(message):
    bot.send_message(message.chat.id, 'Choose market:', reply_markup=market_markup())

# === Open orders ===
@bot.message_handler(func=lambda mess: "Open orders" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Open orders" == mess.text, content_types=['text'])
def open_order(message):
    bot.send_message(message.chat.id, 'Choose an instrument:', reply_markup=instrument_markup())
    set_step(message.chat.id, 'instr_open')

# === Make order ===
@bot.message_handler(func=lambda mess: "Make order" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Make order" == mess.text, content_types=['text'])
def make_order(message):
    bot.send_message(message.chat.id, 'Choose an instrument:', reply_markup=instrument_markup())
    set_step(message.chat.id, 'instr_make')

# === Instruments ===
@bot.message_handler(func=lambda mess: "Futures" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Futures" == mess.text, content_types=['text'])
def instr(message):
    instr_handler(message, 'futures')

@bot.message_handler(func=lambda mess: "Options" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Options" == mess.text, content_types=['text'])
def instr(message):
    instr_handler(message, 'options')

@bot.message_handler(func=lambda mess: "Shares" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Shares" == mess.text, content_types=['text'])
def instr(message):
    instr_handler(message, 'shares')

@bot.message_handler(func=lambda mess: "Currency" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Currency" == mess.text, content_types=['text'])
def instr(message):
    instr_handler(message, 'currency')

# === Markets ===
@bot.message_handler(func=lambda mess: "Currency market" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Currency market" == mess.text, content_types=['text'])
def instr(message):
    market_handler(message, 'currency market')

@bot.message_handler(func=lambda mess: "Financial market" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Financial market" == mess.text, content_types=['text'])
def instr(message):
    market_handler(message, 'financial market')

@bot.message_handler(func=lambda mess: "Cryptocurrency market" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Cryptocurrency market" == mess.text, content_types=['text'])
def instr(message):
    market_handler(message, 'cryptocurrency market')

@bot.message_handler(func=lambda mess: "FORTS" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "FORTS" == mess.text, content_types=['text'])
def instr(message):
    market_handler(message, 'FORTS')
    
# === Orders ===
@bot.message_handler(func=lambda mess: "Sell" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Sell" == mess.text, content_types=['text'])
def order(message):
    order_handler(message, 'sell')

@bot.message_handler(func=lambda mess: "Buy" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Buy" == mess.text, content_types=['text'])
def order(message):
    order_handler(message, 'buy')

# === Download ===
@bot.message_handler(func=lambda mess: "Download asset history" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Download asset history" == mess.text, content_types=['text'])
def dwn(message):
    print("dwn")

# === BACK ===
@bot.message_handler(func=lambda mess: "Back" == mess.text, content_types=['text'])
@bot.edited_message_handler(func=lambda mess: "Back" == mess.text, content_types=['text'])
def back(message):
    curr_position = get_step(message.from_user.id)
    if curr_position == 'trade':
        set_step(message.from_user.id, 'main')
        bot.send_message(message.chat.id, 'Back', reply_markup=main_markup())
    elif curr_position == 'period':
        set_step(message.from_user.id, 'trade')
        bot.send_message(message.chat.id, 'Back', reply_markup=trade_markup())
    elif curr_position == 'market':
        set_step(message.from_user.id, 'trade')
        bot.send_message(message.chat.id, 'Back', reply_markup=trade_markup())
    elif curr_position.startswith('instr_'):
        set_step(message.from_user.id, 'trade')
        bot.send_message(message.chat.id, 'Back', reply_markup=trade_markup())
    elif curr_position == 'order_type':
        set_step(message.from_user.id, 'instr_make')
        bot.send_message(message.chat.id, 'Back', reply_markup=order_markup())

# === Inline calls ===
@bot.callback_query_handler(func=lambda call: True)
def callback_inline_all(call):
    if call.message:
        uid = call.message.chat.id
        data = call.data
        if get_psw_mode(uid) == False and (data == "password" or data == "keys"):
            inline_auth(call, bot)
        elif data == "btn_psw_cancel":
            inline_psw_cancel(bot, call.message)
        elif data == "btn_psw_str":
            inline_psw_start(uid)
        elif data == "btn_psw_done":
            inline_psw_done(uid, bot)
        elif data.startswith("btn_d"):
            inline_digits(bot, call)
        elif data == "btn_val":
            bot.send_message(call.message.chat.id, 'Good, your order has been sent')
        elif data.startswith("t_"):
            inline_ticket(bot, call)

# === Handlers ===
def authorized_handler(message):
    bot.send_message(message.chat.id, "You are already authorized. If you wish to change account you have to use \'Logout\' or \'Forget me\'", reply_markup=main_markup())
    set_step(message.chat.id, 'main')
    old = get_old_psw(message.chat.id)
    set_psw(message.chat.id, old)

def psw_input_error(message):
    bot.send_message(message.chat.id, "Sorry, unacceptable input.\nOperation canceled, try again please.")
    set_psw_mode(message.from_user.id, False)

def period_handler(message, period):
    bot.send_message(message.chat.id, 'Be patient: getting data from server ...')

def instr_handler(message, instr):
    position = get_step(message.from_user.id)
    if position.endswith("open"):
        bot.send_message(message.chat.id, 'Getting opened positions on ' + instr + ' from server ...')
    elif position.endswith("make"):
        bot.send_message(message.chat.id, "Now choose order type:", reply_markup=order_markup())
    elif position.endswith("get"):
        bot.send_message(message.chat.id, "Now choose ticker:", reply_markup=ticker_markup())

def market_handler(message, market):
    bot.send_message(message.chat.id, 'Waiting for server to reply ...')
    bot.send_message(message.chat.id, '1598,4')

def order_handler(message, order_type):
    bot.send_message(message.chat.id, "Confirm your order please:", reply_markup=conf_markup())

# ===============================================================================================
# If you want to use webhooks uncommit next lines

server = Flask(__name__)

@server.route('/' + TOKEN, methods=['POST'])
def get_message():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
 	return "POST", 200

@server.route('/')
def index():
 	bot.remove_webhook()
 	bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN))
 	return "* Successfully connected *\n* Cowabunga *", 200
        
# ===============================================================================================
# If you want to use polling uncommit next two lines
bot.set_update_listener(save_new_message)
bot.polling(none_stop=True)
