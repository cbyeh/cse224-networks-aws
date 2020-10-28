from socket import socket

# Create connection to the server
s = socket()
s.connect(("localhost", 8080))

# Compose test for file not found 404
msgPart1 = b"GET /doesnotexist.png \r\nHost: Ha\r\n\r\n"

# Send out the request
s.sendall(msgPart1)

# Listen for response and print it out
print (s.recv(4096))

""""""

s = socket()
s.connect(("localhost", 8080))

# Compose test for escape doc root 404
msgPart2 = b"GET /../secret.pem HTTP/1.1\r\nHost: Ha\r\n\r\n"

# Send out the request
s.sendall(msgPart2)

# Listen for response and print it out
print (s.recv(4096))

""""""

s = socket()
s.connect(("localhost", 8080))

# Compose test for malformed header 400 bad protocol
msgPart3 = b"GET /kitten.jpg HTEEP/1.1\r\nHost: Ha\r\n\r\n"

# Send out the request
s.sendall(msgPart3)

# Listen for response and print it out
print (s.recv(4096))

""""""

s = socket()
s.connect(("localhost", 8080))

# Compose test for malformed header 400 GETT
msgPart4 = b"GETT /kitten.jpg HTTP/1.1\r\nHost: Ha\r\n\r\n"

# Send out the request
s.sendall(msgPart4)

# Listen for response and print it out
print (s.recv(4096))

""""""

s = socket()
s.connect(("localhost", 8080))

# Compose test for malformed header 400 no backslash
msgPart5 = b"GET kitten.jpg HTTP/1.1\r\nHost: Ha\r\n\r\n"

# Send out the request
s.sendall(msgPart5)

# Listen for response and print it out
print (s.recv(4096))

s.close()