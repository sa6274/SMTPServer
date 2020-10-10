from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    data = 'DATA\r\n'
    quitCommand = 'QUIT\r\n'

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
   # print(recv1)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailFrom = "MAIL FROM:<sa6274@nyu.edu>\r\n"
    clientSocket.send(bytes(mailFrom.encode()))

    # Send RCPT TO command and print server response.
    rcptTo = "RCPT TO:<sa6274@nyu.edu>\r\n"
    clientSocket.send(bytes(rcptTo.encode()))

    # Send DATA command and print server response.
    clientSocket.send(bytes(data.encode()))
    recv1 = clientSocket.recv(1024).decode()

    # Send message data.
    clientSocket.send(bytes(msg.encode()))
    recv1 = clientSocket.recv(1024).decode()


    # Message ends with a single period.
    clientSocket.send(bytes(endmsg.encode()))


    # Send QUIT command and get server response.
    clientSocket.send(bytes(quitCommand.encode()))



if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
