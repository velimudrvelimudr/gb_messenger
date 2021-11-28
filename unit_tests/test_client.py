"""
Geek University Python-разработки

Мессенджер
Тесты для клиента

Учебный проект к курсу "Клиент-серверные приложения на Python".

Автор: Михаил Духонин

Октябрь - ноябрь 2021

 """

import  os
import sys
import unittest

sys.path.append(os.path.dirname(os.getcwd()))

from client import get_connection_data, send_presence
from common.variables import DEFAULT_CLIENT_HOST, DEFAULT_PORT, TIME
from test_utils import TestSock


class TestServer(unittest.TestCase):
    """ Тестирование сервера """

    # Тест get_connection_data

    args = ['', 'localhost', '9999']

    def test_cmd(self):
        """ Тестируем командную строку. """

        self.assertEqual(get_connection_data(args=self.args), ('localhost', 9999))

    def test_nocmd(self):
        """ Тестируем без командной строки """

        self.assertEqual(get_connection_data(args=['']), (DEFAULT_CLIENT_HOST, DEFAULT_PORT))

    def test_send_presence(self):
        """ Тест функции send_presence. """

        self.assertIsInstance(send_presence(TestSock), int)
        # Убеждаемся, что функция возвращает целое число.


if __name__ == '__main__':
    unittest.main()
