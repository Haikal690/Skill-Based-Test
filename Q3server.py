import random
import socket
import threading

quotes = ["The way I see it, if you want the rainbow, you gotta put up with the>
          "Not in doing what you like, but in liking what you do is the secret >
          "If your ship doesn't come in, swim out to it"]

def handle_client(client_socket):
    quote = random.choice(quotes)
    c_socket.send(quote.encode())
    c_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.100.198', 8080))
    server_socket.listen(5)

    print("Quotes Of The Day server is listening for incoming connections...")

while True:
        c_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")
        print(f"Connected accepted")
        c_handler = threading.Thread(target=handle_client, args=(c_socket,))
        c_handler.start()


if __name__ == '__main__':
    main()
