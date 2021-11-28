from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
from common.utils import connect_data, get_msg, send_msg
from common.variables import RESPONSE, DEFAULT_PORT,DEFAULT_SERVER_HOST, ALLERT, MAX_CONNECTIONS, ACTION, PRESENCE, TIME


def get_connection_data(args=['']):
    """ Возвращает данные для подключения. Берёт либо из командной строки, если она их содержит, либо данные по умолчанию. """

    if len(args) == 3:
        return connect_data(args)
    else:
        return ((DEFAULT_SERVER_HOST, DEFAULT_PORT))


def create_response(msg: dict) -> dict:
    """ Получает сообщение от клиента (словарь) и возвращает ответ сервера (словарь) """

    if not (isinstance(msg, dict) and ACTION in msg and TIME in msg):
        return {
            RESPONSE: 400,
            ALLERT: 'Некорректные данные'
        }
    if msg[ACTION] == PRESENCE:
        return {
            RESPONSE: 200,
            ALLERT: 'OK'
        }
    else:
        return {
            RESPONSE: 400,
            ALLERT: 'Действие не распознано'
        }


def  main():
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


if __name__ == '__main__':
    main()