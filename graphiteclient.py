import sys
import socket

def upload_to_graphite(message, server='localhost', port=2003, proto='udp'):
    #check message?
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((server, port)) #function takes tuple of (servername, port)
            s.sendall(bytes(message, 'utf-8'))
            s.close()
        except:
            sys.stderr.write('ERROR: Could not write to Graphite')
            sys.exit(1)
