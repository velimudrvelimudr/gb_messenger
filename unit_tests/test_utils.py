import os
import sys
import unittest
from json import loads, dumps

sys.path.append(os.path.dirname(os.getcwd()))

from common.utils import get_msg, send_msg
from common.variables import ACTION, PRESENCE, TIME

# Переписывать тот вариант, что был у вас, мне религия не позволяет. Поэтому сделал так, как понял.

class TestSock:
    def __init__(self) -> None:
        pass

    def recv(self):
        """ Эмуляция метода recv сокета.
        Метод получает данные из сети в виде байтов, которые и возвращает.

         """

        data = {ACTION: PRESENCE, TIME: 1.1}
        # вот это сообщение типа было получено из сети.
        return bytes(dumps(data), 'utf-8')
        # Преобразуем его в байты и отдаём получившийся результат.

    # Тут я не понял. Исходная send должна принимать два параметра, кроме, собственно, сокета (self) должно быть и сообщение. Но если добавить в объявление функции ещё один параметр ((self, msg)), то не работает.
    def send(self):
        """ Эмуляция метода send сокета.
        Единственное, что возвращает метод - длину сообщения.
        Как оттестировать, собственно отправку, не нарушая принципы unittest, я не знаю.

         """

        return len(self)


class TestUtils(unittest.TestCase):

    # Тестируем функцию get_msg.

    def test_get_msg(self):
        """ Удостоверяемся, что функция возвращает тот же словарь, что был отправлен сервером. """

        self.assertEqual(get_msg(TestSock), {ACTION: PRESENCE, TIME: 1.1})

    def test_get_msg_types(self):
        """ Удостоверяемся, что функция возвращает словарь """

        self.assertTrue(isinstance(get_msg(TestSock), dict))

    # Тестируем функцию send_msg.

    def test_send_msg(self):
        """ Тестируем корректность возврата. """

        data = {ACTION: PRESENCE, TIME: 1.1}
        self.assertEqual(send_msg(TestSock, data), 35)

    def test_incorrect_data(self):
        """ Тестируем на совсем случайных данных. """

        with self.assertRaises(TypeError):
            send_msg(TestSock, 'kva')

if __name__ == '__main__':
    unittest.main()