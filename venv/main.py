import telebot
from telebot import types
import time
import bs4
import random
from datetime import datetime
import pandas as pd
import numpy as np

def cal_t():
    months_eng = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months_rus = ['Январь', "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                  "Ноябрь", "Декабрь"]
    days_eng = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days_rus = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    t = time.ctime()
    td_ind = days_eng.index(t[:3])
    t = t.replace(t[:3], days_rus[td_ind]) #аааа
    tm_ind = months_eng.index(t[3:6])
    t = t.replace(t[3:6], months_rus[tm_ind])
    return t


token = '5931893415:AAEjFSs3qjX4DqOsx5oojBXspAoZ52IuU4I'
bot = telebot.TeleBot(token)  #да блть

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Начало работы бота')
    bot.send_message(message.chat.id, 'Введите /com для просмотра списка комманд')

@bot.message_handler(commands=['com'])
def d(message):
    bot.send_message(message.chat.id,'/start - начало \n /долг - долг Виктора \n /писюн \n /топ')


users = pd.read_excel('us.xlsx')



@bot.message_handler(commands=['писюн'])
def penis(message):
    global users
    name = message.from_user.username
    s_t = str(datetime.now().day) + str(datetime.now().month)
    if name in list(users['name']):
        ind = int(users[users['name'] == name].index.tolist()[0])  #индекс чела в бд
        print(users)
        if str(users['date'][ind]) != (str(datetime.now().day) + str(datetime.now().month)): #играл сегодня или нет
            x = random.randint(-5, 10)
            l = int(users['cm'][ind]) + x
            users.loc[[ind], ['cm']] = l
            users.loc[[ind], ['date']] = s_t
            if x >= 0:
                bot.send_message(message.chat.id, f'{name}, твій пісюн виріс на {x} см. Тепер його довжина {l} см')
                users.to_excel('us.xlsx')
            else:
                if l < 0:
                    while l < 0:
                        x = random.randint(-5, 10)
                        l = int(users[ind]['cm']) + x
                bot.send_message(message.chat.id, f'{name}, твій пісюн зменшився на {abs(x)} см. Тепер його довжина {l} см')
                users.to_excel('us.xlsx')

        else:
            bot.send_message(message.chat.id, f'{name}, ти сьогодні вже грав')
    else:
        x = random.randint(1, 10)
        a = pd.DataFrame({'name': name, 'cm': x, 'date': s_t}, index=[len(users['name'])])
        users = pd.concat([users, a])
        ind = int(users[users['name'] == name].index.tolist()[0])  #индекс чела
        bot.send_message(message.chat.id, f'{name} ты в игре, твой кок целых {users["cm"][ind]} см')
        users.to_excel('us.xlsx')


@bot.message_handler(commands=['топ'])
def top(message):
    for i in range(len(users)):
        bot.send_message(message.chat.id, f'{i+1}. {users["name"][i]} -  {users["cm"][i]} cm')



@bot.message_handler(commands=['долг'])
def dolg(message):
    t = cal_t()
    bot.send_message(message.chat.id, f'На сегодняшний день, {t} \n Виктор должен: \n Марку - 1000 руб, Олегу - 1000 руб, Глебу - 1000 руб, Стёпе - 200 руб, Ярику - пачку чапмана с яблоком, а также взять подик в школу')



bot.infinity_polling()()