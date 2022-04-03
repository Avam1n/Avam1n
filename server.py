import socket

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8000

new_socket.bind((host_name, port))
print("=" * 66)
print("Соединение произошло успешно!")
print(f"Это твой IP: {s_ip}")
print("=" * 66)

name = input('Введите имя:')

new_socket.listen(3)

conn, add = new_socket.accept()
print(f"Соединение для {add[0]} произошло успешно!")
print("=" * 66)

client = (conn.recv(1024).decode())
print(f"{client} теперь с нами, GL&HF!")
conn.send((name.encode()))

while True:
    message = input('Я: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
