import json
import time

def timer(fun):
    def tmp(*args, **kwargs):
        t = time.time()
        res = fun(*args, **kwargs)
        print("Время выполнения функции: %fun" % (time.time()-t))
        return res

    return tmp


class Entry:

    def __init__(self, name, address, lastname, phone, email, job):
        self.name = name
        self.address = address
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.job = job

    def to_dict( self):
        return {"name": self.name, "address": self.address, "lastname": self.lastname, "email": self.email,
              "phone": self.phone, "job": self.job}


class AddressBook:

    def __init__(self, filename):
        self.filename = filename
        self.store = {}
        self.store_from_file()

    def store_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                self.store = json.load(f)  # Загружаем объект из файла.
        except Exception :
            self.store = {}

    @timer
    def add_entry(self, entry):
        self.store[entry.phone] = entry.to_dict()
        print('Контакт добавлен')
        print(self.store)
        print('В адерсной книге {0} контактов.\n'.format(len(self.store)))

    @timer
    def del_record(self, phone):
        del self.store[phone]
        print('Контакт удален')
        print(self.store)

    @timer
    def show(self):
        print(self.store)


def enter_information():
    name = input('Введите имя: ')
    address = input('Введите адрес: ')
    lastname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    email = input('Введите email: ')
    job = input('Введите место работы: ')
    return Entry(name, address, lastname, phone, email, job)


book = AddressBook("book")


while True:
    num = int(input(
        'Какое действие необходимо сделать: 1-Добавить; 2-Удалить; 3-Показать все контакты, 4-Закончить ввод: '))

    if num == 1:
        entry = enter_information()
        book.add_entry(entry)
    if num == 2:
        phone = input('Введите имя которе нужно удалить: ')
        book.del_record(phone)
    if num == 3:
        book.show()
    if num == 4:
        break
