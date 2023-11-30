import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message="Test Message"
sock.sendto(message.encode(),("192.168.1.10",3001))

#sock.send("Test Message")
sock.close()