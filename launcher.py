from subprocess import Popen, CREATE_NEW_CONSOLE, PIPE

PROCESS_LIST = []

# Файлы для вывода.

f1 = open('client.log', 'a', encoding='utf-8')
f2 = open('server.log', 'a', encoding='utf-8')

INP_MSG = f'Введите команду:\nq - выход;\no - запустить сервер и клиенты;\nx - закрыть окна.'

while True:
    cmd = input(INP_MSG)

    if cmd == 'q':
        break
    elif cmd == 'o':
        # Добиться того, чтобы окна клиента и сервера оставались открытыми после завершения их работы, мне не удалось.
        PROCESS_LIST.append(
            Popen('python server.py', creationflags=CREATE_NEW_CONSOLE, stdout=f2)
        )
        PROCESS_LIST.append(
            Popen('python client.py', creationflags=CREATE_NEW_CONSOLE, stdout=f1)
        )
    elif cmd == 'x':
        while PROCESS_LIST:
            process = PROCESS_LIST.pop()
            process.kill()

f1.close()
f2.close()

# Добавил перенаправление вывода в файлы. Всё равно окна консолей с дочерними процессами сразу закрываются.