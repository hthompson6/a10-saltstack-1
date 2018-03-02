from acos_client.client import Client

def create(host, version, username, password, port, protocol):
    return Client(host, version, username, password, port, protocol)
