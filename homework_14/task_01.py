import sqlite3


db = sqlite3.connect('phonebook.sqlite')
db.execute(f'''create table  if not exists book
(
    id integer
        constraint book_p
            primary key autoincrement,
    name TEXT not null
        constraint book_p2
            unique,
    phone_number TEXT not null
);
''')
db.commit()


def choose_operation():
    return input('''Выберите операцию:
    0. Выйти из программы
    1. Добавить новый контакт
    2. Показать все контакты в алфавитном порядке
    3. Обновить номер контакта
: ''')


def add_contact():
    name, phone_number = input('Имя: '), input('Номер телефона: ')
    db.execute('insert into book(name, phone_number) values(?, ?);', (name, phone_number))
    db.commit()
    print('Контакт создан!')


def show_all():
    it = db.execute('SELECT name, phone_number FROM book ORDER BY name;')
    for name, phone_number in it.fetchall():
        print(f'{name}: {phone_number}')


def update_number():
    name = input('Введите имя: ')
    new_number = input('Введите новый номер: ')
    pr = db.execute('update book set phone_number = ? where name = ?', (new_number, name))
    if not pr.rowcount:
        print(f'Пользователь с таким именем не существует')
    db.commit()


while True:
    operation = choose_operation()
    match operation:
        case '0':
            exit(0)
        case '1':
            add_contact()
        case '2':
            show_all()
        case '3':
            update_number()
        case _:
            print('Такой функции не существует')
