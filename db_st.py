import psycopg2

from config_db import *

# ===== USER =====
def save_new_trader(uid):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    insert_stmt = 'INSERT INTO trader (uid, u_state, psw_mode, step, password, old_password) VALUES (%s, \'t\', \'f\', \'none\', \'no\', \'no\')'
    cursor.execute(insert_stmt, (uid, ))
    conn.commit()
    cursor.close()
    conn.close()

def delete_trader(uid):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    delete_stmt = 'DELETE FROM trader WHERE uid = %s'
    cursor.execute(delete_stmt, (uid, ))
    conn.commit()
    cursor.close()
    conn.close()

def is_usr_present(uid):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    select_stmt = 'SELECT * FROM trader WHERE uid = %(uid)s'
    cursor.execute(select_stmt, {'uid': uid})
    num = cursor.rowcount
    cursor.close()
    conn.close()
    if num == 1:
        return True
    return False


# ===== PASSWORD =====
def get_psw_mode(uid):
    if is_usr_present(uid) == False:
        return False
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    select_stmt = 'SELECT psw_mode FROM trader WHERE uid = %(uid)s'
    cursor.execute(select_stmt, {'uid': uid})
    mode = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return mode

def set_psw_mode(uid, mode):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    upd_stmt = 'UPDATE trader SET psw_mode = %s  WHERE uid = %s'
    cursor.execute(upd_stmt, (mode, uid, ))
    conn.commit()
    cursor.close()
    conn.close()

def get_psw(uid):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    select_stmt = 'SELECT password FROM trader WHERE uid = %(uid)s'
    cursor.execute(select_stmt, {'uid': uid})
    psw = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return psw

def set_psw(uid, psw):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    upd_stmt = 'UPDATE trader SET password = %s  WHERE uid = %s'
    cursor.execute(upd_stmt, (psw, uid, ))
    conn.commit()
    cursor.close()
    conn.close()


def get_old_psw(uid):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    select_stmt = 'SELECT old_password FROM trader WHERE uid = %(uid)s'
    cursor.execute(select_stmt, {'uid': uid})
    psw = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return psw

def set_old_psw(uid, psw):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    upd_stmt = 'UPDATE trader SET old_password = %s  WHERE uid = %s'
    cursor.execute(upd_stmt, (psw, uid, ))
    conn.commit()
    cursor.close()
    conn.close()


def get_usr_state(uid):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    select_stmt = 'SELECT u_state FROM trader WHERE uid = %(uid)s'
    cursor.execute(select_stmt, {'uid': uid})
    state = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return state

def set_usr_state(uid, state):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    upd_stmt = 'UPDATE trader SET u_state = %s  WHERE uid = %s'
    cursor.execute(upd_stmt, (state, uid, ))
    conn.commit()
    cursor.close()
    conn.close()

# ===== STEPS ===== 
def get_step(uid):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    select_stmt = 'SELECT step FROM trader WHERE uid = %(uid)s'
    cursor.execute(select_stmt, {'uid': uid})
    step = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return step

def set_step(uid, step):
    conn = psycopg2.connect(dbname = DB_NAME,
                            user = DB_USR,
                            password = DB_PSW,
                            host=DB_HOST)
    cursor = conn.cursor()
    upd_stmt = 'UPDATE trader SET step = %s  WHERE uid = %s'
    cursor.execute(upd_stmt, (step, uid, ))
    conn.commit()
    cursor.close()
    conn.close()
