"""
Geek University Python-разработки

Мессенджер
Сервер

Учебный проект к курсу "Клиент-серверные приложения на Python".

Автор: Михаил Духонин

Октябрь - ноябрь 2021

 """


from sys import argv
from socket import socket, AF_INET, SOCK_STREAM
from logging import getLogger, error, info

from common.utils import connect_data, get_msg, send_msg
from common.variables import RESPONSE, DEFAULT_PORT,DEFAULT_SERVER_HOST, ALLERT, MAX_CONNECTIONS, ACTION, PRESENCE, TIME
from common.decorators import log_func
import log_configs.server_log_config

log = getLogger('msgr.srv')

@log_func(log)
def get_connection_data(args):
    """ Возвращает данные для подключения. Берёт либо из командной строки,
    если она их содержит, либо данные по умолчанию.

    """

    if len(args) == 3:
        return connect_data(args)
    else:
        return (DEFAULT_SERVER_HOST, DEFAULT_PORT)


@log_func(log)
def create_response(msg: dict) -> dict:
    """ Получает сообщение от клиента (словарь) и возвращает ответ сервера (словарь) """

    if not (isinstance(msg, dict) and ACTION in msg and TIME in msg):
        log.error('Получены некорректные данные', exc_info=True)
        return {
            RESPONSE: 400,
            ALLERT: 'Некорректные данные'
        }
    if msg[ACTION] == PRESENCE:
        log.info('Сообщение успешно отправлено')
        return {
            RESPONSE: 200,
            ALLERT: 'OK'
        }
    else:
        log.error('Действие не было распознано')
        return {
            RESPONSE: 400,
            ALLERT: 'Действие не распознано'
        }


def  main():
    """ Основная программа. """

    log.info('Старт сервера')
    sock = socket(AF_INET, SOCK_STREAM)
    cn = get_connection_data(args=argv)
    sock.bind(cn)
    sock.listen(MAX_CONNECTIONS)
    conn, addr = sock.accept()

    while True:
        data = get_msg(conn)
        if not data:
            break
        resp = create_response(data)
        send_msg(conn, resp)

    conn.close()
    log.info('Завершение работы сервера')


if __name__ == '__main__':
    main()
