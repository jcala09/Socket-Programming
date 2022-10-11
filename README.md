# Socket-Programming

CS-4392-001&002 Computer Networks Socket Programming and Google Cloud Platform


Environment: 
Python

Adopted Libraries:
argparse
Socket
logging

This project is a project that helped me understand how to create a network client. I have learned how clients and servers work, and how sockets are programmed.
To be honest, this is very similar to what I usually do because I have delved in on Web Development. This is the same as sending and receiving values. 
This gave me an idea of how packets are sent over a network. I have learned how to capture packets through Wireshark and save them for future references. I have also
learned how to parse a sentence and put them in each individual variables.


This application reads a command line, parses away the server ID, the port, and the log location. After that, it uses these values to connect to the server from the 
client code I have created. I imported socket to connect the client and the server, and I used argparse to parse the command line itself. I then print these values
and see if these values correspond to my given server and port. 
