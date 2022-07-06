import socket
from PIL import Image
import pickle
import sys

from server import BUFFER_IMG
import user
import feature
import bill

HOST = "127.0.0.1"
SERVER_PORT = 55544
FORMAT = "utf8"
BUFFER_IMG = 4096

# Constant for all server functions
LOGIN = "login"
SIGNUP = "signup"
SEARCHING = "searching"
BOOKING = "booking"
CANCEL_BOOKING = "cancel booking"
EXIT = "exit"


def sendList(client, list):

    for item in list:
        client.sendall(item.encode(FORMAT))
        # wait response
        client.recv(1024)

    msg = "end"
    client.send(msg.encode(FORMAT))


def Login(client):
    account = []
    print("Please input username and password")
    username = input('Username:')
    password = input('Password:')
    bool = user.User.check_username_availability(
        username) and user.User.check_password(password)
    while (bool == False):
        print('Please try again')
        print('The maximum length of username is 32 letters ')
        print('The min of pass is 4 and must have lowercase, uppercase, number, special character')
        username = input('Username:')
        password = input('Password:')
        bool = user.User.check_username_availability(
            username) and user.User.check_password(password)
    account.append(username)
    account.append(password)
    sendList(client, account)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("CLIENT SIDE")


try:
    client.connect((HOST, SERVER_PORT))
    print("Connected to server")
    is_login = False
    request = []
    while True:
        # print("1. Login")
        # print("2. Sign up")
        # print("\n")
        # choice = input("Please choose: ")
        # if choice == "1":
        #     request.append(LOGIN)
        #     user_name = input("Username: ")
        #     user_password = input("Password: ")
        #     request.append(user_name)
        #     request.append(user_password)
        #     sendList(client, request)
        #     is_login = client.recv(1024).decode(FORMAT)
        #     if is_login == "True":
        #         print("Login success")
        #         break
        #     else:
        #         print("Login failed")
        #         continue
        # elif choice == "2":
        #     request.append(SIGNUP)
        #     user_name = input("Username: ")
        #     user_password = input("Password: ")
        #     request.append(user_name)
        #     request.append(user_password)
        #     sendList(client, request)
        #     is_login = client.recv(1024).decode(FORMAT)
        #     if is_login == "True":
        #         print("Sign up success")
        #         break
        #     else:
        #         print("Sign up failed")
        #         continue
        break
    user_name = "mhuy3323"
    is_login = "True"
    while is_login == "True":
        print("1. Searching")
        print("2. Booking")
        print("3. Cancel booking")
        print("4. Logout and exit")
        print("\n")
        choice = input("Please choose: ")
        if choice == "1":
            request.append(SEARCHING)
            # Write your function to search hotel here
        elif choice == "2":
            # Write your function to booking hotel here
            msg = feature.get_info_booking(user_name)
            sendList(client, msg)
            print("Sent booking info to server")
            print("Waiting for server response . . .")
            response = client.recv(1024).decode(FORMAT)
            if response == "Success: Booking room successfully":
                print(response)
                revc_data = client.recv(4096)
                your_bill = pickle.loads(revc_data)
                print("Here is your bill:")
                bill.print_bill(your_bill)
            else:
                print(response)
        elif choice == "3":
            request.append(CANCEL_BOOKING)
            # Write your function to cancel booking here
        elif choice == "4":
            request.append(EXIT)
            # Write your function to logout here
        else:
            print("Please choose again")
            continue
    # print("client address:", client.getsockname())
    # print("client:", HOST, SERVER_PORT)
    # print("Connected to server")
    # reply = client.recv(1024).decode(FORMAT)
    # print("reply:", reply)
    # msg = None
    # while (msg != "x"):
    #     user_info = ["benn", "122345", "end"]
    #     sendList(client, user_info)
    #     print("user_info:", user_info)
    #     print("Received:", client.recv(1024).decode(FORMAT))
        # msg = input("talk: ")
        # client.sendall(msg.encode(FORMAT))
        # if (msg == "list"):
        #     # wait response
        #     client.recv(1024)
        #     sendList(client, list)
        # elif (msg == "img"):
        #     # Receive the number of packet
        #     num_packet = int(client.recv(1024).decode(FORMAT))
        #     print("num_packet:", num_packet)
        #     with open("test.jpg", "wb") as f:
        #         for i in range(num_packet):
        #             data = client.recv(BUFFER_IMG)
        #             f.write(data)
        #     f.close()
        # Ask to see the image
        # print("Do you want to see the image? (y/n)")
        # answer = input()
        # if (answer == "y"):
        #     img = Image.open("test.jpg")
        #     img.show()
        # else:
        #     print("Image is not shown")
        # msg = input("talk: ")
        # client.sendall(msg.encode(FORMAT))
        # if (msg == LOGIN):
        #     # wait response
        #     client.recv(1024)
        #     Login(client)


except:
    print("Error")


client.close()
