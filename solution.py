from socket import *


def smtp_client(port=587, mailserver='smtp.nyu.edu'):
    mailserver = ('smtp.nyu.edu')
    port= 25
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    #recv1 = clientSocket.recv(1024)
    #print(recv1)
    #if recv1[:3] != '220':
     #   print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
   # recv1 = clientSocket.recv(1024).decode()
    #print(recv1 + 'test')
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')


    # Send MAIL FROM command and print server response.
    mailfromCommand = 'MAIL From: <sa6274@nyu.edu>\r\n'
    clientSocket.send(mailfromCommand.encode())
  #  recv1 = clientSocket.recv(1024).decode()
  #  print (recv1)
   # if recv1[:3] != '250':
    #    print('250 reply not received from server., 3')

    # Send RCPT TO command and print server response.
    rcpttoCommand = 'RCPT To: <sa6274@nyu.edu>\r\n'
    clientSocket.send(rcpttoCommand.encode())
 #   recv1 = clientSocket.recv(1024).decode()
   # print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server., 4')

    # Send DATA command and print server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())

    # Send message data.
    subject = "Subject: SMTP Test Mail:"
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())

    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
  #  print(endmsg)

# Send QUIT command and get server response.
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
  #  recv1 = clientSocket.recv(1024)
   # print(recv1)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')

if __name__ == '__main__':
    smtp_client('smtp.nyu.edu', 25)