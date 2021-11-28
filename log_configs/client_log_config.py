"""
Geek University Python-разработки

Мессенджер
Конфигурация логирования для клиента.

Учебный проект к курсу "Клиент-серверные приложения на Python".

Автор: Михаил Духонин

Октябрь - ноябрь 2021

 """

from locale import setlocale, LC_ALL
import os
from logging import DEBUG, FileHandler, Formatter, getLogger

setlocale(LC_ALL, 'ru_RU')

path_log = os.path.join(os.getcwd(), 'logs', 'client.log')
log_file_handler = FileHandler(path_log, encoding='utf-8')
log_file_handler.setLevel(DEBUG)

formatter = Formatter(fmt='%(levelname)s\t%(asctime)s\t%(module)s\t%(message)s', datefmt='%d %B %Y, %H %M, %A')
log_file_handler.setFormatter(formatter)

log = getLogger('msgr.clnt')
log.addHandler(log_file_handler)
log.setLevel(DEBUG)

if __name__ == '__main__':
    log.info('Тест журналирования клиента')
    