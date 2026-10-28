import socket

host = input("Host or IP address: ").strip()

try:
    port = int(input("Port number: "))
    if not 1 <= port <= 65535:
        raise ValueError

    with socket.create_connection((host, port), timeout=3):
        print(f"Port {port} is open on {host}.")
except ValueError:
    print("Enter a port number from 1 to 65535.")
except socket.gaierror:
    print("Could not find that host.")
except ConnectionRefusedError:
    print(f"Port {port} is closed on {host}.")
except socket.timeout:
    print("The connection timed out.")
except OSError as error:
    print(f"Could not connect: {error}")
