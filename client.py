from json import dumps
from socket import AF_INET, SOCK_STREAM, socket
from sys import argv
from datetime import datetime
from common.utils import connect_data, get_msg, send_msg
from common.variables import ACTION, PRESENCE, TIME, DEFAULT_CLIENT_HOST, DEFAULT_PORT, RESPONSE, ALLERT


def get_connection_data(args=['']):
    """ Получает данные для подключения """

    if len(args) == 3:
        return connect_data(args)
    else:
        return (DEFAULT_CLIENT_HOST, DEFAULT_PORT)


def send_presence(sock):
    """ Отправляет приветствие серверу.
    Возвращает число отправленных байтов.

     """

    msg_presence = {
        ACTION: PRESENCE,
        TIME: datetime.timestamp(datetime.now())
    }

    return send_msg(sock, msg_presence)


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    cn = get_connection_data(argv)
    sock.connect(cn)
    send_presence(sock)
    msg = get_msg(sock)
    sock.close()
    return msg[RESPONSE], msg[ALLERT]


if __name__ == '__main__':
    print(main())