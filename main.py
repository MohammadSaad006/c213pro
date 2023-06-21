import scoket
from threadign import Thread
from pynput.mouse import Button,Controller
from screeninfo import get_moniters
from pynput.keyboard import Key,Controller

SERVER =None
PORT =8000
IP_ADDRESS = "192.168.0.111"

screen_width = None
screen_height = None

keyboard = Controller()

def getDeviceSize():

    global screen_width
    global screen_height

    for m in get_monitors():

        print(m)

        screen_width = int(str(m).split(",")[2].strip().split('width=')[1])
        screen_height = int(str(m).split(",")[3].strip().split('height=')[1])

def acceptConnections():
    global SERVER

    while True:
        client_socket, addr = SERVER.accept()

        print(f"Connection established with {client_socket} : {addr}")

        therad1=Thread(target=recvMessage,args=(client_socket))
        therad1.start()

def recvMessage (client_socket):

    global keyboard

    while True:
        try:
            message =client_socket.recv(2048).decode()
            if(message):
                keyboard.press(message)
                keyboard.release(message)

                print(message)

            except Exception as error:
                pass

def setup():

    print("\n\t\t\t\t\t*** WELCOME TO REMOTE KEYBOARD ***\n")
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(scoket.AF_INET, scoket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(10)
    print("\t\t\t\t SERVER IS WATING FOR INCOMMING CONNECTION")

    getDeviceSize()
    acceptConnections()
setup()