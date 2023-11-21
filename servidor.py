import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 8888))
servidor.listen()

print("Aguardando conexão...")
cliente, end = servidor.accept()
print(f"Conectado a {end}")

terminado = False

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
    else:
        print(f"Cliente: {msg}")

    resposta = input('Mensagem: ')
    cliente.send(resposta.encode('utf-8'))

cliente.close()
servidor.close()
