import socket

BYTES_TO_READ = 4096

def get(host, port):
    # created a request
    request_data= b"GET / HTTP/ 1.1\nHOST: "+ host.encode('utf-8') + b'\n\n'

    # created a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # we have sent some data here
    s.connect((host,port))
    s.send(request_data)
    s.shutdown(socket.SHUT_WR)

    # listeing for reponse form the server
    response = s.recv(BYTES_TO_READ)
    while (len(response) > 0):
        print(response)
        response = s.recv(BYTES_TO_READ)
    
    s.close()

get("www.google.com", 80)
