from json import dumps, loads

from common.variables import ENCODING, MAX_CONNECTIONS, MAX_SIZE_PACKAGE

def connect_data (args=None):
    """ Получает список из трёх элементов (командная трока) и возвращает кортеж из второго и третьего элемента.
    В   них содержатся данные для подключения/прослушивания клиента/сервера (адрес и порт). """

    if args and len(args) == 3:
        return (args[1], int(args[2]))

# Если честно, мне откровенно лень заморачиваться с парсингом командной строки. Если реально надо будет сделать соответствующий интерфейс, я лучше заморочусь с аргпарсе.

def get_msg(sock):

    msg = sock.recv(MAX_SIZE_PACKAGE)

    try:
        msg = msg.decode(ENCODING)
    except UnicodeDecodeError: 
        raise ValueError('Не utf-8')

    if len(msg) != 0:
        msg = loads(msg)
    else:
        print("Пустая строка")
        return {}
        
    if isinstance(msg, dict):
        return msg
    else:
        raise TypeError('не словарь')


def send_msg(sock, msg):

    if isinstance(msg, dict):
        j_msg = dumps(msg)
    else:
        raise TypeError('Сообщение должно быть словарём.')

    b_msg = bytes(j_msg, 'utf-8')

    sock.send(b_msg)

