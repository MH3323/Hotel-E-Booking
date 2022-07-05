import socket
import user

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf8"

LOGIN = "login"
SIGNUP = "signup"
def sendList(client, list):

    for item in list:
        client.sendall(item.encode(FORMAT))
        #wait response
        client.recv(1024)

    msg = "end"
    client.send(msg.encode(FORMAT))   

def Login(client):
    account = []
    print("Please input username and password")
    username = input('Username:')
    password = input('Password:')
    account.append(username)
    account.append(password)
    sendList(client, account)   

def Signup(client):
    list = []
    print("Please input these information")
    new_account = user.User.create_new_user()
    list.append(new_account)
    sendList(client,list)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("CLIENT SIDE")


try:
    client.connect( (HOST, SERVER_PORT) )
    print("client address:",client.getsockname())

    msg = None
    while (msg != "x"):
        msg = input("talk: ")
        client.sendall(msg.encode(FORMAT))
        if (msg == LOGIN):
            # wait response
            client.recv(1024)
            Login(client)
        if(msg == SIGNUP):
            client.recv(1024)
            Signup(client)


except:
    print("Error")


client.close()