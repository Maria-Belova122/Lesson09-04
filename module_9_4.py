# ЗАДАНИЕ ПО ТЕМЕ "Создание функций на лету"

# 1. Метод __call__

from random import choice


class MysticBall:

    def __init__(self, *args):
        self.args = list(args)

    def __call__(self, *args):
        return choice(self.args)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# 2. Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first, second)
print(list(result))


# 3. Замыкание

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        data1 = list(data_set)
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in range(len(data1)):
                string = f'{str(data1[i])}\n'
                file.write(string)
        return file

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
