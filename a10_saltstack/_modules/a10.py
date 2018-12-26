# Import Python libraries
from __future__ import absolute_import, print_function, unicode_literals
import logging

def client_factory(host, port, protocol, username, password):
    http_cli = http_factory(host, port, protocol)
    session = session_factory(http_cli, username, password)
    return A10Client(session)
