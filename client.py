import socket

message_cnt = 10
print(f'You have only {message_cnt} messages. Enjoy.')

while True:
    print(f'Available messages = {message_cnt}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    sock.connect(('localhost', 55001))  # подключемся к серверному сокету
    sock.send(bytes(input("Введите сообщение: "), encoding='UTF-8'))  # отправляем сообщение
    data = sock.recv(1024)  # читаем ответ от серверного сокета
    print(f">>> {data}")
    message_cnt -= 1
    if message_cnt == 0:
        print(f'Start new connection.')
        break

sock.close()  # закрываем соединение
