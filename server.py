import random
import socket
from DHP import *


PORT = 9393

with socket.socket() as sock:

    sock.bind(("", PORT))  # Создание сокета
    sock.listen(1)
    print("\nСокет создан\n")
    conn, addr = sock.accept()

    print("Успешно подключено к {}\n\n".format(addr[0]))  # Сообщение об успешном подключении, с выводом адреса клиента

    print("{}\n\n".format(conn.recv(1024).decode()))  # Получение приветственного сообщения

    private_key = random.randint(10000, 100000)  # Генерация приватного ключа
    public_c = int(conn.recv(1024).decode())  # Получает публичный ключ клиента
    conn.send(str(prod(x = private_key)).encode())  # Отправляет публичный ключ клиенту

    key = prod(g = public_c, x = private_key)  # Просчитывает секретный ключ, seed
    print("(ключ - {})\n".format(key))  # Выводит готовый seed, ключ

    random.seed(key)  # Настраиваем seed

    while True:  # Бесконечный цикл, с получением и расшифровкой сообщения
        encrypted = conn.recv(1024).decode()
        message = ""
        for i, j in zip(range(len(encrypted)), [random.randint(0, 400) for i in range(len(encrypted))]):
            message += chr(ord(encrypted[i]) - j)
        print("Зашифровано:\t{}\nДешифровано:\t{}\n".format(encrypted, message))
