import socket, argparse
serverSideSocket= socket.socket()
host= "34.173.12.133"
port= "3389"

# Parser
parser = argparse.ArgumentParser(description='command line parser')

parser.add_argument('$', type=str,
                    help='$ ')

parser.add_argument('client', type=str,
                    help='client ')
# Required positional argument
parser.add_argument('-s', type=str,
                    help='Server ID ')

# Optional positional argument
parser.add_argument('-p', type=int, nargs='?',
                    help='Port')

# Optional argument
parser.add_argument('-l', type=str,
                    help='Log File Location')

args = parser.parse_args()

print("Argument values:")
HOST= args.s 
PORT= args.p
LOGFILELOCATION= args.l

##

# Print the values to show what we have

print(f"SERVER IP: {HOST}")
print(f"PORT: {PORT}")
print(f"LOGFILELOCATION: {LOGFILELOCATION}")


#socket object, connect to port, input sentence, send it encoded to the server, receive from server if word is right, and close the socket.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    sentence= input ('Input lowercase sentence:')
    s.send(sentence.encode())
    data = s.recv(1024)
    print('From server: ', data.decode())
    s.close()

#print the data
print(f"Received {data!r}")

# received : b"Hello there ('208.180.250.178', 63063). Here is another random quote of wisdom for you:but-i'm-not-even-motivated-enough-to-finish-this-sig-, Tim Peters, 20 Dec 2000\n"