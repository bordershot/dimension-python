import sys
import socket


def upload_to_graphite(message, server='localhost', port=2003, proto='udp'):
    # add a check for message formatting?
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((server, port))   # tuple of (servername, port)
            s.sendall(message.encode('ascii'))
            s.close()
        except:
            sys.stderr.write('ERROR: Could not write to Graphite ' +
                             str(sys.exc_info()[0]))
            sys.exit(1)
