import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 8888))

terminado = False
print('Digite tt para terminar o chat')

while not terminado:
    mensagem = input('mensagem: ')
    cliente.send(mensagem.encode('utf-8'))

    if mensagem == 'tt':
        terminado = True
    else:
        msg_servidor = cliente.recv(1024).decode('utf-8')
        print(f"Servidor: {msg_servidor}")

cliente.close()
