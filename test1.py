import socket

# Define the server address and port
SERVER_ADDRESS = ('127.0.0.1', 12345)

def main():
    # Create a socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            if data.startswith('QUESTION:'):
                print(data)  # Display the question
                options = []
                while True:
                    option = client_socket.recv(1024).decode('utf-8')
                    if not option:
                        break
                    options.append(option)
                for option in options:
                    print(option)
                answer = input("Your answer: ").strip().upper()
                client_socket.send(answer.encode('utf-8'))
            elif data == 'QUIZ_OVER':
                print("The quiz is over.")
                break
        except Exception as e:
            print(f"Error in the quiz: {e}")
            break

    client_socket.close()

if __name__ == "__main__":
    main()
