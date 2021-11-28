import  os
import sys
import unittest

sys.path.append(os.path.dirname(os.getcwd()))

from common.variables import ACTION, DEFAULT_CLIENT_HOST, DEFAULT_PORT, PRESENCE, RESPONSE, TIME
from client import get_connection_data, send_msg, send_presence
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