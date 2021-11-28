from json import dumps
from socket import AF_INET, SOCK_STREAM, socket
from sys import argv
from datetime import datetime
from common.utils import connect_data, get_msg, send_msg
from common.variables import *

sock = socket(AF_INET, SOCK_STREAM)

if len(argv) == 3:
    cn = connect_data(argv)
else:
    cn = ((DEFAULT_CLIENT_HOST, DEFAULT_PORT))

sock.connect(cn)

msg_presence = {
    ACTION: PRESENCE,
    TIME: datetime.timestamp(datetime.now())
}

send_msg(sock, msg_presence)
msg = get_msg(sock)
sock.close()
print(msg[RESPONSE], msg[ALLERT])
