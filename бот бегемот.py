import telebot
from telebot import types
import json
import random
import datetime
import time
import threading
from operator import itemgetter
#from funcs import *



with open('content_r.json', 'r+', encoding='utf-8') as bege_json:
    bege_data = json.load(bege_json)
    print(bege_data)

    

state = True
def check_state():
    global state
    if state == False:
        time.sleep(2)
        state = True
    else:
        state = False

state2 = True
def check_state2():
    global state2
    if state2 == False:
        time.sleep(2)
        state2 = True
    else:
        state2 = False
        
state3 = True
def check_state3():
    global state3
    if state3 == False:
        time.sleep(2)
        state3 = True
    else:
        state3 = False

state4 = True
def check_state4():
    global state4
    if state4 == False:
        time.sleep(1.5)
        state4 = True
    else:
        state4 = False

state5 = True
def check_state5():
    global state5
    if state5 == False:
        time.sleep(2)
        state5 = True
    else:
        state5 = False

state6 = True
def check_state6():
    global state6
    if state6 == False:
        time.sleep(2)
        state6 = True
    else:
        state6 = False

state7 = True
def check_state7():
    global state7
    if state7 == False:
        time.sleep(2)
        state7 = True
    else:
        state7 = False

state8 = True
def check_state8():
    global state8
    if state8 == False:
        time.sleep(2)
        state8 = True
    else:
        state8 = False

state9 = True
def check_state9():
    global state9
    if state9 == False:
        time.sleep(2)
        state9 = True
    else:
        state9 = False

state10 = True
def check_state10():
    global state10
    if state10 == False:
        time.sleep(2)
        state10 = True
    else:
        state10 = False

state11 = True
def check_state11():
    global state11
    if state11 == False:
        time.sleep(2)
        state11 = True
    else:
        state11 = False

     

def user_add(user):
    check_state3()
    
    users = bege_data['Users']
    
    if user in users:
        state3 = True
        pass
        
    if user not in users:
        rand_pfp = random.choice(list(bege_data['Begemotiki']['default_begemotiki'].values()))
        with open('content_r.json', 'w', encoding='utf-8') as bege_json:
            bege_data['Users'][user] = {"user_begemotiki": {"default_user_begemotiki": [], "elite_user_begemotiki": []}, 'money': 0, 'pfp': rand_pfp, 'exp': 0, 'level': 1}
            json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

        state3 = True

def get_salary(message):
    #Старая формула получения уровня: Salary = 10 + [(5/2)*level]
    with open('content_r.json', 'w', encoding='utf-8') as bege_json:
        level = bege_data['Users'][str(message.from_user.id)]['level']
        bege_data['Users'][str(message.from_user.id)]['money'] += (10 + 8*level)
        json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

    zp = 10 + 8*level
    bot.reply_to(message, text=f"Вы получили зарплату в размере {zp} бегекоинов! Следующая з/п через 12 часов")

def default_begemotik_add(message, default_begemotik):
    check_state4()
    user = message.from_user.id
    print(user)
    
    default_begemotiks = bege_data['Users'][str(user)]['user_begemotiki']['default_user_begemotiki']
    
    if default_begemotik in default_begemotiks:
        bot.reply_to(message, text='Ого! Повторка! Держи 5 бегекоинов в качестве компенсации!\n+10 EXP')
        with open('content_r.json', 'w', encoding='utf-8') as bege_json:
            bege_data['Users'][str(user)]['money']+=5
            bege_data['Users'][str(user)]['exp']+= 20
            json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

        state4 = True
            
    if default_begemotik not in default_begemotiks:
        with open('content_r.json', 'w', encoding='utf-8') as bege_json:
            bege_data['Users'][str(user)]['user_begemotiki']['default_user_begemotiki'].append(default_begemotik)
            bege_data['Users'][str(user)]['exp']+= 10
            json.dump(bege_data, bege_json, indent=4, ensure_ascii=False)

        state4 = True

def elite_begemotik_add(message, elite_begemotik):
    check_state6()
    user = message.from_user.id
    print(user)
    
    elite_begemotiks = bege_data['Users'][str(user)]['user_begemotiki']['elite_user_begemotiki']

    if elite_begemotik not in elite_begemotiks:
        with open('content_r.json', 'w', encoding='utf-8') as bege_json:
            bege_data['Users'][str(user)]['user_begemotiki']['elite_user_begemotiki'].append(str(elite_begemotik))
            bege_data['Users'][str(user)]['exp']+= 25
            json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

        state6 = True
    
    elif elite_begemotik in elite_begemotiks:
        bot.reply_to(message, text='Повторка! Держи 20 бегекоинов в качестве компенсации')
        with open('content_r.json', 'w', encoding='utf-8') as bege_json:
            bege_data['Users'][str(user)]['money']+=20
            bege_data['Users'][str(user)]['exp']+= 25
            json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

        
        state6 = True


def change_pfp_func(message):
    txt = message.text
    print(txt)
    default_user_begemotiki = bege_data['Users'][str(message.from_user.id)]['user_begemotiki']['default_user_begemotiki']
    elite_user_begemotiki = bege_data['Users'][str(message.from_user.id)]['user_begemotiki']['elite_user_begemotiki']

    if txt[0] != 'E':
        
        if txt in default_user_begemotiki:
            with open('content_r.json', 'w', encoding='utf-8', ) as bege_json:
                bege_data['Users'][str(message.from_user.id)]['pfp'] = bege_data['Begemotiki']['default_begemotiki'][txt]
                json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)
                bot.reply_to(message, text='Фото профиля было успешно обновлено')

        if txt not in default_user_begemotiki:
            bot.reply_to(message, text='У вас походу нет этого бегемотика. Попробуйте ещё раз')

    if txt[0] == 'E':
        
        if txt in elite_user_begemotiki:
            with open('content_r.json', 'w', encoding='utf-8', ) as bege_json:
                bege_data['Users'][str(message.from_user.id)]['pfp'] = bege_data['Begemotiki']['elite_begemotiki'][txt]
                json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)
                bot.reply_to(message, text='Фото профиля было успешно обновлено')

        if txt not in elite_user_begemotiki:
            bot.reply_to(message, text='У вас походу нет этого бегемотика. Попробуйте ещё раз')


def check_and_change_level(message):
    check_state11()
    
    if bege_data['Users'][str(message.from_user.id)]['level'] == 1:
        if bege_data['Users'][str(message.from_user.id)]['exp'] >= 100:
            bot.reply_to(message, text='Поздравляю! У тебя теперь 2 уровень!')
            with open('content_r.json', 'w', encoding='utf-8') as bege_json:
                bege_data['Users'][str(message.from_user.id)]['level'] = 2
                json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

    elif bege_data['Users'][str(message.from_user.id)]['level'] == 2:
        if bege_data['Users'][str(message.from_user.id)]['exp'] >= 500:
            bot.reply_to(message, text='Поздравляю! У тебя теперь 3 уровень!')
            with open('content_r.json', 'w', encoding='utf-8') as bege_json:
                bege_data['Users'][str(message.from_user.id)]['level'] = 3
                json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

    elif bege_data['Users'][str(message.from_user.id)]['level'] == 3:
        if bege_data['Users'][str(message.from_user.id)]['exp'] >= 1000:
            bot.reply_to(message, text='Поздравляю! У тебя теперь 4 уровень!')
            with open('content_r.json', 'w', encoding='utf-8') as bege_json:
                bege_data['Users'][str(message.from_user.id)]['level'] = 4
                json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

    elif bege_data['Users'][str(message.from_user.id)]['level'] == 4:
        if bege_data['Users'][str(message.from_user.id)]['exp'] >= 2500:
            bot.reply_to(message, text='Поздравляю! У тебя теперь 5 уровень!')
            with open('content_r.json', 'w', encoding='utf-8') as bege_json:
                bege_data['Users'][str(message.from_user.id)]['level'] = 5
                json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)
    
    
    state11 = True




bot = telebot.TeleBot('8780791669:AAF39ExUdwiDiywTw6OWP8Ztlq3ziiMSVc0')

@bot.callback_query_handler(func=lambda callback: True)
def del_govno(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)

@bot.message_handler(commands=['start'])
def start(message):
    check_state2()
    user_add(str(message.from_user.id))
     
    with open('begemotiki/func/start_begemotik.jpg', 'rb') as start_photo:
        bot.send_photo(message.chat.id, photo = start_photo, caption = f'''Привет, {message.from_user.first_name}, Я Бот-Бегемот!
Напиши /card для того, чтобы получить карточку
Напиши /help для того, чтобы узнать больше''')

    state2 = True


@bot.message_handler(commands=['card'])
def get_card(message):
    user_add(str(message.from_user.id))
    check_state()
    queue_card = bege_data['Queue']['for_card']

    if str(message.from_user.id) not in queue_card:
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(hours=1)
        with open('content_r.json', 'w', encoding='utf-8') as bege_json:
            bege_data['Queue']['for_card'][str(message.from_user.id)] = str(end_time)
            json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)
        
        rand_int = random.randint(0, len(bege_data['Begemotiki']['default_begemotiki'])-1)
        print(rand_int)
        with open(bege_data['Begemotiki']['default_begemotiki'][str(rand_int)], 'rb') as bege_photo:
            print(bege_data['Begemotiki']['default_begemotiki'][str(rand_int)])
            bot.send_photo(message.chat.id, bege_photo, f'{message.from_user.first_name}, тебе достался бегемотик: {rand_int}!\n+10 EXP\nСледующая карточка через час')
            print('бот успешно отправил сообщение')
            
        default_begemotik_add(message, str(rand_int))
        print('Рандомный бегемотик: ', rand_int)
        
        #with open('content_r.json', 'w', encoding='utf-8') as bege_json:
        #    bege_data['Queue']['for_card'][str(message.from_user.id)] = str(end_time)
        #    json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)
            
        #print(queue_card)
        
        state = True
                
    elif str(message.from_user.id) in queue_card:
        new_end_time = datetime.datetime.strptime(bege_data['Queue']['for_card'][str(message.from_user.id)], '%Y-%m-%d %H:%M:%S.%f')
        delta_time = new_end_time - datetime.datetime.now()
        
        if datetime.datetime.now() < new_end_time:
            #hours = str(delta_time)[0]
            minutes = str(delta_time)[2:4]
            seconds = str(delta_time)[5:7]
            print(message.from_user.id, delta_time)

            bot.reply_to(message, text=f'Вы получите карточку через: {minutes} минут, {seconds} секунд')

            state = True
        
        elif datetime.datetime.now() >= new_end_time:
            with open('content_r.json', 'w', encoding='utf-8') as bege_json:
                del bege_data['Queue']['for_card'][str(message.from_user.id)]
                json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

            get_card(message)

            state = True

    check_and_change_level(message)



@bot.message_handler(commands=['elite_card'])
def get_elite_card(message):
    user_add(str(message.from_user.id))
    check_state5()
    
    if bege_data['Users'][str(message.from_user.id)]['money'] >= 100:
        rand_int_2 = random.randint(0, len(bege_data['Begemotiki']['elite_begemotiki'])-1)
        with open('content_r.json', 'w', encoding='utf-8') as bege_json:
            bege_data['Users'][str(message.from_user.id)]['money']-=100
            json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

        with open(bege_data['Begemotiki']['elite_begemotiki']["E"+str(rand_int_2)], 'rb') as elite_bege_photo:
            bot.send_photo(message.chat.id, elite_bege_photo, f'{message.from_user.first_name}, тебе достался бегемотик: E{str(rand_int_2)}!\n+25 EXP')

        elite_begemotik_add(message, "E"+str(rand_int_2))

    elif bege_data['Users'][str(message.from_user.id)]['money'] < 100:
        bot.reply_to(message, text=f"У тебя всего лишь {bege_data['Users'][str(message.from_user.id)]['money']} бегекоинов, а нужно 100")

        state5 = True

    check_and_change_level(message)

@bot.message_handler(commands=['help'])
def help(message):
    check_state7()
    
    user_add(str(message.from_user.id))
    with open('begemotiki/func/help_begemotik.jpg', 'rb') as help_photo:
        bot.send_photo(message.chat.id, help_photo, f"""Команды:\n
/start - начать
/help - помощь
/card - получить карточку с кислотным бегемотиком
/salary - получить зарплату
/elite_card - (стоимость - 100 бегекоинов) получить карточку с элитным бегемотиком
/profile - посмотреть профиль
/change_pfp - поменять аватарку
/top - топ 10 игроков по кол-ву бегемотиков""")

    state7 = True

@bot.message_handler(commands=['change_pfp'])
def change_pfp(message):
    check_state8()
    
    bot.reply_to(message, text=f'Выберите номер карточки с бегемотиком, который хотите поставить в профиль')
    bot.register_next_step_handler(message, change_pfp_func)
    
@bot.message_handler(commands=['profile'])
def check_profile(message):
    user_level = bege_data['Users'][str(message.from_user.id)]['level']
    check_exp = bege_data['Users'][str(message.from_user.id)]['exp']
    
    if user_level == 1:
        exp_to_next_level = 100
    elif user_level == 2:
        exp_to_next_level = 500
    elif user_level == 3:
        exp_to_next_level = 1000
    elif user_level == 4:
        exp_to_next_level = 2500
    elif user_level == 5:
        exp_to_next_level = 'max'

    print(user_level, check_exp, exp_to_next_level)
        
    with open(bege_data['Users'][str(message.from_user.id)]['pfp'], 'rb') as pfp_photo:
        bot.send_photo(message.chat.id, pfp_photo, f"""{message.from_user.first_name}, вот твой профиль!

Баланс: {bege_data['Users'][str(message.from_user.id)]['money']} бегекоинов
Кол-во обычных бегемотиков: {len(bege_data['Users'][str(message.from_user.id)]['user_begemotiki']['default_user_begemotiki'])}
Кол-во элитных бегемотиков: {len(bege_data['Users'][str(message.from_user.id)]['user_begemotiki']['elite_user_begemotiki'])}
Уровень: {bege_data['Users'][str(message.from_user.id)]['level']}
Опыт: {check_exp}/{exp_to_next_level}""")

@bot.message_handler(commands=['salary'])
def salary(message):
    user_add(str(message.from_user.id))
    check_state9()
    queue_salary = bege_data['Queue']['for_salary']

    if str(message.from_user.id) not in queue_salary:
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(hours=12)
        #print(start_time, end_time)
        
        with open('content_r.json', 'w', encoding='utf-8') as bege_json:
            bege_data['Queue']['for_salary'][str(message.from_user.id)] = str(end_time)
            json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)

        get_salary(message)

    elif str(message.from_user.id) in queue_salary:
        new_end_time = datetime.datetime.strptime(bege_data['Queue']['for_salary'][str(message.from_user.id)], '%Y-%m-%d %H:%M:%S.%f')
        delta_time = new_end_time - datetime.datetime.now()
        #print(new_end_time, delta_time)
        
        if datetime.datetime.now() < new_end_time:
            #hours = str(delta_time[0:1])
            #minutes = str(delta_time[4:5])
            #seconds = str(delta_time[:])
            bot.reply_to(message, text=f'Вы получите зарплату только через {delta_time}')

            state9 = True
            
        if datetime.datetime.now() >= new_end_time:
            with open('content_r.json', 'w', encoding='utf-8') as bege_json:
                del bege_data['Queue']['for_salary'][str(message.from_user.id)]
                json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)
                
            salary(message)
            
            state9 = True
    
@bot.message_handler(commands=['top'])
def show_top(message):
    check_state10()
    top = dict()
    
    for user in bege_data['Users']:
        if user == '1100002591' or user == '1898774534':
            continue
        else:
            begs = len(bege_data['Users'][user]['user_begemotiki']['default_user_begemotiki']) + len(bege_data['Users'][user]['user_begemotiki']['elite_user_begemotiki'])
            chat = bot.get_chat(user)
            name = f'{chat.first_name}'
            top[name] = begs
            
    top_10 = sorted(top.items(), key=itemgetter(1), reverse=True)  
        
    bot.send_message(message.chat.id, f"""
Топ 10 игроков по кол-ву бегемотиков:

1) {top_10[0][0]}: {top_10[0][1]} бегемотиков
2) {top_10[1][0]}: {top_10[1][1]} бегемотиков
3) {top_10[2][0]}: {top_10[2][1]} бегемотиков
4) {top_10[3][0]}: {top_10[3][1]} бегемотиков
5) {top_10[4][0]}: {top_10[4][1]} бегемотиков
6) {top_10[5][0]}: {top_10[5][1]} бегемотиков
7) {top_10[6][0]}: {top_10[6][1]} бегемотиков
8) {top_10[7][0]}: {top_10[7][1]} бегемотиков
9) {top_10[8][0]}: {top_10[8][1]} бегемотиков
10) {top_10[9][0]}: {top_10[9][1]} бегемотиков""")

    state10 = True

#######################################################################
#with open('content_r.json', 'w', encoding = 'utf-8') as bege_json:
#    for user in bege_data['Users']:
#        bege_data['Users'][user]['money'] += 50
#
#    json.dump(bege_data, bege_json, indent = 4, ensure_ascii=False)
#######################################################################

for user in bege_data['Users']:
    if bege_data['Users'][user]['money'] < 1:
        print(user, bege_data['Users'][user]['money'])



print('Пользователей: ', len(bege_data['Users']))
print(bege_data['Users']['6444735563'])




@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == 'хей!' or message.text.lower() == 'хей':
        bot.reply_to(message, text='Хей!')


#bot.send_message('1667108905', text = 'Пошёл нахуй я твою мать ебу')
#bot.send_message('1452256067', text = 'Пошёл нахуй я твою мать ебу')
#bot.send_message('5971903817', text = 'Пошёл нахуй я твою мать ебу')


bot.polling(none_stop=True, timeout=123)
