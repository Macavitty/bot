from telebot import types

def start_markup():
	start_markup = types.ReplyKeyboardMarkup(True, False)
	start_markup.row('Authorize')
	start_markup.row('Info')
	return start_markup
    	
def main_markup():
	main_markup = types.ReplyKeyboardMarkup(True, False)
	# main_markup.row('Download asset history')
	main_markup.row('Logout', 'Trading')
	main_markup.row('Forget me', 'Info')
	return main_markup

def trade_markup():
	trade_markup = types.ReplyKeyboardMarkup(True, False)
	trade_markup.row('Profit/Loss', 'Get course', 'Open orders')
	trade_markup.row('Make order', 'Check balance')
	trade_markup.row('Reboot', 'Back')
	return trade_markup

def instrument_markup():
	instrument_markup = types.ReplyKeyboardMarkup(True, False)
	instrument_markup.row('Futures', 'Options')
	instrument_markup.row('Shares', 'Currency')
	instrument_markup.row('Reboot', 'Back')
	return instrument_markup

def market_markup():
	market_markup = types.ReplyKeyboardMarkup(True, False)
	market_markup.row('Financial market', 'Currency market')
	market_markup.row('Cryptocurrency market', 'FORTS')
	market_markup.row('Reboot', 'Back')
	return market_markup


def order_markup():
    order_markup = types.ReplyKeyboardMarkup(True, False)
    order_markup.row('Sell', 'Buy')
    order_markup.row('Reboot', 'Back')
    return order_markup

def period_markup():
    period_markup = types.ReplyKeyboardMarkup(True, False)
    period_markup.row('All', 'Year', 'Month')
    period_markup.row('Week', 'Day', 'Hour')
    period_markup.row('Reboot', 'Back')
    return period_markup


def auth_markup():
	auth_markup = types.InlineKeyboardMarkup()
	pass_btn = types.InlineKeyboardButton(text="Use login and password", callback_data="password")
	keys_btn = types.InlineKeyboardButton(text="Use keys", callback_data="keys")
	auth_markup.add(pass_btn)
	auth_markup.add(keys_btn)
	return auth_markup

def password_markup():
    btn_1 = types.InlineKeyboardButton(text="1", callback_data="btn_d_1")
    btn_2 = types.InlineKeyboardButton(text="2", callback_data="btn_d_2")
    btn_3 = types.InlineKeyboardButton(text="3", callback_data="btn_d_3")
    btn_4 = types.InlineKeyboardButton(text="4", callback_data="btn_d_4")
    btn_5 = types.InlineKeyboardButton(text="5", callback_data="btn_d_5")
    btn_6 = types.InlineKeyboardButton(text="6", callback_data="btn_d_6")
    btn_7 = types.InlineKeyboardButton(text="7", callback_data="btn_d_7")
    btn_8 = types.InlineKeyboardButton(text="8", callback_data="btn_d_8")
    btn_9 = types.InlineKeyboardButton(text="9", callback_data="btn_d_9")
    btn_0 = types.InlineKeyboardButton(text="0", callback_data="btn_d_0")
    btn_del = types.InlineKeyboardButton(text="C", callback_data="btn_d_del")
    btn_start = types.InlineKeyboardButton(text="Start", callback_data="btn_psw_str")
    btn_complited = types.InlineKeyboardButton(text="Done", callback_data="btn_psw_done")
    btn_cancel = types.InlineKeyboardButton(text="Cancel", callback_data="btn_psw_cancel")
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(btn_1, btn_2, btn_3,
        btn_4, btn_5, btn_6,
        btn_7, btn_8, btn_9,
        btn_cancel, btn_0, btn_del,
        btn_start, btn_complited)
    return kb

def conf_markup():
    btn_1 = types.InlineKeyboardButton(text="1", callback_data="btn_1")
    btn_2 = types.InlineKeyboardButton(text="2", callback_data="btn_2")
    btn_3 = types.InlineKeyboardButton(text="3", callback_data="btn_3")
    btn_4 = types.InlineKeyboardButton(text="4", callback_data="btn_4")
    btn_5 = types.InlineKeyboardButton(text="5", callback_data="btn_5")
    btn_6 = types.InlineKeyboardButton(text="6", callback_data="btn_6")
    btn_7 = types.InlineKeyboardButton(text="7", callback_data="btn_7")
    btn_8 = types.InlineKeyboardButton(text="8", callback_data="btn_8")
    btn_9 = types.InlineKeyboardButton(text="9", callback_data="btn_9")
    btn_0 = types.InlineKeyboardButton(text="0", callback_data="btn_0")
    btn_val = types.InlineKeyboardButton(text="Validate", callback_data="btn_val")
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9, btn_0, btn_val)
    return kb

def ticker_markup():
    MSFT = types.InlineKeyboardButton(text="MSFT", callback_data="t_1")
    MRRT = types.InlineKeyboardButton(text="MRRT", callback_data="t_2")
    RGBI = types.InlineKeyboardButton(text="RGBI", callback_data="t_3")
    RURVOL = types.InlineKeyboardButton(text="RURVOL", callback_data="t_4")
    RUPCI = types.InlineKeyboardButton(text="RUPCI", callback_data="t_5")
    TESTNAV = types.InlineKeyboardButton(text="TESTNAV", callback_data="t_6")
    a = types.InlineKeyboardButton(text="SRATE_ED_ON", callback_data="t_7")
    b = types.InlineKeyboardButton(text="MCX BO 2W", callback_data="t_8")
    c = types.InlineKeyboardButton(text="UX", callback_data="t_9")
    d = types.InlineKeyboardButton(text="MEMMTR", callback_data="t_10")
    e = types.InlineKeyboardButton(text="MSFT", callback_data="t_11")
    f = types.InlineKeyboardButton(text="RTS2", callback_data="t_12")
    g = types.InlineKeyboardButton(text="MOEXBC", callback_data="t_13")
    h = types.InlineKeyboardButton(text="VTBSN", callback_data="t_14")
    i = types.InlineKeyboardButton(text="SBCBA", callback_data="t_15")
    j = types.InlineKeyboardButton(text="RUCBCP5Y", callback_data="t_16")
    k = types.InlineKeyboardButton(text="MOEXOG", callback_data="t_17")
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(MRRT, MSFT, RGBI, RURVOL, RUPCI, a, b, c, d, e, f, g, h, i, j , k)
    return kb
