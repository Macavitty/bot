from db_st import *
from markups import *

def inline_auth(call, bot):
    if call.message:
        uid = call.from_user.id
        if is_usr_present(uid) and get_usr_state(uid):
            bot.send_message(call.message.chat.id, "You are already authorized. If you wish to change account use \'Logout\' or \'Forget me\'", reply_markup=main_markup())
            set_step(uid, 'main')
        else:
            if call.data == "password":
                bot.send_message(call.message.chat.id, 'Some black magic with you entering data and ...')
                # here goes password taking operation
            elif call.data == "keys":
                bot.send_message(call.message.chat.id, 'Some black magic with you entering keys and ...')
                # here goes keys taking operation
            if is_usr_present(uid) == False:
                save_new_trader(uid)
                bot.send_message(call.message.chat.id, 'You`re successfully authorized', reply_markup=main_markup())
                bot.send_message(call.message.chat.id, "Now pick up the password for authentication (or you can do it later)\nPress \"start\", enter your password (4-6 digits) press \"done\" once you`re finished.\nCaution! If you forget it or just want to reset use \'Forget me\'", reply_markup=password_markup())
                bot.send_message(call.message.chat.id, "Password:")
                set_step(uid, 'main')
            else:
                set_usr_state(uid, True)
                bot.send_message(call.message.chat.id, 'You`re successfully authorized', reply_markup=main_markup())
                set_step(uid, 'main')


def inline_psw_cancel(bot, message):
    bot.delete_message(message.chat.id, message.message_id)
    set_psw_mode(message.chat.id, False)
    old = get_old_psw(message.chat.id)
    set_psw(message.chat.id, old)


def inline_psw_start(uid):
    if get_psw_mode(uid) == False:
        set_psw_mode(uid, True)

def inline_digits(bot, call):
    uid = call.message.chat.id
    if get_psw_mode(uid):
        psw = get_psw(uid)
        if len(psw) <= 6:
            digit = call.data[-1]
            if psw == 'no':
                psw = ''
            if digit == 'l':
                if len(psw) > 0:
                    psw = psw[:-1]
            else:
               if len(psw) < 6:
                psw += digit
            set_psw(uid, psw)
            astr = '*'*len(psw)
            bot.edit_message_text('Password:\n'+astr, chat_id=call.message.chat.id, message_id=call.message.message_id+1)


def inline_psw_done(uid, bot):
    if get_psw_mode(uid):
        psw = get_psw(uid)
        if len(psw) > 3 and len(psw) < 7:
            bot.send_message(uid, "Password accepted.")
            set_old_psw(uid, psw)
            set_psw_mode(uid, False)

def inline_ticket(bot, call):
    bot.send_message(call.message.chat.id, '-4’133руб.')

