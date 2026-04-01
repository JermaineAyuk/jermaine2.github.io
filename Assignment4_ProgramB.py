# Program Name: Assignment4_ProgramB.py
# Course: IT3883/Section W01
# Student Name: Jermaine Ayuk
# Assignment Number: Lab 4
# Due Date: 04/01/2026
# Purpose:
#   Program B listens for a connection from Program A, receives a string,
#   converts it to uppercase, prints it locally, and sends it back to Program A.
#
# Resources Used:
#   - Python socket documentation (for understanding socket functions)
#   - Help from AI assistant for conceptual guidance only; all code written by me

import socket   # Import socket library for network communication

def main():
    # Hard-coded IP and port to listen on
    host_ip = "127.0.0.1"        # Localhost for testing
    listen_port = 45000          # Same port used by Program A

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP and port
    server_socket.bind((host_ip, listen_port))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Program B is listening for incoming connections...")

    # Accept a connection from Program A
    connection, address = server_socket.accept()
    print("Connected to Program A at:", address)

    try:
        # Receive data from Program A
        data = connection.recv(1024).decode()

        # Convert to uppercase
        upper_data = data.upper()

        # Print uppercase string in Program B
        print("Received and converted to uppercase:", upper_data)

        # Send uppercase string back to Program A
        connection.send(upper_data.encode())

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection and socket
        connection.close()
        server_socket.close()

# Run the program
main()
