# Program Name: Assignment4_ProgramA.py
# Course: IT3883/Section W01
# Student Name: Jermaine Ayuk
# Assignment Number: Lab 4
# Due Date: 04/01/2026
# Purpose: 
#   Program A prompts the user for a string, sends it to Program B over a socket,
#   waits for a response, and prints whatever Program B sends back.
#
# Resources Used:
#   - Python socket documentation (for understanding socket functions)
#   - Help from AI assistant for conceptual guidance only; all code written by me

import socket   # Import socket library for network communication

def main():
    # Hard-coded IP and port for Program B (server)
    server_ip = "127.0.0.1"      # Localhost for testing
    server_port = 45000          # Port number above 40000

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to Program B
        client_socket.connect((server_ip, server_port))

        # Prompt user for input
        user_message = input("Enter a string to send to Program B: ")

        # Send the string to Program B
        client_socket.send(user_message.encode())

        # Wait for response from Program B
        response = client_socket.recv(1024).decode()

        # Print the response received
        print("Received from Program B:", response)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the socket connection
        client_socket.close()

# Run the program
main()
