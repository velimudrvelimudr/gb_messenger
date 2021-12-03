"""
Geek University Python-разработки

Мессенджер
Общие компоненты

Учебный проект к курсу "Клиент-серверные приложения на Python".

Автор: Михаил Духонин

Октябрь - ноябрь 2021

 """

import sys
from logging import getLogger
from json import dumps, loads
from common.variables import ENCODING, MAX_SIZE_PACKAGE
from common.decorators import log_func

sys.path.append('..')

import log_configs.client_log_config
import log_configs.server_log_config

if sys.argv[0].find('server') != -1:
    log = getLogger('server')
elif sys.argv[0].find('client') != -1:
    log = getLogger('client')
else:
    print('логгер не найден')

@log_func(log)
def connect_data (args):
    """ Получает список из трёх элементов (командная трока)
    и возвращает кортеж из второго и третьего элемента.
    В   них содержатся данные для подключения/прослушивания клиента/сервера (адрес и порт).

    """

    if args and len(args) == 3:
        return (args[1], int(args[2]))

# Если честно, мне откровенно лень заморачиваться с парсингом командной строки.
# Если реально надо будет сделать соответствующий интерфейс, я лучше заморочусь с аргпарсе.

@log_func(log)
def get_msg(sock):
    """ Получает сообщение из сокета """

    msg = sock.recv(MAX_SIZE_PACKAGE)

    try:
        msg = msg.decode(ENCODING)
    except UnicodeDecodeError:
        raise ValueError('Не utf-8') from UnicodeDecodeError

    if len(msg) != 0:
        msg = loads(msg)
    else:
        print("Пустая строка")
        return {}

    if isinstance(msg, dict):
        return msg
    else:
        raise TypeError('не словарь')


@log_func(log)
def send_msg(sock, msg):
    """ Отправляет сообщение msg в сокет сервера sock. """

    if isinstance(msg, dict):
        j_msg = dumps(msg)
    else:
        raise TypeError('Сообщение должно быть словарём.')

    b_msg = bytes(j_msg, 'utf-8')
    return sock.send(b_msg)
