import telebot
import psycopg2
from flask import Flask, request
import os

from config import *
from markups import *

bot = telebot.TeleBot(TOKEN)

# === Authorization ===
def auth():
    uid = 'a'
    conn = psycopg2.connect(dbname='trade', user='general', password='bezoar', host='localhost')
    cursor = conn.cursor()
    select_stmt = 'SELECT * FROM trader WHERE uid = %(uid)s'
    cursor.execute(select_stmt, {'uid' : uid })
    is_present = cursor.rowcount
    if is_present == 1:
        print('present')
    else:
        print('NOT present')
    cursor.close()
    conn.close()

auth()
