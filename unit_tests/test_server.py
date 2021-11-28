"""
Geek University Python-разработки

Мессенджер
Тесты для Сервера

Учебный проект к курсу "Клиент-серверные приложения на Python".

Автор: Михаил Духонин

Октябрь - ноябрь 2021

 """

import  os
import sys
import unittest

sys.path.append(os.path.dirname(os.getcwd()))

from server import create_response, get_connection_data
from common.variables import ACTION, DEFAULT_SERVER_HOST, DEFAULT_PORT, PRESENCE, RESPONSE, TIME

class TestServer(unittest.TestCase):
    """ Тестирование сервера """

    # Тест get_connection_data

    args = [None, '', '9999']

    def test_cmd(self):
        """ Тестируем командную строку. """

        self.assertEqual(get_connection_data(args=self.args), ('', 9999))

    def test_nocmd(self):
        """ Тестируем без командной строки """

        self.assertEqual(get_connection_data(args=['']), (DEFAULT_SERVER_HOST, DEFAULT_PORT))

    # Тестирование функции create_response

    corr_req = {
        ACTION: PRESENCE,
        TIME: 1635572238.724969
    }

    unknow_action_req = {
        ACTION: 'kva',
        TIME: 1635572238.724969
    }

    def test_create_response(self):
        """ Проверяет корректность ответа на валидных данных. """

        self.assertEqual(create_response(self.corr_req)[RESPONSE], 200, 'Ответ сервера не 200')

    def test_incorrect_data1(self):
        """ Подсунем совсем левые данные """

        self.assertEqual(create_response('kva')[RESPONSE], 400)

    def test_incorrect_data2(self):
        """ Поработаем с невалидными данными """

        self.assertEqual(create_response(self.unknow_action_req)[RESPONSE], 400)

if __name__ == '__main__':
    unittest.main()
