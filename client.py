"""
Geek University Python-разработки

Мессенджер
Клиентское приложение

Учебный проект к курсу "Клиент-серверные приложения на Python".

Автор: Михаил Духонин

Октябрь - ноябрь 2021

 """

from sys import argv
from datetime import datetime
from socket import AF_INET, SOCK_STREAM, socket
from logging import getLogger

from common.utils import connect_data, get_msg, send_msg
from common.variables import ACTION, PRESENCE, TIME, DEFAULT_CLIENT_HOST, DEFAULT_PORT, RESPONSE, ALLERT
from common.decorators import log_func
import log_configs.client_log_config

log = getLogger('msgr.clnt')

@log_func(log)
def get_connection_data(args):
    """ Получает данные для подключения """

    if len(args) == 3:
        return connect_data(args)
    else:
        return (DEFAULT_CLIENT_HOST, DEFAULT_PORT)


@log_func(log)
def send_presence(sock):
    """ Отправляет приветствие серверу.
    Возвращает число отправленных байтов.

    """

    log.info('Запуск функции send_presence')
    # Чтобы что-то писалось в клиентский лог при запуске тестов.

    msg_presence = {
        ACTION: PRESENCE,
        TIME: datetime.timestamp(datetime.now())
    }

    return send_msg(sock, msg_presence)


def main():
    """ Основной код """

    sock = socket(AF_INET, SOCK_STREAM)
    cn = get_connection_data(argv)
    sock.connect(cn)
    send_presence(sock)
    msg = get_msg(sock)
    sock.close()
    return msg[RESPONSE], msg[ALLERT]


if __name__ == '__main__':
    try:
        print(main())
        log.info('Клиент отработал!')
    except ConnectionRefusedError as e:
        log.error('Ошибка соединения', exc_info=True)
