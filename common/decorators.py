"""
Geek University Python-разработки

Мессенджер
Декораторы

Учебный проект к курсу "Клиент-серверные приложения на Python".

Автор: Михаил Духонин

Октябрь - ноябрь 2021

 """

import logging
import traceback
import inspect


def log_func(logger):
    """ Записывает в логи информацию о функции при её вызове """

    def logging_func(func):
        def wrap(*args, **kwargs):
            ret = func(*args, **kwargs)
            logger.debug(
                f'Функция: {func.__name__}\n'
                f'Параметры: {args}, {kwargs}\n'
                f'Модуль: {func.__module__}\n'
                f'Вызов из функции: {traceback.format_stack()[0].strip().split()[-1]}\n'
                f'Вызов из функции: {inspect.stack()[1][3]}\n'
            )
            return ret
        return wrap
    return logging_func
