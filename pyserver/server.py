import configparser
import logging
import socket

config = configparser.ConfigParser()
config.read("conf.ini")

logging.basicConfig(filename="server.log", level=logging.INFO)

ip = config['DEFAULT']['BIND_IP']
port = int(config['DEFAULT']['BIND_PORT'])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

print("Listening on {}:{}".format(ip, port))


def server_loop(client):
    request = client.recv(1024).decode("UTF-8")
    print("Request received: {}".format(request))
    logging.info("Request from {}:{}\n{}".format(ip, port, request))
    html_page = request[request.find("/") + 1:request.find('HTTP') - 1]
    if not html_page:
        file = open(config['DEFAULT']['DEFAULT_HTML'], "rb")
    else:
        file = open(html_page, "rb")
    f = file.read()
    client.send(f)
    client.close()


while True:
    client, addr = server.accept()
    print("Accepted connection from {}:{}".format(ip, port))
    server_loop(client)
