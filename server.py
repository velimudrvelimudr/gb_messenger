from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv
from common.utils import connect_data, get_msg, send_msg
from common.variables import *

sock = socket(AF_INET, SOCK_STREAM)

if len(argv) == 3:
    cn = connect_data(argv)
else:
    cn = ((DEFAULT_SERVER_HOST, DEFAULT_PORT))

sock.bind(cn)
sock.listen(MAX_CONNECTIONS)
conn, addr = sock.accept()

while True:
    data = get_msg(conn)
    if not data:
        break
    if data[ACTION] == PRESENCE:
        resp = {
            RESPONSE: 200,
            ALLERT: 'OK'
        }
    send_msg(conn, resp)

conn.close()
