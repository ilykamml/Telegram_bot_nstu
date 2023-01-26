def main():
    pass

def new_one(id, info=''):
    # читаем txt файл с id пользователей, если такого id ещё нет - добавляем
    try:
        with open('users.txt', 'r') as f:
            users = f.read()
    except FileNotFoundError:
        users = ''
    if str(id) not in users:
        with open('users.txt', 'a') as f:
            f.write(str(id) + f'\n{info}\n')
        return True