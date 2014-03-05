# Echo server program
import socket
import thread

TARGET = None
DEFAULT_PORT = 45000

def reciever():
    """ Revive messages... """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind(('', DEFAULT_PORT)) # Listens on all interfaces... 
    s.listen(True) # Listen on the newly created socket... 
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        print "\nMessage> %s\n" % data


def sender():
    """ The 'client' which sends the messages """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TARGET, DEFAULT_PORT)) # Connect... 

    while True: 
        msg = raw_input("\nMe> ")
        s.sendall(msg)
    s.close()

while not TARGET:
    TARGET = raw_input("Please specify the other client to connect to: ")

thread.start_new_thread(reciever, ())
thread.start_new_thread(sender, ())

while True:
   pass
