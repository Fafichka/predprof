import random
import csv
import string


def login(s:string):
    surname, name, patronimic = s.split()
    return surname+'_'+name[0]+patronimic[0]

""" создание логина: функция принимает имя человека в формате ФИО и возвращает в формате Фамилия_ИмяОтчество инициалами
"""


def password():
    simbols= '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    alph_lower = 'qwertyuiopasdfghjklzxcvbnm'
    alph_upper = 'WERTYUIOPASDFGHJKLZXCVBNM'
    numbers = '1234567890'
    fl = True
    while fl:
        f1,f2,f3 = False, False, False
        passw=''
        for i in range(10):
             passw += random.choice(simbols)
        for i in passw:
            if i in alph_upper:
                f1 = True
            if i in alph_lower:
                f2 = True
            if i in numbers:
                f3= True
        if f1 and f2 and f3:
            fl= False
    return passw


"""
процедура генерирует пароль из символов алфавита, строчных и прописных, цифр и проверяет чтобы из каждого набора был хотя бы 1 
символ
"""


rows = []
with open('scientist.txt', encoding='utf8') as file:
    data = list(csv.DictReader(file, delimiter='#', quotechar='"'))
    for i in range(len(data)):
        data[i]['login'] = login(data[i]['ScientistName'])
        data[i]['password'] = password()
        rows.append(data[i]) # генерируем пароли и логины и записываем их
with open('scientist_password.csv', 'w', newline='', encoding='utf8') as f:
    w=csv.DictWriter(f, fieldnames=['ScientistName', 'preparation', 'date', 'components', 'login', 'password'], delimiter='#')
    w.writeheader()
    w.writerows(rows)
