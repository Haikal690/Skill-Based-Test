import socket

def main():
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect(('192.168.100.198', 8080))

    quote = c_socket.recv(1024).decode()
    print(f"Quotes Of The Day: {quote}")

    c_socket.close()

if __name__ == '__main__':
    main()
