"""
Geek University Python-разработки

Мессенджер
Конфигурация логирования для сервера.

Учебный проект к курсу "Клиент-серверные приложения на Python".

Автор: Михаил Духонин

Октябрь - ноябрь 2021

 """

from locale import setlocale, LC_ALL
import os
from logging import DEBUG, handlers, Formatter, getLogger

setlocale(LC_ALL, 'ru_RU')

# Оставил как образец базовой настройки логгера.
""" basicConfig(
    filename='server.log',
    format='%(levelname)s\t%(asctime)s\t%(message)s',
    datefmt='%d %B %Y, %H %M, %A',
    level= DEBUG
)
 """

path_log = os.path.join(os.getcwd(), 'logs', 'server.log')
log_file_handler = handlers.TimedRotatingFileHandler(path_log, encoding='utf-8', interval=1, when='D')
log_file_handler.setLevel(DEBUG)

formatter = Formatter(
    fmt='%(levelname)s\t%(asctime)s\t%(module)s\t%(message)s',
    datefmt='%d %B %Y, %H %M, %A'
)

log_file_handler.setFormatter(formatter)

log = getLogger('msgr.srv')
log.addHandler(log_file_handler)
log.setLevel(DEBUG)

if __name__ == '__main__':
    log.info('Тестовая запись в логе.')
