import socket
import sys

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建Socket连接
    sock.connect(('127.0.0.1', 8001))  # 连接服务器
    while True:
        data = input('Please input data:')
        data = data.encode()
        if not data:
            break
        try:
            sock.sendall(data)
        except socket.error as e:
            print('Send Failed...', e)
            sys.exit(0)
        print('Send Successfully')

        res = sock.recv(4096)  # 获取服务器返回的数据，还可以用recvfrom()、recv_into()等
        print(res)
    sock.close()