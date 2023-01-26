import json
import datetime

def main():
    pass

# функция записи в json файл
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# функция чтения из json файла
def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# функция добавления нового пользователя в json файл
def new_one(id, info=''):
    # читаем txt файл с id пользователей, если такого id ещё нет - добавляем
    try:
        data = read_json('users.json')
    except:
        data = {}
    if str(id) not in data:
        print(f'{get_time()} - New user: {id}, {info.get("username")}!')
        data[str(id)] = info
        write_json(data, 'users.json')
        return True
    return False

# функция удаления пользователя из json файла
def delete_one(id):
    data = read_json('users.json')
    if str(id) in data:
        del data[str(id)]
        write_json(data, 'users.json')
        return True
    return False

# функция перевода timestamp в дату
def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%d.%m.%Y %H:%M:%S")

#узнать время
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")
